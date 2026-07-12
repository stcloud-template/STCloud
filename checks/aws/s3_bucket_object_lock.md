# Check if S3 buckets have object lock enabled

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `s3_bucket_object_lock` |
| クラウドプラットフォーム | AWS |
| サービス | s3 |
| 重大度 | low |
| カテゴリ | Uncategorized |
| チェックタイプ | Data Protection |
| リソースタイプ | AwsS3Bucket |
| リソースグループ | storage |

## 説明

Check if S3 buckets have object lock enabled

## リスク

Store objects using a write-once-read-many (WORM) model to help you prevent objects from being deleted or overwritten for a fixed amount of time or indefinitely. That helps to prevent ransomware attacks.

## 推奨事項

Ensure that your Amazon S3 buckets have Object Lock feature enabled in order to prevent the objects they store from being deleted.

- 推奨リンク：[https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-lock-overview.html](https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-lock-overview.html)

## 修正手順


### CLI

```text
aws s3 put-object-lock-configuration --bucket <BUCKET_NAME> --object-lock-configuration '{"ObjectLockEnabled":"Enabled","Rule":{"DefaultRetention":{"Mode":"GOVERNANCE","Days":1}}}'
```

### Terraform

[https://docs.ST Cloud.com/checks/aws/general-policies/ensure-that-s3-bucket-has-lock-configuration-enabled-by-default#terraform](https://docs.ST Cloud.com/checks/aws/general-policies/ensure-that-s3-bucket-has-lock-configuration-enabled-by-default#terraform)

### Other

[https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/S3/object-lock.html](https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/S3/object-lock.html)

## 参考資料

- [https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-lock-overview.html](https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-lock-overview.html)

## 技術情報

- Source Metadata：[sources/aws/s3_bucket_object_lock/metadata.json](../../sources/aws/s3_bucket_object_lock/metadata.json)
- Source Code：[sources/aws/s3_bucket_object_lock/check.py](../../sources/aws/s3_bucket_object_lock/check.py)
- Source Metadata Path：`sources/aws/s3_bucket_object_lock/metadata.json`
- Source Code Path：`sources/aws/s3_bucket_object_lock/check.py`
