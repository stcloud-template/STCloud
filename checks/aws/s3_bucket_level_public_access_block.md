# Check S3 Bucket Level Public Access Block.

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `s3_bucket_level_public_access_block` |
| 云平台 | AWS |
| 服务 | s3 |
| 严重等级 | medium |
| 类别 | Uncategorized |
| 检查类型 | Data Protection |
| 资源类型 | AwsS3Bucket |
| 资源组 | storage |

## 描述

Check S3 Bucket Level Public Access Block.

## 风险

Public access policies may be applied to sensitive data buckets.

## 推荐措施

You can enable Public Access Block at the bucket level to prevent the exposure of your data stored in S3.

- 推荐链接：[https://docs.aws.amazon.com/AmazonS3/latest/userguide/access-control-block-public-access.html](https://docs.aws.amazon.com/AmazonS3/latest/userguide/access-control-block-public-access.html)

## 修复步骤


### CLI

```text
aws s3api put-public-access-block --region <REGION_NAME> --public-access-block-configuration BlockPublicAcls=true,IgnorePublicAcls=true,BlockPublicPolicy=true,RestrictPublicBuckets=true --bucket <BUCKET_NAME>
```

### Terraform

[https://docs.ST Cloud.com/checks/aws/s3-policies/bc_aws_s3_20#terraform](https://docs.ST Cloud.com/checks/aws/s3-policies/bc_aws_s3_20#terraform)

### Other

[https://github.com/cloudmatos/matos/tree/master/remediations/aws/s3/s3/block-public-access](https://github.com/cloudmatos/matos/tree/master/remediations/aws/s3/s3/block-public-access)

## 参考资料

- [https://docs.aws.amazon.com/AmazonS3/latest/userguide/access-control-block-public-access.html](https://docs.aws.amazon.com/AmazonS3/latest/userguide/access-control-block-public-access.html)

## 技术信息

- Source Metadata：[sources/aws/s3_bucket_level_public_access_block/metadata.json](../../sources/aws/s3_bucket_level_public_access_block/metadata.json)
- Source Code：[sources/aws/s3_bucket_level_public_access_block/check.py](../../sources/aws/s3_bucket_level_public_access_block/check.py)
- Source Metadata Path：`sources/aws/s3_bucket_level_public_access_block/metadata.json`
- Source Code Path：`sources/aws/s3_bucket_level_public_access_block/check.py`
