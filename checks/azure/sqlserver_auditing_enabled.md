# Ensure that SQL Servers have an audit policy configured

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `sqlserver_auditing_enabled` |
| クラウドプラットフォーム | Azure |
| サービス | sqlserver |
| 重大度 | medium |
| カテゴリ | Uncategorized |
| リソースタイプ | SQLServer |
| リソースグループ | database |

## 説明

Ensure that there is an audit policy configured

## リスク

Audit policies are used to store logs associated to the SQL server (for instance, successful/unsuccesful log in attempts). These logs may be useful to detect anomalies or to perform an investigation in case a security incident is detected

## 推奨事項

Create an audit policy for the SQL server

- 推奨リンク：[https://www.trendmicro.com/cloudoneconformity/knowledge-base/azure/Sql/auditing.html](https://www.trendmicro.com/cloudoneconformity/knowledge-base/azure/Sql/auditing.html)

## 修正手順


### CLI

Set-AzureRmSqlServerAuditingPolicy -ResourceGroupName <RESOURCE_GROUP_NAME> -ServerName <SERVER_NAME> -AuditType <AUDIT_TYPE> -StorageAccountName <STORAGE_ACCOUNT_NAME>

### Terraform

[https://docs.ST Cloud.com/checks/azure/azure-logging-policies/bc_azr_logging_2#terraform](https://docs.ST Cloud.com/checks/azure/azure-logging-policies/bc_azr_logging_2#terraform)

### Other

[https://docs.ST Cloud.com/checks/azure/azure-logging-policies/bc_azr_logging_2](https://docs.ST Cloud.com/checks/azure/azure-logging-policies/bc_azr_logging_2)

## 参考資料

- [https://docs.microsoft.com/en-us/azure/sql-database/sql-database-auditing](https://docs.microsoft.com/en-us/azure/sql-database/sql-database-auditing)
- [https://www.trendmicro.com/cloudoneconformity/knowledge-base/azure/Sql/auditing.html](https://www.trendmicro.com/cloudoneconformity/knowledge-base/azure/Sql/auditing.html)

## 技術情報

- Source Metadata：[sources/azure/sqlserver_auditing_enabled/metadata.json](../../sources/azure/sqlserver_auditing_enabled/metadata.json)
- Source Code：[sources/azure/sqlserver_auditing_enabled/check.py](../../sources/azure/sqlserver_auditing_enabled/check.py)
- Source Metadata Path：`sources/azure/sqlserver_auditing_enabled/metadata.json`
- Source Code Path：`sources/azure/sqlserver_auditing_enabled/check.py`
