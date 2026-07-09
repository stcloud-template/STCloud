# Ensure that advanced security features are enabled for Amazon Cognito User Pools to block sign-in by users with suspected compromised credentials

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `cognito_user_pool_blocks_compromised_credentials_sign_in_attempts` |
| 云平台 | AWS |
| 服务 | cognito |
| 严重等级 | medium |
| 类别 | Uncategorized |
| 资源类型 | AwsCognitoUserPool |
| 资源组 | IAM |

## 描述

Amazon Cognito User Pools can be configured to block sign-in by users with suspected compromised credentials. This feature uses Amazon Cognito advanced security features to detect anomalous sign-in attempts and block them. When enabled, Amazon Cognito User Pools will block sign-in by users with suspected compromised credentials. This helps protect your users from unauthorized access to their accounts.

## 风险

If advanced security features are not enabled for an Amazon Cognito User Pool, users with compromised credentials may be able to sign in to their accounts. This could lead to unauthorized access to user data and other resources.

## 推荐措施

To enable advanced security features for an Amazon Cognito User Pool, follow the steps below:

- 推荐链接：[https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-pool-settings-advanced-security.html](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-pool-settings-advanced-security.html)

## 修复步骤

No remediation steps available.

## 参考资料

- [https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-pool-settings-advanced-security.html](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-pool-settings-advanced-security.html)

## 技术信息

- Source Metadata：[sources/aws/cognito_user_pool_blocks_compromised_credentials_sign_in_attempts/metadata.json](../../sources/aws/cognito_user_pool_blocks_compromised_credentials_sign_in_attempts/metadata.json)
- Source Code：[sources/aws/cognito_user_pool_blocks_compromised_credentials_sign_in_attempts/check.py](../../sources/aws/cognito_user_pool_blocks_compromised_credentials_sign_in_attempts/check.py)
- Source Metadata Path：`sources/aws/cognito_user_pool_blocks_compromised_credentials_sign_in_attempts/metadata.json`
- Source Code Path：`sources/aws/cognito_user_pool_blocks_compromised_credentials_sign_in_attempts/check.py`
