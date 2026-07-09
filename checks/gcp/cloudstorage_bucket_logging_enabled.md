# Cloud Storage buckets have Usage and Storage Logs enabled

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `cloudstorage_bucket_logging_enabled` |
| 云平台 | GCP |
| 服务 | cloudstorage |
| 严重等级 | medium |
| 类别 | logging |
| 资源类型 | storage.googleapis.com/Bucket |
| 资源组 | storage |

## 描述

**Google Cloud Storage buckets** are evaluated to ensure that **Usage and Storage Logs** are enabled. Enabling these logs provides detailed visibility into access requests, usage patterns, and storage activity within each bucket.

## 风险

Buckets without Usage and Storage Logs enabled lack visibility into access and storage activity, which increases the risk of undetected data exfiltration, misuse, or configuration errors.

## 推荐措施

Enable Usage and Storage Logs for all Cloud Storage buckets to track access, detect anomalies, and maintain audit visibility of data operations.

## 修复步骤


### CLI

gsutil logging set on -b gs://<LOGGING_BUCKET> -o <LOG_OBJECT_PREFIX> gs://<BUCKET_NAME>

### Terraform

```hcl
# Example: enable Usage and Storage Logs on a Cloud Storage bucket
resource "google_storage_bucket" "example" {
  name     = var.bucket_name
  location = var.location

  logging {
    log_bucket        = var.log_bucket_name
    log_object_prefix = "${var.bucket_name}/"
  }
}
```

## 参考资料

- [https://www.trendmicro.com/cloudoneconformity/knowledge-base/gcp/CloudStorage/enable-usage-and-storage-logs.html](https://www.trendmicro.com/cloudoneconformity/knowledge-base/gcp/CloudStorage/enable-usage-and-storage-logs.html)
- [https://cloud.google.com/storage/docs/access-logs](https://cloud.google.com/storage/docs/access-logs)

## 技术信息

- Source Metadata：[sources/gcp/cloudstorage_bucket_logging_enabled/metadata.json](../../sources/gcp/cloudstorage_bucket_logging_enabled/metadata.json)
- Source Code：[sources/gcp/cloudstorage_bucket_logging_enabled/check.py](../../sources/gcp/cloudstorage_bucket_logging_enabled/check.py)
- Source Metadata Path：`sources/gcp/cloudstorage_bucket_logging_enabled/metadata.json`
- Source Code Path：`sources/gcp/cloudstorage_bucket_logging_enabled/check.py`
