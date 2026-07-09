# Ensure that Vulnerability Assessment (VA) setting 'Periodic recurring scans' is set to 'on' for each SQL server

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `sqlserver_va_periodic_recurring_scans_enabled` |
| 云平台 | Azure |
| 服务 | sqlserver |
| 严重等级 | medium |
| 类别 | Uncategorized |
| 资源类型 | SQLServer |
| 资源组 | database |

## 描述

Enable Vulnerability Assessment (VA) Periodic recurring scans for critical SQL servers and corresponding SQL databases.

## 风险

VA setting 'Periodic recurring scans' schedules periodic (weekly) vulnerability scanning for the SQL server and corresponding Databases. Periodic and regular vulnerability scanning provides risk visibility based on updated known vulnerability signatures and best practices.

## 推荐措施

1. Go to SQL servers 2. For each server instance 3. Click on Security Center 4. In Section Vulnerability Assessment Settings, set Storage Account if not already 5. Toggle 'Periodic recurring scans' to ON. 6. Click Save

- 推荐链接：[https://learn.microsoft.com/en-us/azure/defender-for-cloud/sql-azure-vulnerability-assessment-enable](https://learn.microsoft.com/en-us/azure/defender-for-cloud/sql-azure-vulnerability-assessment-enable)

## 修复步骤


### Terraform

[https://docs.ST Cloud.com/checks/azure/azure-general-policies/ensure-that-va-setting-periodic-recurring-scans-is-enabled-on-a-sql-server#terraform](https://docs.ST Cloud.com/checks/azure/azure-general-policies/ensure-that-va-setting-periodic-recurring-scans-is-enabled-on-a-sql-server#terraform)

### Other

[https://www.trendmicro.com/cloudoneconformity-staging/knowledge-base/azure/Sql/periodic-vulnerability-scans.html#](https://www.trendmicro.com/cloudoneconformity-staging/knowledge-base/azure/Sql/periodic-vulnerability-scans.html#)

## 参考资料

- [https://docs.microsoft.com/en-us/azure/sql-database/sql-vulnerability-assessment](https://docs.microsoft.com/en-us/azure/sql-database/sql-vulnerability-assessment)
- [https://learn.microsoft.com/en-us/azure/defender-for-cloud/sql-azure-vulnerability-assessment-enable](https://learn.microsoft.com/en-us/azure/defender-for-cloud/sql-azure-vulnerability-assessment-enable)

## 技术信息

- Source Metadata：[sources/azure/sqlserver_va_periodic_recurring_scans_enabled/metadata.json](../../sources/azure/sqlserver_va_periodic_recurring_scans_enabled/metadata.json)
- Source Code：[sources/azure/sqlserver_va_periodic_recurring_scans_enabled/check.py](../../sources/azure/sqlserver_va_periodic_recurring_scans_enabled/check.py)
- Source Metadata Path：`sources/azure/sqlserver_va_periodic_recurring_scans_enabled/metadata.json`
- Source Code Path：`sources/azure/sqlserver_va_periodic_recurring_scans_enabled/check.py`
