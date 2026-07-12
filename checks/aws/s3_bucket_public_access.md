# Ensure there are no S3 buckets open to Everyone or Any AWS user.

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `s3_bucket_public_access` |
| クラウドプラットフォーム | AWS |
| サービス | s3 |
| 重大度 | critical |
| カテゴリ | internet-exposed |
| チェックタイプ | Data Protection |
| リソースタイプ | AwsS3Bucket |
| リソースグループ | storage |

## 説明

Ensure there are no S3 buckets open to Everyone or Any AWS user.

## リスク

Even if you enable all possible bucket ACL options available in the Amazon S3 console the ACL alone does not allow everyone to download objects from your bucket. Depending on which option you select any user could perform some actions.

## 推奨事項

You can enable block public access settings only for access points, buckets and AWS accounts. Amazon S3 does not support block public access settings on a per-object basis. When you apply block public access settings to an account, the settings apply to all AWS Regions globally. The settings might not take effect in all Regions immediately or simultaneously, but they eventually propagate to all Regions.

- 推奨リンク：[https://docs.aws.amazon.com/AmazonS3/latest/userguide/access-control-block-public-access.html](https://docs.aws.amazon.com/AmazonS3/latest/userguide/access-control-block-public-access.html)

## 修正手順


### CLI

```text
aws s3api put-public-access-block --public-access-block-configuration BlockPublicAcls=true,IgnorePublicAcls=true,BlockPublicPolicy=true,RestrictPublicBuckets=true --bucket <bucket_name>
```

### Terraform

[https://docs.ST Cloud.com/checks/aws/networking-policies/s3-bucket-should-have-public-access-blocks-defaults-to-false-if-the-public-access-block-is-not-attached#terraform](https://docs.ST Cloud.com/checks/aws/networking-policies/s3-bucket-should-have-public-access-blocks-defaults-to-false-if-the-public-access-block-is-not-attached#terraform)

### Other

[https://github.com/cloudmatos/matos/tree/master/remediations/aws/s3/s3/block-public-access](https://github.com/cloudmatos/matos/tree/master/remediations/aws/s3/s3/block-public-access)

## 参考資料

- [https://docs.aws.amazon.com/AmazonS3/latest/userguide/access-control-block-public-access.html](https://docs.aws.amazon.com/AmazonS3/latest/userguide/access-control-block-public-access.html)

## 技術情報

- Source Metadata：[sources/aws/s3_bucket_public_access/metadata.json](../../sources/aws/s3_bucket_public_access/metadata.json)
- Source Code：[sources/aws/s3_bucket_public_access/check.py](../../sources/aws/s3_bucket_public_access/check.py)
- Source Metadata Path：`sources/aws/s3_bucket_public_access/metadata.json`
- Source Code Path：`sources/aws/s3_bucket_public_access/check.py`
