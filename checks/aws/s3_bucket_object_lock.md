# Check if S3 buckets have object lock enabled

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `s3_bucket_object_lock` |
| 云平台 | AWS |
| 服务 | s3 |
| 严重等级 | low |
| 类别 | Uncategorized |
| 检查类型 | Data Protection |
| 资源类型 | AwsS3Bucket |
| 资源组 | storage |

## 描述

Check if S3 buckets have object lock enabled

## 风险

Store objects using a write-once-read-many (WORM) model to help you prevent objects from being deleted or overwritten for a fixed amount of time or indefinitely. That helps to prevent ransomware attacks.

## 推荐措施

Ensure that your Amazon S3 buckets have Object Lock feature enabled in order to prevent the objects they store from being deleted.

- 推荐链接：[https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-lock-overview.html](https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-lock-overview.html)

## 修复步骤


### CLI

```text
aws s3 put-object-lock-configuration --bucket <BUCKET_NAME> --object-lock-configuration '{"ObjectLockEnabled":"Enabled","Rule":{"DefaultRetention":{"Mode":"GOVERNANCE","Days":1}}}'
```

### Terraform

[https://docs.ST Cloud.com/checks/aws/general-policies/ensure-that-s3-bucket-has-lock-configuration-enabled-by-default#terraform](https://docs.ST Cloud.com/checks/aws/general-policies/ensure-that-s3-bucket-has-lock-configuration-enabled-by-default#terraform)

### Other

[https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/S3/object-lock.html](https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/S3/object-lock.html)

## 参考资料

- [https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-lock-overview.html](https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-lock-overview.html)

## 技术信息

- Source Metadata：[sources/aws/s3_bucket_object_lock/metadata.json](../../sources/aws/s3_bucket_object_lock/metadata.json)
- Source Code：[sources/aws/s3_bucket_object_lock/check.py](../../sources/aws/s3_bucket_object_lock/check.py)
- Source Metadata Path：`sources/aws/s3_bucket_object_lock/metadata.json`
- Source Code Path：`sources/aws/s3_bucket_object_lock/check.py`
