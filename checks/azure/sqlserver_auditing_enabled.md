# Ensure that SQL Servers have an audit policy configured

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `sqlserver_auditing_enabled` |
| 云平台 | Azure |
| 服务 | sqlserver |
| 严重等级 | medium |
| 类别 | Uncategorized |
| 资源类型 | SQLServer |
| 资源组 | database |

## 描述

Ensure that there is an audit policy configured

## 风险

Audit policies are used to store logs associated to the SQL server (for instance, successful/unsuccesful log in attempts). These logs may be useful to detect anomalies or to perform an investigation in case a security incident is detected

## 推荐措施

Create an audit policy for the SQL server

- 推荐链接：[https://www.trendmicro.com/cloudoneconformity/knowledge-base/azure/Sql/auditing.html](https://www.trendmicro.com/cloudoneconformity/knowledge-base/azure/Sql/auditing.html)

## 修复步骤


### CLI

Set-AzureRmSqlServerAuditingPolicy -ResourceGroupName <RESOURCE_GROUP_NAME> -ServerName <SERVER_NAME> -AuditType <AUDIT_TYPE> -StorageAccountName <STORAGE_ACCOUNT_NAME>

### Terraform

[https://docs.ST Cloud.com/checks/azure/azure-logging-policies/bc_azr_logging_2#terraform](https://docs.ST Cloud.com/checks/azure/azure-logging-policies/bc_azr_logging_2#terraform)

### Other

[https://docs.ST Cloud.com/checks/azure/azure-logging-policies/bc_azr_logging_2](https://docs.ST Cloud.com/checks/azure/azure-logging-policies/bc_azr_logging_2)

## 参考资料

- [https://docs.microsoft.com/en-us/azure/sql-database/sql-database-auditing](https://docs.microsoft.com/en-us/azure/sql-database/sql-database-auditing)
- [https://www.trendmicro.com/cloudoneconformity/knowledge-base/azure/Sql/auditing.html](https://www.trendmicro.com/cloudoneconformity/knowledge-base/azure/Sql/auditing.html)

## 技术信息

- Source Metadata：[sources/azure/sqlserver_auditing_enabled/metadata.json](../../sources/azure/sqlserver_auditing_enabled/metadata.json)
- Source Code：[sources/azure/sqlserver_auditing_enabled/check.py](../../sources/azure/sqlserver_auditing_enabled/check.py)
- Source Metadata Path：`sources/azure/sqlserver_auditing_enabled/metadata.json`
- Source Code Path：`sources/azure/sqlserver_auditing_enabled/check.py`
