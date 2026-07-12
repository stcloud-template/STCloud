# Ensure Azure Databricks workspaces are deployed in a customer-managed VNet (VNet Injection)

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `databricks_workspace_vnet_injection_enabled` |
| クラウドプラットフォーム | Azure |
| サービス | databricks |
| 重大度 | medium |
| カテゴリ | Uncategorized |
| リソースタイプ | AzureDatabricksWorkspace |
| リソースグループ | ai_ml |

## 説明

Checks whether Azure Databricks workspaces are deployed in a customer-managed Virtual Network (VNet Injection) instead of a Databricks-managed VNet.

## リスク

Using a Databricks-managed VNet limits control over network security policies, firewall configurations, and routing, increasing the risk of unauthorized access or data exfiltration.

## 推奨事項

Deploy Databricks workspaces into a customer-managed VNet to ensure better control over network security and compliance.

- 推奨リンク：[https://www.trendmicro.com/cloudoneconformity/knowledge-base/azure/Databricks/check-for-vnet-injection.html](https://www.trendmicro.com/cloudoneconformity/knowledge-base/azure/Databricks/check-for-vnet-injection.html)

## 修正手順


### CLI

```text
az databricks workspace create --name <databricks-workspace-name> --resource-group <resource-group-name> --location <region> --managed-resource-group <managed-rg-name> --enable-no-public-ip true --network-security-group-rule "NoAzureServices" --public-network-access Disabled --custom-virtual-network-id /subscriptions/<subscription-id>/resourceGroups/<resource-group-name>/providers/Microsoft.Network/virtualNetworks/<vnet-name>
```

## 参考資料

- [https://learn.microsoft.com/en-us/azure/databricks/administration-guide/cloud-configurations/azure/vnet-inject](https://learn.microsoft.com/en-us/azure/databricks/administration-guide/cloud-configurations/azure/vnet-inject)
- [https://www.trendmicro.com/cloudoneconformity/knowledge-base/azure/Databricks/check-for-vnet-injection.html](https://www.trendmicro.com/cloudoneconformity/knowledge-base/azure/Databricks/check-for-vnet-injection.html)

## 技術情報

- Source Metadata：[sources/azure/databricks_workspace_vnet_injection_enabled/metadata.json](../../sources/azure/databricks_workspace_vnet_injection_enabled/metadata.json)
- Source Code：[sources/azure/databricks_workspace_vnet_injection_enabled/check.py](../../sources/azure/databricks_workspace_vnet_injection_enabled/check.py)
- Source Metadata Path：`sources/azure/databricks_workspace_vnet_injection_enabled/metadata.json`
- Source Code Path：`sources/azure/databricks_workspace_vnet_injection_enabled/check.py`
