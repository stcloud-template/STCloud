# Ensure that the password policy for your user pool requires at least one uppercase letter

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `cognito_user_pool_password_policy_uppercase` |
| 云平台 | AWS |
| 服务 | cognito |
| 严重等级 | medium |
| 类别 | Uncategorized |
| 资源类型 | AwsCognitoUserPool |
| 资源组 | IAM |

## 描述

User pools allow you to configure a password policy for your user pool to specify requirements for user passwords. You can require that passwords have a minimum length, contain at least one uppercase letter, and contain at least one number. You can also require that passwords have at least one special character. You can also set the password policy to require that passwords be case-sensitive.

## 风险

If the password policy for your user pool does not require at least one uppercase letter, it may be easier for an attacker to guess or crack user passwords.

## 推荐措施

To require that the password policy for your user pool requires at least one uppercase letter, you can use the AWS Management Console or the AWS CLI. For more information, see the documentation on user pool settings and policies.

- 推荐链接：[https://docs.aws.amazon.com/cognito/latest/developerguide/user-pool-settings-policies.html](https://docs.aws.amazon.com/cognito/latest/developerguide/user-pool-settings-policies.html)

## 修复步骤

No remediation steps available.

## 参考资料

- [https://docs.aws.amazon.com/cognito/latest/developerguide/user-pool-settings-policies.html](https://docs.aws.amazon.com/cognito/latest/developerguide/user-pool-settings-policies.html)

## 技术信息

- Source Metadata：[sources/aws/cognito_user_pool_password_policy_uppercase/metadata.json](../../sources/aws/cognito_user_pool_password_policy_uppercase/metadata.json)
- Source Code：[sources/aws/cognito_user_pool_password_policy_uppercase/check.py](../../sources/aws/cognito_user_pool_password_policy_uppercase/check.py)
- Source Metadata Path：`sources/aws/cognito_user_pool_password_policy_uppercase/metadata.json`
- Source Code Path：`sources/aws/cognito_user_pool_password_policy_uppercase/check.py`
