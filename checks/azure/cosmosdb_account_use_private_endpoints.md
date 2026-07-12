# Ensure That Private Endpoints Are Used Where Possible

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `cosmosdb_account_use_private_endpoints` |
| クラウドプラットフォーム | Azure |
| サービス | cosmosdb |
| 重大度 | medium |
| カテゴリ | Uncategorized |
| リソースタイプ | CosmosDB |
| リソースグループ | database |

## 説明

Private endpoints limit network traffic to approved sources.

## リスク

For sensitive data, private endpoints allow granular control of which services can communicate with Cosmos DB and ensure that this network traffic is private. You set this up on a case by case basis for each service you wish to be connected.

## 推奨事項

1. Open the portal menu. 2. Select the Azure Cosmos DB blade. 3. Select the Azure Cosmos DB account. 4. Select Networking. 5. Select Private access. 6. Click + Private Endpoint. 7. Provide a Name. 8. Click Next. 9. From the Resource type drop down, select Microsoft.AzureCosmosDB/databaseAccounts. 10. From the Resource drop down, select the Cosmos DB account. 11. Click Next. 12. Provide appropriate Virtual Network details. 13. Click Next. 14. Provide appropriate DNS details. 15. Click Next. 16. Optionally provide Tags. 17. Click Next : Review + create. 18. Click Create.

- 推奨リンク：[https://docs.microsoft.com/en-us/azure/private-link/tutorial-private-endpoint-cosmosdb-portal](https://docs.microsoft.com/en-us/azure/private-link/tutorial-private-endpoint-cosmosdb-portal)

## 修正手順

No remediation steps available.

## 参考資料

- [https://docs.microsoft.com/en-us/azure/cosmos-db/how-to-configure-private-endpoints](https://docs.microsoft.com/en-us/azure/cosmos-db/how-to-configure-private-endpoints)
- [https://docs.microsoft.com/en-us/azure/private-link/tutorial-private-endpoint-cosmosdb-portal](https://docs.microsoft.com/en-us/azure/private-link/tutorial-private-endpoint-cosmosdb-portal)

## 技術情報

- Source Metadata：[sources/azure/cosmosdb_account_use_private_endpoints/metadata.json](../../sources/azure/cosmosdb_account_use_private_endpoints/metadata.json)
- Source Code：[sources/azure/cosmosdb_account_use_private_endpoints/check.py](../../sources/azure/cosmosdb_account_use_private_endpoints/check.py)
- Source Metadata Path：`sources/azure/cosmosdb_account_use_private_endpoints/metadata.json`
- Source Code Path：`sources/azure/cosmosdb_account_use_private_endpoints/check.py`
