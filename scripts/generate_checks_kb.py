#!/usr/bin/env python3
"""Generate ST Cloud check knowledge base pages from Prowler metadata."""

from __future__ import annotations

import argparse
import json
import re
import shutil
from pathlib import Path
from typing import Any


PROVIDERS = ("aws", "azure", "gcp")
DEFAULT_SOURCE_ROOT = (
    Path(__file__).resolve().parents[2]
    / "cspm-backend-main"
    / "prowler"
    / "providers"
)
REPO_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_OUTPUT_ROOT = REPO_ROOT / "checks"
DEFAULT_SOURCES_ROOT = REPO_ROOT / "sources"


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--source-root", type=Path, default=DEFAULT_SOURCE_ROOT)
    parser.add_argument("--output-root", type=Path, default=DEFAULT_OUTPUT_ROOT)
    parser.add_argument("--sources-output-root", type=Path, default=DEFAULT_SOURCES_ROOT)
    args = parser.parse_args()

    source_root = args.source_root.resolve()
    output_root = args.output_root.resolve()
    sources_output_root = args.sources_output_root.resolve()
    records = collect_records(source_root)

    if output_root.exists():
        shutil.rmtree(output_root)
    if sources_output_root.exists():
        shutil.rmtree(sources_output_root)
    output_root.mkdir(parents=True)
    sources_output_root.mkdir(parents=True)

    for provider in PROVIDERS:
        (output_root / provider).mkdir()
        (sources_output_root / provider).mkdir()

    for record in records:
        copy_source_files(record, sources_output_root)
        page_path = output_root / record["provider"] / f"{record['check_id']}.md"
        page_path.write_text(render_page(record), encoding="utf-8")

    (output_root / "index.json").write_text(
        json.dumps([public_index_record(record) for record in records], ensure_ascii=False, indent=2)
        + "\n",
        encoding="utf-8",
    )
    (output_root / "README.md").write_text(render_index_readme(records), encoding="utf-8")
    print(f"Generated {len(records)} checks into {output_root}")
    print(f"Copied source files into {sources_output_root}")


def collect_records(source_root: Path) -> list[dict[str, Any]]:
    records: list[dict[str, Any]] = []
    for provider in PROVIDERS:
        provider_root = source_root / provider
        for metadata_path in sorted(provider_root.rglob("*.metadata.json")):
            if metadata_path.name.endswith((".metadata.zh-CN.json", ".metadata.ja-JP.json")):
                continue
            metadata = json.loads(metadata_path.read_text(encoding="utf-8"))
            records.append(build_record(source_root, metadata_path, metadata))

    return sorted(
        records,
        key=lambda item: (
            item["provider"],
            item["service"],
            severity_rank(item["severity"]),
            item["check_id"],
        ),
    )


def build_record(
    source_root: Path,
    metadata_path: Path,
    metadata: dict[str, Any],
) -> dict[str, Any]:
    provider = str(metadata.get("Provider") or "").lower()
    check_id = str(metadata.get("CheckID") or metadata_path.name.split(".metadata.")[0])
    relative_metadata_path = metadata_path.relative_to(source_root)
    source_code_path = metadata_path.with_name(f"{check_id}.py")
    relative_source_code_path = (
        source_code_path.relative_to(source_root) if source_code_path.exists() else None
    )
    remediation = metadata.get("Remediation") or {}
    recommendation = remediation.get("Recommendation") or {}
    remediation_code = remediation.get("Code") or {}
    references = unique_nonempty(
        [
            metadata.get("RelatedUrl"),
            public_reference(recommendation.get("Url")),
            *(metadata.get("AdditionalURLs") or []),
        ]
    )
    references = [reference for reference in references if not is_prowler_url(reference)]
    categories = normalize_list(metadata.get("Categories"))
    check_type = normalize_list(metadata.get("CheckType"))

    return {
        "check_id": check_id,
        "title": display_text(metadata.get("CheckTitle")),
        "provider": provider,
        "service": display_text(metadata.get("ServiceName")),
        "sub_service": display_text(metadata.get("SubServiceName")),
        "severity": display_text(metadata.get("Severity")),
        "categories": categories,
        "check_type": check_type,
        "resource_type": display_text(metadata.get("ResourceType")),
        "resource_group": display_text(metadata.get("ResourceGroup")),
        "description": display_text(metadata.get("Description")),
        "risk": display_text(metadata.get("Risk")),
        "recommendation": display_text(recommendation.get("Text")),
        "recommendation_url": public_reference(recommendation.get("Url")),
        "remediation": {
            key: clean_multiline_text(value)
            for key, value in remediation_code.items()
            if clean_multiline_text(value)
            and not is_prowler_url(clean_multiline_text(value))
        },
        "references": references,
        "source": {
            "metadata_file": str(metadata_path),
            "code_file": str(source_code_path) if source_code_path.exists() else "",
            "metadata_path": relative_metadata_path.as_posix(),
            "code_path": (
                relative_source_code_path.as_posix() if relative_source_code_path else ""
            ),
            "local_metadata_path": f"sources/{provider}/{check_id}/metadata.json",
            "local_code_path": (
                f"sources/{provider}/{check_id}/check.py"
                if source_code_path.exists()
                else ""
            ),
        },
        "page": f"checks/{provider}/{check_id}.md",
    }


