# Ensure self registration is disabled for Amazon Cognito User Pools

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `cognito_user_pool_self_registration_disabled` |
| クラウドプラットフォーム | AWS |
| サービス | cognito |
| 重大度 | medium |
| カテゴリ | Uncategorized |
| リソースタイプ | AwsCognitoUserPool |
| リソースグループ | IAM |

## 説明

Checks whether self registration is disabled for the Amazon Cognito User Pool. Self registration allows users to sign up for an account in the user pool. If self registration is enabled, users can sign up for an account in the user pool without any intervention from the administrator. This can lead to unauthorized access to the application.

## リスク

If self registration is enabled, users can sign up for an account in the user pool without any intervention from the administrator. This can lead to unauthorized access to the application.

## 推奨事項

To disable self registration for the Amazon Cognito User Pool, perform the following actions:

- 推奨リンク：[https://docs.aws.amazon.com/cognito/latest/developerguide/signing-up-users-in-your-app.html](https://docs.aws.amazon.com/cognito/latest/developerguide/signing-up-users-in-your-app.html)

## 修正手順

No remediation steps available.

## 参考資料

- [https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_SignUp.html](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_SignUp.html)
- [https://docs.aws.amazon.com/cognito/latest/developerguide/signing-up-users-in-your-app.html](https://docs.aws.amazon.com/cognito/latest/developerguide/signing-up-users-in-your-app.html)

## 技術情報

- Source Metadata：[sources/aws/cognito_user_pool_self_registration_disabled/metadata.json](../../sources/aws/cognito_user_pool_self_registration_disabled/metadata.json)
- Source Code：[sources/aws/cognito_user_pool_self_registration_disabled/check.py](../../sources/aws/cognito_user_pool_self_registration_disabled/check.py)
- Source Metadata Path：`sources/aws/cognito_user_pool_self_registration_disabled/metadata.json`
- Source Code Path：`sources/aws/cognito_user_pool_self_registration_disabled/check.py`
