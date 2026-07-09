# Check if S3 buckets have a Lifecycle configuration enabled

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `s3_bucket_lifecycle_enabled` |
| 云平台 | AWS |
| 服务 | s3 |
| 严重等级 | low |
| 类别 | Uncategorized |
| 检查类型 | AWS Foundational Security Best Practices |
| 资源类型 | AwsS3Bucket |
| 资源组 | storage |

## 描述

Check if S3 buckets have Lifecycle configuration enabled.

## 风险

The risks of not having lifecycle management enabled for S3 buckets include higher storage costs, unmanaged data retention, and potential non-compliance with data policies.

## 推荐措施

Enable lifecycle policies on your S3 buckets to automatically manage the transition and expiration of data.

- 推荐链接：[https://docs.aws.amazon.com/AmazonS3/latest/userguide/how-to-set-lifecycle-configuration-intro.html](https://docs.aws.amazon.com/AmazonS3/latest/userguide/how-to-set-lifecycle-configuration-intro.html)

## 修复步骤


### Terraform

[https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/S3/lifecycle-configuration.html](https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/S3/lifecycle-configuration.html)

### Other

[https://docs.aws.amazon.com/securityhub/latest/userguide/s3-controls.html#s3-13](https://docs.aws.amazon.com/securityhub/latest/userguide/s3-controls.html#s3-13)

## 参考资料

- [https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-lifecycle-mgmt.html](https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-lifecycle-mgmt.html)
- [https://docs.aws.amazon.com/AmazonS3/latest/userguide/how-to-set-lifecycle-configuration-intro.html](https://docs.aws.amazon.com/AmazonS3/latest/userguide/how-to-set-lifecycle-configuration-intro.html)

## 技术信息

- Source Metadata：[sources/aws/s3_bucket_lifecycle_enabled/metadata.json](../../sources/aws/s3_bucket_lifecycle_enabled/metadata.json)
- Source Code：[sources/aws/s3_bucket_lifecycle_enabled/check.py](../../sources/aws/s3_bucket_lifecycle_enabled/check.py)
- Source Metadata Path：`sources/aws/s3_bucket_lifecycle_enabled/metadata.json`
- Source Code Path：`sources/aws/s3_bucket_lifecycle_enabled/check.py`
