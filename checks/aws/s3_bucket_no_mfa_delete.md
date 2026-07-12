# Check if S3 bucket MFA Delete is not enabled.

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `s3_bucket_no_mfa_delete` |
| クラウドプラットフォーム | AWS |
| サービス | s3 |
| 重大度 | medium |
| カテゴリ | Uncategorized |
| チェックタイプ | Logging and Monitoring |
| リソースタイプ | AwsS3Bucket |
| リソースグループ | storage |

## 説明

Check if S3 bucket MFA Delete is not enabled.

## リスク

Your security credentials are compromised or unauthorized access is granted.

## 推奨事項

Adding MFA delete to an S3 bucket, requires additional authentication when you change the version state of your bucket or you delete and object version adding another layer of security in the event your security credentials are compromised or unauthorized access is granted.

- 推奨リンク：[https://docs.aws.amazon.com/AmazonS3/latest/userguide/MultiFactorAuthenticationDelete.html](https://docs.aws.amazon.com/AmazonS3/latest/userguide/MultiFactorAuthenticationDelete.html)

## 修正手順


### CLI

```text
aws s3api put-bucket-versioning --profile my-root-profile --bucket my-bucket-name --versioning-configuration Status=Enabled,MFADelete=Enabled --mfa 'arn:aws:iam::00000000:mfa/root-account-mfa-device 123456'
```

### Terraform

[https://docs.ST Cloud.com/checks/aws/s3-policies/bc_aws_s3_24#terraform](https://docs.ST Cloud.com/checks/aws/s3-policies/bc_aws_s3_24#terraform)

## 参考資料

- [https://docs.aws.amazon.com/AmazonS3/latest/userguide/MultiFactorAuthenticationDelete.html](https://docs.aws.amazon.com/AmazonS3/latest/userguide/MultiFactorAuthenticationDelete.html)

## 技術情報

- Source Metadata：[sources/aws/s3_bucket_no_mfa_delete/metadata.json](../../sources/aws/s3_bucket_no_mfa_delete/metadata.json)
- Source Code：[sources/aws/s3_bucket_no_mfa_delete/check.py](../../sources/aws/s3_bucket_no_mfa_delete/check.py)
- Source Metadata Path：`sources/aws/s3_bucket_no_mfa_delete/metadata.json`
- Source Code Path：`sources/aws/s3_bucket_no_mfa_delete/check.py`
