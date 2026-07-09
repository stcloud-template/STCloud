# Ensure that the password policy for your Amazon Cognito user pool requires at least one symbol.

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `cognito_user_pool_password_policy_symbol` |
| 云平台 | AWS |
| 服务 | cognito |
| 严重等级 | medium |
| 类别 | Uncategorized |
| 资源类型 | AwsCognitoUserPool |
| 资源组 | IAM |

## 描述

Check whether the password policy for your Amazon Cognito user pool requires at least one symbol.

## 风险

If the password policy for your Amazon Cognito user pool does not require at least one symbol, it can be easier for attackers to crack passwords.

## 推荐措施

To require at least one symbol in the password policy for your Amazon Cognito user pool, you can use the AWS Management Console or the AWS CLI.

- 推荐链接：[https://docs.aws.amazon.com/cognito/latest/developerguide/user-pool-settings-policies.html](https://docs.aws.amazon.com/cognito/latest/developerguide/user-pool-settings-policies.html)

## 修复步骤

No remediation steps available.

## 参考资料

- [https://docs.aws.amazon.com/cognito/latest/developerguide/user-pool-settings-policies.html](https://docs.aws.amazon.com/cognito/latest/developerguide/user-pool-settings-policies.html)

## 技术信息

- Source Metadata：[sources/aws/cognito_user_pool_password_policy_symbol/metadata.json](../../sources/aws/cognito_user_pool_password_policy_symbol/metadata.json)
- Source Code：[sources/aws/cognito_user_pool_password_policy_symbol/check.py](../../sources/aws/cognito_user_pool_password_policy_symbol/check.py)
- Source Metadata Path：`sources/aws/cognito_user_pool_password_policy_symbol/metadata.json`
- Source Code Path：`sources/aws/cognito_user_pool_password_policy_symbol/check.py`
