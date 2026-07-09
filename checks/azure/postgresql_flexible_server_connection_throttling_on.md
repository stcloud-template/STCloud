# Ensure server parameter 'connection_throttling' is set to 'ON' for PostgreSQL Database Server

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `postgresql_flexible_server_connection_throttling_on` |
| 云平台 | Azure |
| 服务 | postgresql |
| 严重等级 | medium |
| 类别 | Uncategorized |
| 资源类型 | PostgreSQL |
| 资源组 | database |

## 描述

Enable connection_throttling on PostgreSQL Servers.

## 风险

Enabling connection_throttling helps the PostgreSQL Database to Set the verbosity of logged messages. This in turn generates query and error logs with respect to concurrent connections that could lead to a successful Denial of Service (DoS) attack by exhausting connection resources. A system can also fail or be degraded by an overload of legitimate users. Query and error logs can be used to identify, troubleshoot, and repair configuration errors and sub-optimal performance.

## 推荐措施

From Azure Portal 1. Login to Azure Portal using https://portal.azure.com. 2. Go to Azure Database for PostgreSQL servers. 3. For each database, click on Server parameters. 4. Search for connection_throttling. 5. Click ON and save. From Azure CLI Use the below command to update connection_throttling configuration. az postgres server configuration set --resource-group <resourceGroupName> -- server-name <serverName> --name connection_throttling --value on From PowerShell Use the below command to update connection_throttling configuration. Update-AzPostgreSqlConfiguration -ResourceGroupName <ResourceGroupName> - ServerName <ServerName> -Name connection_throttling -Value on

- 推荐链接：[https://learn.microsoft.com/en-us/azure/postgresql/single-server/how-to-configure-server-parameters-using-portal](https://learn.microsoft.com/en-us/azure/postgresql/single-server/how-to-configure-server-parameters-using-portal)

## 修复步骤


### CLI

```text
az postgres server configuration set --resource-group <resourceGroupName> --server-name <serverName> --name connection_throttling --value on
```

### Terraform

[https://docs.ST Cloud.com/checks/azure/azure-networking-policies/bc_azr_networking_13#terraform](https://docs.ST Cloud.com/checks/azure/azure-networking-policies/bc_azr_networking_13#terraform)

### Other

[https://www.trendmicro.com/cloudoneconformity-staging/knowledge-base/azure/PostgreSQL/connection-throttling.html](https://www.trendmicro.com/cloudoneconformity-staging/knowledge-base/azure/PostgreSQL/connection-throttling.html)

## 参考资料

- [https://docs.microsoft.com/en-us/rest/api/postgresql/configurations/listbyserver](https://docs.microsoft.com/en-us/rest/api/postgresql/configurations/listbyserver)
- [https://learn.microsoft.com/en-us/azure/postgresql/single-server/how-to-configure-server-parameters-using-portal](https://learn.microsoft.com/en-us/azure/postgresql/single-server/how-to-configure-server-parameters-using-portal)

## 技术信息

- Source Metadata：[sources/azure/postgresql_flexible_server_connection_throttling_on/metadata.json](../../sources/azure/postgresql_flexible_server_connection_throttling_on/metadata.json)
- Source Code：[sources/azure/postgresql_flexible_server_connection_throttling_on/check.py](../../sources/azure/postgresql_flexible_server_connection_throttling_on/check.py)
- Source Metadata Path：`sources/azure/postgresql_flexible_server_connection_throttling_on/metadata.json`
- Source Code Path：`sources/azure/postgresql_flexible_server_connection_throttling_on/check.py`
