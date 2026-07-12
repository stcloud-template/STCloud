# Ensure IAM password policy expires passwords within 90 days or less

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `iam_password_policy_expires_passwords_within_90_days_or_less` |
| クラウドプラットフォーム | AWS |
| サービス | iam |
| 重大度 | medium |
| カテゴリ | Uncategorized |
| チェックタイプ | Software and Configuration Checks, Industry and Regulatory Standards, CIS AWS Foundations Benchmark |
| リソースタイプ | Other |
| リソースグループ | IAM |

## 説明

Ensure IAM password policy expires passwords within 90 days or less

## リスク

Password policies are used to enforce password complexity requirements. IAM password policies can be used to ensure password are comprised of different character sets. It is recommended that the password policy require at least one uppercase letter.

## 推奨事項

Ensure Password expiration period (in days): is set to 90 or less.

- 推奨リンク：[https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_passwords_account-policy.html](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_passwords_account-policy.html)

## 修正手順

No remediation steps available.

## 参考資料

- [https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_passwords_account-policy.html](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_passwords_account-policy.html)

## 技術情報

- Source Metadata：[sources/aws/iam_password_policy_expires_passwords_within_90_days_or_less/metadata.json](../../sources/aws/iam_password_policy_expires_passwords_within_90_days_or_less/metadata.json)
- Source Code：[sources/aws/iam_password_policy_expires_passwords_within_90_days_or_less/check.py](../../sources/aws/iam_password_policy_expires_passwords_within_90_days_or_less/check.py)
- Source Metadata Path：`sources/aws/iam_password_policy_expires_passwords_within_90_days_or_less/metadata.json`
- Source Code Path：`sources/aws/iam_password_policy_expires_passwords_within_90_days_or_less/check.py`
