# Cloud Storage buckets have lifecycle management enabled

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `cloudstorage_bucket_lifecycle_management_enabled` |
| クラウドプラットフォーム | GCP |
| サービス | cloudstorage |
| 重大度 | medium |
| カテゴリ | Uncategorized |
| リソースタイプ | storage.googleapis.com/Bucket |
| リソースグループ | storage |

## 説明

**Google Cloud Storage buckets** are evaluated for the presence of **lifecycle management** with at least one valid rule (supported action and non-empty condition) to automatically transition or delete objects and optimize storage costs.

## リスク

Buckets without lifecycle rules can accumulate stale data, increase storage costs, and fail to meet data retention and internal compliance requirements.

## 推奨事項

Configure lifecycle rules to automatically delete stale objects or transition them to colder storage classes according to your organization's retention and cost-optimization policy.

## 修正手順


### CLI

```text
gcloud storage buckets update gs://<BUCKET_NAME> --lifecycle-file=<PATH_TO_JSON>
```

### Terraform

```hcl
# Example: enable lifecycle to transition and delete objects
resource "google_storage_bucket" "example" {
  name     = var.bucket_name
  location = var.location

  # Transition STANDARD → NEARLINE after 90 days
  lifecycle_rule {
    action {
      type          = "SetStorageClass"
      storage_class = "NEARLINE"
    }
    condition {
      age                   = 90
      matches_storage_class = ["STANDARD"]
    }
  }

  # Delete objects after 365 days
  lifecycle_rule {
    action {
      type = "Delete"
    }
    condition {
      age = 365
    }
  }
}
```

### Other

1) Open Google Cloud Console → Storage → Buckets → <BUCKET_NAME>
2) Tab 'Lifecycle'
3) Add rule(s) to delete or transition objects (e.g., delete after 365 days; transition STANDARD→NEARLINE after 90 days)
4) Save

## 参考資料

- [https://www.trendmicro.com/cloudoneconformity/knowledge-base/gcp/CloudStorage/enable-lifecycle-management.html](https://www.trendmicro.com/cloudoneconformity/knowledge-base/gcp/CloudStorage/enable-lifecycle-management.html)
- [https://cloud.google.com/storage/docs/lifecycle](https://cloud.google.com/storage/docs/lifecycle)

## 技術情報

- Source Metadata：[sources/gcp/cloudstorage_bucket_lifecycle_management_enabled/metadata.json](../../sources/gcp/cloudstorage_bucket_lifecycle_management_enabled/metadata.json)
- Source Code：[sources/gcp/cloudstorage_bucket_lifecycle_management_enabled/check.py](../../sources/gcp/cloudstorage_bucket_lifecycle_management_enabled/check.py)
- Source Metadata Path：`sources/gcp/cloudstorage_bucket_lifecycle_management_enabled/metadata.json`
- Source Code Path：`sources/gcp/cloudstorage_bucket_lifecycle_management_enabled/check.py`
