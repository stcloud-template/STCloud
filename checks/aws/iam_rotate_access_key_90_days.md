# Ensure access keys are rotated every 90 days or less

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `iam_rotate_access_key_90_days` |
| クラウドプラットフォーム | AWS |
| サービス | iam |
| 重大度 | medium |
| カテゴリ | Uncategorized |
| チェックタイプ | Software and Configuration Checks, Industry and Regulatory Standards, CIS AWS Foundations Benchmark |
| リソースタイプ | AwsIamAccessKey |
| リソースグループ | IAM |

## 説明

Ensure access keys are rotated every 90 days or less

## リスク

Access keys consist of an access key ID and secret access key which are used to sign programmatic requests that you make to AWS. AWS users need their own access keys to make programmatic calls to AWS from the AWS Command Line Interface (AWS CLI)- Tools for Windows PowerShell- the AWS SDKs- or direct HTTP calls using the APIs for individual AWS services. It is recommended that all access keys be regularly rotated.

## 推奨事項

Use the credential report to ensure access_key_X_last_rotated is less than 90 days ago.

- 推奨リンク：[https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_getting-report.html](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_getting-report.html)

## 修正手順

No remediation steps available.

## 参考資料

- [https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_getting-report.html](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_getting-report.html)

## 技術情報

- Source Metadata：[sources/aws/iam_rotate_access_key_90_days/metadata.json](../../sources/aws/iam_rotate_access_key_90_days/metadata.json)
- Source Code：[sources/aws/iam_rotate_access_key_90_days/check.py](../../sources/aws/iam_rotate_access_key_90_days/check.py)
- Source Metadata Path：`sources/aws/iam_rotate_access_key_90_days/metadata.json`
- Source Code Path：`sources/aws/iam_rotate_access_key_90_days/check.py`
