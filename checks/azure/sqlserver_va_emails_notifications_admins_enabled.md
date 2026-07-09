# Ensure that Vulnerability Assessment (VA) setting 'Also send email notifications to admins and subscription owners' is set for each SQL Server

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `sqlserver_va_emails_notifications_admins_enabled` |
| 云平台 | Azure |
| 服务 | sqlserver |
| 严重等级 | medium |
| 类别 | Uncategorized |
| 资源类型 | SQLServer |
| 资源组 | database |

## 描述

Enable Vulnerability Assessment (VA) setting 'Also send email notifications to admins and subscription owners'.

## 风险

VA scan reports and alerts will be sent to admins and subscription owners by enabling setting 'Also send email notifications to admins and subscription owners'. This may help in reducing time required for identifying risks and taking corrective measures.

## 推荐措施

1. Go to SQL servers 2. Select a server instance 3. Click on Security Center 4. Select Configure next to Enabled at subscription-level 5. In Section Vulnerability Assessment Settings, configure Storage Accounts if not already 6. Check/enable 'Also send email notifications to admins and subscription owners' 7. Click Save

- 推荐链接：[https://learn.microsoft.com/en-us/azure/defender-for-cloud/sql-azure-vulnerability-assessment-enable](https://learn.microsoft.com/en-us/azure/defender-for-cloud/sql-azure-vulnerability-assessment-enable)

## 修复步骤


### Terraform

[https://docs.ST Cloud.com/checks/azure/azure-general-policies/ensure-that-va-setting-also-send-email-notifications-to-admins-and-subscription-owners-is-set-for-an-sql-server#terraform](https://docs.ST Cloud.com/checks/azure/azure-general-policies/ensure-that-va-setting-also-send-email-notifications-to-admins-and-subscription-owners-is-set-for-an-sql-server#terraform)

## 参考资料

- [https://docs.microsoft.com/en-us/azure/sql-database/sql-vulnerability-assessment](https://docs.microsoft.com/en-us/azure/sql-database/sql-vulnerability-assessment)
- [https://learn.microsoft.com/en-us/azure/defender-for-cloud/sql-azure-vulnerability-assessment-enable](https://learn.microsoft.com/en-us/azure/defender-for-cloud/sql-azure-vulnerability-assessment-enable)

## 技术信息

- Source Metadata：[sources/azure/sqlserver_va_emails_notifications_admins_enabled/metadata.json](../../sources/azure/sqlserver_va_emails_notifications_admins_enabled/metadata.json)
- Source Code：[sources/azure/sqlserver_va_emails_notifications_admins_enabled/check.py](../../sources/azure/sqlserver_va_emails_notifications_admins_enabled/check.py)
- Source Metadata Path：`sources/azure/sqlserver_va_emails_notifications_admins_enabled/metadata.json`
- Source Code Path：`sources/azure/sqlserver_va_emails_notifications_admins_enabled/check.py`
