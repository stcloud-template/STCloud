# Ensure That 'Firewalls & Networks' Is Limited to Use Selected Networks Instead of All Networks

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `cosmosdb_account_firewall_use_selected_networks` |
| クラウドプラットフォーム | Azure |
| サービス | cosmosdb |
| 重大度 | medium |
| カテゴリ | Uncategorized |
| リソースタイプ | CosmosDB |
| リソースグループ | database |

## 説明

Limiting your Cosmos DB to only communicate on whitelisted networks lowers its attack footprint.

## リスク

Selecting certain networks for your Cosmos DB to communicate restricts the number of networks including the internet that can interact with what is stored within the database.

## 推奨事項

1. Open the portal menu. 2. Select the Azure Cosmos DB blade. 3. Select a Cosmos DB account to audit. 4. Select Networking. 5. Under Public network access, select Selected networks. 6. Under Virtual networks, select + Add existing virtual network or + Add a new virtual network. 7. For existing networks, select subscription, virtual network, subnet and click Add. For new networks, provide a name, update the default values if required, and click Create. 8. Click Save.

- 推奨リンク：[https://learn.microsoft.com/en-us/azure/storage/common/storage-network-security?tabs=azure-portal](https://learn.microsoft.com/en-us/azure/storage/common/storage-network-security?tabs=azure-portal)

## 修正手順


### CLI

```text
az cosmosdb database list / az cosmosdb show <database id> **isVirtualNetworkFilterEnabled should be set to true**
```

## 参考資料

- [https://docs.microsoft.com/en-us/azure/cosmos-db/how-to-configure-private-endpoints](https://docs.microsoft.com/en-us/azure/cosmos-db/how-to-configure-private-endpoints)
- [https://learn.microsoft.com/en-us/azure/storage/common/storage-network-security?tabs=azure-portal](https://learn.microsoft.com/en-us/azure/storage/common/storage-network-security?tabs=azure-portal)

## 技術情報

- Source Metadata：[sources/azure/cosmosdb_account_firewall_use_selected_networks/metadata.json](../../sources/azure/cosmosdb_account_firewall_use_selected_networks/metadata.json)
- Source Code：[sources/azure/cosmosdb_account_firewall_use_selected_networks/check.py](../../sources/azure/cosmosdb_account_firewall_use_selected_networks/check.py)
- Source Metadata Path：`sources/azure/cosmosdb_account_firewall_use_selected_networks/metadata.json`
- Source Code Path：`sources/azure/cosmosdb_account_firewall_use_selected_networks/check.py`
