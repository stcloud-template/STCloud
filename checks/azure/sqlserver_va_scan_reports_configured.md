# Ensure that Vulnerability Assessment (VA) setting 'Send scan reports to' is configured for a SQL server

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `sqlserver_va_scan_reports_configured` |
| 云平台 | Azure |
| 服务 | sqlserver |
| 严重等级 | medium |
| 类别 | Uncategorized |
| 资源类型 | SQLServer |
| 资源组 | database |

## 描述

Configure 'Send scan reports to' with email addresses of concerned data owners/stakeholders for a critical SQL servers.

## 风险

Vulnerability Assessment (VA) scan reports and alerts will be sent to email addresses configured at 'Send scan reports to'. This may help in reducing time required for identifying risks and taking corrective measures

## 推荐措施

1. Go to SQL servers 2. Select a server instance 3. Select Microsoft Defender for Cloud 4. Select Configure next to Enablement status 5. Set Microsoft Defender for SQL to On 6. Under Vulnerability Assessment Settings, select a Storage Account 7. Set Periodic recurring scans to On 8. Under Send scan reports to, provide email addresses for data owners and stakeholders 9. Click Save

- 推荐链接：[https://learn.microsoft.com/en-us/azure/defender-for-cloud/sql-azure-vulnerability-assessment-enable](https://learn.microsoft.com/en-us/azure/defender-for-cloud/sql-azure-vulnerability-assessment-enable)

## 修复步骤


### Terraform

[https://docs.ST Cloud.com/checks/azure/azure-general-policies/ensure-that-va-setting-send-scan-reports-to-is-configured-for-a-sql-server#terraform](https://docs.ST Cloud.com/checks/azure/azure-general-policies/ensure-that-va-setting-send-scan-reports-to-is-configured-for-a-sql-server#terraform)

## 参考资料

- [https://docs.microsoft.com/en-us/azure/sql-database/sql-vulnerability-assessment](https://docs.microsoft.com/en-us/azure/sql-database/sql-vulnerability-assessment)
- [https://learn.microsoft.com/en-us/azure/defender-for-cloud/sql-azure-vulnerability-assessment-enable](https://learn.microsoft.com/en-us/azure/defender-for-cloud/sql-azure-vulnerability-assessment-enable)

## 技术信息

- Source Metadata：[sources/azure/sqlserver_va_scan_reports_configured/metadata.json](../../sources/azure/sqlserver_va_scan_reports_configured/metadata.json)
- Source Code：[sources/azure/sqlserver_va_scan_reports_configured/check.py](../../sources/azure/sqlserver_va_scan_reports_configured/check.py)
- Source Metadata Path：`sources/azure/sqlserver_va_scan_reports_configured/metadata.json`
- Source Code Path：`sources/azure/sqlserver_va_scan_reports_configured/check.py`
