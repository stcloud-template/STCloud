# Ensure cognito user pools deletion protection enabled to prevent accidental deletion

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `cognito_user_pool_deletion_protection_enabled` |
| クラウドプラットフォーム | AWS |
| サービス | cognito |
| 重大度 | medium |
| カテゴリ | Uncategorized |
| リソースタイプ | AwsCognitoUserPool |
| リソースグループ | IAM |

## 説明

Deletion protection is a feature that allows you to lock a user pool to prevent it from being deleted. When deletion protection is enabled, you cannot delete the user pool. By default, deletion protection is disabled

## リスク

If deletion protection is not enabled, the user pool can be deleted by any user with the necessary permissions. This can lead to loss of data and service disruption

## 推奨事項

Deletion protection should be enabled for the user pool to prevent accidental deletion

- 推奨リンク：[https://docs.aws.amazon.com/cognito/latest/developerguide/user-pool-settings-deletion-protection.html](https://docs.aws.amazon.com/cognito/latest/developerguide/user-pool-settings-deletion-protection.html)

## 修正手順

No remediation steps available.

## 参考資料

- [https://docs.aws.amazon.com/cognito/latest/developerguide/user-pool-settings-deletion-protection.html](https://docs.aws.amazon.com/cognito/latest/developerguide/user-pool-settings-deletion-protection.html)

## 技術情報

- Source Metadata：[sources/aws/cognito_user_pool_deletion_protection_enabled/metadata.json](../../sources/aws/cognito_user_pool_deletion_protection_enabled/metadata.json)
- Source Code：[sources/aws/cognito_user_pool_deletion_protection_enabled/check.py](../../sources/aws/cognito_user_pool_deletion_protection_enabled/check.py)
- Source Metadata Path：`sources/aws/cognito_user_pool_deletion_protection_enabled/metadata.json`
- Source Code Path：`sources/aws/cognito_user_pool_deletion_protection_enabled/check.py`
