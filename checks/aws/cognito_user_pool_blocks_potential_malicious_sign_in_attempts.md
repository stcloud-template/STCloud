# Ensure that your Amazon Cognito user pool blocks potential malicious sign-in attempts

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `cognito_user_pool_blocks_potential_malicious_sign_in_attempts` |
| クラウドプラットフォーム | AWS |
| サービス | cognito |
| 重大度 | medium |
| カテゴリ | Uncategorized |
| リソースタイプ | AwsCognitoUserPool |
| リソースグループ | IAM |

## 説明

Amazon Cognito provides adaptive authentication, which helps protect your applications from malicious actors and compromised credentials by evaluating the risk associated with each user login and providing the appropriate level of security to mitigate that risk. Adaptive authentication is a feature of advanced security that you can enable for your user pool. When adaptive authentication is enabled, Amazon Cognito evaluates the risk associated with each user login and provides the appropriate level of security to mitigate that risk. You can configure adaptive authentication to block sign-in attempts that are likely to be malicious.

## リスク

If adaptive authentication with automatic risk response as block sign-in is not enabled, your user pool may not be able to block sign-in attempts that are likely to be malicious.

## 推奨事項

To enable adaptive authentication with automatic risk response as block sign-in, perform the following actions:

- 推奨リンク：[https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-pool-settings-advanced-security.html](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-pool-settings-advanced-security.html)

## 修正手順

No remediation steps available.

## 参考資料

- [https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-pool-settings-advanced-security.html](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-pool-settings-advanced-security.html)

## 技術情報

- Source Metadata：[sources/aws/cognito_user_pool_blocks_potential_malicious_sign_in_attempts/metadata.json](../../sources/aws/cognito_user_pool_blocks_potential_malicious_sign_in_attempts/metadata.json)
- Source Code：[sources/aws/cognito_user_pool_blocks_potential_malicious_sign_in_attempts/check.py](../../sources/aws/cognito_user_pool_blocks_potential_malicious_sign_in_attempts/check.py)
- Source Metadata Path：`sources/aws/cognito_user_pool_blocks_potential_malicious_sign_in_attempts/metadata.json`
- Source Code Path：`sources/aws/cognito_user_pool_blocks_potential_malicious_sign_in_attempts/check.py`
