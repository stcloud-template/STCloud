# Ensure that your Azure functions are not configured with an identity with admin privileges

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `app_function_identity_without_admin_privileges` |
| 云平台 | Azure |
| 服务 | app |
| 子服务 | function |
| 严重等级 | high |
| 类别 | Uncategorized |
| 资源类型 | Microsoft.Web/sites |
| 资源组 | serverless |

## 描述

It is important to ensure that Azure functions are not configured with administrative privileges to maintain the principle of least privilege and reduce the attack surface. By limiting the privileges of Azure functions, potential security risks and data leaks can be mitigated.

## 风险

If Azure functions are configured with administrative privileges, it increases the risk of unauthorized access, privilege escalation, and data breaches. Attackers can exploit these privileges to gain access to sensitive data and compromise the entire system.

## 推荐措施

To remediate this issue, ensure that Azure functions are not configured with an identity that has administrative privileges. Instead, use the principle of least privilege to grant only the necessary permissions to Azure functions. For more information, refer to the official documentation: Use the principle of least privilege.

- 推荐链接：[https://docs.microsoft.com/en-us/azure/architecture/framework/security/design-identity-authorization#use-the-principle-of-least-privilege](https://docs.microsoft.com/en-us/azure/architecture/framework/security/design-identity-authorization#use-the-principle-of-least-privilege)

## 修复步骤


### Other

[https://www.trendmicro.com/cloudoneconformity/knowledge-base/azure/Functions/azure-function-admin-permissions.html](https://www.trendmicro.com/cloudoneconformity/knowledge-base/azure/Functions/azure-function-admin-permissions.html)

## 参考资料

- [https://learn.microsoft.com/en-us/entra/identity/managed-identities-azure-resources/overview](https://learn.microsoft.com/en-us/entra/identity/managed-identities-azure-resources/overview)
- [https://docs.microsoft.com/en-us/azure/architecture/framework/security/design-identity-authorization#use-the-principle-of-least-privilege](https://docs.microsoft.com/en-us/azure/architecture/framework/security/design-identity-authorization#use-the-principle-of-least-privilege)

## 技术信息

- Source Metadata：[sources/azure/app_function_identity_without_admin_privileges/metadata.json](../../sources/azure/app_function_identity_without_admin_privileges/metadata.json)
- Source Code：[sources/azure/app_function_identity_without_admin_privileges/check.py](../../sources/azure/app_function_identity_without_admin_privileges/check.py)
- Source Metadata Path：`sources/azure/app_function_identity_without_admin_privileges/metadata.json`
- Source Code Path：`sources/azure/app_function_identity_without_admin_privileges/check.py`
