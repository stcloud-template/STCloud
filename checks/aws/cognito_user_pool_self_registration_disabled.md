# Ensure self registration is disabled for Amazon Cognito User Pools

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `cognito_user_pool_self_registration_disabled` |
| 云平台 | AWS |
| 服务 | cognito |
| 严重等级 | medium |
| 类别 | Uncategorized |
| 资源类型 | AwsCognitoUserPool |
| 资源组 | IAM |

## 描述

Checks whether self registration is disabled for the Amazon Cognito User Pool. Self registration allows users to sign up for an account in the user pool. If self registration is enabled, users can sign up for an account in the user pool without any intervention from the administrator. This can lead to unauthorized access to the application.

## 风险

If self registration is enabled, users can sign up for an account in the user pool without any intervention from the administrator. This can lead to unauthorized access to the application.

## 推荐措施

To disable self registration for the Amazon Cognito User Pool, perform the following actions:

- 推荐链接：[https://docs.aws.amazon.com/cognito/latest/developerguide/signing-up-users-in-your-app.html](https://docs.aws.amazon.com/cognito/latest/developerguide/signing-up-users-in-your-app.html)

## 修复步骤

No remediation steps available.

## 参考资料

- [https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_SignUp.html](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_SignUp.html)
- [https://docs.aws.amazon.com/cognito/latest/developerguide/signing-up-users-in-your-app.html](https://docs.aws.amazon.com/cognito/latest/developerguide/signing-up-users-in-your-app.html)

## 技术信息

- Source Metadata：[sources/aws/cognito_user_pool_self_registration_disabled/metadata.json](../../sources/aws/cognito_user_pool_self_registration_disabled/metadata.json)
- Source Code：[sources/aws/cognito_user_pool_self_registration_disabled/check.py](../../sources/aws/cognito_user_pool_self_registration_disabled/check.py)
- Source Metadata Path：`sources/aws/cognito_user_pool_self_registration_disabled/metadata.json`
- Source Code Path：`sources/aws/cognito_user_pool_self_registration_disabled/check.py`
