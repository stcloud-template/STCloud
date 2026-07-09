# Ensure that the password policy for your user pools require a minimum length of 14 or greater

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `cognito_user_pool_password_policy_minimum_length_14` |
| 云平台 | AWS |
| 服务 | cognito |
| 严重等级 | medium |
| 类别 | Uncategorized |
| 资源类型 | AwsCognitoUserPool |
| 资源组 | IAM |

## 描述

User pools allow you to configure a password policy for your user pool to specify complexity requirements for user passwords. The password policy for your user pools should require a minimum length of 14 or greater.

## 风险

If the password policy for your user pools does not require a minimum length of 14 or greater, it may be easier for attackers to guess or brute force user passwords.

## 推荐措施

To require a minimum length of 14 or greater for user passwords in your user pools, you can update the password policy for your user pool using the AWS Management Console, AWS CLI, or SDK.

- 推荐链接：[https://docs.aws.amazon.com/cognito/latest/developerguide/user-pool-settings-policies.html](https://docs.aws.amazon.com/cognito/latest/developerguide/user-pool-settings-policies.html)

## 修复步骤

No remediation steps available.

## 参考资料

- [https://docs.aws.amazon.com/cognito/latest/developerguide/user-pool-settings-policies.html](https://docs.aws.amazon.com/cognito/latest/developerguide/user-pool-settings-policies.html)

## 技术信息

- Source Metadata：[sources/aws/cognito_user_pool_password_policy_minimum_length_14/metadata.json](../../sources/aws/cognito_user_pool_password_policy_minimum_length_14/metadata.json)
- Source Code：[sources/aws/cognito_user_pool_password_policy_minimum_length_14/check.py](../../sources/aws/cognito_user_pool_password_policy_minimum_length_14/check.py)
- Source Metadata Path：`sources/aws/cognito_user_pool_password_policy_minimum_length_14/metadata.json`
- Source Code Path：`sources/aws/cognito_user_pool_password_policy_minimum_length_14/check.py`
