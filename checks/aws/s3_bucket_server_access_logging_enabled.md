# Check if S3 buckets have server access logging enabled

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `s3_bucket_server_access_logging_enabled` |
| 云平台 | AWS |
| 服务 | s3 |
| 严重等级 | medium |
| 类别 | forensics-ready |
| 检查类型 | Logging and Monitoring |
| 资源类型 | AwsS3Bucket |
| 资源组 | storage |

## 描述

Check if S3 buckets have server access logging enabled

## 风险

Server access logs can assist you in security and access audits, help you learn about your customer base, and understand your Amazon S3 bill.

## 推荐措施

Ensure that S3 buckets have Logging enabled. CloudTrail data events can be used in place of S3 bucket logging. If that is the case, this finding can be considered a false positive.

- 推荐链接：[https://docs.aws.amazon.com/AmazonS3/latest/userguide/security-best-practices.html](https://docs.aws.amazon.com/AmazonS3/latest/userguide/security-best-practices.html)

## 修复步骤


### CLI

```text
aws s3api put-bucket-logging --bucket <BUCKET_NAME> --bucket-logging-status <LOGGING_FILE_JSON>
```

### Terraform

[https://docs.ST Cloud.com/checks/aws/s3-policies/s3_13-enable-logging#terraform](https://docs.ST Cloud.com/checks/aws/s3-policies/s3_13-enable-logging#terraform)

### Other

[https://docs.ST Cloud.com/checks/aws/s3-policies/s3_13-enable-logging](https://docs.ST Cloud.com/checks/aws/s3-policies/s3_13-enable-logging)

## 参考资料

- [https://docs.aws.amazon.com/AmazonS3/latest/userguide/security-best-practices.html](https://docs.aws.amazon.com/AmazonS3/latest/userguide/security-best-practices.html)

## 技术信息

- Source Metadata：[sources/aws/s3_bucket_server_access_logging_enabled/metadata.json](../../sources/aws/s3_bucket_server_access_logging_enabled/metadata.json)
- Source Code：[sources/aws/s3_bucket_server_access_logging_enabled/check.py](../../sources/aws/s3_bucket_server_access_logging_enabled/check.py)
- Source Metadata Path：`sources/aws/s3_bucket_server_access_logging_enabled/metadata.json`
- Source Code Path：`sources/aws/s3_bucket_server_access_logging_enabled/check.py`
