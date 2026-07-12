# Ensure 'Enforce SSL connection' is set to 'ENABLED' for PostgreSQL Database Server

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `postgresql_flexible_server_enforce_ssl_enabled` |
| クラウドプラットフォーム | Azure |
| サービス | postgresql |
| 重大度 | medium |
| カテゴリ | Uncategorized |
| リソースタイプ | PostgreSQL |
| リソースグループ | database |

## 説明

Enable SSL connection on PostgreSQL Servers.

## リスク

SSL connectivity helps to provide a new layer of security by connecting database server to client applications using Secure Sockets Layer (SSL). Enforcing SSL connections between database server and client applications helps protect against 'man in the middle' attacks by encrypting the data stream between the server and application.

## 推奨事項

From Azure Portal 1. Login to Azure Portal using https://portal.azure.com 2. Go to Azure Database for PostgreSQL server 3. For each database, click on Connection security 4. In SSL settings, click on ENABLED to enforce SSL connections 5. Click Save From Azure CLI Use the below command to enforce ssl connection for PostgreSQL Database. az postgres server update --resource-group <resourceGroupName> --name <serverName> --ssl-enforcement Enabled From PowerShell Update-AzPostgreSqlServer -ResourceGroupName <ResourceGroupName > -ServerName <ServerName> -SslEnforcement Enabled

- 推奨リンク：[https://learn.microsoft.com/en-us/azure/postgresql/single-server/concepts-ssl-connection-security](https://learn.microsoft.com/en-us/azure/postgresql/single-server/concepts-ssl-connection-security)

## 修正手順


### CLI

```text
az postgres server update --resource-group <resourceGroupName> --name <serverName> --ssl-enforcement Enabled
```

### Terraform

[https://docs.ST Cloud.com/checks/azure/azure-networking-policies/bc_azr_networking_10#terraform](https://docs.ST Cloud.com/checks/azure/azure-networking-policies/bc_azr_networking_10#terraform)

### Other

[https://docs.ST Cloud.com/checks/azure/azure-networking-policies/bc_azr_networking_10](https://docs.ST Cloud.com/checks/azure/azure-networking-policies/bc_azr_networking_10)

## 参考資料

- [https://learn.microsoft.com/en-us/azure/postgresql/single-server/concepts-ssl-connection-security](https://learn.microsoft.com/en-us/azure/postgresql/single-server/concepts-ssl-connection-security)

## 技術情報

- Source Metadata：[sources/azure/postgresql_flexible_server_enforce_ssl_enabled/metadata.json](../../sources/azure/postgresql_flexible_server_enforce_ssl_enabled/metadata.json)
- Source Code：[sources/azure/postgresql_flexible_server_enforce_ssl_enabled/check.py](../../sources/azure/postgresql_flexible_server_enforce_ssl_enabled/check.py)
- Source Metadata Path：`sources/azure/postgresql_flexible_server_enforce_ssl_enabled/metadata.json`
- Source Code Path：`sources/azure/postgresql_flexible_server_enforce_ssl_enabled/check.py`
