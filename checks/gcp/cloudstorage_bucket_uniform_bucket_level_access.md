# Ensure That Cloud Storage Buckets Have Uniform Bucket-Level Access Enabled

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `cloudstorage_bucket_uniform_bucket_level_access` |
| クラウドプラットフォーム | GCP |
| サービス | cloudstorage |
| 重大度 | medium |
| カテゴリ | Uncategorized |
| リソースタイプ | Bucket |
| リソースグループ | storage |

## 説明

Ensure That Cloud Storage Buckets Have Uniform Bucket-Level Access Enabled

## リスク

Enabling uniform bucket-level access guarantees that if a Storage bucket is not publicly accessible, no object in the bucket is publicly accessible either.

## 推奨事項

It is recommended that uniform bucket-level access is enabled on Cloud Storage buckets.

- 推奨リンク：[https://cloud.google.com/storage/docs/using-uniform-bucket-level-access](https://cloud.google.com/storage/docs/using-uniform-bucket-level-access)

## 修正手順


### CLI

gsutil uniformbucketlevelaccess set on gs://BUCKET_NAME/

### Terraform

[https://docs.ST Cloud.com/checks/gcp/google-cloud-storage-gcs-policies/bc_gcp_gcs_2#terraform](https://docs.ST Cloud.com/checks/gcp/google-cloud-storage-gcs-policies/bc_gcp_gcs_2#terraform)

### Other

[https://www.trendmicro.com/cloudoneconformity/knowledge-base/gcp/CloudStorage/enable-uniform-bucket-level-access.html](https://www.trendmicro.com/cloudoneconformity/knowledge-base/gcp/CloudStorage/enable-uniform-bucket-level-access.html)

## 参考資料

- [https://cloud.google.com/storage/docs/using-uniform-bucket-level-access](https://cloud.google.com/storage/docs/using-uniform-bucket-level-access)

## 技術情報

- Source Metadata：[sources/gcp/cloudstorage_bucket_uniform_bucket_level_access/metadata.json](../../sources/gcp/cloudstorage_bucket_uniform_bucket_level_access/metadata.json)
- Source Code：[sources/gcp/cloudstorage_bucket_uniform_bucket_level_access/check.py](../../sources/gcp/cloudstorage_bucket_uniform_bucket_level_access/check.py)
- Source Metadata Path：`sources/gcp/cloudstorage_bucket_uniform_bucket_level_access/metadata.json`
- Source Code Path：`sources/gcp/cloudstorage_bucket_uniform_bucket_level_access/check.py`
