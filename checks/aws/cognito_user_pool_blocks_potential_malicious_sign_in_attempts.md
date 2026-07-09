# Ensure that your Amazon Cognito user pool blocks potential malicious sign-in attempts

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `cognito_user_pool_blocks_potential_malicious_sign_in_attempts` |
| 云平台 | AWS |
| 服务 | cognito |
| 严重等级 | medium |
| 类别 | Uncategorized |
| 资源类型 | AwsCognitoUserPool |
| 资源组 | IAM |

## 描述

Amazon Cognito provides adaptive authentication, which helps protect your applications from malicious actors and compromised credentials by evaluating the risk associated with each user login and providing the appropriate level of security to mitigate that risk. Adaptive authentication is a feature of advanced security that you can enable for your user pool. When adaptive authentication is enabled, Amazon Cognito evaluates the risk associated with each user login and provides the appropriate level of security to mitigate that risk. You can configure adaptive authentication to block sign-in attempts that are likely to be malicious.

## 风险

If adaptive authentication with automatic risk response as block sign-in is not enabled, your user pool may not be able to block sign-in attempts that are likely to be malicious.

## 推荐措施

To enable adaptive authentication with automatic risk response as block sign-in, perform the following actions:

- 推荐链接：[https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-pool-settings-advanced-security.html](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-pool-settings-advanced-security.html)

## 修复步骤

No remediation steps available.

## 参考资料

- [https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-pool-settings-advanced-security.html](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-pool-settings-advanced-security.html)

## 技术信息

- Source Metadata：[sources/aws/cognito_user_pool_blocks_potential_malicious_sign_in_attempts/metadata.json](../../sources/aws/cognito_user_pool_blocks_potential_malicious_sign_in_attempts/metadata.json)
- Source Code：[sources/aws/cognito_user_pool_blocks_potential_malicious_sign_in_attempts/check.py](../../sources/aws/cognito_user_pool_blocks_potential_malicious_sign_in_attempts/check.py)
- Source Metadata Path：`sources/aws/cognito_user_pool_blocks_potential_malicious_sign_in_attempts/metadata.json`
- Source Code Path：`sources/aws/cognito_user_pool_blocks_potential_malicious_sign_in_attempts/check.py`
