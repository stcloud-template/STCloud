# Ensure that Vulnerability Assessment (VA) setting 'Periodic recurring scans' is set to 'on' for each SQL server

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `sqlserver_va_periodic_recurring_scans_enabled` |
| クラウドプラットフォーム | Azure |
| サービス | sqlserver |
| 重大度 | medium |
| カテゴリ | Uncategorized |
| リソースタイプ | SQLServer |
| リソースグループ | database |

## 説明

Enable Vulnerability Assessment (VA) Periodic recurring scans for critical SQL servers and corresponding SQL databases.

## リスク

VA setting 'Periodic recurring scans' schedules periodic (weekly) vulnerability scanning for the SQL server and corresponding Databases. Periodic and regular vulnerability scanning provides risk visibility based on updated known vulnerability signatures and best practices.

## 推奨事項

1. Go to SQL servers 2. For each server instance 3. Click on Security Center 4. In Section Vulnerability Assessment Settings, set Storage Account if not already 5. Toggle 'Periodic recurring scans' to ON. 6. Click Save

- 推奨リンク：[https://learn.microsoft.com/en-us/azure/defender-for-cloud/sql-azure-vulnerability-assessment-enable](https://learn.microsoft.com/en-us/azure/defender-for-cloud/sql-azure-vulnerability-assessment-enable)

## 修正手順


### Terraform

[https://docs.ST Cloud.com/checks/azure/azure-general-policies/ensure-that-va-setting-periodic-recurring-scans-is-enabled-on-a-sql-server#terraform](https://docs.ST Cloud.com/checks/azure/azure-general-policies/ensure-that-va-setting-periodic-recurring-scans-is-enabled-on-a-sql-server#terraform)

### Other

[https://www.trendmicro.com/cloudoneconformity-staging/knowledge-base/azure/Sql/periodic-vulnerability-scans.html#](https://www.trendmicro.com/cloudoneconformity-staging/knowledge-base/azure/Sql/periodic-vulnerability-scans.html#)

## 参考資料

- [https://docs.microsoft.com/en-us/azure/sql-database/sql-vulnerability-assessment](https://docs.microsoft.com/en-us/azure/sql-database/sql-vulnerability-assessment)
- [https://learn.microsoft.com/en-us/azure/defender-for-cloud/sql-azure-vulnerability-assessment-enable](https://learn.microsoft.com/en-us/azure/defender-for-cloud/sql-azure-vulnerability-assessment-enable)

## 技術情報

- Source Metadata：[sources/azure/sqlserver_va_periodic_recurring_scans_enabled/metadata.json](../../sources/azure/sqlserver_va_periodic_recurring_scans_enabled/metadata.json)
- Source Code：[sources/azure/sqlserver_va_periodic_recurring_scans_enabled/check.py](../../sources/azure/sqlserver_va_periodic_recurring_scans_enabled/check.py)
- Source Metadata Path：`sources/azure/sqlserver_va_periodic_recurring_scans_enabled/metadata.json`
- Source Code Path：`sources/azure/sqlserver_va_periodic_recurring_scans_enabled/check.py`
