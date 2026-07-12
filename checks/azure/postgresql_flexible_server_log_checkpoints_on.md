# Ensure Server Parameter 'log_checkpoints' is set to 'ON' for PostgreSQL Database Server

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `postgresql_flexible_server_log_checkpoints_on` |
| クラウドプラットフォーム | Azure |
| サービス | postgresql |
| 重大度 | medium |
| カテゴリ | Uncategorized |
| リソースタイプ | PostgreSQL |
| リソースグループ | database |

## 説明

Enable log_checkpoints on PostgreSQL Servers.

## リスク

Enabling log_checkpoints helps the PostgreSQL Database to Log each checkpoint in turn generates query and error logs. However, access to transaction logs is not supported. Query and error logs can be used to identify, troubleshoot, and repair configuration errors and sub-optimal performance.

## 推奨事項

From Azure Portal 1. From Azure Home select the Portal Menu. 2. Go to Azure Database for PostgreSQL servers. 3. For each database, click on Server parameters. 4. Search for log_checkpoints. 5. Click ON and save. From Azure CLI Use the below command to update log_checkpoints configuration. az postgres server configuration set --resource-group <resourceGroupName> -- server-name <serverName> --name log_checkpoints --value on From PowerShell Update-AzPostgreSqlConfiguration -ResourceGroupName <ResourceGroupName> - ServerName <ServerName> -Name log_checkpoints -Value on

- 推奨リンク：[https://docs.microsoft.com/en-us/azure/postgresql/howto-configure-server-parameters-using-portal](https://docs.microsoft.com/en-us/azure/postgresql/howto-configure-server-parameters-using-portal)

## 修正手順


### CLI

```text
az postgres server configuration set --resource-group <resourceGroupName> --server-name <serverName> --name log_checkpoints --value on
```

### Terraform

[https://docs.ST Cloud.com/checks/azure/azure-networking-policies/bc_azr_networking_11#terraform](https://docs.ST Cloud.com/checks/azure/azure-networking-policies/bc_azr_networking_11#terraform)

### Other

[https://www.trendmicro.com/cloudoneconformity-staging/knowledge-base/azure/PostgreSQL/log-checkpoints.html#](https://www.trendmicro.com/cloudoneconformity-staging/knowledge-base/azure/PostgreSQL/log-checkpoints.html#)

## 参考資料

- [https://docs.microsoft.com/en-us/rest/api/postgresql/singleserver/configurations/list-by-server](https://docs.microsoft.com/en-us/rest/api/postgresql/singleserver/configurations/list-by-server)
- [https://docs.microsoft.com/en-us/azure/postgresql/howto-configure-server-parameters-using-portal](https://docs.microsoft.com/en-us/azure/postgresql/howto-configure-server-parameters-using-portal)

## 技術情報

- Source Metadata：[sources/azure/postgresql_flexible_server_log_checkpoints_on/metadata.json](../../sources/azure/postgresql_flexible_server_log_checkpoints_on/metadata.json)
- Source Code：[sources/azure/postgresql_flexible_server_log_checkpoints_on/check.py](../../sources/azure/postgresql_flexible_server_log_checkpoints_on/check.py)
- Source Metadata Path：`sources/azure/postgresql_flexible_server_log_checkpoints_on/metadata.json`
- Source Code Path：`sources/azure/postgresql_flexible_server_log_checkpoints_on/check.py`
