# Ensure 'User Access Administrator' role is restricted

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `iam_role_user_access_admin_restricted` |
| 云平台 | Azure |
| 服务 | iam |
| 严重等级 | high |
| 类别 | Uncategorized |
| 资源类型 | AzureIAMRoleassignment |
| 资源组 | IAM |

## 描述

Checks for active assignments of the highly privileged 'User Access Administrator' role in Azure subscriptions.

## 风险

Persistent assignment of this role can lead to privilege escalation and unauthorized access, increasing the risk of security breaches.

## 推荐措施

Remove 'User Access Administrator' role assignments immediately after use to minimize security risks.

- 推荐链接：[https://learn.microsoft.com/en-us/azure/role-based-access-control/elevate-access-global-admin?tabs=azure-portal%2Centra-audit-logs](https://learn.microsoft.com/en-us/azure/role-based-access-control/elevate-access-global-admin?tabs=azure-portal%2Centra-audit-logs)

## 修复步骤


### CLI

```text
az role assignment delete --role 'User Access Administrator' --scope '/subscriptions/<subscription_id>'
```

## 参考资料

- [https://learn.microsoft.com/en-us/azure/role-based-access-control/built-in-roles/privileged#user-access-administrator](https://learn.microsoft.com/en-us/azure/role-based-access-control/built-in-roles/privileged#user-access-administrator)
- [https://learn.microsoft.com/en-us/azure/role-based-access-control/elevate-access-global-admin?tabs=azure-portal%2Centra-audit-logs](https://learn.microsoft.com/en-us/azure/role-based-access-control/elevate-access-global-admin?tabs=azure-portal%2Centra-audit-logs)

## 技术信息

- Source Metadata：[sources/azure/iam_role_user_access_admin_restricted/metadata.json](../../sources/azure/iam_role_user_access_admin_restricted/metadata.json)
- Source Code：[sources/azure/iam_role_user_access_admin_restricted/check.py](../../sources/azure/iam_role_user_access_admin_restricted/check.py)
- Source Metadata Path：`sources/azure/iam_role_user_access_admin_restricted/metadata.json`
- Source Code Path：`sources/azure/iam_role_user_access_admin_restricted/check.py`
