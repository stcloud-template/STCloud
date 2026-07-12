# Ensure 'Allow access to Azure services' for PostgreSQL Database Server is disabled

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `postgresql_flexible_server_allow_access_services_disabled` |
| クラウドプラットフォーム | Azure |
| サービス | postgresql |
| 重大度 | medium |
| カテゴリ | Uncategorized |
| リソースタイプ | PostgreSQL |
| リソースグループ | database |

## 説明

Disable access from Azure services to PostgreSQL Database Server.

## リスク

If access from Azure services is enabled, the server's firewall will accept connections from all Azure resources, including resources not in your subscription. This is usually not a desired configuration. Instead, set up firewall rules to allow access from specific network ranges or VNET rules to allow access from specific virtual networks.

## 推奨事項

From Azure Portal 1. Login to Azure Portal using https://portal.azure.com. 2. Go to Azure Database for PostgreSQL servers. 3. For each database, click on Connection security. 4. Under Firewall rules, set Allow access to Azure services to No. 5. Click Save. From Azure CLI Use the below command to delete the AllowAllWindowsAzureIps rule for PostgreSQL Database. az postgres server firewall-rule delete --name AllowAllWindowsAzureIps -- resource-group <resourceGroupName> --server-name <serverName>

- 推奨リンク：[https://learn.microsoft.com/en-us/azure/postgresql/single-server/quickstart-create-server-database-azure-cli#configure-a-server-based-firewall-rule](https://learn.microsoft.com/en-us/azure/postgresql/single-server/quickstart-create-server-database-azure-cli#configure-a-server-based-firewall-rule)

## 修正手順


### CLI

```text
az postgres server firewall-rule delete --name AllowAllWindowsAzureIps --resource-group <resourceGroupName> --server-name <serverName>
```

### Terraform

[https://docs.ST Cloud.com/checks/azure/azure-general-policies/ensure-allow-access-to-azure-services-for-postgresql-database-server-is-disabled#terraform](https://docs.ST Cloud.com/checks/azure/azure-general-policies/ensure-allow-access-to-azure-services-for-postgresql-database-server-is-disabled#terraform)

### Other

[https://www.trendmicro.com/cloudoneconformity/knowledge-base/azure/PostgreSQL/disable-all-services-access.html#](https://www.trendmicro.com/cloudoneconformity/knowledge-base/azure/PostgreSQL/disable-all-services-access.html#)

## 参考資料

- [https://docs.microsoft.com/en-us/azure/postgresql/concepts-firewall-rules](https://docs.microsoft.com/en-us/azure/postgresql/concepts-firewall-rules)
- [https://learn.microsoft.com/en-us/azure/postgresql/single-server/quickstart-create-server-database-azure-cli#configure-a-server-based-firewall-rule](https://learn.microsoft.com/en-us/azure/postgresql/single-server/quickstart-create-server-database-azure-cli#configure-a-server-based-firewall-rule)

## 技術情報

- Source Metadata：[sources/azure/postgresql_flexible_server_allow_access_services_disabled/metadata.json](../../sources/azure/postgresql_flexible_server_allow_access_services_disabled/metadata.json)
- Source Code：[sources/azure/postgresql_flexible_server_allow_access_services_disabled/check.py](../../sources/azure/postgresql_flexible_server_allow_access_services_disabled/check.py)
- Source Metadata Path：`sources/azure/postgresql_flexible_server_allow_access_services_disabled/metadata.json`
- Source Code Path：`sources/azure/postgresql_flexible_server_allow_access_services_disabled/check.py`
