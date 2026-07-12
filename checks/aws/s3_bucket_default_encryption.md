# Check if S3 buckets have default encryption (SSE) enabled or use a bucket policy to enforce it.

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `s3_bucket_default_encryption` |
| クラウドプラットフォーム | AWS |
| サービス | s3 |
| 重大度 | medium |
| カテゴリ | encryption |
| チェックタイプ | Data Protection |
| リソースタイプ | AwsS3Bucket |
| リソースグループ | storage |

## 説明

Check if S3 buckets have default encryption (SSE) enabled or use a bucket policy to enforce it.

## リスク

Amazon S3 default encryption provides a way to set the default encryption behavior for an S3 bucket. This will ensure data-at-rest is encrypted.

## 推奨事項

Ensure that S3 buckets have encryption at rest enabled.

- 推奨リンク：[https://aws.amazon.com/blogs/security/how-to-prevent-uploads-of-unencrypted-objects-to-amazon-s3/](https://aws.amazon.com/blogs/security/how-to-prevent-uploads-of-unencrypted-objects-to-amazon-s3/)

## 修正手順


### CLI

```text
aws s3api put-bucket-encryption --bucket <bucket_name> --server-side-encryption-configuration '{'Rules': [{'ApplyServerSideEncryptionByDefault': {'SSEAlgorithm': 'AES256'}}]}'
```

### Native IaC

[https://docs.ST Cloud.com/checks/aws/s3-policies/s3_14-data-encrypted-at-rest#cloudformation](https://docs.ST Cloud.com/checks/aws/s3-policies/s3_14-data-encrypted-at-rest#cloudformation)

### Terraform

[https://docs.ST Cloud.com/checks/aws/s3-policies/s3_14-data-encrypted-at-rest#terraform](https://docs.ST Cloud.com/checks/aws/s3-policies/s3_14-data-encrypted-at-rest#terraform)

## 参考資料

- [https://aws.amazon.com/blogs/security/how-to-prevent-uploads-of-unencrypted-objects-to-amazon-s3/](https://aws.amazon.com/blogs/security/how-to-prevent-uploads-of-unencrypted-objects-to-amazon-s3/)

## 技術情報

- Source Metadata：[sources/aws/s3_bucket_default_encryption/metadata.json](../../sources/aws/s3_bucket_default_encryption/metadata.json)
- Source Code：[sources/aws/s3_bucket_default_encryption/check.py](../../sources/aws/s3_bucket_default_encryption/check.py)
- Source Metadata Path：`sources/aws/s3_bucket_default_encryption/metadata.json`
- Source Code Path：`sources/aws/s3_bucket_default_encryption/check.py`
