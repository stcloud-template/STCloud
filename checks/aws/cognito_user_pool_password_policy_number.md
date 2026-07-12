# Ensure that the password policy for your user pool requires a number

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `cognito_user_pool_password_policy_number` |
| クラウドプラットフォーム | AWS |
| サービス | cognito |
| 重大度 | medium |
| カテゴリ | Uncategorized |
| リソースタイプ | AwsCognitoUserPool |
| リソースグループ | IAM |

## 説明

Checks whether the password policy for your user pool requires a number.

## リスク

If the password policy for your user pool does not require a number, the user pool is less secure and more vulnerable to attacks.

## 推奨事項

To require a number in the password policy for your user pool, perform the following actions:

- 推奨リンク：[https://docs.aws.amazon.com/cognito/latest/developerguide/user-pool-settings-policies.html](https://docs.aws.amazon.com/cognito/latest/developerguide/user-pool-settings-policies.html)

## 修正手順

No remediation steps available.

## 参考資料

- [https://docs.aws.amazon.com/cognito/latest/developerguide/user-pool-settings-policies.html](https://docs.aws.amazon.com/cognito/latest/developerguide/user-pool-settings-policies.html)

## 技術情報

- Source Metadata：[sources/aws/cognito_user_pool_password_policy_number/metadata.json](../../sources/aws/cognito_user_pool_password_policy_number/metadata.json)
- Source Code：[sources/aws/cognito_user_pool_password_policy_number/check.py](../../sources/aws/cognito_user_pool_password_policy_number/check.py)
- Source Metadata Path：`sources/aws/cognito_user_pool_password_policy_number/metadata.json`
- Source Code Path：`sources/aws/cognito_user_pool_password_policy_number/check.py`
