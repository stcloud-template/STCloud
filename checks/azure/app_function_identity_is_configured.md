# Ensure Azure function has system or user assigned managed identity configured

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `app_function_identity_is_configured` |
| 云平台 | Azure |
| 服务 | app |
| 子服务 | function |
| 严重等级 | medium |
| 类别 | Uncategorized |
| 资源类型 | Microsoft.Web/sites |
| 资源组 | serverless |

## 描述

Azure Functions should have managed identities configured for enhanced security and access control.

## 风险

Not using managed identities can lead to less secure authentication and authorization practices, potentially exposing sensitive data.

## 推荐措施

It is recommended to enable managed identities for Azure Functions to enhance security and access control. This allows the function app to easily access other Azure resources securely and with the appropriate permissions.

- 推荐链接：[https://learn.microsoft.com/en-us/azure/app-service/overview-managed-identity](https://learn.microsoft.com/en-us/azure/app-service/overview-managed-identity)

## 修复步骤


### CLI

```text
az functionapp identity assign --name <function_name> --resource-group <resource_group> --identities [system]
```

### Other

[https://www.trendmicro.com/cloudoneconformity/knowledge-base/azure/Functions/azure-function-system-assigned-identity.html](https://www.trendmicro.com/cloudoneconformity/knowledge-base/azure/Functions/azure-function-system-assigned-identity.html)

## 参考资料

- [https://learn.microsoft.com/en-us/entra/identity/managed-identities-azure-resources/overview](https://learn.microsoft.com/en-us/entra/identity/managed-identities-azure-resources/overview)
- [https://learn.microsoft.com/en-us/azure/app-service/overview-managed-identity](https://learn.microsoft.com/en-us/azure/app-service/overview-managed-identity)

## 技术信息

- Source Metadata：[sources/azure/app_function_identity_is_configured/metadata.json](../../sources/azure/app_function_identity_is_configured/metadata.json)
- Source Code：[sources/azure/app_function_identity_is_configured/check.py](../../sources/azure/app_function_identity_is_configured/check.py)
- Source Metadata Path：`sources/azure/app_function_identity_is_configured/metadata.json`
- Source Code Path：`sources/azure/app_function_identity_is_configured/check.py`
