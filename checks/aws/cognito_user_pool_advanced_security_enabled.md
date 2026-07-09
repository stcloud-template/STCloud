# Ensure cognito user pools has advanced security enabled with full-function

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `cognito_user_pool_advanced_security_enabled` |
| 云平台 | AWS |
| 服务 | cognito |
| 严重等级 | medium |
| 类别 | Uncategorized |
| 资源类型 | AwsCognitoUserPool |
| 资源组 | IAM |

## 描述

Advanced security features for Amazon Cognito User Pools provide additional security for your user pool. These features include compromised credentials protection, phone number verification, and account takeover protection.

## 风险

If advanced security features are not enabled, your user pool is more vulnerable to unauthorized access.

## 推荐措施

To enable advanced security features for an Amazon Cognito User Pool, follow the instructions in the Amazon Cognito documentation.

- 推荐链接：[https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-pool-settings-advanced-security.html](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-pool-settings-advanced-security.html)

## 修复步骤

No remediation steps available.

## 参考资料

- [https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-pool-settings-advanced-security.html](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-pool-settings-advanced-security.html)

## 技术信息

- Source Metadata：[sources/aws/cognito_user_pool_advanced_security_enabled/metadata.json](../../sources/aws/cognito_user_pool_advanced_security_enabled/metadata.json)
- Source Code：[sources/aws/cognito_user_pool_advanced_security_enabled/check.py](../../sources/aws/cognito_user_pool_advanced_security_enabled/check.py)
- Source Metadata Path：`sources/aws/cognito_user_pool_advanced_security_enabled/metadata.json`
- Source Code Path：`sources/aws/cognito_user_pool_advanced_security_enabled/check.py`
