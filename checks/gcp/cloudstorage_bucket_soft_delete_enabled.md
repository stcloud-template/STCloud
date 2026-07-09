# Cloud Storage buckets have Soft Delete enabled

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `cloudstorage_bucket_soft_delete_enabled` |
| 云平台 | GCP |
| 服务 | cloudstorage |
| 严重等级 | medium |
| 类别 | resilience |
| 资源类型 | storage.googleapis.com/Bucket |
| 资源组 | storage |

## 描述

**Google Cloud Storage buckets** are evaluated to ensure that **Soft Delete** is enabled. Soft Delete helps protect data from accidental or malicious deletion by retaining deleted objects for a specified duration, allowing recovery within that retention window.

## 风险

Buckets without Soft Delete enabled are at higher risk of irreversible data loss caused by accidental or unauthorized deletions, since deleted objects cannot be recovered once removed.

## 推荐措施

Enable Soft Delete on Cloud Storage buckets to retain deleted objects for a defined period, improving data recoverability and resilience against accidental or malicious deletions.

## 修复步骤


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

## 参考资料

- [https://cloud.google.com/storage/docs/soft-delete](https://cloud.google.com/storage/docs/soft-delete)
- [https://cloud.google.com/blog/products/storage-data-transfer/understanding-cloud-storages-new-soft-delete-feature](https://cloud.google.com/blog/products/storage-data-transfer/understanding-cloud-storages-new-soft-delete-feature)

## 技术信息

- Source Metadata：[sources/gcp/cloudstorage_bucket_soft_delete_enabled/metadata.json](../../sources/gcp/cloudstorage_bucket_soft_delete_enabled/metadata.json)
- Source Code：[sources/gcp/cloudstorage_bucket_soft_delete_enabled/check.py](../../sources/gcp/cloudstorage_bucket_soft_delete_enabled/check.py)
- Source Metadata Path：`sources/gcp/cloudstorage_bucket_soft_delete_enabled/metadata.json`
- Source Code Path：`sources/gcp/cloudstorage_bucket_soft_delete_enabled/check.py`
