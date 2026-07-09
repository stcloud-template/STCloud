# Ensure that email notifications for attack paths are enabled with minimal risk level

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `defender_attack_path_notifications_properly_configured` |
| 云平台 | Azure |
| 服务 | defender |
| 严重等级 | medium |
| 类别 | Uncategorized |
| 资源类型 | AzureEmailNotifications |
| 资源组 | monitoring |

## 描述

Ensure that Microsoft Defender for Cloud is configured to send email notifications for attack paths identified in the Azure subscription with an appropriate minimal risk level.

## 风险

If attack path notifications are not enabled, security teams may not be promptly informed about exploitable attack sequences, increasing the risk of delayed mitigation and potential breaches.

## 推荐措施

Enable attack path email notifications in Microsoft Defender for Cloud to ensure that security teams are notified when potential attack paths are identified. Configure the minimal risk level as appropriate for your organization.

- 推荐链接：[https://learn.microsoft.com/en-us/azure/defender-for-cloud/configure-email-notifications](https://learn.microsoft.com/en-us/azure/defender-for-cloud/configure-email-notifications)

## 修复步骤


### Other

[https://learn.microsoft.com/en-us/azure/defender-for-cloud/configure-email-notifications](https://learn.microsoft.com/en-us/azure/defender-for-cloud/configure-email-notifications)

## 参考资料

- [https://learn.microsoft.com/en-us/azure/defender-for-cloud/configure-email-notifications](https://learn.microsoft.com/en-us/azure/defender-for-cloud/configure-email-notifications)

## 技术信息

- Source Metadata：[sources/azure/defender_attack_path_notifications_properly_configured/metadata.json](../../sources/azure/defender_attack_path_notifications_properly_configured/metadata.json)
- Source Code：[sources/azure/defender_attack_path_notifications_properly_configured/check.py](../../sources/azure/defender_attack_path_notifications_properly_configured/check.py)
- Source Metadata Path：`sources/azure/defender_attack_path_notifications_properly_configured/metadata.json`
- Source Code Path：`sources/azure/defender_attack_path_notifications_properly_configured/check.py`
