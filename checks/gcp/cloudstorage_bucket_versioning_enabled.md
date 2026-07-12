# Cloud Storage buckets have Object Versioning enabled

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `cloudstorage_bucket_versioning_enabled` |
| クラウドプラットフォーム | GCP |
| サービス | cloudstorage |
| 重大度 | medium |
| カテゴリ | resilience |
| リソースタイプ | storage.googleapis.com/Bucket |
| リソースグループ | storage |

## 説明

**Google Cloud Storage buckets** are evaluated to ensure that **Object Versioning** is enabled. Object Versioning preserves older versions of objects, allowing data recovery, maintaining audit trails, and protecting against accidental deletions or overwrites.

## リスク

Buckets without Object Versioning enabled cannot recover previous object versions, which increases the risk of permanent data loss from accidental deletion or modification.

## 推奨事項

Enable Object Versioning on Cloud Storage buckets to preserve previous object versions and improve data recoverability and auditability.

## 修正手順


### CLI

```text
gcloud storage buckets update gs://<BUCKET_NAME> --versioning
```

### Terraform

```hcl
# Example: enable Object Versioning on a Cloud Storage bucket
resource "google_storage_bucket" "example" {
  name     = var.bucket_name
  location = var.location

  versioning {
    enabled = true
  }
}
```

### Other

1) Open Google Cloud Console → Storage → Buckets → <BUCKET_NAME>
2) Tab 'Configuration'
3) Under 'Object versioning', click 'Enable Object Versioning'
4) Save changes

## 参考資料

- [https://www.trendmicro.com/cloudoneconformity/knowledge-base/gcp/CloudStorage/enable-versioning.html](https://www.trendmicro.com/cloudoneconformity/knowledge-base/gcp/CloudStorage/enable-versioning.html)
- [https://cloud.google.com/storage/docs/object-versioning](https://cloud.google.com/storage/docs/object-versioning)

## 技術情報

- Source Metadata：[sources/gcp/cloudstorage_bucket_versioning_enabled/metadata.json](../../sources/gcp/cloudstorage_bucket_versioning_enabled/metadata.json)
- Source Code：[sources/gcp/cloudstorage_bucket_versioning_enabled/check.py](../../sources/gcp/cloudstorage_bucket_versioning_enabled/check.py)
- Source Metadata Path：`sources/gcp/cloudstorage_bucket_versioning_enabled/metadata.json`
- Source Code Path：`sources/gcp/cloudstorage_bucket_versioning_enabled/check.py`
