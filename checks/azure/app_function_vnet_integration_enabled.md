# Ensure Virtual Network Integration is Enabled for Azure Functions

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `app_function_vnet_integration_enabled` |
| クラウドプラットフォーム | Azure |
| サービス | app |
| サブサービス | function |
| 重大度 | high |
| カテゴリ | Uncategorized |
| リソースタイプ | Microsoft.Web/sites |
| リソースグループ | serverless |

## 説明

Enabling Virtual Network Integration for Azure Functions provides an additional layer of security by restricting access to selected virtual network subnets. This helps to protect your Function Apps from unauthorized access and potential threats.

## リスク

Without Virtual Network Integration, your Function Apps may be exposed to the public internet, increasing the risk of unauthorized access and potential security breaches.

## 推奨事項

It is recommended to enable Virtual Network Integration for Azure Functions to enhance security and protect against unauthorized access.

- 推奨リンク：[https://docs.microsoft.com/en-us/azure/azure-functions/functions-networking-options#enable-virtual-network-integration](https://docs.microsoft.com/en-us/azure/azure-functions/functions-networking-options#enable-virtual-network-integration)

## 修正手順


### CLI

```text
az functionapp vnet-integration update --name <function_app_name> --resource-group <resource_group_name> --vnet <vnet_name> --subnet <subnet_name>
```

### Other

[https://www.trendmicro.com/cloudoneconformity/knowledge-base/azure/Functions/azure-function-vnet-integration-on.html](https://www.trendmicro.com/cloudoneconformity/knowledge-base/azure/Functions/azure-function-vnet-integration-on.html)

## 参考資料

- [https://docs.microsoft.com/en-us/azure/azure-functions/functions-networking-options#virtual-network-integration](https://docs.microsoft.com/en-us/azure/azure-functions/functions-networking-options#virtual-network-integration)
- [https://docs.microsoft.com/en-us/azure/azure-functions/functions-networking-options#enable-virtual-network-integration](https://docs.microsoft.com/en-us/azure/azure-functions/functions-networking-options#enable-virtual-network-integration)

## 技術情報

- Source Metadata：[sources/azure/app_function_vnet_integration_enabled/metadata.json](../../sources/azure/app_function_vnet_integration_enabled/metadata.json)
- Source Code：[sources/azure/app_function_vnet_integration_enabled/check.py](../../sources/azure/app_function_vnet_integration_enabled/check.py)
- Source Metadata Path：`sources/azure/app_function_vnet_integration_enabled/metadata.json`
- Source Code Path：`sources/azure/app_function_vnet_integration_enabled/check.py`
