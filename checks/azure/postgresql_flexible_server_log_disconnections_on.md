# Ensure server parameter 'log_disconnections' is set to 'ON' for PostgreSQL Database Server

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `postgresql_flexible_server_log_disconnections_on` |
| クラウドプラットフォーム | Azure |
| サービス | postgresql |
| 重大度 | medium |
| カテゴリ | Uncategorized |
| リソースタイプ | PostgreSQL |
| リソースグループ | database |

## 説明

Enable log_disconnections on PostgreSQL Servers.

## リスク

Enabling log_disconnections helps PostgreSQL Database to Logs end of a session, including duration, which in turn generates query and error logs. Query and error logs can be used to identify, troubleshoot, and repair configuration errors and sub-optimal performance.

## 推奨事項

From Azure Portal 1. From Azure Home select the Portal Menu 2. Go to Azure Database for PostgreSQL servers 3. For each database, click on Server parameters 4. Search for log_disconnections. 5. Click ON and save. From Azure CLI Use the below command to update log_disconnections configuration. az postgres server configuration set --resource-group <resourceGroupName> -- server-name <serverName> --name log_disconnections --value on From PowerShell Use the below command to update log_disconnections configuration. Update-AzPostgreSqlConfiguration -ResourceGroupName <ResourceGr

- 推奨リンク：[https://learn.microsoft.com/en-us/azure/postgresql/single-server/how-to-configure-server-parameters-using-portal](https://learn.microsoft.com/en-us/azure/postgresql/single-server/how-to-configure-server-parameters-using-portal)

## 修正手順


### CLI

```text
az postgres server configuration set --resource-group <resourceGroupName> --server-name <serverName> --name log_disconnections --value on
```

### Other

[https://www.trendmicro.com/cloudoneconformity/knowledge-base/azure/PostgreSQL/log-disconnections.html](https://www.trendmicro.com/cloudoneconformity/knowledge-base/azure/PostgreSQL/log-disconnections.html)

## 参考資料

- [https://docs.microsoft.com/en-us/rest/api/postgresql/singleserver/configurations/list-by-server](https://docs.microsoft.com/en-us/rest/api/postgresql/singleserver/configurations/list-by-server)
- [https://learn.microsoft.com/en-us/azure/postgresql/single-server/how-to-configure-server-parameters-using-portal](https://learn.microsoft.com/en-us/azure/postgresql/single-server/how-to-configure-server-parameters-using-portal)

## 技術情報

- Source Metadata：[sources/azure/postgresql_flexible_server_log_disconnections_on/metadata.json](../../sources/azure/postgresql_flexible_server_log_disconnections_on/metadata.json)
- Source Code：[sources/azure/postgresql_flexible_server_log_disconnections_on/check.py](../../sources/azure/postgresql_flexible_server_log_disconnections_on/check.py)
- Source Metadata Path：`sources/azure/postgresql_flexible_server_log_disconnections_on/metadata.json`
- Source Code Path：`sources/azure/postgresql_flexible_server_log_disconnections_on/check.py`
