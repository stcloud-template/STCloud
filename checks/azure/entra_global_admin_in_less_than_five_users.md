# Ensure fewer than 5 users have global administrator assignment

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `entra_global_admin_in_less_than_five_users` |
| 云平台 | Azure |
| 服务 | entra |
| 严重等级 | high |
| 类别 | Uncategorized |
| 资源类型 | #microsoft.graph.directoryRole |
| 资源组 | IAM |

## 描述

This recommendation aims to maintain a balance between security and operational efficiency by ensuring that a minimum of 2 and a maximum of 4 users are assigned the Global Administrator role in Microsoft Entra ID. Having at least two Global Administrators ensures redundancy, while limiting the number to four reduces the risk of excessive privileged access.

## 风险

The Global Administrator role has extensive privileges across all services in Microsoft Entra ID. The Global Administrator role should never be used in regular daily activities, administrators should have a regular user account for daily activities, and a separate account for administrative responsibilities. Limiting the number of Global Administrators helps mitigate the risk of unauthorized access, reduces the potential impact of human error, and aligns with the principle of least privilege to reduce the attack surface of an Azure tenant. Conversely, having at least two Global Administrators ensures that administrative functions can be performed without interruption in case of unavailability of a single admin.

## 推荐措施

1. From Azure Home select the Portal Menu 2. Select Microsoft Entra ID 3. Select Roles and Administrators 4. Select Global Administrator 5. Ensure less than 5 users are actively assigned the role. 6. Ensure that at least 2 users are actively assigned the role.

- 推荐链接：[https://learn.microsoft.com/en-us/microsoft-365/admin/add-users/about-admin-roles?view=o365-worldwide#security-guidelines-for-assigning-roles](https://learn.microsoft.com/en-us/microsoft-365/admin/add-users/about-admin-roles?view=o365-worldwide#security-guidelines-for-assigning-roles)

## 修复步骤

No remediation steps available.

## 参考资料

- [https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/best-practices#5-limit-the-number-of-global-administrators-to-less-than-5](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/best-practices#5-limit-the-number-of-global-administrators-to-less-than-5)
- [https://learn.microsoft.com/en-us/microsoft-365/admin/add-users/about-admin-roles?view=o365-worldwide#security-guidelines-for-assigning-roles](https://learn.microsoft.com/en-us/microsoft-365/admin/add-users/about-admin-roles?view=o365-worldwide#security-guidelines-for-assigning-roles)

## 技术信息

- Source Metadata：[sources/azure/entra_global_admin_in_less_than_five_users/metadata.json](../../sources/azure/entra_global_admin_in_less_than_five_users/metadata.json)
- Source Code：[sources/azure/entra_global_admin_in_less_than_five_users/check.py](../../sources/azure/entra_global_admin_in_less_than_five_users/check.py)
- Source Metadata Path：`sources/azure/entra_global_admin_in_less_than_five_users/metadata.json`
- Source Code Path：`sources/azure/entra_global_admin_in_less_than_five_users/check.py`
