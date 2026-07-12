# Check if S3 buckets have a Lifecycle configuration enabled

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `s3_bucket_lifecycle_enabled` |
| クラウドプラットフォーム | AWS |
| サービス | s3 |
| 重大度 | low |
| カテゴリ | Uncategorized |
| チェックタイプ | AWS Foundational Security Best Practices |
| リソースタイプ | AwsS3Bucket |
| リソースグループ | storage |

## 説明

Check if S3 buckets have Lifecycle configuration enabled.

## リスク

The risks of not having lifecycle management enabled for S3 buckets include higher storage costs, unmanaged data retention, and potential non-compliance with data policies.

## 推奨事項

Enable lifecycle policies on your S3 buckets to automatically manage the transition and expiration of data.

- 推奨リンク：[https://docs.aws.amazon.com/AmazonS3/latest/userguide/how-to-set-lifecycle-configuration-intro.html](https://docs.aws.amazon.com/AmazonS3/latest/userguide/how-to-set-lifecycle-configuration-intro.html)

## 修正手順


### Terraform

[https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/S3/lifecycle-configuration.html](https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/S3/lifecycle-configuration.html)

### Other

[https://docs.aws.amazon.com/securityhub/latest/userguide/s3-controls.html#s3-13](https://docs.aws.amazon.com/securityhub/latest/userguide/s3-controls.html#s3-13)

## 参考資料

- [https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-lifecycle-mgmt.html](https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-lifecycle-mgmt.html)
- [https://docs.aws.amazon.com/AmazonS3/latest/userguide/how-to-set-lifecycle-configuration-intro.html](https://docs.aws.amazon.com/AmazonS3/latest/userguide/how-to-set-lifecycle-configuration-intro.html)

## 技術情報

- Source Metadata：[sources/aws/s3_bucket_lifecycle_enabled/metadata.json](../../sources/aws/s3_bucket_lifecycle_enabled/metadata.json)
- Source Code：[sources/aws/s3_bucket_lifecycle_enabled/check.py](../../sources/aws/s3_bucket_lifecycle_enabled/check.py)
- Source Metadata Path：`sources/aws/s3_bucket_lifecycle_enabled/metadata.json`
- Source Code Path：`sources/aws/s3_bucket_lifecycle_enabled/check.py`
