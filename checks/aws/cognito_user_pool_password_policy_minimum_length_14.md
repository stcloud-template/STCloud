# Ensure that the password policy for your user pools require a minimum length of 14 or greater

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `cognito_user_pool_password_policy_minimum_length_14` |
| クラウドプラットフォーム | AWS |
| サービス | cognito |
| 重大度 | medium |
| カテゴリ | Uncategorized |
| リソースタイプ | AwsCognitoUserPool |
| リソースグループ | IAM |

## 説明

User pools allow you to configure a password policy for your user pool to specify complexity requirements for user passwords. The password policy for your user pools should require a minimum length of 14 or greater.

## リスク

If the password policy for your user pools does not require a minimum length of 14 or greater, it may be easier for attackers to guess or brute force user passwords.

## 推奨事項

To require a minimum length of 14 or greater for user passwords in your user pools, you can update the password policy for your user pool using the AWS Management Console, AWS CLI, or SDK.

- 推奨リンク：[https://docs.aws.amazon.com/cognito/latest/developerguide/user-pool-settings-policies.html](https://docs.aws.amazon.com/cognito/latest/developerguide/user-pool-settings-policies.html)

## 修正手順

No remediation steps available.

## 参考資料

- [https://docs.aws.amazon.com/cognito/latest/developerguide/user-pool-settings-policies.html](https://docs.aws.amazon.com/cognito/latest/developerguide/user-pool-settings-policies.html)

## 技術情報

- Source Metadata：[sources/aws/cognito_user_pool_password_policy_minimum_length_14/metadata.json](../../sources/aws/cognito_user_pool_password_policy_minimum_length_14/metadata.json)
- Source Code：[sources/aws/cognito_user_pool_password_policy_minimum_length_14/check.py](../../sources/aws/cognito_user_pool_password_policy_minimum_length_14/check.py)
- Source Metadata Path：`sources/aws/cognito_user_pool_password_policy_minimum_length_14/metadata.json`
- Source Code Path：`sources/aws/cognito_user_pool_password_policy_minimum_length_14/check.py`
