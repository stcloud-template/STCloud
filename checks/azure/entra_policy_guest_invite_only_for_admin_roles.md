# Ensure that 'Guest invite restrictions' is set to 'Only users assigned to specific admin roles can invite guest users'

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `entra_policy_guest_invite_only_for_admin_roles` |
| 云平台 | Azure |
| 服务 | entra |
| 严重等级 | medium |
| 类别 | Uncategorized |
| 资源类型 | #microsoft.graph.authorizationPolicy |
| 资源组 | IAM |

## 描述

Restrict invitations to users with specific administrative roles only.

## 风险

Restricting invitations to users with specific administrator roles ensures that only authorized accounts have access to cloud resources. This helps to maintain 'Need to Know' permissions and prevents inadvertent access to data. By default the setting Guest invite restrictions is set to Anyone in the organization can invite guest users including guests and non-admins. This would allow anyone within the organization to invite guests and non-admins to the tenant, posing a security risk.

## 推荐措施

1. From Azure Home select the Portal Menu 2. Select Microsoft Entra ID 3. Then External Identities 4. Select External collaboration settings 5. Under Guest invite settings, for Guest invite restrictions, ensure that Only users assigned to specific admin roles can invite guest users is selected

- 推荐链接：[https://learn.microsoft.com/en-us/answers/questions/685101/how-to-allow-only-admins-to-add-guests](https://learn.microsoft.com/en-us/answers/questions/685101/how-to-allow-only-admins-to-add-guests)

## 修复步骤

No remediation steps available.

## 参考资料

- [https://learn.microsoft.com/en-us/entra/external-id/external-collaboration-settings-configure](https://learn.microsoft.com/en-us/entra/external-id/external-collaboration-settings-configure)
- [https://learn.microsoft.com/en-us/answers/questions/685101/how-to-allow-only-admins-to-add-guests](https://learn.microsoft.com/en-us/answers/questions/685101/how-to-allow-only-admins-to-add-guests)

## 技术信息

- Source Metadata：[sources/azure/entra_policy_guest_invite_only_for_admin_roles/metadata.json](../../sources/azure/entra_policy_guest_invite_only_for_admin_roles/metadata.json)
- Source Code：[sources/azure/entra_policy_guest_invite_only_for_admin_roles/check.py](../../sources/azure/entra_policy_guest_invite_only_for_admin_roles/check.py)
- Source Metadata Path：`sources/azure/entra_policy_guest_invite_only_for_admin_roles/metadata.json`
- Source Code Path：`sources/azure/entra_policy_guest_invite_only_for_admin_roles/check.py`