def copy_source_files(record: dict[str, Any], sources_output_root: Path) -> None:
    target_dir = sources_output_root / record["provider"] / record["check_id"]
    target_dir.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(record["source"]["metadata_file"], target_dir / "metadata.json")
    if record["source"]["code_file"]:
        shutil.copyfile(record["source"]["code_file"], target_dir / "check.py")


def public_index_record(record: dict[str, Any]) -> dict[str, Any]:
    public_record = dict(record)
    public_record["source"] = {
        key: value
        for key, value in record["source"].items()
        if key not in {"metadata_file", "code_file"}
    }
    return public_record


def render_page(record: dict[str, Any]) -> str:
    lines = [
        f"# {record['title'] or record['check_id']}",
        "",
        "ST Cloud check knowledge base entry.",
        "",
        "## 检查项信息",
        "",
        "| 字段 | 内容 |",
        "| --- | --- |",
        table_row("检查项 ID", code_span(record["check_id"])),
        table_row("云平台", display_provider(record["provider"])),
        table_row("服务", record["service"]),
    ]
    optional_rows = [
        ("子服务", record["sub_service"]),
        ("严重等级", record["severity"]),
        ("类别", ", ".join(record["categories"]) or "Uncategorized"),
        ("检查类型", ", ".join(record["check_type"])),
        ("资源类型", record["resource_type"]),
        ("资源组", record["resource_group"]),
    ]
    lines.extend(table_row(label, value) for label, value in optional_rows if value)
    lines.extend(
        [
            "",
            "## 描述",
            "",
            paragraph(record["description"]),
            "",
            "## 风险",
            "",
            paragraph(record["risk"]),
            "",
            "## 推荐措施",
            "",
            paragraph(record["recommendation"]),
        ]
    )
    if record["recommendation_url"]:
        lines.extend(["", f"- 推荐链接：{markdown_link(record['recommendation_url'])}"])

    lines.extend(["", "## 修复步骤", ""])
    remediation_lines = render_remediation(record["remediation"])
    lines.extend(remediation_lines or ["No remediation steps available."])

    lines.extend(["", "## 参考资料", ""])
    if record["references"]:
        lines.extend(f"- {markdown_link(reference)}" for reference in record["references"])
    else:
        lines.append("No external references available.")

    lines.extend(
        [
            "",
            "## 技术信息",
            "",
            f"- Source Metadata：[{record['source']['local_metadata_path']}](../../{record['source']['local_metadata_path']})",
        ]
    )
    if record["source"]["local_code_path"]:
        lines.append(
            f"- Source Code：[{record['source']['local_code_path']}](../../{record['source']['local_code_path']})"
        )
    lines.extend(
        [
            f"- Source Metadata Path：`{record['source']['local_metadata_path']}`",
        ]
    )
    if record["source"]["local_code_path"]:
        lines.append(f"- Source Code Path：`{record['source']['local_code_path']}`")
    lines.append("")
    return "\n".join(lines)


