# Check S3 Bucket Level Public Access Block.

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `s3_bucket_level_public_access_block` |
| クラウドプラットフォーム | AWS |
| サービス | s3 |
| 重大度 | medium |
| カテゴリ | Uncategorized |
| チェックタイプ | Data Protection |
| リソースタイプ | AwsS3Bucket |
| リソースグループ | storage |

## 説明

Check S3 Bucket Level Public Access Block.

## リスク

Public access policies may be applied to sensitive data buckets.

## 推奨事項

You can enable Public Access Block at the bucket level to prevent the exposure of your data stored in S3.

- 推奨リンク：[https://docs.aws.amazon.com/AmazonS3/latest/userguide/access-control-block-public-access.html](https://docs.aws.amazon.com/AmazonS3/latest/userguide/access-control-block-public-access.html)

## 修正手順


### CLI

```text
aws s3api put-public-access-block --region <REGION_NAME> --public-access-block-configuration BlockPublicAcls=true,IgnorePublicAcls=true,BlockPublicPolicy=true,RestrictPublicBuckets=true --bucket <BUCKET_NAME>
```

### Terraform

[https://docs.ST Cloud.com/checks/aws/s3-policies/bc_aws_s3_20#terraform](https://docs.ST Cloud.com/checks/aws/s3-policies/bc_aws_s3_20#terraform)

### Other

[https://github.com/cloudmatos/matos/tree/master/remediations/aws/s3/s3/block-public-access](https://github.com/cloudmatos/matos/tree/master/remediations/aws/s3/s3/block-public-access)

## 参考資料

- [https://docs.aws.amazon.com/AmazonS3/latest/userguide/access-control-block-public-access.html](https://docs.aws.amazon.com/AmazonS3/latest/userguide/access-control-block-public-access.html)

## 技術情報

- Source Metadata：[sources/aws/s3_bucket_level_public_access_block/metadata.json](../../sources/aws/s3_bucket_level_public_access_block/metadata.json)
- Source Code：[sources/aws/s3_bucket_level_public_access_block/check.py](../../sources/aws/s3_bucket_level_public_access_block/check.py)
- Source Metadata Path：`sources/aws/s3_bucket_level_public_access_block/metadata.json`
- Source Code Path：`sources/aws/s3_bucket_level_public_access_block/check.py`
