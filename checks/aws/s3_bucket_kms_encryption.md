# Check if S3 buckets have KMS encryption enabled.

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `s3_bucket_kms_encryption` |
| クラウドプラットフォーム | AWS |
| サービス | s3 |
| 重大度 | medium |
| カテゴリ | encryption |
| チェックタイプ | Data Protection |
| リソースタイプ | AwsS3Bucket |
| リソースグループ | storage |

## 説明

Check if S3 buckets have KMS encryption enabled.

## リスク

Amazon S3 KMS encryption provides a way to set the encryption behavior for an S3 bucket using a managed key. This will ensure data-at-rest is encrypted.

## 推奨事項

Ensure that S3 buckets have encryption at rest enabled using KMS.

- 推奨リンク：[https://docs.aws.amazon.com/AmazonS3/latest/userguide/UsingKMSEncryption.html](https://docs.aws.amazon.com/AmazonS3/latest/userguide/UsingKMSEncryption.html)

## 修正手順


### CLI

```text
aws put-bucket-encryption --bucket <BUCKET_NAME> --server-side-encryption-configuration '{"Rules":[{"ApplyServerSideEncryptionByDefault":{"SSEAlgorithm":"aws:kms","KMSMasterKeyID":"arn:aws:kms:<REGION>:<ACCOUNT_ID>:key/<KEY_ID>"}}]}'
```

### Native IaC

[https://www.trendmicro.com/cloudoneconformity-staging/knowledge-base/aws/S3/encrypted-with-kms-customer-master-keys.html](https://www.trendmicro.com/cloudoneconformity-staging/knowledge-base/aws/S3/encrypted-with-kms-customer-master-keys.html)

### Terraform

[https://docs.ST Cloud.com/checks/aws/general-policies/ensure-that-s3-buckets-are-encrypted-with-kms-by-default#terraform](https://docs.ST Cloud.com/checks/aws/general-policies/ensure-that-s3-buckets-are-encrypted-with-kms-by-default#terraform)

### Other

[https://www.trendmicro.com/cloudoneconformity-staging/knowledge-base/aws/S3/encrypted-with-kms-customer-master-keys.html](https://www.trendmicro.com/cloudoneconformity-staging/knowledge-base/aws/S3/encrypted-with-kms-customer-master-keys.html)

## 参考資料

- [https://docs.aws.amazon.com/AmazonS3/latest/userguide/UsingKMSEncryption.html](https://docs.aws.amazon.com/AmazonS3/latest/userguide/UsingKMSEncryption.html)

## 技術情報

- Source Metadata：[sources/aws/s3_bucket_kms_encryption/metadata.json](../../sources/aws/s3_bucket_kms_encryption/metadata.json)
- Source Code：[sources/aws/s3_bucket_kms_encryption/check.py](../../sources/aws/s3_bucket_kms_encryption/check.py)
- Source Metadata Path：`sources/aws/s3_bucket_kms_encryption/metadata.json`
- Source Code Path：`sources/aws/s3_bucket_kms_encryption/check.py`
