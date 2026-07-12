# Check S3 Account Level Public Access Block.

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `s3_account_level_public_access_blocks` |
| クラウドプラットフォーム | AWS |
| サービス | s3 |
| 重大度 | high |
| カテゴリ | Uncategorized |
| チェックタイプ | Data Protection |
| リソースタイプ | AwsS3AccountPublicAccessBlock |
| リソースグループ | storage |

## 説明

Check S3 Account Level Public Access Block.

## リスク

Public access policies may be applied to sensitive data buckets.

## 推奨事項

You can enable Public Access Block at the account level to prevent the exposure of your data stored in S3.

- 推奨リンク：[https://docs.aws.amazon.com/AmazonS3/latest/userguide/access-control-block-public-access.html](https://docs.aws.amazon.com/AmazonS3/latest/userguide/access-control-block-public-access.html)

## 修正手順


### CLI

```text
aws s3control put-public-access-block --public-access-block-configuration BlockPublicAcls=true,IgnorePublicAcls=true,BlockPublicPolicy=true,RestrictPublicBuckets=true --account-id <account_id>
```

### Native IaC

[https://docs.ST Cloud.com/checks/aws/s3-policies/bc_aws_s3_21#cloudformation](https://docs.ST Cloud.com/checks/aws/s3-policies/bc_aws_s3_21#cloudformation)

### Terraform

[https://docs.ST Cloud.com/checks/aws/s3-policies/bc_aws_s3_21#terraform](https://docs.ST Cloud.com/checks/aws/s3-policies/bc_aws_s3_21#terraform)

### Other

[https://github.com/cloudmatos/matos/tree/master/remediations/aws/s3/s3control/block-public-access](https://github.com/cloudmatos/matos/tree/master/remediations/aws/s3/s3control/block-public-access)

## 参考資料

- [https://docs.aws.amazon.com/AmazonS3/latest/userguide/access-control-block-public-access.html](https://docs.aws.amazon.com/AmazonS3/latest/userguide/access-control-block-public-access.html)

## 技術情報

- Source Metadata：[sources/aws/s3_account_level_public_access_blocks/metadata.json](../../sources/aws/s3_account_level_public_access_blocks/metadata.json)
- Source Code：[sources/aws/s3_account_level_public_access_blocks/check.py](../../sources/aws/s3_account_level_public_access_blocks/check.py)
- Source Metadata Path：`sources/aws/s3_account_level_public_access_blocks/metadata.json`
- Source Code Path：`sources/aws/s3_account_level_public_access_blocks/check.py`
