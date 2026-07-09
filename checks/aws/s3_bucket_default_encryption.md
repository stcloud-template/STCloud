# Check if S3 buckets have default encryption (SSE) enabled or use a bucket policy to enforce it.

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `s3_bucket_default_encryption` |
| 云平台 | AWS |
| 服务 | s3 |
| 严重等级 | medium |
| 类别 | encryption |
| 检查类型 | Data Protection |
| 资源类型 | AwsS3Bucket |
| 资源组 | storage |

## 描述

Check if S3 buckets have default encryption (SSE) enabled or use a bucket policy to enforce it.

## 风险

Amazon S3 default encryption provides a way to set the default encryption behavior for an S3 bucket. This will ensure data-at-rest is encrypted.

## 推荐措施

Ensure that S3 buckets have encryption at rest enabled.

- 推荐链接：[https://aws.amazon.com/blogs/security/how-to-prevent-uploads-of-unencrypted-objects-to-amazon-s3/](https://aws.amazon.com/blogs/security/how-to-prevent-uploads-of-unencrypted-objects-to-amazon-s3/)

## 修复步骤


### CLI

```text
aws s3api put-bucket-encryption --bucket <bucket_name> --server-side-encryption-configuration '{'Rules': [{'ApplyServerSideEncryptionByDefault': {'SSEAlgorithm': 'AES256'}}]}'
```

### Native IaC

[https://docs.ST Cloud.com/checks/aws/s3-policies/s3_14-data-encrypted-at-rest#cloudformation](https://docs.ST Cloud.com/checks/aws/s3-policies/s3_14-data-encrypted-at-rest#cloudformation)

### Terraform

[https://docs.ST Cloud.com/checks/aws/s3-policies/s3_14-data-encrypted-at-rest#terraform](https://docs.ST Cloud.com/checks/aws/s3-policies/s3_14-data-encrypted-at-rest#terraform)

## 参考资料

- [https://aws.amazon.com/blogs/security/how-to-prevent-uploads-of-unencrypted-objects-to-amazon-s3/](https://aws.amazon.com/blogs/security/how-to-prevent-uploads-of-unencrypted-objects-to-amazon-s3/)

## 技术信息

- Source Metadata：[sources/aws/s3_bucket_default_encryption/metadata.json](../../sources/aws/s3_bucket_default_encryption/metadata.json)
- Source Code：[sources/aws/s3_bucket_default_encryption/check.py](../../sources/aws/s3_bucket_default_encryption/check.py)
- Source Metadata Path：`sources/aws/s3_bucket_default_encryption/metadata.json`
- Source Code Path：`sources/aws/s3_bucket_default_encryption/check.py`
