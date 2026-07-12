# Ensure that Vulnerability Assessment (VA) setting 'Also send email notifications to admins and subscription owners' is set for each SQL Server

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `sqlserver_va_emails_notifications_admins_enabled` |
| クラウドプラットフォーム | Azure |
| サービス | sqlserver |
| 重大度 | medium |
| カテゴリ | Uncategorized |
| リソースタイプ | SQLServer |
| リソースグループ | database |

## 説明

Enable Vulnerability Assessment (VA) setting 'Also send email notifications to admins and subscription owners'.

## リスク

VA scan reports and alerts will be sent to admins and subscription owners by enabling setting 'Also send email notifications to admins and subscription owners'. This may help in reducing time required for identifying risks and taking corrective measures.

## 推奨事項

1. Go to SQL servers 2. Select a server instance 3. Click on Security Center 4. Select Configure next to Enabled at subscription-level 5. In Section Vulnerability Assessment Settings, configure Storage Accounts if not already 6. Check/enable 'Also send email notifications to admins and subscription owners' 7. Click Save

- 推奨リンク：[https://learn.microsoft.com/en-us/azure/defender-for-cloud/sql-azure-vulnerability-assessment-enable](https://learn.microsoft.com/en-us/azure/defender-for-cloud/sql-azure-vulnerability-assessment-enable)

## 修正手順


### Terraform

[https://docs.ST Cloud.com/checks/azure/azure-general-policies/ensure-that-va-setting-also-send-email-notifications-to-admins-and-subscription-owners-is-set-for-an-sql-server#terraform](https://docs.ST Cloud.com/checks/azure/azure-general-policies/ensure-that-va-setting-also-send-email-notifications-to-admins-and-subscription-owners-is-set-for-an-sql-server#terraform)

## 参考資料

- [https://docs.microsoft.com/en-us/azure/sql-database/sql-vulnerability-assessment](https://docs.microsoft.com/en-us/azure/sql-database/sql-vulnerability-assessment)
- [https://learn.microsoft.com/en-us/azure/defender-for-cloud/sql-azure-vulnerability-assessment-enable](https://learn.microsoft.com/en-us/azure/defender-for-cloud/sql-azure-vulnerability-assessment-enable)

## 技術情報

- Source Metadata：[sources/azure/sqlserver_va_emails_notifications_admins_enabled/metadata.json](../../sources/azure/sqlserver_va_emails_notifications_admins_enabled/metadata.json)
- Source Code：[sources/azure/sqlserver_va_emails_notifications_admins_enabled/check.py](../../sources/azure/sqlserver_va_emails_notifications_admins_enabled/check.py)
- Source Metadata Path：`sources/azure/sqlserver_va_emails_notifications_admins_enabled/metadata.json`
- Source Code Path：`sources/azure/sqlserver_va_emails_notifications_admins_enabled/check.py`
