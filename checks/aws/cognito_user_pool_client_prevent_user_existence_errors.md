# Amazon Cognito User Pool should prevent user existence errors

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `cognito_user_pool_client_prevent_user_existence_errors` |
| 云平台 | AWS |
| 服务 | cognito |
| 严重等级 | medium |
| 类别 | Uncategorized |
| 资源类型 | AwsCognitoUserPoolClient |
| 资源组 | IAM |

## 描述

Amazon Cognito User Pool should be configured to prevent user existence errors. This setting prevents user existence errors by requiring the user to enter a username and password to sign in. If the user does not exist, the user will receive an error message.

## 风险

Revealing user existence errors can be a security risk as it can allow an attacker to determine if a user exists in the system. This can be used to perform user enumeration attacks.

## 推荐措施

To prevent user existence errors, you should configure the Amazon Cognito User Pool to require a username and password to sign in. If the user does not exist, the user will receive an error message.

- 推荐链接：[https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-pool-managing-errors.html](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-pool-managing-errors.html)

## 修复步骤

No remediation steps available.

## 参考资料

- [https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-pool-managing-errors.html](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-pool-managing-errors.html)

## 技术信息

- Source Metadata：[sources/aws/cognito_user_pool_client_prevent_user_existence_errors/metadata.json](../../sources/aws/cognito_user_pool_client_prevent_user_existence_errors/metadata.json)
- Source Code：[sources/aws/cognito_user_pool_client_prevent_user_existence_errors/check.py](../../sources/aws/cognito_user_pool_client_prevent_user_existence_errors/check.py)
- Source Metadata Path：`sources/aws/cognito_user_pool_client_prevent_user_existence_errors/metadata.json`
- Source Code Path：`sources/aws/cognito_user_pool_client_prevent_user_existence_errors/check.py`
