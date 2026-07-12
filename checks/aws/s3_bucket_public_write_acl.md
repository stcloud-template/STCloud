# Ensure there are no S3 buckets writable by Everyone or Any AWS customer.

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `s3_bucket_public_write_acl` |
| クラウドプラットフォーム | AWS |
| サービス | s3 |
| 重大度 | critical |
| カテゴリ | internet-exposed |
| チェックタイプ | Data Protection |
| リソースタイプ | AwsS3Bucket |
| リソースグループ | storage |

## 説明

Ensure there are no S3 buckets writable by Everyone or Any AWS customer.

## リスク

Even if you enable all possible bucket ACL options available in the Amazon S3 console the ACL alone does not allow everyone to download objects from your bucket. Depending on which option you select any user could perform some actions.

## 推奨事項

You can enable block public access settings only for access points, buckets and AWS accounts. Amazon S3 does not support block public access settings on a per-object basis. When you apply block public access settings to an account, the settings apply to all AWS Regions globally. The settings might not take effect in all Regions immediately or simultaneously, but they eventually propagate to all Regions.

- 推奨リンク：[https://docs.aws.amazon.com/AmazonS3/latest/userguide/access-control-block-public-access.html](https://docs.aws.amazon.com/AmazonS3/latest/userguide/access-control-block-public-access.html)

## 修正手順


### CLI

```text
aws s3api put-bucket-acl --bucket <bucket_name> --acl private
```

### Native IaC

[https://www.trendmicro.com/cloudoneconformity-staging/knowledge-base/aws/S3/s3-bucket-public-write-access.html](https://www.trendmicro.com/cloudoneconformity-staging/knowledge-base/aws/S3/s3-bucket-public-write-access.html)

### Terraform

[https://www.trendmicro.com/cloudoneconformity-staging/knowledge-base/aws/S3/s3-bucket-public-write-access.html](https://www.trendmicro.com/cloudoneconformity-staging/knowledge-base/aws/S3/s3-bucket-public-write-access.html)

## 参考資料

- [https://docs.aws.amazon.com/AmazonS3/latest/userguide/access-control-block-public-access.html](https://docs.aws.amazon.com/AmazonS3/latest/userguide/access-control-block-public-access.html)

## 技術情報

- Source Metadata：[sources/aws/s3_bucket_public_write_acl/metadata.json](../../sources/aws/s3_bucket_public_write_acl/metadata.json)
- Source Code：[sources/aws/s3_bucket_public_write_acl/check.py](../../sources/aws/s3_bucket_public_write_acl/check.py)
- Source Metadata Path：`sources/aws/s3_bucket_public_write_acl/metadata.json`
- Source Code Path：`sources/aws/s3_bucket_public_write_acl/check.py`
