# GCP project has Artifact Registry Container Analysis API enabled

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `artifacts_container_analysis_enabled` |
| クラウドプラットフォーム | GCP |
| サービス | artifacts |
| 重大度 | medium |
| カテゴリ | Uncategorized |
| リソースタイプ | serviceusage.googleapis.com/Service |
| リソースグループ | governance |

## 説明

Evaluates whether **Artifact Analysis** (`containeranalysis.googleapis.com`) is enabled at the project level to support **vulnerability scanning** and metadata for container images in Artifact Registry or Container Registry.

## リスク

Absent this service, images aren't continuously scanned, leaving known CVEs unnoticed. Attackers can run vulnerable containers, gain code execution, move laterally, and exfiltrate data, eroding the **integrity** and **confidentiality** of workloads and the software supply chain.

## 推奨事項

Enable **Artifact Analysis** (`containeranalysis.googleapis.com`) for projects hosting container images. Integrate scan results into CI/CD policy gates, apply **least privilege** to findings access, and rebuild images promptly to maintain **defense in depth**.

## 修正手順


### CLI

```text
gcloud services enable containeranalysis.googleapis.com --project <PROJECT_ID>
```

### Terraform

```hcl
resource "google_project_service" "<example_resource_name>" {
  project = "<example_project_id>"
  service = "containeranalysis.googleapis.com" # Enables Artifact Analysis (Container Analysis) API to pass the check
}
```

### Other

1. In Google Cloud Console, ensure the correct project is selected
2. Go to APIs & Services > Library
3. Search for "Container Analysis API"
4. Click the API, then click "Enable"

## 参考資料

- [https://cloud.google.com/artifact-analysis/docs](https://cloud.google.com/artifact-analysis/docs)
- [https://cloud.google.com/artifact-analysis/docs/container-scanning-overview](https://cloud.google.com/artifact-analysis/docs/container-scanning-overview)

## 技術情報

- Source Metadata：[sources/gcp/artifacts_container_analysis_enabled/metadata.json](../../sources/gcp/artifacts_container_analysis_enabled/metadata.json)
- Source Code：[sources/gcp/artifacts_container_analysis_enabled/check.py](../../sources/gcp/artifacts_container_analysis_enabled/check.py)
- Source Metadata Path：`sources/gcp/artifacts_container_analysis_enabled/metadata.json`
- Source Code Path：`sources/gcp/artifacts_container_analysis_enabled/check.py`
