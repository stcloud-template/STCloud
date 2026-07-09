# Ensure Multi-Factor Authentication (MFA) is enabled for Amazon Cognito User Pools

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `cognito_user_pool_mfa_enabled` |
| 云平台 | AWS |
| 服务 | cognito |
| 严重等级 | medium |
| 类别 | Uncategorized |
| 资源类型 | AwsCognitoUserPool |
| 资源组 | IAM |

## 描述

Checks whether Multi-Factor Authentication (MFA) is enabled for Amazon Cognito User Pools.

## 风险

If MFA is not enabled, unauthorized users could gain access to the user pool and potentially compromise the security of the application.

## 推荐措施

To enable MFA for an Amazon Cognito User Pool, follow the instructions in the Amazon Cognito documentation.

- 推荐链接：[https://docs.aws.amazon.com/cognito/latest/developerguide/user-pool-settings-mfa.html](https://docs.aws.amazon.com/cognito/latest/developerguide/user-pool-settings-mfa.html)

## 修复步骤

No remediation steps available.

## 参考资料

- [https://docs.aws.amazon.com/cognito/latest/developerguide/user-pool-settings-mfa.html](https://docs.aws.amazon.com/cognito/latest/developerguide/user-pool-settings-mfa.html)

## 技术信息

- Source Metadata：[sources/aws/cognito_user_pool_mfa_enabled/metadata.json](../../sources/aws/cognito_user_pool_mfa_enabled/metadata.json)
- Source Code：[sources/aws/cognito_user_pool_mfa_enabled/check.py](../../sources/aws/cognito_user_pool_mfa_enabled/check.py)
- Source Metadata Path：`sources/aws/cognito_user_pool_mfa_enabled/metadata.json`
- Source Code Path：`sources/aws/cognito_user_pool_mfa_enabled/check.py`
