# Ensure 'Enforce SSL connection' is set to 'Enabled' for Standard MySQL Database Server

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `mysql_flexible_server_ssl_connection_enabled` |
| 云平台 | Azure |
| 服务 | mysql |
| 严重等级 | high |
| 类别 | Uncategorized |
| 资源类型 | Microsoft.DBforMySQL/flexibleServers |
| 资源组 | database |

## 描述

Enable SSL connection on MYSQL Servers.

## 风险

SSL connectivity helps to provide a new layer of security by connecting database server to client applications using Secure Sockets Layer (SSL). Enforcing SSL connections between database server and client applications helps protect against 'man in the middle' attacks by encrypting the data stream between the server and application.

## 推荐措施

1. Login to Azure Portal using https://portal.azure.com 2. Go to Azure Database for MySQL servers 3. For each database, click on Connection security 4. In SSL settings, click on ENABLED to Enforce SSL connections

- 推荐链接：[https://docs.microsoft.com/en-us/azure/mysql/single-server/how-to-configure-ssl](https://docs.microsoft.com/en-us/azure/mysql/single-server/how-to-configure-ssl)

## 修复步骤


### Other

[https://www.tenable.com/policies/[type]/AC_AZURE_0131](https://www.tenable.com/policies/[type]/AC_AZURE_0131)

## 参考资料

- [https://learn.microsoft.com/en-us/azure/mysql/single-server/concepts-ssl-connection-security](https://learn.microsoft.com/en-us/azure/mysql/single-server/concepts-ssl-connection-security)
- [https://docs.microsoft.com/en-us/azure/mysql/single-server/how-to-configure-ssl](https://docs.microsoft.com/en-us/azure/mysql/single-server/how-to-configure-ssl)

## 技术信息

- Source Metadata：[sources/azure/mysql_flexible_server_ssl_connection_enabled/metadata.json](../../sources/azure/mysql_flexible_server_ssl_connection_enabled/metadata.json)
- Source Code：[sources/azure/mysql_flexible_server_ssl_connection_enabled/check.py](../../sources/azure/mysql_flexible_server_ssl_connection_enabled/check.py)
- Source Metadata Path：`sources/azure/mysql_flexible_server_ssl_connection_enabled/metadata.json`
- Source Code Path：`sources/azure/mysql_flexible_server_ssl_connection_enabled/check.py`
