# Ensure that the password policy for your Amazon Cognito user pool requires at least one symbol.

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `cognito_user_pool_password_policy_symbol` |
| クラウドプラットフォーム | AWS |
| サービス | cognito |
| 重大度 | medium |
| カテゴリ | Uncategorized |
| リソースタイプ | AwsCognitoUserPool |
| リソースグループ | IAM |

## 説明

Check whether the password policy for your Amazon Cognito user pool requires at least one symbol.

## リスク

If the password policy for your Amazon Cognito user pool does not require at least one symbol, it can be easier for attackers to crack passwords.

## 推奨事項

To require at least one symbol in the password policy for your Amazon Cognito user pool, you can use the AWS Management Console or the AWS CLI.

- 推奨リンク：[https://docs.aws.amazon.com/cognito/latest/developerguide/user-pool-settings-policies.html](https://docs.aws.amazon.com/cognito/latest/developerguide/user-pool-settings-policies.html)

## 修正手順

No remediation steps available.

## 参考資料

- [https://docs.aws.amazon.com/cognito/latest/developerguide/user-pool-settings-policies.html](https://docs.aws.amazon.com/cognito/latest/developerguide/user-pool-settings-policies.html)

## 技術情報

- Source Metadata：[sources/aws/cognito_user_pool_password_policy_symbol/metadata.json](../../sources/aws/cognito_user_pool_password_policy_symbol/metadata.json)
- Source Code：[sources/aws/cognito_user_pool_password_policy_symbol/check.py](../../sources/aws/cognito_user_pool_password_policy_symbol/check.py)
- Source Metadata Path：`sources/aws/cognito_user_pool_password_policy_symbol/metadata.json`
- Source Code Path：`sources/aws/cognito_user_pool_password_policy_symbol/check.py`
