# Ensure Image Vulnerability Scanning using GCR Container Scanning or a third-party provider

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `gcr_container_scanning_enabled` |
| クラウドプラットフォーム | GCP |
| サービス | gcr |
| サブサービス | Container Scanning |
| 重大度 | medium |
| カテゴリ | Uncategorized |
| チェックタイプ | Security, Configuration |
| リソースタイプ | Service |
| リソースグループ | container |

## 説明

Scan images stored in Google Container Registry (GCR) for vulnerabilities using GCR Container Scanning or a third-party provider. This helps identify and mitigate security risks associated with known vulnerabilities in container images.

## リスク

Without image vulnerability scanning, container images stored in GCR may contain known vulnerabilities, increasing the risk of exploitation by malicious actors.

## 推奨事項

Enable vulnerability scanning for images stored in GCR using GCR Container Scanning or a third-party provider.

- 推奨リンク：[https://cloud.google.com/container-registry/docs/container-best-practices](https://cloud.google.com/container-registry/docs/container-best-practices)

## 修正手順


### CLI

```text
gcloud services enable containerscanning.googleapis.com
```

### Terraform

[https://docs.ST Cloud.com/checks/gcp/google-cloud-networking-policies/ensure-gcp-gcr-container-vulnerability-scanning-is-enabled#terraform](https://docs.ST Cloud.com/checks/gcp/google-cloud-networking-policies/ensure-gcp-gcr-container-vulnerability-scanning-is-enabled#terraform)

## 参考資料

- [https://cloud.google.com/container-registry/docs/container-analysis](https://cloud.google.com/container-registry/docs/container-analysis)
- [https://cloud.google.com/container-registry/docs/container-best-practices](https://cloud.google.com/container-registry/docs/container-best-practices)

## 技術情報

- Source Metadata：[sources/gcp/gcr_container_scanning_enabled/metadata.json](../../sources/gcp/gcr_container_scanning_enabled/metadata.json)
- Source Code：[sources/gcp/gcr_container_scanning_enabled/check.py](../../sources/gcp/gcr_container_scanning_enabled/check.py)
- Source Metadata Path：`sources/gcp/gcr_container_scanning_enabled/metadata.json`
- Source Code Path：`sources/gcp/gcr_container_scanning_enabled/check.py`
