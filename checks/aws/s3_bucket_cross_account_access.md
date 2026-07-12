# Ensure that general-purpose bucket policies restrict access to other AWS accounts.

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `s3_bucket_cross_account_access` |
| クラウドプラットフォーム | AWS |
| サービス | s3 |
| 重大度 | high |
| カテゴリ | Uncategorized |
| チェックタイプ | Effects/Data Exposure |
| リソースタイプ | AwsS3Bucket |
| リソースグループ | storage |

## 説明

This check verifies that S3 bucket policies are configured in a way that limits access to the intended AWS accounts only, preventing unauthorized access by external or unintended accounts.

## リスク

Allowing other AWS accounts to perform sensitive actions (e.g., modifying bucket policies, ACLs, or encryption settings) on your S3 buckets can lead to data exposure, unauthorized access, or misconfigurations, increasing the risk of insider threats or attacks.

## 推奨事項

Review and update your S3 bucket policies to remove permissions that grant external AWS accounts access to critical actions and implement least privilege principles to ensure sensitive operations are restricted to trusted accounts only

- 推奨リンク：[https://docs.aws.amazon.com/AmazonS3/latest/userguide/access-control-block-public-access.html](https://docs.aws.amazon.com/AmazonS3/latest/userguide/access-control-block-public-access.html)

## 修正手順


### Other

[https://docs.aws.amazon.com/securityhub/latest/userguide/s3-controls.html#s3-6](https://docs.aws.amazon.com/securityhub/latest/userguide/s3-controls.html#s3-6)

## 参考資料

- [https://docs.aws.amazon.com/AmazonS3/latest/userguide/access-control-block-public-access.html](https://docs.aws.amazon.com/AmazonS3/latest/userguide/access-control-block-public-access.html)

## 技術情報

- Source Metadata：[sources/aws/s3_bucket_cross_account_access/metadata.json](../../sources/aws/s3_bucket_cross_account_access/metadata.json)
- Source Code：[sources/aws/s3_bucket_cross_account_access/check.py](../../sources/aws/s3_bucket_cross_account_access/check.py)
- Source Metadata Path：`sources/aws/s3_bucket_cross_account_access/metadata.json`
- Source Code Path：`sources/aws/s3_bucket_cross_account_access/check.py`
