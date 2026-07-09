# Ensure Server Parameter 'log_retention_days' is greater than 3 days for PostgreSQL Database Server

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `postgresql_flexible_server_log_retention_days_greater_3` |
| 云平台 | Azure |
| 服务 | postgresql |
| 严重等级 | medium |
| 类别 | Uncategorized |
| 资源类型 | PostgreSQL |
| 资源组 | database |

## 描述

Ensure log_retention_days on PostgreSQL Servers is set to an appropriate value.

## 风险

Configuring log_retention_days determines the duration in days that Azure Database for PostgreSQL retains log files. Query and error logs can be used to identify, troubleshoot, and repair configuration errors and sub-optimal performance.

## 推荐措施

From Azure Portal 1. From Azure Home select the Portal Menu. 2. Go to Azure Database for PostgreSQL servers. 3. For each database, click on Server parameters. 4. Search for log_retention_days. 5. Input a value between 4 and 7 (inclusive) and click Save. From Azure CLI Use the below command to update log_retention_days configuration. az postgres server configuration set --resource-group <resourceGroupName> -- server-name <serverName> --name log_retention_days --value <4-7> From Powershell Use the below command to update log_retention_days configuration. Update-AzPostgreSqlConfiguration -ResourceGroupName <ResourceGroupName> - ServerName <ServerName> -Name log_retention_days -Value <4-7>

- 推荐链接：[https://learn.microsoft.com/en-us/rest/api/postgresql/singleserver/configurations/list-by-server?view=rest-postgresql-singleserver-2017-12-01&tabs=HTTP](https://learn.microsoft.com/en-us/rest/api/postgresql/singleserver/configurations/list-by-server?view=rest-postgresql-singleserver-2017-12-01&tabs=HTTP)

## 修复步骤


### CLI

```text
az postgres server configuration set --resource-group <resourceGroupName> --server-name <serverName> --name log_retention_days --value <4-7>
```

### Other

[https://www.trendmicro.com/cloudoneconformity-staging/knowledge-base/azure/PostgreSQL/log-retention-days.html](https://www.trendmicro.com/cloudoneconformity-staging/knowledge-base/azure/PostgreSQL/log-retention-days.html)

## 参考资料

- [https://docs.microsoft.com/en-us/azure/postgresql/howto-configure-server-parameters-using-portal](https://docs.microsoft.com/en-us/azure/postgresql/howto-configure-server-parameters-using-portal)
- [https://learn.microsoft.com/en-us/rest/api/postgresql/singleserver/configurations/list-by-server?view=rest-postgresql-singleserver-2017-12-01&tabs=HTTP](https://learn.microsoft.com/en-us/rest/api/postgresql/singleserver/configurations/list-by-server?view=rest-postgresql-singleserver-2017-12-01&tabs=HTTP)

## 技术信息

- Source Metadata：[sources/azure/postgresql_flexible_server_log_retention_days_greater_3/metadata.json](../../sources/azure/postgresql_flexible_server_log_retention_days_greater_3/metadata.json)
- Source Code：[sources/azure/postgresql_flexible_server_log_retention_days_greater_3/check.py](../../sources/azure/postgresql_flexible_server_log_retention_days_greater_3/check.py)
- Source Metadata Path：`sources/azure/postgresql_flexible_server_log_retention_days_greater_3/metadata.json`
- Source Code Path：`sources/azure/postgresql_flexible_server_log_retention_days_greater_3/check.py`
