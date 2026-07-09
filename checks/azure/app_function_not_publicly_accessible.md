# Ensure Azure Functions are not publicly accessible

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `app_function_not_publicly_accessible` |
| 云平台 | Azure |
| 服务 | app |
| 子服务 | function |
| 严重等级 | high |
| 类别 | Uncategorized |
| 资源类型 | Microsoft.Web/sites |
| 资源组 | serverless |

## 描述

Azure Functions should not be exposed to the public internet. Restricting access helps protect applications from potential threats and reduces the attack surface.

## 风险

Exposing Azure Functions to the public internet increases the risk of unauthorized access, data breaches, and other security threats.

## 推荐措施

Review the Azure Functions security guidelines and ensure that access restrictions are in place. Use Azure Private Link and Key Vault for enhanced security.

- 推荐链接：[https://learn.microsoft.com/en-us/azure/app-service/overview-access-restrictions](https://learn.microsoft.com/en-us/azure/app-service/overview-access-restrictions)

## 修复步骤


### Other

[https://www.trendmicro.com/cloudoneconformity/knowledge-base/azure/Functions/azure-function-exposed.html](https://www.trendmicro.com/cloudoneconformity/knowledge-base/azure/Functions/azure-function-exposed.html)

## 参考资料

- [https://learn.microsoft.com/en-us/azure/azure-functions/functions-networking-options](https://learn.microsoft.com/en-us/azure/azure-functions/functions-networking-options)
- [https://learn.microsoft.com/en-us/azure/app-service/overview-access-restrictions](https://learn.microsoft.com/en-us/azure/app-service/overview-access-restrictions)

## 技术信息

- Source Metadata：[sources/azure/app_function_not_publicly_accessible/metadata.json](../../sources/azure/app_function_not_publicly_accessible/metadata.json)
- Source Code：[sources/azure/app_function_not_publicly_accessible/check.py](../../sources/azure/app_function_not_publicly_accessible/check.py)
- Source Metadata Path：`sources/azure/app_function_not_publicly_accessible/metadata.json`
- Source Code Path：`sources/azure/app_function_not_publicly_accessible/check.py`
