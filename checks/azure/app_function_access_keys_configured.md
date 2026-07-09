# Ensure that Azure Functions are using access keys for enhanced security

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `app_function_access_keys_configured` |
| 云平台 | Azure |
| 服务 | app |
| 子服务 | function |
| 严重等级 | high |
| 类别 | Uncategorized |
| 资源类型 | Microsoft.Web/sites |
| 资源组 | serverless |

## 描述

Azure Functions provide a way to secure HTTP function endpoints during development and production. Using access keys adds an extra layer of protection, ensuring that only authorized users or systems can access the functions. This is particularly important when dealing with public apps or sensitive data.

## 风险

Unprotected function endpoints may be vulnerable to unauthorized access, leading to potential data breaches or malicious activity.

## 推荐措施

Use access keys to secure Azure Functions. You can create and manage keys in the Azure portal or using the Azure CLI. For more information, see the official documentation.

- 推荐链接：[https://learn.microsoft.com/en-us/azure/azure-functions/security-concepts?tabs=v4#function-access-keys](https://learn.microsoft.com/en-us/azure/azure-functions/security-concepts?tabs=v4#function-access-keys)

## 修复步骤


### Other

[https://www.trendmicro.com/cloudoneconformity/knowledge-base/azure/Functions/azure-function-anonymous-access.html](https://www.trendmicro.com/cloudoneconformity/knowledge-base/azure/Functions/azure-function-anonymous-access.html)

## 参考资料

- [https://learn.microsoft.com/en-us/azure/azure-functions/functions-bindings-http-webhook-trigger?tabs=python-v2%2Cisolated-process%2Cnodejs-v4%2Cfunctionsv2&pivots=programming-language-csharp#authorization-keys](https://learn.microsoft.com/en-us/azure/azure-functions/functions-bindings-http-webhook-trigger?tabs=python-v2%2Cisolated-process%2Cnodejs-v4%2Cfunctionsv2&pivots=programming-language-csharp#authorization-keys)
- [https://learn.microsoft.com/en-us/azure/azure-functions/security-concepts?tabs=v4#function-access-keys](https://learn.microsoft.com/en-us/azure/azure-functions/security-concepts?tabs=v4#function-access-keys)

## 技术信息

- Source Metadata：[sources/azure/app_function_access_keys_configured/metadata.json](../../sources/azure/app_function_access_keys_configured/metadata.json)
- Source Code：[sources/azure/app_function_access_keys_configured/check.py](../../sources/azure/app_function_access_keys_configured/check.py)
- Source Metadata Path：`sources/azure/app_function_access_keys_configured/metadata.json`
- Source Code Path：`sources/azure/app_function_access_keys_configured/check.py`
