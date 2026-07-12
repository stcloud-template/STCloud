# Do not setup access keys during initial user setup for all IAM users that have a console password

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `iam_user_no_setup_initial_access_key` |
| クラウドプラットフォーム | AWS |
| サービス | iam |
| 重大度 | medium |
| カテゴリ | Uncategorized |
| チェックタイプ | Software and Configuration Checks, Industry and Regulatory Standards, CIS AWS Foundations Benchmark |
| リソースタイプ | AwsIamAccessKey |
| リソースグループ | IAM |

## 説明

Do not setup access keys during initial user setup for all IAM users that have a console password

## リスク

AWS console defaults the checkbox for creating access keys to enabled. This results in many access keys being generated unnecessarily. In addition to unnecessary credentials, it also generates unnecessary management work in auditing and rotating these keys. Requiring that additional steps be taken by the user after their profile has been created will give a stronger indication of intent that access keys are (a) necessary for their work and (b) once the access key is established on an account that the keys may be in use somewhere in the organization.

## 推奨事項

From the IAM console: generate credential report and disable not required keys.

- 推奨リンク：[https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_getting-report.html](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_getting-report.html)

## 修正手順

No remediation steps available.

## 参考資料

- [https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_getting-report.html](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_getting-report.html)

## 技術情報

- Source Metadata：[sources/aws/iam_user_no_setup_initial_access_key/metadata.json](../../sources/aws/iam_user_no_setup_initial_access_key/metadata.json)
- Source Code：[sources/aws/iam_user_no_setup_initial_access_key/check.py](../../sources/aws/iam_user_no_setup_initial_access_key/check.py)
- Source Metadata Path：`sources/aws/iam_user_no_setup_initial_access_key/metadata.json`
- Source Code Path：`sources/aws/iam_user_no_setup_initial_access_key/check.py`
