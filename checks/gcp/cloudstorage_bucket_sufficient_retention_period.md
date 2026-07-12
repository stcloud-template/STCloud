# Cloud Storage bucket has a sufficient Retention Policy period

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `cloudstorage_bucket_sufficient_retention_period` |
| クラウドプラットフォーム | GCP |
| サービス | cloudstorage |
| 重大度 | medium |
| カテゴリ | resilience |
| リソースタイプ | storage.googleapis.com/Bucket |
| リソースグループ | storage |

## 説明

Cloud Storage bucket has a bucket-level Retention Policy with a retentionPeriod that meets or exceeds the organization-defined minimum, preventing deletion or modification of objects before the required time.

## リスク

Insufficient or missing retention allows premature deletion or modification of objects, weakening data recovery and compliance with retention requirements.

## 推奨事項

Define and apply a bucket-level Retention Policy that meets your minimum retention requirement (e.g., 90 or 365 days) to enforce data recoverability and compliance.

## 修正手順


### CLI

```text
gcloud storage buckets update gs://<BUCKET_NAME> --retention-period=<SECONDS>
```

### Terraform

```hcl
resource "google_storage_bucket" "example" {
  name     = var.bucket_name
  location = var.location

  retention_policy {
    retention_period = 7776000 # 90 days in seconds
  }
}
```

### Other

1) Console → Storage → Buckets → <BUCKET_NAME>
2) Tab 'Configuration' → 'Retention policy'
3) Set the required retention period (e.g., 90 or 365 days) and save
4) (Optional) Lock the policy if required by compliance

## 参考資料

- [https://www.trendmicro.com/cloudoneconformity/knowledge-base/gcp/CloudStorage/sufficient-retention-period.html](https://www.trendmicro.com/cloudoneconformity/knowledge-base/gcp/CloudStorage/sufficient-retention-period.html)

## 技術情報

- Source Metadata：[sources/gcp/cloudstorage_bucket_sufficient_retention_period/metadata.json](../../sources/gcp/cloudstorage_bucket_sufficient_retention_period/metadata.json)
- Source Code：[sources/gcp/cloudstorage_bucket_sufficient_retention_period/check.py](../../sources/gcp/cloudstorage_bucket_sufficient_retention_period/check.py)
- Source Metadata Path：`sources/gcp/cloudstorage_bucket_sufficient_retention_period/metadata.json`
- Source Code Path：`sources/gcp/cloudstorage_bucket_sufficient_retention_period/check.py`
