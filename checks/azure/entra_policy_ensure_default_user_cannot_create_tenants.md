# Ensure that 'Restrict non-admin users from creating tenants' is set to 'Yes'

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `entra_policy_ensure_default_user_cannot_create_tenants` |
| 云平台 | Azure |
| 服务 | entra |
| 严重等级 | high |
| 类别 | Uncategorized |
| 资源类型 | #microsoft.graph.authorizationPolicy |
| 资源组 | IAM |

## 描述

Require administrators or appropriately delegated users to create new tenants.

## 风险

It is recommended to only allow an administrator to create new tenants. This prevent users from creating new Azure AD or Azure AD B2C tenants and ensures that only authorized users are able to do so.

## 推荐措施

1. From Azure Home select the Portal Menu 2. Select Azure Active Directory 3. Select Users 4. Select User settings 5. Set 'Restrict non-admin users from creating' tenants to 'Yes'

- 推荐链接：[https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#tenant-creator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#tenant-creator)

## 修复步骤

No remediation steps available.

## 参考资料

- [https://learn.microsoft.com/en-us/entra/fundamentals/users-default-permissions](https://learn.microsoft.com/en-us/entra/fundamentals/users-default-permissions)
- [https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#tenant-creator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#tenant-creator)

## 技术信息

- Source Metadata：[sources/azure/entra_policy_ensure_default_user_cannot_create_tenants/metadata.json](../../sources/azure/entra_policy_ensure_default_user_cannot_create_tenants/metadata.json)
- Source Code：[sources/azure/entra_policy_ensure_default_user_cannot_create_tenants/check.py](../../sources/azure/entra_policy_ensure_default_user_cannot_create_tenants/check.py)
- Source Metadata Path：`sources/azure/entra_policy_ensure_default_user_cannot_create_tenants/metadata.json`
- Source Code Path：`sources/azure/entra_policy_ensure_default_user_cannot_create_tenants/check.py`
