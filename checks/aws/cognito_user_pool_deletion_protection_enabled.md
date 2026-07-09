# Ensure cognito user pools deletion protection enabled to prevent accidental deletion

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `cognito_user_pool_deletion_protection_enabled` |
| 云平台 | AWS |
| 服务 | cognito |
| 严重等级 | medium |
| 类别 | Uncategorized |
| 资源类型 | AwsCognitoUserPool |
| 资源组 | IAM |

## 描述

Deletion protection is a feature that allows you to lock a user pool to prevent it from being deleted. When deletion protection is enabled, you cannot delete the user pool. By default, deletion protection is disabled

## 风险

If deletion protection is not enabled, the user pool can be deleted by any user with the necessary permissions. This can lead to loss of data and service disruption

## 推荐措施

Deletion protection should be enabled for the user pool to prevent accidental deletion

- 推荐链接：[https://docs.aws.amazon.com/cognito/latest/developerguide/user-pool-settings-deletion-protection.html](https://docs.aws.amazon.com/cognito/latest/developerguide/user-pool-settings-deletion-protection.html)

## 修复步骤

No remediation steps available.

## 参考资料

- [https://docs.aws.amazon.com/cognito/latest/developerguide/user-pool-settings-deletion-protection.html](https://docs.aws.amazon.com/cognito/latest/developerguide/user-pool-settings-deletion-protection.html)

## 技术信息

- Source Metadata：[sources/aws/cognito_user_pool_deletion_protection_enabled/metadata.json](../../sources/aws/cognito_user_pool_deletion_protection_enabled/metadata.json)
- Source Code：[sources/aws/cognito_user_pool_deletion_protection_enabled/check.py](../../sources/aws/cognito_user_pool_deletion_protection_enabled/check.py)
- Source Metadata Path：`sources/aws/cognito_user_pool_deletion_protection_enabled/metadata.json`
- Source Code Path：`sources/aws/cognito_user_pool_deletion_protection_enabled/check.py`
