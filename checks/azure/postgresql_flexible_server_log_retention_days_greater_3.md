# Ensure Server Parameter 'log_retention_days' is greater than 3 days for PostgreSQL Database Server

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `postgresql_flexible_server_log_retention_days_greater_3` |
| クラウドプラットフォーム | Azure |
| サービス | postgresql |
| 重大度 | medium |
| カテゴリ | Uncategorized |
| リソースタイプ | PostgreSQL |
| リソースグループ | database |

## 説明

Ensure log_retention_days on PostgreSQL Servers is set to an appropriate value.

## リスク

Configuring log_retention_days determines the duration in days that Azure Database for PostgreSQL retains log files. Query and error logs can be used to identify, troubleshoot, and repair configuration errors and sub-optimal performance.

## 推奨事項

From Azure Portal 1. From Azure Home select the Portal Menu. 2. Go to Azure Database for PostgreSQL servers. 3. For each database, click on Server parameters. 4. Search for log_retention_days. 5. Input a value between 4 and 7 (inclusive) and click Save. From Azure CLI Use the below command to update log_retention_days configuration. az postgres server configuration set --resource-group <resourceGroupName> -- server-name <serverName> --name log_retention_days --value <4-7> From Powershell Use the below command to update log_retention_days configuration. Update-AzPostgreSqlConfiguration -ResourceGroupName <ResourceGroupName> - ServerName <ServerName> -Name log_retention_days -Value <4-7>

- 推奨リンク：[https://learn.microsoft.com/en-us/rest/api/postgresql/singleserver/configurations/list-by-server?view=rest-postgresql-singleserver-2017-12-01&tabs=HTTP](https://learn.microsoft.com/en-us/rest/api/postgresql/singleserver/configurations/list-by-server?view=rest-postgresql-singleserver-2017-12-01&tabs=HTTP)

## 修正手順


### CLI

```text
az postgres server configuration set --resource-group <resourceGroupName> --server-name <serverName> --name log_retention_days --value <4-7>
```

### Other

[https://www.trendmicro.com/cloudoneconformity-staging/knowledge-base/azure/PostgreSQL/log-retention-days.html](https://www.trendmicro.com/cloudoneconformity-staging/knowledge-base/azure/PostgreSQL/log-retention-days.html)

## 参考資料

- [https://docs.microsoft.com/en-us/azure/postgresql/howto-configure-server-parameters-using-portal](https://docs.microsoft.com/en-us/azure/postgresql/howto-configure-server-parameters-using-portal)
- [https://learn.microsoft.com/en-us/rest/api/postgresql/singleserver/configurations/list-by-server?view=rest-postgresql-singleserver-2017-12-01&tabs=HTTP](https://learn.microsoft.com/en-us/rest/api/postgresql/singleserver/configurations/list-by-server?view=rest-postgresql-singleserver-2017-12-01&tabs=HTTP)

## 技術情報

- Source Metadata：[sources/azure/postgresql_flexible_server_log_retention_days_greater_3/metadata.json](../../sources/azure/postgresql_flexible_server_log_retention_days_greater_3/metadata.json)
- Source Code：[sources/azure/postgresql_flexible_server_log_retention_days_greater_3/check.py](../../sources/azure/postgresql_flexible_server_log_retention_days_greater_3/check.py)
- Source Metadata Path：`sources/azure/postgresql_flexible_server_log_retention_days_greater_3/metadata.json`
- Source Code Path：`sources/azure/postgresql_flexible_server_log_retention_days_greater_3/check.py`
