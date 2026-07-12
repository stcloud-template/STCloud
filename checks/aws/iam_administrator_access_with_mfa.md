# Ensure users of groups with AdministratorAccess policy have MFA tokens enabled

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `iam_administrator_access_with_mfa` |
| クラウドプラットフォーム | AWS |
| サービス | iam |
| 重大度 | high |
| カテゴリ | Uncategorized |
| チェックタイプ | Infrastructure Security |
| リソースタイプ | AwsIamUser |
| リソースグループ | IAM |

## 説明

Ensure users of groups with AdministratorAccess policy have MFA tokens enabled

## リスク

Policy may allow Anonymous users to perform actions.

## 推奨事項

Ensure this repository and its contents should be publicly accessible.

- 推奨リンク：[https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_mfa_enable_virtual.html](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_mfa_enable_virtual.html)

## 修正手順

No remediation steps available.

## 参考資料

- [https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_mfa_enable_virtual.html](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_mfa_enable_virtual.html)

## 技術情報

- Source Metadata：[sources/aws/iam_administrator_access_with_mfa/metadata.json](../../sources/aws/iam_administrator_access_with_mfa/metadata.json)
- Source Code：[sources/aws/iam_administrator_access_with_mfa/check.py](../../sources/aws/iam_administrator_access_with_mfa/check.py)
- Source Metadata Path：`sources/aws/iam_administrator_access_with_mfa/metadata.json`
- Source Code Path：`sources/aws/iam_administrator_access_with_mfa/check.py`
