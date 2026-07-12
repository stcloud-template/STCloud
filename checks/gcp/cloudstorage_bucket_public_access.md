# Ensure That Cloud Storage Bucket Is Not Anonymously or Publicly Accessible

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `cloudstorage_bucket_public_access` |
| クラウドプラットフォーム | GCP |
| サービス | cloudstorage |
| 重大度 | high |
| カテゴリ | internet-exposed |
| リソースタイプ | Bucket |
| リソースグループ | storage |

## 説明

Ensure That Cloud Storage Bucket Is Not Anonymously or Publicly Accessible

## リスク

Allowing anonymous or public access grants permissions to anyone to access bucket content. Such access might not be desired if you are storing any sensitive data. Hence, ensure that anonymous or public access to a bucket is not allowed.

## 推奨事項

It is recommended that IAM policy on Cloud Storage bucket does not allows anonymous or public access.

- 推奨リンク：[https://cloud.google.com/storage/docs/access-control/iam-reference](https://cloud.google.com/storage/docs/access-control/iam-reference)

## 修正手順


### Terraform

[https://docs.ST Cloud.com/checks/gcp/google-cloud-public-policies/bc_gcp_public_1#terraform](https://docs.ST Cloud.com/checks/gcp/google-cloud-public-policies/bc_gcp_public_1#terraform)

### Other

[https://docs.ST Cloud.com/checks/gcp/google-cloud-public-policies/bc_gcp_public_1](https://docs.ST Cloud.com/checks/gcp/google-cloud-public-policies/bc_gcp_public_1)

## 参考資料

- [https://www.trendmicro.com/cloudoneconformity/knowledge-base/gcp/CloudStorage/publicly-accessible-storage-buckets.html](https://www.trendmicro.com/cloudoneconformity/knowledge-base/gcp/CloudStorage/publicly-accessible-storage-buckets.html)
- [https://cloud.google.com/storage/docs/access-control/iam-reference](https://cloud.google.com/storage/docs/access-control/iam-reference)

## 技術情報

- Source Metadata：[sources/gcp/cloudstorage_bucket_public_access/metadata.json](../../sources/gcp/cloudstorage_bucket_public_access/metadata.json)
- Source Code：[sources/gcp/cloudstorage_bucket_public_access/check.py](../../sources/gcp/cloudstorage_bucket_public_access/check.py)
- Source Metadata Path：`sources/gcp/cloudstorage_bucket_public_access/metadata.json`
- Source Code Path：`sources/gcp/cloudstorage_bucket_public_access/check.py`
