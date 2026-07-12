# Ensure Multi-Factor Authentication (MFA) is enabled for Amazon Cognito User Pools

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `cognito_user_pool_mfa_enabled` |
| クラウドプラットフォーム | AWS |
| サービス | cognito |
| 重大度 | medium |
| カテゴリ | Uncategorized |
| リソースタイプ | AwsCognitoUserPool |
| リソースグループ | IAM |

## 説明

Checks whether Multi-Factor Authentication (MFA) is enabled for Amazon Cognito User Pools.

## リスク

If MFA is not enabled, unauthorized users could gain access to the user pool and potentially compromise the security of the application.

## 推奨事項

To enable MFA for an Amazon Cognito User Pool, follow the instructions in the Amazon Cognito documentation.

- 推奨リンク：[https://docs.aws.amazon.com/cognito/latest/developerguide/user-pool-settings-mfa.html](https://docs.aws.amazon.com/cognito/latest/developerguide/user-pool-settings-mfa.html)

## 修正手順

No remediation steps available.

## 参考資料

- [https://docs.aws.amazon.com/cognito/latest/developerguide/user-pool-settings-mfa.html](https://docs.aws.amazon.com/cognito/latest/developerguide/user-pool-settings-mfa.html)

## 技術情報

- Source Metadata：[sources/aws/cognito_user_pool_mfa_enabled/metadata.json](../../sources/aws/cognito_user_pool_mfa_enabled/metadata.json)
- Source Code：[sources/aws/cognito_user_pool_mfa_enabled/check.py](../../sources/aws/cognito_user_pool_mfa_enabled/check.py)
- Source Metadata Path：`sources/aws/cognito_user_pool_mfa_enabled/metadata.json`
- Source Code Path：`sources/aws/cognito_user_pool_mfa_enabled/check.py`
