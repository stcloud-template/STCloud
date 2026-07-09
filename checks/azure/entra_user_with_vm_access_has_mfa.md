# Ensure only MFA enabled identities can access privileged Virtual Machine

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `entra_user_with_vm_access_has_mfa` |
| 云平台 | Azure |
| 服务 | entra |
| 严重等级 | medium |
| 类别 | Uncategorized |
| 资源类型 | #microsoft.graph.users |
| 资源组 | IAM |

## 描述

Verify identities without MFA that can log in to a privileged virtual machine using separate login credentials. An adversary can leverage the access to move laterally and perform actions with the virtual machine's managed identity. Make sure the virtual machine only has necessary permissions, and revoke the admin-level permissions according to the least privileges principal

## 风险

Managed disks are by default encrypted on the underlying hardware, so no additional encryption is required for basic protection. It is available if additional encryption is required. Managed disks are by design more resilient that storage accounts. For ARM-deployed Virtual Machines, Azure Adviser will at some point recommend moving VHDs to managed disks both from a security and cost management perspective.

## 推荐措施

1. Log in to the Azure portal. Reducing access of managed identities attached to virtual machines. 2. This can be remediated by enabling MFA for user, Removing user access or • Case I : Enable MFA for users having access on virtual machines. 1. Navigate to Azure AD from the left pane and select Users from the Manage section. 2. Click on Per-User MFA from the top menu options and select each user with MULTI-FACTOR AUTH STATUS as Disabled and can login to virtual machines:  From quick steps on the right side select enable.  Click on enable multi-factor auth and share the link with the user to setup MFA as required. • Case II : Removing user access on a virtual machine. 1. Select the Subscription, then click on Access control (IAM). 2. Select Role assignments and search for Virtual Machine Administrator Login or Virtual Machine User Login or any role that provides access to log into virtual machines. 3. Click on Role Name, Select Assignments, and remove identities with no MFA configured. • Case III : Reducing access of managed identities attached to virtual machines. 1. Select the Subscription, then click on Access control (IAM). 2. Select Role Assignments from the top menu and apply filters on Assignment type as Privileged administrator roles and Type as Virtual Machines. 3. Click on Role Name, Select Assignments, and remove identities access make sure this follows the least privileges principal.

## 修复步骤

No remediation steps available.

## 参考资料

No external references available.

## 技术信息

- Source Metadata：[sources/azure/entra_user_with_vm_access_has_mfa/metadata.json](../../sources/azure/entra_user_with_vm_access_has_mfa/metadata.json)
- Source Code：[sources/azure/entra_user_with_vm_access_has_mfa/check.py](../../sources/azure/entra_user_with_vm_access_has_mfa/check.py)
- Source Metadata Path：`sources/azure/entra_user_with_vm_access_has_mfa/metadata.json`
- Source Code Path：`sources/azure/entra_user_with_vm_access_has_mfa/check.py`
