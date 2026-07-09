# Use Azure Active Directory (AAD) Client Authentication and Azure RBAC where possible.

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `cosmosdb_account_use_aad_and_rbac` |
| 云平台 | Azure |
| 服务 | cosmosdb |
| 严重等级 | medium |
| 类别 | Uncategorized |
| 资源类型 | CosmosDB |
| 资源组 | database |

## 描述

Cosmos DB can use tokens or AAD for client authentication which in turn will use Azure RBAC for authorization. Using AAD is significantly more secure because AAD handles the credentials and allows for MFA and centralized management, and the Azure RBAC better integrated with the rest of Azure.

## 风险

AAD client authentication is considerably more secure than token-based authentication because the tokens must be persistent at the client. AAD does not require this.

## 推荐措施

Map all the resources that currently access to the Azure Cosmos DB account with keys or access tokens. Create an Azure Active Directory (AAD) identity for each of these resources: For Azure resources, you can create a managed identity . You may choose between system-assigned and user-assigned managed identities. For non-Azure resources, create an AAD identity. Grant each AAD identity the minimum permission it requires. When possible, we recommend you use one of the 2 built-in role definitions: Cosmos DB Built-in Data Reader or Cosmos DB Built-in Data Contributor. Validate that the new resource is functioning correctly. After new permissions are granted to identities, it may take a few hours until they propagate. When all resources are working correctly with the new identities, continue to the next step. You can use the az resource update powershell command: $cosmosdbname = 'cosmos-db-account-name' $resourcegroup = 'resource-group-name' $cosmosdb = az cosmosdb show --name $cosmosdbname --resource-group $resourcegroup | ConvertFrom-Json az resource update --ids $cosmosdb.id --set properties.disableLocalAuth=true --latest- include-preview

- 推荐链接：[https://learn.microsoft.com/en-us/azure/cosmos-db/role-based-access-control](https://learn.microsoft.com/en-us/azure/cosmos-db/role-based-access-control)

## 修复步骤

No remediation steps available.

## 参考资料

- [https://learn.microsoft.com/en-us/azure/cosmos-db/role-based-access-control](https://learn.microsoft.com/en-us/azure/cosmos-db/role-based-access-control)

## 技术信息

- Source Metadata：[sources/azure/cosmosdb_account_use_aad_and_rbac/metadata.json](../../sources/azure/cosmosdb_account_use_aad_and_rbac/metadata.json)
- Source Code：[sources/azure/cosmosdb_account_use_aad_and_rbac/check.py](../../sources/azure/cosmosdb_account_use_aad_and_rbac/check.py)
- Source Metadata Path：`sources/azure/cosmosdb_account_use_aad_and_rbac/metadata.json`
- Source Code Path：`sources/azure/cosmosdb_account_use_aad_and_rbac/check.py`
