# Ensure there are no S3 buckets listable by Everyone or Any AWS customer.

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `s3_bucket_public_list_acl` |
| 云平台 | AWS |
| 服务 | s3 |
| 严重等级 | critical |
| 类别 | internet-exposed |
| 检查类型 | Data Protection |
| 资源类型 | AwsS3Bucket |
| 资源组 | storage |

## 描述

Ensure there are no S3 buckets listable by Everyone or Any AWS customer.

## 风险

Even if you enable all possible bucket ACL options available in the Amazon S3 console the ACL alone does not allow everyone to download objects from your bucket. Depending on which option you select any user could perform some actions.

## 推荐措施

You can enable block public access settings only for access points, buckets and AWS accounts. Amazon S3 does not support block public access settings on a per-object basis. When you apply block public access settings to an account, the settings apply to all AWS Regions globally. The settings might not take effect in all Regions immediately or simultaneously, but they eventually propagate to all Regions.

- 推荐链接：[https://docs.aws.amazon.com/AmazonS3/latest/userguide/access-control-block-public-access.html](https://docs.aws.amazon.com/AmazonS3/latest/userguide/access-control-block-public-access.html)

## 修复步骤


### CLI

```text
aws s3api put-bucket-acl --bucket <bucket_name> --acl private
```

### Native IaC

[https://www.trendmicro.com/cloudoneconformity-staging/knowledge-base/aws/S3/s3-bucket-public-read-access.html](https://www.trendmicro.com/cloudoneconformity-staging/knowledge-base/aws/S3/s3-bucket-public-read-access.html)

### Terraform

[https://www.trendmicro.com/cloudoneconformity-staging/knowledge-base/aws/S3/s3-bucket-public-read-access.html](https://www.trendmicro.com/cloudoneconformity-staging/knowledge-base/aws/S3/s3-bucket-public-read-access.html)

## 参考资料

- [https://docs.aws.amazon.com/AmazonS3/latest/userguide/access-control-block-public-access.html](https://docs.aws.amazon.com/AmazonS3/latest/userguide/access-control-block-public-access.html)

## 技术信息

- Source Metadata：[sources/aws/s3_bucket_public_list_acl/metadata.json](../../sources/aws/s3_bucket_public_list_acl/metadata.json)
- Source Code：[sources/aws/s3_bucket_public_list_acl/check.py](../../sources/aws/s3_bucket_public_list_acl/check.py)
- Source Metadata Path：`sources/aws/s3_bucket_public_list_acl/metadata.json`
- Source Code Path：`sources/aws/s3_bucket_public_list_acl/check.py`
