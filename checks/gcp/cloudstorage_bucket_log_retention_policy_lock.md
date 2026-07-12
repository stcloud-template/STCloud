# Cloud Storage log bucket has a Retention Policy with Bucket Lock enabled

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `cloudstorage_bucket_log_retention_policy_lock` |
| クラウドプラットフォーム | GCP |
| サービス | cloudstorage |
| 重大度 | medium |
| カテゴリ | Uncategorized |
| リソースタイプ | storage.googleapis.com/Bucket |
| リソースグループ | storage |

## 説明

**Google Cloud Storage buckets** used as **log sinks** are evaluated to ensure that a **Retention Policy** is configured and **Bucket Lock** is enabled. Enabling Bucket Lock permanently prevents the retention policy from being reduced or removed, protecting logs from modification or deletion.

## リスク

Log sink buckets without a locked retention policy are at risk of log tampering or accidental deletion. Without Bucket Lock, an attacker or user could remove or shorten the retention policy, compromising the integrity of audit logs required for forensics and compliance investigations.

## 推奨事項

Configure a retention policy and enable Bucket Lock on all Cloud Storage buckets used as log sinks to ensure log integrity and immutability.

## 修正手順


### CLI

```text
gcloud storage buckets lock-retention-policy gs://<LOG_BUCKET_NAME>
```

### Terraform

```hcl
resource "google_storage_bucket" "log_bucket" {
  name     = var.log_bucket_name
  location = var.location

  retention_policy {
    retention_period = 31536000 # 365 days in seconds
    is_locked        = true
  }
}
```

### Other

1) Open Google Cloud Console → Storage → Buckets → <LOG_BUCKET_NAME>
2) Go to the **Configuration** tab
3) Under **Retention policy**, ensure a retention duration is set
4) Click **Lock** to enable Bucket Lock and confirm the operation

## 参考資料

- [https://www.trendmicro.com/cloudoneconformity/knowledge-base/gcp/CloudStorage/retention-policies-with-bucket-lock.html](https://www.trendmicro.com/cloudoneconformity/knowledge-base/gcp/CloudStorage/retention-policies-with-bucket-lock.html)

## 技術情報

- Source Metadata：[sources/gcp/cloudstorage_bucket_log_retention_policy_lock/metadata.json](../../sources/gcp/cloudstorage_bucket_log_retention_policy_lock/metadata.json)
- Source Code：[sources/gcp/cloudstorage_bucket_log_retention_policy_lock/check.py](../../sources/gcp/cloudstorage_bucket_log_retention_policy_lock/check.py)
- Source Metadata Path：`sources/gcp/cloudstorage_bucket_log_retention_policy_lock/metadata.json`
- Source Code Path：`sources/gcp/cloudstorage_bucket_log_retention_policy_lock/check.py`
