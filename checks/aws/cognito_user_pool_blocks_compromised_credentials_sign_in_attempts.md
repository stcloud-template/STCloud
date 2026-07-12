# Ensure that advanced security features are enabled for Amazon Cognito User Pools to block sign-in by users with suspected compromised credentials

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `cognito_user_pool_blocks_compromised_credentials_sign_in_attempts` |
| クラウドプラットフォーム | AWS |
| サービス | cognito |
| 重大度 | medium |
| カテゴリ | Uncategorized |
| リソースタイプ | AwsCognitoUserPool |
| リソースグループ | IAM |

## 説明

Amazon Cognito User Pools can be configured to block sign-in by users with suspected compromised credentials. This feature uses Amazon Cognito advanced security features to detect anomalous sign-in attempts and block them. When enabled, Amazon Cognito User Pools will block sign-in by users with suspected compromised credentials. This helps protect your users from unauthorized access to their accounts.

## リスク

If advanced security features are not enabled for an Amazon Cognito User Pool, users with compromised credentials may be able to sign in to their accounts. This could lead to unauthorized access to user data and other resources.

## 推奨事項

To enable advanced security features for an Amazon Cognito User Pool, follow the steps below:

- 推奨リンク：[https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-pool-settings-advanced-security.html](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-pool-settings-advanced-security.html)

## 修正手順

No remediation steps available.

## 参考資料

- [https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-pool-settings-advanced-security.html](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-pool-settings-advanced-security.html)

## 技術情報

- Source Metadata：[sources/aws/cognito_user_pool_blocks_compromised_credentials_sign_in_attempts/metadata.json](../../sources/aws/cognito_user_pool_blocks_compromised_credentials_sign_in_attempts/metadata.json)
- Source Code：[sources/aws/cognito_user_pool_blocks_compromised_credentials_sign_in_attempts/check.py](../../sources/aws/cognito_user_pool_blocks_compromised_credentials_sign_in_attempts/check.py)
- Source Metadata Path：`sources/aws/cognito_user_pool_blocks_compromised_credentials_sign_in_attempts/metadata.json`
- Source Code Path：`sources/aws/cognito_user_pool_blocks_compromised_credentials_sign_in_attempts/check.py`
