# Ensure that 'Auditing' Retention is 'greater than 90 days'

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `sqlserver_auditing_retention_90_days` |
| 云平台 | Azure |
| 服务 | sqlserver |
| 严重等级 | medium |
| 类别 | Uncategorized |
| 资源类型 | SQLServer |
| 资源组 | database |

## 描述

SQL Server Audit Retention should be configured to be greater than 90 days.

## 风险

Audit Logs can be used to check for anomalies and give insight into suspected breaches or misuse of information and access.

## 推荐措施

1. Go to SQL servers 2. For each server instance 3. Click on Auditing 4. If storage is selected, expand Advanced properties 5. Set the Retention (days) setting greater than 90 days or 0 for unlimited retention. 6. Select Save

- 推荐链接：[https://learn.microsoft.com/en-us/purview/audit-log-retention-policies](https://learn.microsoft.com/en-us/purview/audit-log-retention-policies)

## 修复步骤


### CLI

Set-AzSqlServerAudit -ResourceGroupName resource_group_name -ServerName SQL_Server_name -RetentionInDays 100 -LogAnalyticsTargetState Enabled -WorkspaceResourceId '/subscriptions/subscription_ID/resourceGroups/insights-integration/providers/Microsoft.OperationalInsights/workspaces/workspace_name'

### Terraform

[https://docs.ST Cloud.com/checks/azure/azure-logging-policies/bc_azr_logging_3](https://docs.ST Cloud.com/checks/azure/azure-logging-policies/bc_azr_logging_3)

### Other

[https://www.trendmicro.com/cloudoneconformity-staging/knowledge-base/azure/Sql/auditing-retention.html#](https://www.trendmicro.com/cloudoneconformity-staging/knowledge-base/azure/Sql/auditing-retention.html#)

## 参考资料

- [https://docs.microsoft.com/en-us/azure/sql-database/sql-database-auditing](https://docs.microsoft.com/en-us/azure/sql-database/sql-database-auditing)
- [https://learn.microsoft.com/en-us/purview/audit-log-retention-policies](https://learn.microsoft.com/en-us/purview/audit-log-retention-policies)

## 技术信息

- Source Metadata：[sources/azure/sqlserver_auditing_retention_90_days/metadata.json](../../sources/azure/sqlserver_auditing_retention_90_days/metadata.json)
- Source Code：[sources/azure/sqlserver_auditing_retention_90_days/check.py](../../sources/azure/sqlserver_auditing_retention_90_days/check.py)
- Source Metadata Path：`sources/azure/sqlserver_auditing_retention_90_days/metadata.json`
- Source Code Path：`sources/azure/sqlserver_auditing_retention_90_days/check.py`
