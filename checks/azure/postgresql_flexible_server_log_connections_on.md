# Ensure server parameter 'log_connections' is set to 'ON' for PostgreSQL Database Server

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `postgresql_flexible_server_log_connections_on` |
| クラウドプラットフォーム | Azure |
| サービス | postgresql |
| 重大度 | medium |
| カテゴリ | Uncategorized |
| リソースタイプ | PostgreSQL |
| リソースグループ | database |

## 説明

Enable log_connections on PostgreSQL Servers.

## リスク

Enabling log_connections helps PostgreSQL Database to log attempted connection to the server, as well as successful completion of client authentication. Log data can be used to identify, troubleshoot, and repair configuration errors and suboptimal performance.

## 推奨事項

From Azure Portal 1. Login to Azure Portal using https://portal.azure.com. 2. Go to Azure Database for PostgreSQL servers. 3. For each database, click on Server parameters. 4. Search for log_connections. 5. Click ON and save. From Azure CLI Use the below command to update log_connections configuration. az postgres server configuration set --resource-group <resourceGroupName> -- server-name <serverName> --name log_connections --value on From PowerShell Use the below command to update log_connections configuration. Update-AzPostgreSqlConfiguration -ResourceGroupName <ResourceGroupName> - ServerName <ServerName> -Name log_connections -Value on

- 推奨リンク：[https://learn.microsoft.com/en-us/azure/postgresql/single-server/how-to-configure-server-parameters-using-portal](https://learn.microsoft.com/en-us/azure/postgresql/single-server/how-to-configure-server-parameters-using-portal)

## 修正手順


### CLI

```text
az postgres server configuration set --resource-group <resourceGroupName> --server-name <serverName> --name log_connections --value on
```

### Terraform

[https://docs.ST Cloud.com/checks/azure/azure-networking-policies/bc_azr_networking_12#terraform](https://docs.ST Cloud.com/checks/azure/azure-networking-policies/bc_azr_networking_12#terraform)

### Other

[https://www.trendmicro.com/cloudoneconformity-staging/knowledge-base/azure/PostgreSQL/log-connections.html](https://www.trendmicro.com/cloudoneconformity-staging/knowledge-base/azure/PostgreSQL/log-connections.html)

## 参考資料

- [https://docs.microsoft.com/en-us/rest/api/postgresql/configurations/listbyserver](https://docs.microsoft.com/en-us/rest/api/postgresql/configurations/listbyserver)
- [https://learn.microsoft.com/en-us/azure/postgresql/single-server/how-to-configure-server-parameters-using-portal](https://learn.microsoft.com/en-us/azure/postgresql/single-server/how-to-configure-server-parameters-using-portal)

## 技術情報

- Source Metadata：[sources/azure/postgresql_flexible_server_log_connections_on/metadata.json](../../sources/azure/postgresql_flexible_server_log_connections_on/metadata.json)
- Source Code：[sources/azure/postgresql_flexible_server_log_connections_on/check.py](../../sources/azure/postgresql_flexible_server_log_connections_on/check.py)
- Source Metadata Path：`sources/azure/postgresql_flexible_server_log_connections_on/metadata.json`
- Source Code Path：`sources/azure/postgresql_flexible_server_log_connections_on/check.py`
