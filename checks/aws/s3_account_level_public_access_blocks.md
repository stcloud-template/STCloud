# Check S3 Account Level Public Access Block.

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `s3_account_level_public_access_blocks` |
| 云平台 | AWS |
| 服务 | s3 |
| 严重等级 | high |
| 类别 | Uncategorized |
| 检查类型 | Data Protection |
| 资源类型 | AwsS3AccountPublicAccessBlock |
| 资源组 | storage |

## 描述

Check S3 Account Level Public Access Block.

## 风险

Public access policies may be applied to sensitive data buckets.

## 推荐措施

You can enable Public Access Block at the account level to prevent the exposure of your data stored in S3.

- 推荐链接：[https://docs.aws.amazon.com/AmazonS3/latest/userguide/access-control-block-public-access.html](https://docs.aws.amazon.com/AmazonS3/latest/userguide/access-control-block-public-access.html)

## 修复步骤


### CLI

```text
aws s3control put-public-access-block --public-access-block-configuration BlockPublicAcls=true,IgnorePublicAcls=true,BlockPublicPolicy=true,RestrictPublicBuckets=true --account-id <account_id>
```

### Native IaC

[https://docs.ST Cloud.com/checks/aws/s3-policies/bc_aws_s3_21#cloudformation](https://docs.ST Cloud.com/checks/aws/s3-policies/bc_aws_s3_21#cloudformation)

### Terraform

[https://docs.ST Cloud.com/checks/aws/s3-policies/bc_aws_s3_21#terraform](https://docs.ST Cloud.com/checks/aws/s3-policies/bc_aws_s3_21#terraform)

### Other

[https://github.com/cloudmatos/matos/tree/master/remediations/aws/s3/s3control/block-public-access](https://github.com/cloudmatos/matos/tree/master/remediations/aws/s3/s3control/block-public-access)

## 参考资料

- [https://docs.aws.amazon.com/AmazonS3/latest/userguide/access-control-block-public-access.html](https://docs.aws.amazon.com/AmazonS3/latest/userguide/access-control-block-public-access.html)

## 技术信息

- Source Metadata：[sources/aws/s3_account_level_public_access_blocks/metadata.json](../../sources/aws/s3_account_level_public_access_blocks/metadata.json)
- Source Code：[sources/aws/s3_account_level_public_access_blocks/check.py](../../sources/aws/s3_account_level_public_access_blocks/check.py)
- Source Metadata Path：`sources/aws/s3_account_level_public_access_blocks/metadata.json`
- Source Code Path：`sources/aws/s3_account_level_public_access_blocks/check.py`
