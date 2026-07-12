# Cloud Storage buckets have Soft Delete enabled

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `cloudstorage_bucket_soft_delete_enabled` |
| クラウドプラットフォーム | GCP |
| サービス | cloudstorage |
| 重大度 | medium |
| カテゴリ | resilience |
| リソースタイプ | storage.googleapis.com/Bucket |
| リソースグループ | storage |

## 説明

**Google Cloud Storage buckets** are evaluated to ensure that **Soft Delete** is enabled. Soft Delete helps protect data from accidental or malicious deletion by retaining deleted objects for a specified duration, allowing recovery within that retention window.

## リスク

Buckets without Soft Delete enabled are at higher risk of irreversible data loss caused by accidental or unauthorized deletions, since deleted objects cannot be recovered once removed.

## 推奨事項

Enable Soft Delete on Cloud Storage buckets to retain deleted objects for a defined period, improving data recoverability and resilience against accidental or malicious deletions.

## 修正手順


### CLI

```text
gcloud storage buckets update gs://<BUCKET_NAME> --soft-delete-retention-duration=<SECONDS>
```

### Terraform

```hcl
# Example: enable Soft Delete on a Cloud Storage bucket
resource "google_storage_bucket" "example" {
  name     = var.bucket_name
  location = var.location

  soft_delete_policy {
    retention_duration_seconds = 604800  # 7 days
  }
}
```

### Other

1) Open Google Cloud Console → Storage → Buckets → <BUCKET_NAME>
2) Tab 'Configuration'
3) Under 'Soft Delete', click 'Enable Soft Delete'
4) Set the desired retention duration and save changes

## 参考資料

- [https://cloud.google.com/storage/docs/soft-delete](https://cloud.google.com/storage/docs/soft-delete)
- [https://cloud.google.com/blog/products/storage-data-transfer/understanding-cloud-storages-new-soft-delete-feature](https://cloud.google.com/blog/products/storage-data-transfer/understanding-cloud-storages-new-soft-delete-feature)

## 技術情報

- Source Metadata：[sources/gcp/cloudstorage_bucket_soft_delete_enabled/metadata.json](../../sources/gcp/cloudstorage_bucket_soft_delete_enabled/metadata.json)
- Source Code：[sources/gcp/cloudstorage_bucket_soft_delete_enabled/check.py](../../sources/gcp/cloudstorage_bucket_soft_delete_enabled/check.py)
- Source Metadata Path：`sources/gcp/cloudstorage_bucket_soft_delete_enabled/metadata.json`
- Source Code Path：`sources/gcp/cloudstorage_bucket_soft_delete_enabled/check.py`
