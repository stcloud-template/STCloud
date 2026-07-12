# Ensure no root account access key exists

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `iam_no_root_access_key` |
| クラウドプラットフォーム | AWS |
| サービス | iam |
| 重大度 | critical |
| カテゴリ | Uncategorized |
| チェックタイプ | Software and Configuration Checks, Industry and Regulatory Standards, CIS AWS Foundations Benchmark |
| リソースタイプ | AwsIamAccessKey |
| リソースグループ | IAM |

## 説明

Ensure no root account access key exists

## リスク

The root account is the most privileged user in an AWS account. AWS Access Keys provide programmatic access to a given AWS account. It is recommended that all access keys associated with the root account be removed. Removing access keys associated with the root account limits vectors by which the account can be compromised. Removing the root access keys encourages the creation and use of role based accounts that are least privileged.

## 推奨事項

Use the credential report to check the user and ensure the access_key_1_active and access_key_2_active fields are set to FALSE. If using AWS Organizations, consider enabling Centralized Root Management and removing individual root credentials.

- 推奨リンク：[https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_getting-report.html](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_getting-report.html)

## 修正手順

No remediation steps available.

## 参考資料

- [https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_getting-report.html](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_getting-report.html)

## 技術情報

- Source Metadata：[sources/aws/iam_no_root_access_key/metadata.json](../../sources/aws/iam_no_root_access_key/metadata.json)
- Source Code：[sources/aws/iam_no_root_access_key/check.py](../../sources/aws/iam_no_root_access_key/check.py)
- Source Metadata Path：`sources/aws/iam_no_root_access_key/metadata.json`
- Source Code Path：`sources/aws/iam_no_root_access_key/check.py`