def render_remediation(remediation: dict[str, str]) -> list[str]:
    order = ("CLI", "NativeIaC", "Terraform", "Arm", "Other")
    labels = {
        "CLI": "CLI",
        "NativeIaC": "Native IaC",
        "Terraform": "Terraform",
        "Arm": "ARM",
        "Other": "Other",
    }
    lines: list[str] = []
    for key in order:
        value = remediation.get(key)
        if not value:
            continue
        lines.extend(["", f"### {labels[key]}", ""])
        if is_url(value):
            lines.append(markdown_link(value))
        elif value.strip().startswith("```"):
            lines.append(value)
        elif key != "Other" and ("\n" in value or looks_like_command(value)):
            lines.extend(["```text", value, "```"])
        else:
            lines.append(value)
    return lines


def render_index_readme(records: list[dict[str, Any]]) -> str:
    counts_by_provider = {provider: 0 for provider in PROVIDERS}
    for record in records:
        counts_by_provider[record["provider"]] += 1

    lines = [
        "# ST Cloud 检查项知识库",
        "",
        "本目录由 `scripts/generate_checks_kb.py` 从本地检查项元数据生成。",
        "",
        "## 统计",
        "",
        f"- 总检查项：{len(records)}",
    ]
    lines.extend(
        f"- {display_provider(provider)}：{counts_by_provider[provider]}"
        for provider in PROVIDERS
    )
    lines.extend(
        [
            "",
            "## 目录",
            "",
            "- `index.json`：机器可读索引",
            "- `aws/`：AWS 检查项",
            "- `azure/`：Azure 检查项",
            "- `gcp/`：GCP 检查项",
            "",
            "每个检查项页面包含检查项信息、描述、风险、推荐措施、修复步骤、参考资料和技术信息。",
            "",
        ]
    )
    return "\n".join(lines)


def severity_rank(value: str) -> int:
    order = {"critical": 0, "high": 1, "medium": 2, "low": 3, "informational": 4}
    return order.get(str(value).lower(), 99)


def normalize_list(value: Any) -> list[str]:
    if not value:
        return []
    if isinstance(value, list):
        return [display_text(item) for item in value if display_text(item)]
    return [display_text(value)]


def unique_nonempty(values: list[Any]) -> list[str]:
    seen = set()
    result = []
    for value in values:
        text = clean_text(value)
        if text and text not in seen:
            seen.add(text)
            result.append(text)
    return result


def public_reference(value: Any) -> str:
    text = clean_text(value)
    return "" if is_prowler_url(text) else text


def is_prowler_url(value: str) -> bool:
    return bool(re.search(r"https?://(?:[^/\s]+\.)?prowler\.com(?:/|\b)", value))


def clean_text(value: Any) -> str:
    if value is None:
        return ""
    return re.sub(r"\s+", " ", str(value)).strip()


def display_text(value: Any) -> str:
    return replace_brand_name(clean_text(value))


def clean_multiline_text(value: Any) -> str:
    if value is None:
        return ""
    lines = [line.rstrip() for line in str(value).strip().splitlines()]
    return replace_brand_name("\n".join(lines).strip())


def replace_brand_name(value: str) -> str:
    return re.sub(r"\bprowler\b", "ST Cloud", value, flags=re.IGNORECASE)


def table_row(label: str, value: str) -> str:
    return f"| {escape_table(label)} | {escape_table(value)} |"


def escape_table(value: str) -> str:
    return str(value).replace("|", "\\|")


def code_span(value: str) -> str:
    return f"`{value}`" if value else ""


def paragraph(value: str) -> str:
    return value or "No content available."


def display_provider(provider: str) -> str:
    return {"aws": "AWS", "azure": "Azure", "gcp": "GCP"}.get(provider, provider)


def is_url(value: str) -> bool:
    return value.startswith(("http://", "https://"))


def looks_like_command(value: str) -> bool:
    return bool(re.match(r"^(aws|az|gcloud|kubectl|terraform|prowler)\b", value.strip()))


def markdown_link(url: str) -> str:
    return f"[{url}]({url})"


if __name__ == "__main__":
    main()
