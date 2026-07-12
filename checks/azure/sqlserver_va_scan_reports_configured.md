# Ensure that Vulnerability Assessment (VA) setting 'Send scan reports to' is configured for a SQL server

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `sqlserver_va_scan_reports_configured` |
| クラウドプラットフォーム | Azure |
| サービス | sqlserver |
| 重大度 | medium |
| カテゴリ | Uncategorized |
| リソースタイプ | SQLServer |
| リソースグループ | database |

## 説明

Configure 'Send scan reports to' with email addresses of concerned data owners/stakeholders for a critical SQL servers.

## リスク

Vulnerability Assessment (VA) scan reports and alerts will be sent to email addresses configured at 'Send scan reports to'. This may help in reducing time required for identifying risks and taking corrective measures

## 推奨事項

1. Go to SQL servers 2. Select a server instance 3. Select Microsoft Defender for Cloud 4. Select Configure next to Enablement status 5. Set Microsoft Defender for SQL to On 6. Under Vulnerability Assessment Settings, select a Storage Account 7. Set Periodic recurring scans to On 8. Under Send scan reports to, provide email addresses for data owners and stakeholders 9. Click Save

- 推奨リンク：[https://learn.microsoft.com/en-us/azure/defender-for-cloud/sql-azure-vulnerability-assessment-enable](https://learn.microsoft.com/en-us/azure/defender-for-cloud/sql-azure-vulnerability-assessment-enable)

## 修正手順


### Terraform

[https://docs.ST Cloud.com/checks/azure/azure-general-policies/ensure-that-va-setting-send-scan-reports-to-is-configured-for-a-sql-server#terraform](https://docs.ST Cloud.com/checks/azure/azure-general-policies/ensure-that-va-setting-send-scan-reports-to-is-configured-for-a-sql-server#terraform)

## 参考資料

- [https://docs.microsoft.com/en-us/azure/sql-database/sql-vulnerability-assessment](https://docs.microsoft.com/en-us/azure/sql-database/sql-vulnerability-assessment)
- [https://learn.microsoft.com/en-us/azure/defender-for-cloud/sql-azure-vulnerability-assessment-enable](https://learn.microsoft.com/en-us/azure/defender-for-cloud/sql-azure-vulnerability-assessment-enable)

## 技術情報

- Source Metadata：[sources/azure/sqlserver_va_scan_reports_configured/metadata.json](../../sources/azure/sqlserver_va_scan_reports_configured/metadata.json)
- Source Code：[sources/azure/sqlserver_va_scan_reports_configured/check.py](../../sources/azure/sqlserver_va_scan_reports_configured/check.py)
- Source Metadata Path：`sources/azure/sqlserver_va_scan_reports_configured/metadata.json`
- Source Code Path：`sources/azure/sqlserver_va_scan_reports_configured/check.py`
