# Check if S3 buckets have policies which allow WRITE access.

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `s3_bucket_policy_public_write_access` |
| クラウドプラットフォーム | AWS |
| サービス | s3 |
| 重大度 | critical |
| カテゴリ | internet-exposed |
| チェックタイプ | IAM |
| リソースタイプ | AwsS3Bucket |
| リソースグループ | storage |

## 説明

Check if S3 buckets have policies which allow WRITE access.

## リスク

Non intended users can put objects in a given bucket.

## 推奨事項

Ensure proper bucket policy is in place with the least privilege principle applied.

- 推奨リンク：[https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_examples_s3_rw-bucket.html](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_examples_s3_rw-bucket.html)

## 修正手順


### Other

[https://docs.ST Cloud.com/checks/aws/s3-policies/s3_18-write-permissions-public#aws-console](https://docs.ST Cloud.com/checks/aws/s3-policies/s3_18-write-permissions-public#aws-console)

## 参考資料

- [https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_examples_s3_rw-bucket.html](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_examples_s3_rw-bucket.html)

## 技術情報

- Source Metadata：[sources/aws/s3_bucket_policy_public_write_access/metadata.json](../../sources/aws/s3_bucket_policy_public_write_access/metadata.json)
- Source Code：[sources/aws/s3_bucket_policy_public_write_access/check.py](../../sources/aws/s3_bucket_policy_public_write_access/check.py)
- Source Metadata Path：`sources/aws/s3_bucket_policy_public_write_access/metadata.json`
- Source Code Path：`sources/aws/s3_bucket_policy_public_write_access/check.py`
