# Check if S3 buckets have policies which allow WRITE access.

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `s3_bucket_policy_public_write_access` |
| 云平台 | AWS |
| 服务 | s3 |
| 严重等级 | critical |
| 类别 | internet-exposed |
| 检查类型 | IAM |
| 资源类型 | AwsS3Bucket |
| 资源组 | storage |

## 描述

Check if S3 buckets have policies which allow WRITE access.

## 风险

Non intended users can put objects in a given bucket.

## 推荐措施

Ensure proper bucket policy is in place with the least privilege principle applied.

- 推荐链接：[https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_examples_s3_rw-bucket.html](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_examples_s3_rw-bucket.html)

## 修复步骤


### Other

[https://docs.ST Cloud.com/checks/aws/s3-policies/s3_18-write-permissions-public#aws-console](https://docs.ST Cloud.com/checks/aws/s3-policies/s3_18-write-permissions-public#aws-console)

## 参考资料

- [https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_examples_s3_rw-bucket.html](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_examples_s3_rw-bucket.html)

## 技术信息

- Source Metadata：[sources/aws/s3_bucket_policy_public_write_access/metadata.json](../../sources/aws/s3_bucket_policy_public_write_access/metadata.json)
- Source Code：[sources/aws/s3_bucket_policy_public_write_access/check.py](../../sources/aws/s3_bucket_policy_public_write_access/check.py)
- Source Metadata Path：`sources/aws/s3_bucket_policy_public_write_access/metadata.json`
- Source Code Path：`sources/aws/s3_bucket_policy_public_write_access/check.py`
