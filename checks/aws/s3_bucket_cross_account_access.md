# Ensure that general-purpose bucket policies restrict access to other AWS accounts.

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `s3_bucket_cross_account_access` |
| 云平台 | AWS |
| 服务 | s3 |
| 严重等级 | high |
| 类别 | Uncategorized |
| 检查类型 | Effects/Data Exposure |
| 资源类型 | AwsS3Bucket |
| 资源组 | storage |

## 描述

This check verifies that S3 bucket policies are configured in a way that limits access to the intended AWS accounts only, preventing unauthorized access by external or unintended accounts.

## 风险

Allowing other AWS accounts to perform sensitive actions (e.g., modifying bucket policies, ACLs, or encryption settings) on your S3 buckets can lead to data exposure, unauthorized access, or misconfigurations, increasing the risk of insider threats or attacks.

## 推荐措施

Review and update your S3 bucket policies to remove permissions that grant external AWS accounts access to critical actions and implement least privilege principles to ensure sensitive operations are restricted to trusted accounts only

- 推荐链接：[https://docs.aws.amazon.com/AmazonS3/latest/userguide/access-control-block-public-access.html](https://docs.aws.amazon.com/AmazonS3/latest/userguide/access-control-block-public-access.html)

## 修复步骤


### Other

[https://docs.aws.amazon.com/securityhub/latest/userguide/s3-controls.html#s3-6](https://docs.aws.amazon.com/securityhub/latest/userguide/s3-controls.html#s3-6)

## 参考资料

- [https://docs.aws.amazon.com/AmazonS3/latest/userguide/access-control-block-public-access.html](https://docs.aws.amazon.com/AmazonS3/latest/userguide/access-control-block-public-access.html)

## 技术信息

- Source Metadata：[sources/aws/s3_bucket_cross_account_access/metadata.json](../../sources/aws/s3_bucket_cross_account_access/metadata.json)
- Source Code：[sources/aws/s3_bucket_cross_account_access/check.py](../../sources/aws/s3_bucket_cross_account_access/check.py)
- Source Metadata Path：`sources/aws/s3_bucket_cross_account_access/metadata.json`
- Source Code Path：`sources/aws/s3_bucket_cross_account_access/check.py`
