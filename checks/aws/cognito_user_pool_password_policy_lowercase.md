# Ensure Cognito User Pool has password policy to require at least one lowercase letter

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `cognito_user_pool_password_policy_lowercase` |
| クラウドプラットフォーム | AWS |
| サービス | cognito |
| 重大度 | medium |
| カテゴリ | Uncategorized |
| リソースタイプ | AwsCognitoUserPool |
| リソースグループ | IAM |

## 説明

User pool password policy should require at least one lowercase letter.

## リスク

If the password policy does not require at least one lowercase letter, it may be easier for an attacker to crack the password.

## 推奨事項

To require at least one lowercase letter in the password, update the password policy for the user pool.

- 推奨リンク：[https://docs.aws.amazon.com/cognito/latest/developerguide/user-pool-settings-policies.html](https://docs.aws.amazon.com/cognito/latest/developerguide/user-pool-settings-policies.html)

## 修正手順

No remediation steps available.

## 参考資料

- [https://docs.aws.amazon.com/cognito/latest/developerguide/user-pool-settings-policies.html](https://docs.aws.amazon.com/cognito/latest/developerguide/user-pool-settings-policies.html)

## 技術情報

- Source Metadata：[sources/aws/cognito_user_pool_password_policy_lowercase/metadata.json](../../sources/aws/cognito_user_pool_password_policy_lowercase/metadata.json)
- Source Code：[sources/aws/cognito_user_pool_password_policy_lowercase/check.py](../../sources/aws/cognito_user_pool_password_policy_lowercase/check.py)
- Source Metadata Path：`sources/aws/cognito_user_pool_password_policy_lowercase/metadata.json`
- Source Code Path：`sources/aws/cognito_user_pool_password_policy_lowercase/check.py`
