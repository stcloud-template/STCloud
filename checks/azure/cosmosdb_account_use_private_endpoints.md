# Ensure That Private Endpoints Are Used Where Possible

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `cosmosdb_account_use_private_endpoints` |
| 云平台 | Azure |
| 服务 | cosmosdb |
| 严重等级 | medium |
| 类别 | Uncategorized |
| 资源类型 | CosmosDB |
| 资源组 | database |

## 描述

Private endpoints limit network traffic to approved sources.

## 风险

For sensitive data, private endpoints allow granular control of which services can communicate with Cosmos DB and ensure that this network traffic is private. You set this up on a case by case basis for each service you wish to be connected.

## 推荐措施

1. Open the portal menu. 2. Select the Azure Cosmos DB blade. 3. Select the Azure Cosmos DB account. 4. Select Networking. 5. Select Private access. 6. Click + Private Endpoint. 7. Provide a Name. 8. Click Next. 9. From the Resource type drop down, select Microsoft.AzureCosmosDB/databaseAccounts. 10. From the Resource drop down, select the Cosmos DB account. 11. Click Next. 12. Provide appropriate Virtual Network details. 13. Click Next. 14. Provide appropriate DNS details. 15. Click Next. 16. Optionally provide Tags. 17. Click Next : Review + create. 18. Click Create.

- 推荐链接：[https://docs.microsoft.com/en-us/azure/private-link/tutorial-private-endpoint-cosmosdb-portal](https://docs.microsoft.com/en-us/azure/private-link/tutorial-private-endpoint-cosmosdb-portal)

## 修复步骤

No remediation steps available.

## 参考资料

- [https://docs.microsoft.com/en-us/azure/cosmos-db/how-to-configure-private-endpoints](https://docs.microsoft.com/en-us/azure/cosmos-db/how-to-configure-private-endpoints)
- [https://docs.microsoft.com/en-us/azure/private-link/tutorial-private-endpoint-cosmosdb-portal](https://docs.microsoft.com/en-us/azure/private-link/tutorial-private-endpoint-cosmosdb-portal)

## 技术信息

- Source Metadata：[sources/azure/cosmosdb_account_use_private_endpoints/metadata.json](../../sources/azure/cosmosdb_account_use_private_endpoints/metadata.json)
- Source Code：[sources/azure/cosmosdb_account_use_private_endpoints/check.py](../../sources/azure/cosmosdb_account_use_private_endpoints/check.py)
- Source Metadata Path：`sources/azure/cosmosdb_account_use_private_endpoints/metadata.json`
- Source Code Path：`sources/azure/cosmosdb_account_use_private_endpoints/check.py`
