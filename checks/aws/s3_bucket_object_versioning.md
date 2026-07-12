# Check if S3 buckets have object versioning enabled

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `s3_bucket_object_versioning` |
| クラウドプラットフォーム | AWS |
| サービス | s3 |
| 重大度 | medium |
| カテゴリ | Uncategorized |
| チェックタイプ | Data Protection |
| リソースタイプ | AwsS3Bucket |
| リソースグループ | storage |

## 説明

Check if S3 buckets have object versioning enabled

## リスク

With versioning, you can easily recover from both unintended user actions and application failures.

## 推奨事項

Configure versioning using the Amazon console or API for buckets with sensitive information that is changing frequently, and backup may not be enough to capture all the changes.

- 推奨リンク：[https://docs.aws.amazon.com/AmazonS3/latest/userguide/Versioning.html](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Versioning.html)

## 修正手順


### Terraform

[https://docs.ST Cloud.com/checks/aws/s3-policies/s3_16-enable-versioning#terraform](https://docs.ST Cloud.com/checks/aws/s3-policies/s3_16-enable-versioning#terraform)

### Other

[https://docs.ST Cloud.com/checks/aws/s3-policies/s3_16-enable-versioning#aws-console](https://docs.ST Cloud.com/checks/aws/s3-policies/s3_16-enable-versioning#aws-console)

## 参考資料

- [https://docs.aws.amazon.com/AmazonS3/latest/userguide/Versioning.html](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Versioning.html)

## 技術情報

- Source Metadata：[sources/aws/s3_bucket_object_versioning/metadata.json](../../sources/aws/s3_bucket_object_versioning/metadata.json)
- Source Code：[sources/aws/s3_bucket_object_versioning/check.py](../../sources/aws/s3_bucket_object_versioning/check.py)
- Source Metadata Path：`sources/aws/s3_bucket_object_versioning/metadata.json`
- Source Code Path：`sources/aws/s3_bucket_object_versioning/check.py`
