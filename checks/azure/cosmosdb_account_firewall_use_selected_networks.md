# Ensure That 'Firewalls & Networks' Is Limited to Use Selected Networks Instead of All Networks

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `cosmosdb_account_firewall_use_selected_networks` |
| 云平台 | Azure |
| 服务 | cosmosdb |
| 严重等级 | medium |
| 类别 | Uncategorized |
| 资源类型 | CosmosDB |
| 资源组 | database |

## 描述

Limiting your Cosmos DB to only communicate on whitelisted networks lowers its attack footprint.

## 风险

Selecting certain networks for your Cosmos DB to communicate restricts the number of networks including the internet that can interact with what is stored within the database.

## 推荐措施

1. Open the portal menu. 2. Select the Azure Cosmos DB blade. 3. Select a Cosmos DB account to audit. 4. Select Networking. 5. Under Public network access, select Selected networks. 6. Under Virtual networks, select + Add existing virtual network or + Add a new virtual network. 7. For existing networks, select subscription, virtual network, subnet and click Add. For new networks, provide a name, update the default values if required, and click Create. 8. Click Save.

- 推荐链接：[https://learn.microsoft.com/en-us/azure/storage/common/storage-network-security?tabs=azure-portal](https://learn.microsoft.com/en-us/azure/storage/common/storage-network-security?tabs=azure-portal)

## 修复步骤


### CLI

```text
az cosmosdb database list / az cosmosdb show <database id> **isVirtualNetworkFilterEnabled should be set to true**
```

## 参考资料

- [https://docs.microsoft.com/en-us/azure/cosmos-db/how-to-configure-private-endpoints](https://docs.microsoft.com/en-us/azure/cosmos-db/how-to-configure-private-endpoints)
- [https://learn.microsoft.com/en-us/azure/storage/common/storage-network-security?tabs=azure-portal](https://learn.microsoft.com/en-us/azure/storage/common/storage-network-security?tabs=azure-portal)

## 技术信息

- Source Metadata：[sources/azure/cosmosdb_account_firewall_use_selected_networks/metadata.json](../../sources/azure/cosmosdb_account_firewall_use_selected_networks/metadata.json)
- Source Code：[sources/azure/cosmosdb_account_firewall_use_selected_networks/check.py](../../sources/azure/cosmosdb_account_firewall_use_selected_networks/check.py)
- Source Metadata Path：`sources/azure/cosmosdb_account_firewall_use_selected_networks/metadata.json`
- Source Code Path：`sources/azure/cosmosdb_account_firewall_use_selected_networks/check.py`
