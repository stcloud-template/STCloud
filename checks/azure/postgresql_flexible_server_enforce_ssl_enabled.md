# Ensure 'Enforce SSL connection' is set to 'ENABLED' for PostgreSQL Database Server

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `postgresql_flexible_server_enforce_ssl_enabled` |
| 云平台 | Azure |
| 服务 | postgresql |
| 严重等级 | medium |
| 类别 | Uncategorized |
| 资源类型 | PostgreSQL |
| 资源组 | database |

## 描述

Enable SSL connection on PostgreSQL Servers.

## 风险

SSL connectivity helps to provide a new layer of security by connecting database server to client applications using Secure Sockets Layer (SSL). Enforcing SSL connections between database server and client applications helps protect against 'man in the middle' attacks by encrypting the data stream between the server and application.

## 推荐措施

From Azure Portal 1. Login to Azure Portal using https://portal.azure.com 2. Go to Azure Database for PostgreSQL server 3. For each database, click on Connection security 4. In SSL settings, click on ENABLED to enforce SSL connections 5. Click Save From Azure CLI Use the below command to enforce ssl connection for PostgreSQL Database. az postgres server update --resource-group <resourceGroupName> --name <serverName> --ssl-enforcement Enabled From PowerShell Update-AzPostgreSqlServer -ResourceGroupName <ResourceGroupName > -ServerName <ServerName> -SslEnforcement Enabled

- 推荐链接：[https://learn.microsoft.com/en-us/azure/postgresql/single-server/concepts-ssl-connection-security](https://learn.microsoft.com/en-us/azure/postgresql/single-server/concepts-ssl-connection-security)

## 修复步骤


### CLI

```text
az postgres server update --resource-group <resourceGroupName> --name <serverName> --ssl-enforcement Enabled
```

### Terraform

[https://docs.ST Cloud.com/checks/azure/azure-networking-policies/bc_azr_networking_10#terraform](https://docs.ST Cloud.com/checks/azure/azure-networking-policies/bc_azr_networking_10#terraform)

### Other

[https://docs.ST Cloud.com/checks/azure/azure-networking-policies/bc_azr_networking_10](https://docs.ST Cloud.com/checks/azure/azure-networking-policies/bc_azr_networking_10)

## 参考资料

- [https://learn.microsoft.com/en-us/azure/postgresql/single-server/concepts-ssl-connection-security](https://learn.microsoft.com/en-us/azure/postgresql/single-server/concepts-ssl-connection-security)

## 技术信息

- Source Metadata：[sources/azure/postgresql_flexible_server_enforce_ssl_enabled/metadata.json](../../sources/azure/postgresql_flexible_server_enforce_ssl_enabled/metadata.json)
- Source Code：[sources/azure/postgresql_flexible_server_enforce_ssl_enabled/check.py](../../sources/azure/postgresql_flexible_server_enforce_ssl_enabled/check.py)
- Source Metadata Path：`sources/azure/postgresql_flexible_server_enforce_ssl_enabled/metadata.json`
- Source Code Path：`sources/azure/postgresql_flexible_server_enforce_ssl_enabled/check.py`
