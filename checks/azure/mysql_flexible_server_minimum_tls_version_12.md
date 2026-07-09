# Ensure 'TLS Version' is set to 'TLSV1.2' for MySQL flexible Database Server

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `mysql_flexible_server_minimum_tls_version_12` |
| 云平台 | Azure |
| 服务 | mysql |
| 严重等级 | high |
| 类别 | Uncategorized |
| 资源类型 | Microsoft.DBforMySQL/flexibleServers |
| 资源组 | database |

## 描述

Ensure TLS version on MySQL flexible servers is set to the default value.

## 风险

TLS connectivity helps to provide a new layer of security by connecting database server to client applications using Transport Layer Security (TLS). Enforcing TLS connections between database server and client applications helps protect against 'man in the middle' attacks by encrypting the data stream between the server and application.

## 推荐措施

1. Login to Azure Portal using https://portal.azure.com 2. Go to Azure Database for MySQL flexible servers 3. For each database, click on Server parameters under Settings 4. In the search box, type in tls_version 5. Click on the VALUE dropdown, and ensure only TLSV1.2 is selected for tls_version

- 推荐链接：[https://docs.microsoft.com/en-us/azure/mysql/howto-configure-ssl](https://docs.microsoft.com/en-us/azure/mysql/howto-configure-ssl)

## 修复步骤


### CLI

```text
az mysql flexible-server parameter set --name tls_version --resource-group <resourceGroupName> --server-name <serverName> --value TLSV1.2
```

### Terraform

[https://docs.ST Cloud.com/checks/azure/azure-general-policies/ensure-mysql-is-using-the-latest-version-of-tls-encryption#terraform](https://docs.ST Cloud.com/checks/azure/azure-general-policies/ensure-mysql-is-using-the-latest-version-of-tls-encryption#terraform)

### Other

[https://www.trendmicro.com/cloudoneconformity/knowledge-base/azure/MySQL/mysql-flexible-server-tls-version.html](https://www.trendmicro.com/cloudoneconformity/knowledge-base/azure/MySQL/mysql-flexible-server-tls-version.html)

## 参考资料

- [https://docs.microsoft.com/en-us/azure/mysql/concepts-ssl-connection-security](https://docs.microsoft.com/en-us/azure/mysql/concepts-ssl-connection-security)
- [https://docs.microsoft.com/en-us/azure/mysql/howto-configure-ssl](https://docs.microsoft.com/en-us/azure/mysql/howto-configure-ssl)

## 技术信息

- Source Metadata：[sources/azure/mysql_flexible_server_minimum_tls_version_12/metadata.json](../../sources/azure/mysql_flexible_server_minimum_tls_version_12/metadata.json)
- Source Code：[sources/azure/mysql_flexible_server_minimum_tls_version_12/check.py](../../sources/azure/mysql_flexible_server_minimum_tls_version_12/check.py)
- Source Metadata Path：`sources/azure/mysql_flexible_server_minimum_tls_version_12/metadata.json`
- Source Code Path：`sources/azure/mysql_flexible_server_minimum_tls_version_12/check.py`
