# Check if S3 buckets have object versioning enabled

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `s3_bucket_object_versioning` |
| 云平台 | AWS |
| 服务 | s3 |
| 严重等级 | medium |
| 类别 | Uncategorized |
| 检查类型 | Data Protection |
| 资源类型 | AwsS3Bucket |
| 资源组 | storage |

## 描述

Check if S3 buckets have object versioning enabled

## 风险

With versioning, you can easily recover from both unintended user actions and application failures.

## 推荐措施

Configure versioning using the Amazon console or API for buckets with sensitive information that is changing frequently, and backup may not be enough to capture all the changes.

- 推荐链接：[https://docs.aws.amazon.com/AmazonS3/latest/userguide/Versioning.html](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Versioning.html)

## 修复步骤


### Terraform

[https://docs.ST Cloud.com/checks/aws/s3-policies/s3_16-enable-versioning#terraform](https://docs.ST Cloud.com/checks/aws/s3-policies/s3_16-enable-versioning#terraform)

### Other

[https://docs.ST Cloud.com/checks/aws/s3-policies/s3_16-enable-versioning#aws-console](https://docs.ST Cloud.com/checks/aws/s3-policies/s3_16-enable-versioning#aws-console)

## 参考资料

- [https://docs.aws.amazon.com/AmazonS3/latest/userguide/Versioning.html](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Versioning.html)

## 技术信息

- Source Metadata：[sources/aws/s3_bucket_object_versioning/metadata.json](../../sources/aws/s3_bucket_object_versioning/metadata.json)
- Source Code：[sources/aws/s3_bucket_object_versioning/check.py](../../sources/aws/s3_bucket_object_versioning/check.py)
- Source Metadata Path：`sources/aws/s3_bucket_object_versioning/metadata.json`
- Source Code Path：`sources/aws/s3_bucket_object_versioning/check.py`
