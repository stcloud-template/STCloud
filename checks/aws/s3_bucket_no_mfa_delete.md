# Check if S3 bucket MFA Delete is not enabled.

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `s3_bucket_no_mfa_delete` |
| 云平台 | AWS |
| 服务 | s3 |
| 严重等级 | medium |
| 类别 | Uncategorized |
| 检查类型 | Logging and Monitoring |
| 资源类型 | AwsS3Bucket |
| 资源组 | storage |

## 描述

Check if S3 bucket MFA Delete is not enabled.

## 风险

Your security credentials are compromised or unauthorized access is granted.

## 推荐措施

Adding MFA delete to an S3 bucket, requires additional authentication when you change the version state of your bucket or you delete and object version adding another layer of security in the event your security credentials are compromised or unauthorized access is granted.

- 推荐链接：[https://docs.aws.amazon.com/AmazonS3/latest/userguide/MultiFactorAuthenticationDelete.html](https://docs.aws.amazon.com/AmazonS3/latest/userguide/MultiFactorAuthenticationDelete.html)

## 修复步骤


### CLI

```text
aws s3api put-bucket-versioning --profile my-root-profile --bucket my-bucket-name --versioning-configuration Status=Enabled,MFADelete=Enabled --mfa 'arn:aws:iam::00000000:mfa/root-account-mfa-device 123456'
```

### Terraform

[https://docs.ST Cloud.com/checks/aws/s3-policies/bc_aws_s3_24#terraform](https://docs.ST Cloud.com/checks/aws/s3-policies/bc_aws_s3_24#terraform)

## 参考资料

- [https://docs.aws.amazon.com/AmazonS3/latest/userguide/MultiFactorAuthenticationDelete.html](https://docs.aws.amazon.com/AmazonS3/latest/userguide/MultiFactorAuthenticationDelete.html)

## 技术信息

- Source Metadata：[sources/aws/s3_bucket_no_mfa_delete/metadata.json](../../sources/aws/s3_bucket_no_mfa_delete/metadata.json)
- Source Code：[sources/aws/s3_bucket_no_mfa_delete/check.py](../../sources/aws/s3_bucket_no_mfa_delete/check.py)
- Source Metadata Path：`sources/aws/s3_bucket_no_mfa_delete/metadata.json`
- Source Code Path：`sources/aws/s3_bucket_no_mfa_delete/check.py`
