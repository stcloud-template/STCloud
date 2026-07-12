# Check if S3 buckets use cross region replication.

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `s3_bucket_cross_region_replication` |
| クラウドプラットフォーム | AWS |
| サービス | s3 |
| 重大度 | low |
| カテゴリ | redundancy |
| チェックタイプ | Secure access management |
| リソースタイプ | AwsS3Bucket |
| リソースグループ | storage |

## 説明

Verifying whether S3 buckets have cross-region replication enabled, ensuring data redundancy and availability across multiple AWS regions

## リスク

Without cross-region replication in S3 buckets, data is at risk of being lost or inaccessible if an entire region goes down, leading to potential service disruptions and data unavailability.

## 推奨事項

Ensure that S3 buckets have cross region replication.

- 推奨リンク：[https://docs.aws.amazon.com/AmazonS3/latest/userguide/replication-walkthrough1.html](https://docs.aws.amazon.com/AmazonS3/latest/userguide/replication-walkthrough1.html)

## 修正手順


### Terraform

[https://docs.ST Cloud.com/checks/aws/general-policies/ensure-that-s3-bucket-has-cross-region-replication-enabled#terraform](https://docs.ST Cloud.com/checks/aws/general-policies/ensure-that-s3-bucket-has-cross-region-replication-enabled#terraform)

### Other

[https://docs.aws.amazon.com/securityhub/latest/userguide/s3-controls.html#s3-7](https://docs.aws.amazon.com/securityhub/latest/userguide/s3-controls.html#s3-7)

## 参考資料

- [https://docs.aws.amazon.com/AmazonS3/latest/userguide/replication.html](https://docs.aws.amazon.com/AmazonS3/latest/userguide/replication.html)
- [https://docs.aws.amazon.com/AmazonS3/latest/userguide/replication-walkthrough1.html](https://docs.aws.amazon.com/AmazonS3/latest/userguide/replication-walkthrough1.html)

## 技術情報

- Source Metadata：[sources/aws/s3_bucket_cross_region_replication/metadata.json](../../sources/aws/s3_bucket_cross_region_replication/metadata.json)
- Source Code：[sources/aws/s3_bucket_cross_region_replication/check.py](../../sources/aws/s3_bucket_cross_region_replication/check.py)
- Source Metadata Path：`sources/aws/s3_bucket_cross_region_replication/metadata.json`
- Source Code Path：`sources/aws/s3_bucket_cross_region_replication/check.py`
