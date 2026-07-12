# Amazon Cognito User Pool should prevent user existence errors

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `cognito_user_pool_client_prevent_user_existence_errors` |
| クラウドプラットフォーム | AWS |
| サービス | cognito |
| 重大度 | medium |
| カテゴリ | Uncategorized |
| リソースタイプ | AwsCognitoUserPoolClient |
| リソースグループ | IAM |

## 説明

Amazon Cognito User Pool should be configured to prevent user existence errors. This setting prevents user existence errors by requiring the user to enter a username and password to sign in. If the user does not exist, the user will receive an error message.

## リスク

Revealing user existence errors can be a security risk as it can allow an attacker to determine if a user exists in the system. This can be used to perform user enumeration attacks.

## 推奨事項

To prevent user existence errors, you should configure the Amazon Cognito User Pool to require a username and password to sign in. If the user does not exist, the user will receive an error message.

- 推奨リンク：[https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-pool-managing-errors.html](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-pool-managing-errors.html)

## 修正手順

No remediation steps available.

## 参考資料

- [https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-pool-managing-errors.html](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-pool-managing-errors.html)

## 技術情報

- Source Metadata：[sources/aws/cognito_user_pool_client_prevent_user_existence_errors/metadata.json](../../sources/aws/cognito_user_pool_client_prevent_user_existence_errors/metadata.json)
- Source Code：[sources/aws/cognito_user_pool_client_prevent_user_existence_errors/check.py](../../sources/aws/cognito_user_pool_client_prevent_user_existence_errors/check.py)
- Source Metadata Path：`sources/aws/cognito_user_pool_client_prevent_user_existence_errors/metadata.json`
- Source Code Path：`sources/aws/cognito_user_pool_client_prevent_user_existence_errors/check.py`
