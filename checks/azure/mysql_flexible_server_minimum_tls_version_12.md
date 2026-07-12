# Ensure 'TLS Version' is set to 'TLSV1.2' for MySQL flexible Database Server

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `mysql_flexible_server_minimum_tls_version_12` |
| クラウドプラットフォーム | Azure |
| サービス | mysql |
| 重大度 | high |
| カテゴリ | Uncategorized |
| リソースタイプ | Microsoft.DBforMySQL/flexibleServers |
| リソースグループ | database |

## 説明

Ensure TLS version on MySQL flexible servers is set to the default value.

## リスク

TLS connectivity helps to provide a new layer of security by connecting database server to client applications using Transport Layer Security (TLS). Enforcing TLS connections between database server and client applications helps protect against 'man in the middle' attacks by encrypting the data stream between the server and application.

## 推奨事項

1. Login to Azure Portal using https://portal.azure.com 2. Go to Azure Database for MySQL flexible servers 3. For each database, click on Server parameters under Settings 4. In the search box, type in tls_version 5. Click on the VALUE dropdown, and ensure only TLSV1.2 is selected for tls_version

- 推奨リンク：[https://docs.microsoft.com/en-us/azure/mysql/howto-configure-ssl](https://docs.microsoft.com/en-us/azure/mysql/howto-configure-ssl)

## 修正手順


### CLI

```text
az mysql flexible-server parameter set --name tls_version --resource-group <resourceGroupName> --server-name <serverName> --value TLSV1.2
```

### Terraform

[https://docs.ST Cloud.com/checks/azure/azure-general-policies/ensure-mysql-is-using-the-latest-version-of-tls-encryption#terraform](https://docs.ST Cloud.com/checks/azure/azure-general-policies/ensure-mysql-is-using-the-latest-version-of-tls-encryption#terraform)

### Other

[https://www.trendmicro.com/cloudoneconformity/knowledge-base/azure/MySQL/mysql-flexible-server-tls-version.html](https://www.trendmicro.com/cloudoneconformity/knowledge-base/azure/MySQL/mysql-flexible-server-tls-version.html)

## 参考資料

- [https://docs.microsoft.com/en-us/azure/mysql/concepts-ssl-connection-security](https://docs.microsoft.com/en-us/azure/mysql/concepts-ssl-connection-security)
- [https://docs.microsoft.com/en-us/azure/mysql/howto-configure-ssl](https://docs.microsoft.com/en-us/azure/mysql/howto-configure-ssl)

## 技術情報

- Source Metadata：[sources/azure/mysql_flexible_server_minimum_tls_version_12/metadata.json](../../sources/azure/mysql_flexible_server_minimum_tls_version_12/metadata.json)
- Source Code：[sources/azure/mysql_flexible_server_minimum_tls_version_12/check.py](../../sources/azure/mysql_flexible_server_minimum_tls_version_12/check.py)
- Source Metadata Path：`sources/azure/mysql_flexible_server_minimum_tls_version_12/metadata.json`
- Source Code Path：`sources/azure/mysql_flexible_server_minimum_tls_version_12/check.py`
