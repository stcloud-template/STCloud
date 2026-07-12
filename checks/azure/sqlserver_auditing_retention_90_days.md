# Ensure that 'Auditing' Retention is 'greater than 90 days'

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `sqlserver_auditing_retention_90_days` |
| クラウドプラットフォーム | Azure |
| サービス | sqlserver |
| 重大度 | medium |
| カテゴリ | Uncategorized |
| リソースタイプ | SQLServer |
| リソースグループ | database |

## 説明

SQL Server Audit Retention should be configured to be greater than 90 days.

## リスク

Audit Logs can be used to check for anomalies and give insight into suspected breaches or misuse of information and access.

## 推奨事項

1. Go to SQL servers 2. For each server instance 3. Click on Auditing 4. If storage is selected, expand Advanced properties 5. Set the Retention (days) setting greater than 90 days or 0 for unlimited retention. 6. Select Save

- 推奨リンク：[https://learn.microsoft.com/en-us/purview/audit-log-retention-policies](https://learn.microsoft.com/en-us/purview/audit-log-retention-policies)

## 修正手順


### CLI

Set-AzSqlServerAudit -ResourceGroupName resource_group_name -ServerName SQL_Server_name -RetentionInDays 100 -LogAnalyticsTargetState Enabled -WorkspaceResourceId '/subscriptions/subscription_ID/resourceGroups/insights-integration/providers/Microsoft.OperationalInsights/workspaces/workspace_name'

### Terraform

[https://docs.ST Cloud.com/checks/azure/azure-logging-policies/bc_azr_logging_3](https://docs.ST Cloud.com/checks/azure/azure-logging-policies/bc_azr_logging_3)

### Other

[https://www.trendmicro.com/cloudoneconformity-staging/knowledge-base/azure/Sql/auditing-retention.html#](https://www.trendmicro.com/cloudoneconformity-staging/knowledge-base/azure/Sql/auditing-retention.html#)

## 参考資料

- [https://docs.microsoft.com/en-us/azure/sql-database/sql-database-auditing](https://docs.microsoft.com/en-us/azure/sql-database/sql-database-auditing)
- [https://learn.microsoft.com/en-us/purview/audit-log-retention-policies](https://learn.microsoft.com/en-us/purview/audit-log-retention-policies)

## 技術情報

- Source Metadata：[sources/azure/sqlserver_auditing_retention_90_days/metadata.json](../../sources/azure/sqlserver_auditing_retention_90_days/metadata.json)
- Source Code：[sources/azure/sqlserver_auditing_retention_90_days/check.py](../../sources/azure/sqlserver_auditing_retention_90_days/check.py)
- Source Metadata Path：`sources/azure/sqlserver_auditing_retention_90_days/metadata.json`
- Source Code Path：`sources/azure/sqlserver_auditing_retention_90_days/check.py`
