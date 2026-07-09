# Check if S3 buckets use cross region replication.

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `s3_bucket_cross_region_replication` |
| 云平台 | AWS |
| 服务 | s3 |
| 严重等级 | low |
| 类别 | redundancy |
| 检查类型 | Secure access management |
| 资源类型 | AwsS3Bucket |
| 资源组 | storage |

## 描述

Verifying whether S3 buckets have cross-region replication enabled, ensuring data redundancy and availability across multiple AWS regions

## 风险

Without cross-region replication in S3 buckets, data is at risk of being lost or inaccessible if an entire region goes down, leading to potential service disruptions and data unavailability.

## 推荐措施

Ensure that S3 buckets have cross region replication.

- 推荐链接：[https://docs.aws.amazon.com/AmazonS3/latest/userguide/replication-walkthrough1.html](https://docs.aws.amazon.com/AmazonS3/latest/userguide/replication-walkthrough1.html)

## 修复步骤


### Terraform

[https://docs.ST Cloud.com/checks/aws/general-policies/ensure-that-s3-bucket-has-cross-region-replication-enabled#terraform](https://docs.ST Cloud.com/checks/aws/general-policies/ensure-that-s3-bucket-has-cross-region-replication-enabled#terraform)

### Other

[https://docs.aws.amazon.com/securityhub/latest/userguide/s3-controls.html#s3-7](https://docs.aws.amazon.com/securityhub/latest/userguide/s3-controls.html#s3-7)

## 参考资料

- [https://docs.aws.amazon.com/AmazonS3/latest/userguide/replication.html](https://docs.aws.amazon.com/AmazonS3/latest/userguide/replication.html)
- [https://docs.aws.amazon.com/AmazonS3/latest/userguide/replication-walkthrough1.html](https://docs.aws.amazon.com/AmazonS3/latest/userguide/replication-walkthrough1.html)

## 技术信息

- Source Metadata：[sources/aws/s3_bucket_cross_region_replication/metadata.json](../../sources/aws/s3_bucket_cross_region_replication/metadata.json)
- Source Code：[sources/aws/s3_bucket_cross_region_replication/check.py](../../sources/aws/s3_bucket_cross_region_replication/check.py)
- Source Metadata Path：`sources/aws/s3_bucket_cross_region_replication/metadata.json`
- Source Code Path：`sources/aws/s3_bucket_cross_region_replication/check.py`
