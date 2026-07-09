# Check if S3 buckets have KMS encryption enabled.

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `s3_bucket_kms_encryption` |
| 云平台 | AWS |
| 服务 | s3 |
| 严重等级 | medium |
| 类别 | encryption |
| 检查类型 | Data Protection |
| 资源类型 | AwsS3Bucket |
| 资源组 | storage |

## 描述

Check if S3 buckets have KMS encryption enabled.

## 风险

Amazon S3 KMS encryption provides a way to set the encryption behavior for an S3 bucket using a managed key. This will ensure data-at-rest is encrypted.

## 推荐措施

Ensure that S3 buckets have encryption at rest enabled using KMS.

- 推荐链接：[https://docs.aws.amazon.com/AmazonS3/latest/userguide/UsingKMSEncryption.html](https://docs.aws.amazon.com/AmazonS3/latest/userguide/UsingKMSEncryption.html)

## 修复步骤


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

## 参考资料

- [https://docs.aws.amazon.com/AmazonS3/latest/userguide/UsingKMSEncryption.html](https://docs.aws.amazon.com/AmazonS3/latest/userguide/UsingKMSEncryption.html)

## 技术信息

- Source Metadata：[sources/aws/s3_bucket_kms_encryption/metadata.json](../../sources/aws/s3_bucket_kms_encryption/metadata.json)
- Source Code：[sources/aws/s3_bucket_kms_encryption/check.py](../../sources/aws/s3_bucket_kms_encryption/check.py)
- Source Metadata Path：`sources/aws/s3_bucket_kms_encryption/metadata.json`
- Source Code Path：`sources/aws/s3_bucket_kms_encryption/check.py`
