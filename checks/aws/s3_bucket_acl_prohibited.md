# Check if S3 buckets have ACLs enabled

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `s3_bucket_acl_prohibited` |
| クラウドプラットフォーム | AWS |
| サービス | s3 |
| 重大度 | medium |
| カテゴリ | Uncategorized |
| チェックタイプ | Logging and Monitoring |
| リソースタイプ | AwsS3Bucket |
| リソースグループ | storage |

## 説明

Check if S3 buckets have ACLs enabled

## リスク

S3 ACLs are a legacy access control mechanism that predates IAM. IAM and bucket policies are currently the preferred methods.

## 推奨事項

Ensure that S3 ACLs are disabled (BucketOwnerEnforced). Use IAM policies and bucket policies to manage access.

- 推奨リンク：[https://docs.aws.amazon.com/AmazonS3/latest/userguide/about-object-ownership.html](https://docs.aws.amazon.com/AmazonS3/latest/userguide/about-object-ownership.html)

## 修正手順


### CLI

```text
aws s3api put-bucket-ownership-controls --bucket <bucket-name> --ownership-controls Rules=[{ObjectOwnership=BucketOwnerEnforced}]
```

### Native IaC

[https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-bucket-ownershipcontrols.html](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-bucket-ownershipcontrols.html)

## 参考資料

- [https://docs.aws.amazon.com/AmazonS3/latest/userguide/about-object-ownership.html](https://docs.aws.amazon.com/AmazonS3/latest/userguide/about-object-ownership.html)

## 技術情報

- Source Metadata：[sources/aws/s3_bucket_acl_prohibited/metadata.json](../../sources/aws/s3_bucket_acl_prohibited/metadata.json)
- Source Code：[sources/aws/s3_bucket_acl_prohibited/check.py](../../sources/aws/s3_bucket_acl_prohibited/check.py)
- Source Metadata Path：`sources/aws/s3_bucket_acl_prohibited/metadata.json`
- Source Code Path：`sources/aws/s3_bucket_acl_prohibited/check.py`
