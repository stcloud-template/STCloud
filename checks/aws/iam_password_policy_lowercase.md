# Ensure IAM password policy require at least one lowercase letter

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `iam_password_policy_lowercase` |
| クラウドプラットフォーム | AWS |
| サービス | iam |
| 重大度 | medium |
| カテゴリ | Uncategorized |
| チェックタイプ | Software and Configuration Checks, Industry and Regulatory Standards, CIS AWS Foundations Benchmark |
| リソースタイプ | Other |
| リソースグループ | IAM |

## 説明

Ensure IAM password policy requires at least one uppercase letter

## リスク

Password policies are used to enforce password complexity requirements. IAM password policies can be used to ensure password are comprised of different character sets. It is recommended that the password policy require at least one lowercase letter.

## 推奨事項

Ensure "Requires at least one lowercase letter" is checked under "Password Policy".

- 推奨リンク：[https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_passwords_account-policy.html](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_passwords_account-policy.html)

## 修正手順

No remediation steps available.

## 参考資料

- [https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_passwords_account-policy.html](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_passwords_account-policy.html)

## 技術情報

- Source Metadata：[sources/aws/iam_password_policy_lowercase/metadata.json](../../sources/aws/iam_password_policy_lowercase/metadata.json)
- Source Code：[sources/aws/iam_password_policy_lowercase/check.py](../../sources/aws/iam_password_policy_lowercase/check.py)
- Source Metadata Path：`sources/aws/iam_password_policy_lowercase/metadata.json`
- Source Code Path：`sources/aws/iam_password_policy_lowercase/check.py`
