# Check if S3 buckets have ACLs enabled

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `s3_bucket_acl_prohibited` |
| 云平台 | AWS |
| 服务 | s3 |
| 严重等级 | medium |
| 类别 | Uncategorized |
| 检查类型 | Logging and Monitoring |
| 资源类型 | AwsS3Bucket |
| 资源组 | storage |

## 描述

Check if S3 buckets have ACLs enabled

## 风险

S3 ACLs are a legacy access control mechanism that predates IAM. IAM and bucket policies are currently the preferred methods.

## 推荐措施

Ensure that S3 ACLs are disabled (BucketOwnerEnforced). Use IAM policies and bucket policies to manage access.

- 推荐链接：[https://docs.aws.amazon.com/AmazonS3/latest/userguide/about-object-ownership.html](https://docs.aws.amazon.com/AmazonS3/latest/userguide/about-object-ownership.html)

## 修复步骤


### CLI

```text
aws s3api put-bucket-ownership-controls --bucket <bucket-name> --ownership-controls Rules=[{ObjectOwnership=BucketOwnerEnforced}]
```

### Native IaC

[https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-bucket-ownershipcontrols.html](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-bucket-ownershipcontrols.html)

## 参考资料

- [https://docs.aws.amazon.com/AmazonS3/latest/userguide/about-object-ownership.html](https://docs.aws.amazon.com/AmazonS3/latest/userguide/about-object-ownership.html)

## 技术信息

- Source Metadata：[sources/aws/s3_bucket_acl_prohibited/metadata.json](../../sources/aws/s3_bucket_acl_prohibited/metadata.json)
- Source Code：[sources/aws/s3_bucket_acl_prohibited/check.py](../../sources/aws/s3_bucket_acl_prohibited/check.py)
- Source Metadata Path：`sources/aws/s3_bucket_acl_prohibited/metadata.json`
- Source Code Path：`sources/aws/s3_bucket_acl_prohibited/check.py`
