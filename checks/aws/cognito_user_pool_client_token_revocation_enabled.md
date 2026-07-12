# Ensure that token revocation is enabled for Amazon Cognito User Pools

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `cognito_user_pool_client_token_revocation_enabled` |
| クラウドプラットフォーム | AWS |
| サービス | cognito |
| 重大度 | medium |
| カテゴリ | Uncategorized |
| リソースタイプ | AwsCognitoUserPoolClient |
| リソースグループ | IAM |

## 説明

Token revocation is a security feature that allows you to revoke tokens and end sessions for users. When you enable token revocation, Amazon Cognito automatically revokes tokens for users who sign out or are deleted. This helps protect your users' data and prevent unauthorized access to your resources.

## リスク

If token revocation is not enabled, users' tokens will not be revoked when they sign out or are deleted. This can lead to unauthorized access to your resources.

## 推奨事項

To enable token revocation for an Amazon Cognito User Pool, use the Amazon Cognito console or the AWS CLI. For more information, see the Amazon Cognito documentation.

- 推奨リンク：[https://docs.aws.amazon.com/cognito/latest/developerguide/token-revocation.html](https://docs.aws.amazon.com/cognito/latest/developerguide/token-revocation.html)

## 修正手順

No remediation steps available.

## 参考資料

- [https://docs.aws.amazon.com/cognito/latest/developerguide/token-revocation.html](https://docs.aws.amazon.com/cognito/latest/developerguide/token-revocation.html)

## 技術情報

- Source Metadata：[sources/aws/cognito_user_pool_client_token_revocation_enabled/metadata.json](../../sources/aws/cognito_user_pool_client_token_revocation_enabled/metadata.json)
- Source Code：[sources/aws/cognito_user_pool_client_token_revocation_enabled/check.py](../../sources/aws/cognito_user_pool_client_token_revocation_enabled/check.py)
- Source Metadata Path：`sources/aws/cognito_user_pool_client_token_revocation_enabled/metadata.json`
- Source Code Path：`sources/aws/cognito_user_pool_client_token_revocation_enabled/check.py`
