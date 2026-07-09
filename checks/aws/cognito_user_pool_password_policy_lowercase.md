# Ensure Cognito User Pool has password policy to require at least one lowercase letter

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `cognito_user_pool_password_policy_lowercase` |
| 云平台 | AWS |
| 服务 | cognito |
| 严重等级 | medium |
| 类别 | Uncategorized |
| 资源类型 | AwsCognitoUserPool |
| 资源组 | IAM |

## 描述

User pool password policy should require at least one lowercase letter.

## 风险

If the password policy does not require at least one lowercase letter, it may be easier for an attacker to crack the password.

## 推荐措施

To require at least one lowercase letter in the password, update the password policy for the user pool.

- 推荐链接：[https://docs.aws.amazon.com/cognito/latest/developerguide/user-pool-settings-policies.html](https://docs.aws.amazon.com/cognito/latest/developerguide/user-pool-settings-policies.html)

## 修复步骤

No remediation steps available.

## 参考资料

- [https://docs.aws.amazon.com/cognito/latest/developerguide/user-pool-settings-policies.html](https://docs.aws.amazon.com/cognito/latest/developerguide/user-pool-settings-policies.html)

## 技术信息

- Source Metadata：[sources/aws/cognito_user_pool_password_policy_lowercase/metadata.json](../../sources/aws/cognito_user_pool_password_policy_lowercase/metadata.json)
- Source Code：[sources/aws/cognito_user_pool_password_policy_lowercase/check.py](../../sources/aws/cognito_user_pool_password_policy_lowercase/check.py)
- Source Metadata Path：`sources/aws/cognito_user_pool_password_policy_lowercase/metadata.json`
- Source Code Path：`sources/aws/cognito_user_pool_password_policy_lowercase/check.py`
