# Ensure cognito user pools has advanced security enabled with full-function

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `cognito_user_pool_advanced_security_enabled` |
| クラウドプラットフォーム | AWS |
| サービス | cognito |
| 重大度 | medium |
| カテゴリ | Uncategorized |
| リソースタイプ | AwsCognitoUserPool |
| リソースグループ | IAM |

## 説明

Advanced security features for Amazon Cognito User Pools provide additional security for your user pool. These features include compromised credentials protection, phone number verification, and account takeover protection.

## リスク

If advanced security features are not enabled, your user pool is more vulnerable to unauthorized access.

## 推奨事項

To enable advanced security features for an Amazon Cognito User Pool, follow the instructions in the Amazon Cognito documentation.

- 推奨リンク：[https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-pool-settings-advanced-security.html](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-pool-settings-advanced-security.html)

## 修正手順

No remediation steps available.

## 参考資料

- [https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-pool-settings-advanced-security.html](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-pool-settings-advanced-security.html)

## 技術情報

- Source Metadata：[sources/aws/cognito_user_pool_advanced_security_enabled/metadata.json](../../sources/aws/cognito_user_pool_advanced_security_enabled/metadata.json)
- Source Code：[sources/aws/cognito_user_pool_advanced_security_enabled/check.py](../../sources/aws/cognito_user_pool_advanced_security_enabled/check.py)
- Source Metadata Path：`sources/aws/cognito_user_pool_advanced_security_enabled/metadata.json`
- Source Code Path：`sources/aws/cognito_user_pool_advanced_security_enabled/check.py`
