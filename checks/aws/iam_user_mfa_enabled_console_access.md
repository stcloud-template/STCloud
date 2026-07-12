# Ensure multi-factor authentication (MFA) is enabled for all IAM users that have a console password.

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `iam_user_mfa_enabled_console_access` |
| クラウドプラットフォーム | AWS |
| サービス | iam |
| 重大度 | high |
| カテゴリ | Uncategorized |
| チェックタイプ | Software and Configuration Checks, Industry and Regulatory Standards, CIS AWS Foundations Benchmark |
| リソースタイプ | AwsIamUser |
| リソースグループ | IAM |

## 説明

Ensure multi-factor authentication (MFA) is enabled for all IAM users that have a console password.

## リスク

Unauthorized access to this critical account if password is not secure or it is disclosed in any way.

## 推奨事項

Enable MFA for the user's account. MFA is a simple best practice that adds an extra layer of protection on top of your user name and password. Recommended to use hardware keys over virtual MFA.

- 推奨リンク：[https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_mfa_enable_virtual.html](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_mfa_enable_virtual.html)

## 修正手順

No remediation steps available.

## 参考資料

- [https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_mfa_enable_virtual.html](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_mfa_enable_virtual.html)

## 技術情報

- Source Metadata：[sources/aws/iam_user_mfa_enabled_console_access/metadata.json](../../sources/aws/iam_user_mfa_enabled_console_access/metadata.json)
- Source Code：[sources/aws/iam_user_mfa_enabled_console_access/check.py](../../sources/aws/iam_user_mfa_enabled_console_access/check.py)
- Source Metadata Path：`sources/aws/iam_user_mfa_enabled_console_access/metadata.json`
- Source Code Path：`sources/aws/iam_user_mfa_enabled_console_access/check.py`
