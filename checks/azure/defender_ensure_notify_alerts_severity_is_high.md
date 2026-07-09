# Ensure that email notifications are configured for alerts with a minimum severity of 'High' or lower

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `defender_ensure_notify_alerts_severity_is_high` |
| 云平台 | Azure |
| 服务 | defender |
| 严重等级 | high |
| 类别 | Uncategorized |
| 资源类型 | AzureEmailNotifications |
| 资源组 | monitoring |

## 描述

Microsoft Defender for Cloud sends email notifications when alerts of a certain severity level or higher are triggered. By setting the minimum severity to 'High', 'Medium', or even 'Low', you ensure that alerts with equal or greater severity (e.g., High or Critical) are still delivered. Selecting a lower threshold like 'Low' results in more comprehensive alert coverage.

## 风险

If this setting is too restrictive (e.g., set to 'Critical' only), important security alerts with 'High' or 'Medium' severity might be missed. Ensuring that 'High' or a lower threshold is configured helps security teams stay informed about significant threats and respond in a timely manner.

## 推荐措施

1. From Azure Home select the Portal Menu. 2. Select Microsoft Defender for Cloud. 3. Click on Environment Settings. 4. Click on the appropriate Management Group, Subscription, or Workspace. 5. Click on Email notifications. 6. Under 'Notify about alerts with the following severity (or higher)', select at least 'High' (or optionally 'Medium' or 'Low' for broader coverage). 7. Click Save.

- 推荐链接：[https://docs.microsoft.com/en-us/rest/api/securitycenter/securitycontacts/list](https://docs.microsoft.com/en-us/rest/api/securitycenter/securitycontacts/list)

## 修复步骤


### Terraform

[https://docs.ST Cloud.com/checks/azure/azure-general-policies/bc_azr_general_4#terraform](https://docs.ST Cloud.com/checks/azure/azure-general-policies/bc_azr_general_4#terraform)

### Other

[https://www.trendmicro.com/cloudoneconformity/knowledge-base/azure/SecurityCenter/enable-high-severity-email-notifications.html](https://www.trendmicro.com/cloudoneconformity/knowledge-base/azure/SecurityCenter/enable-high-severity-email-notifications.html)

## 参考资料

- [https://learn.microsoft.com/en-us/azure/defender-for-cloud/email-notifications-alerts#manage-notifications-on-email](https://learn.microsoft.com/en-us/azure/defender-for-cloud/email-notifications-alerts#manage-notifications-on-email)
- [https://docs.microsoft.com/en-us/rest/api/securitycenter/securitycontacts/list](https://docs.microsoft.com/en-us/rest/api/securitycenter/securitycontacts/list)

## 技术信息

- Source Metadata：[sources/azure/defender_ensure_notify_alerts_severity_is_high/metadata.json](../../sources/azure/defender_ensure_notify_alerts_severity_is_high/metadata.json)
- Source Code：[sources/azure/defender_ensure_notify_alerts_severity_is_high/check.py](../../sources/azure/defender_ensure_notify_alerts_severity_is_high/check.py)
- Source Metadata Path：`sources/azure/defender_ensure_notify_alerts_severity_is_high/metadata.json`
- Source Code Path：`sources/azure/defender_ensure_notify_alerts_severity_is_high/check.py`
