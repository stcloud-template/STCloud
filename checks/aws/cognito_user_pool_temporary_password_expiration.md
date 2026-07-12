# Ensure that the user pool has a temporary password expiration period of 7 days or less

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `cognito_user_pool_temporary_password_expiration` |
| クラウドプラットフォーム | AWS |
| サービス | cognito |
| 重大度 | medium |
| カテゴリ | Uncategorized |
| リソースタイプ | AwsCognitoUserPool |
| リソースグループ | IAM |

## 説明

Temporary passwords are set by the administrator and are used to allow users to sign in and change their password. Temporary passwords are valid for a limited period of time, after which they expire. Temporary passwords are used when an administrator creates a new user account or resets a user password. The temporary password expiration period is the length of time that the temporary password is valid. The default value is 7 days. You can set the expiration period to a value between 0 and 365 days.

## リスク

If the temporary password expiration period is too long, it increases the risk of unauthorized access to the user account. If the temporary password expiration period is too short, it increases the risk of users being unable to sign in and change their password.

## 推奨事項

Set the temporary password expiration period to 7 days or less.

- 推奨リンク：[https://docs.aws.amazon.com/cognito/latest/developerguide/user-pool-settings-policies.html](https://docs.aws.amazon.com/cognito/latest/developerguide/user-pool-settings-policies.html)

## 修正手順

No remediation steps available.

## 参考資料

- [https://docs.aws.amazon.com/cognito/latest/developerguide/user-pool-settings-policies.html](https://docs.aws.amazon.com/cognito/latest/developerguide/user-pool-settings-policies.html)

## 技術情報

- Source Metadata：[sources/aws/cognito_user_pool_temporary_password_expiration/metadata.json](../../sources/aws/cognito_user_pool_temporary_password_expiration/metadata.json)
- Source Code：[sources/aws/cognito_user_pool_temporary_password_expiration/check.py](../../sources/aws/cognito_user_pool_temporary_password_expiration/check.py)
- Source Metadata Path：`sources/aws/cognito_user_pool_temporary_password_expiration/metadata.json`
- Source Code Path：`sources/aws/cognito_user_pool_temporary_password_expiration/check.py`
