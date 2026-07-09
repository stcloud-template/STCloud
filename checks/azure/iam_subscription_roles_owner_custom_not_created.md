# Ensure that no custom subscription owner roles are created

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `iam_subscription_roles_owner_custom_not_created` |
| 云平台 | Azure |
| 服务 | iam |
| 严重等级 | high |
| 类别 | Uncategorized |
| 资源类型 | AzureRole |
| 资源组 | IAM |

## 描述

Ensure that no custom subscription owner roles are created

## 风险

Subscription ownership should not include permission to create custom owner roles. The principle of least privilege should be followed and only necessary privileges should be assigned instead of allowing full administrative access.

## 推荐措施

Custom subscription owner roles should not be created. This is because the principle of least privilege should be followed and only necessary privileges should be assigned instead of allowing full administrative access

- 推荐链接：[https://www.trendmicro.com/cloudoneconformity-staging/knowledge-base/azure/AccessControl/remove-custom-owner-roles.html](https://www.trendmicro.com/cloudoneconformity-staging/knowledge-base/azure/AccessControl/remove-custom-owner-roles.html)

## 修复步骤


### Other

[https://www.trendmicro.com/cloudoneconformity-staging/knowledge-base/azure/AccessControl/remove-custom-owner-roles.html](https://www.trendmicro.com/cloudoneconformity-staging/knowledge-base/azure/AccessControl/remove-custom-owner-roles.html)

## 参考资料

- [https://learn.microsoft.com/en-us/azure/role-based-access-control/custom-roles](https://learn.microsoft.com/en-us/azure/role-based-access-control/custom-roles)
- [https://www.trendmicro.com/cloudoneconformity-staging/knowledge-base/azure/AccessControl/remove-custom-owner-roles.html](https://www.trendmicro.com/cloudoneconformity-staging/knowledge-base/azure/AccessControl/remove-custom-owner-roles.html)

## 技术信息

- Source Metadata：[sources/azure/iam_subscription_roles_owner_custom_not_created/metadata.json](../../sources/azure/iam_subscription_roles_owner_custom_not_created/metadata.json)
- Source Code：[sources/azure/iam_subscription_roles_owner_custom_not_created/check.py](../../sources/azure/iam_subscription_roles_owner_custom_not_created/check.py)
- Source Metadata Path：`sources/azure/iam_subscription_roles_owner_custom_not_created/metadata.json`
- Source Code Path：`sources/azure/iam_subscription_roles_owner_custom_not_created/check.py`
