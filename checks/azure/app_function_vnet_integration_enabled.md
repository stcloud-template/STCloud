# Ensure Virtual Network Integration is Enabled for Azure Functions

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `app_function_vnet_integration_enabled` |
| 云平台 | Azure |
| 服务 | app |
| 子服务 | function |
| 严重等级 | high |
| 类别 | Uncategorized |
| 资源类型 | Microsoft.Web/sites |
| 资源组 | serverless |

## 描述

Enabling Virtual Network Integration for Azure Functions provides an additional layer of security by restricting access to selected virtual network subnets. This helps to protect your Function Apps from unauthorized access and potential threats.

## 风险

Without Virtual Network Integration, your Function Apps may be exposed to the public internet, increasing the risk of unauthorized access and potential security breaches.

## 推荐措施

It is recommended to enable Virtual Network Integration for Azure Functions to enhance security and protect against unauthorized access.

- 推荐链接：[https://docs.microsoft.com/en-us/azure/azure-functions/functions-networking-options#enable-virtual-network-integration](https://docs.microsoft.com/en-us/azure/azure-functions/functions-networking-options#enable-virtual-network-integration)

## 修复步骤


### CLI

```text
az functionapp vnet-integration update --name <function_app_name> --resource-group <resource_group_name> --vnet <vnet_name> --subnet <subnet_name>
```

### Other

[https://www.trendmicro.com/cloudoneconformity/knowledge-base/azure/Functions/azure-function-vnet-integration-on.html](https://www.trendmicro.com/cloudoneconformity/knowledge-base/azure/Functions/azure-function-vnet-integration-on.html)

## 参考资料

- [https://docs.microsoft.com/en-us/azure/azure-functions/functions-networking-options#virtual-network-integration](https://docs.microsoft.com/en-us/azure/azure-functions/functions-networking-options#virtual-network-integration)
- [https://docs.microsoft.com/en-us/azure/azure-functions/functions-networking-options#enable-virtual-network-integration](https://docs.microsoft.com/en-us/azure/azure-functions/functions-networking-options#enable-virtual-network-integration)

## 技术信息

- Source Metadata：[sources/azure/app_function_vnet_integration_enabled/metadata.json](../../sources/azure/app_function_vnet_integration_enabled/metadata.json)
- Source Code：[sources/azure/app_function_vnet_integration_enabled/check.py](../../sources/azure/app_function_vnet_integration_enabled/check.py)
- Source Metadata Path：`sources/azure/app_function_vnet_integration_enabled/metadata.json`
- Source Code Path：`sources/azure/app_function_vnet_integration_enabled/check.py`
