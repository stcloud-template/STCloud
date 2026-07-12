# Check if S3 buckets have server access logging enabled

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `s3_bucket_server_access_logging_enabled` |
| クラウドプラットフォーム | AWS |
| サービス | s3 |
| 重大度 | medium |
| カテゴリ | forensics-ready |
| チェックタイプ | Logging and Monitoring |
| リソースタイプ | AwsS3Bucket |
| リソースグループ | storage |

## 説明

Check if S3 buckets have server access logging enabled

## リスク

Server access logs can assist you in security and access audits, help you learn about your customer base, and understand your Amazon S3 bill.

## 推奨事項

Ensure that S3 buckets have Logging enabled. CloudTrail data events can be used in place of S3 bucket logging. If that is the case, this finding can be considered a false positive.

- 推奨リンク：[https://docs.aws.amazon.com/AmazonS3/latest/userguide/security-best-practices.html](https://docs.aws.amazon.com/AmazonS3/latest/userguide/security-best-practices.html)

## 修正手順


### CLI

```text
aws s3api put-bucket-logging --bucket <BUCKET_NAME> --bucket-logging-status <LOGGING_FILE_JSON>
```

### Terraform

[https://docs.ST Cloud.com/checks/aws/s3-policies/s3_13-enable-logging#terraform](https://docs.ST Cloud.com/checks/aws/s3-policies/s3_13-enable-logging#terraform)

### Other

[https://docs.ST Cloud.com/checks/aws/s3-policies/s3_13-enable-logging](https://docs.ST Cloud.com/checks/aws/s3-policies/s3_13-enable-logging)

## 参考資料

- [https://docs.aws.amazon.com/AmazonS3/latest/userguide/security-best-practices.html](https://docs.aws.amazon.com/AmazonS3/latest/userguide/security-best-practices.html)

## 技術情報

- Source Metadata：[sources/aws/s3_bucket_server_access_logging_enabled/metadata.json](../../sources/aws/s3_bucket_server_access_logging_enabled/metadata.json)
- Source Code：[sources/aws/s3_bucket_server_access_logging_enabled/check.py](../../sources/aws/s3_bucket_server_access_logging_enabled/check.py)
- Source Metadata Path：`sources/aws/s3_bucket_server_access_logging_enabled/metadata.json`
- Source Code Path：`sources/aws/s3_bucket_server_access_logging_enabled/check.py`
