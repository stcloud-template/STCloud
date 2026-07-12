# Ensure that email notifications for attack paths are enabled with minimal risk level

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `defender_attack_path_notifications_properly_configured` |
| クラウドプラットフォーム | Azure |
| サービス | defender |
| 重大度 | medium |
| カテゴリ | Uncategorized |
| リソースタイプ | AzureEmailNotifications |
| リソースグループ | monitoring |

## 説明

Ensure that Microsoft Defender for Cloud is configured to send email notifications for attack paths identified in the Azure subscription with an appropriate minimal risk level.

## リスク

If attack path notifications are not enabled, security teams may not be promptly informed about exploitable attack sequences, increasing the risk of delayed mitigation and potential breaches.

## 推奨事項

Enable attack path email notifications in Microsoft Defender for Cloud to ensure that security teams are notified when potential attack paths are identified. Configure the minimal risk level as appropriate for your organization.

- 推奨リンク：[https://learn.microsoft.com/en-us/azure/defender-for-cloud/configure-email-notifications](https://learn.microsoft.com/en-us/azure/defender-for-cloud/configure-email-notifications)

## 修正手順


### Other

[https://learn.microsoft.com/en-us/azure/defender-for-cloud/configure-email-notifications](https://learn.microsoft.com/en-us/azure/defender-for-cloud/configure-email-notifications)

## 参考資料

- [https://learn.microsoft.com/en-us/azure/defender-for-cloud/configure-email-notifications](https://learn.microsoft.com/en-us/azure/defender-for-cloud/configure-email-notifications)

## 技術情報

- Source Metadata：[sources/azure/defender_attack_path_notifications_properly_configured/metadata.json](../../sources/azure/defender_attack_path_notifications_properly_configured/metadata.json)
- Source Code：[sources/azure/defender_attack_path_notifications_properly_configured/check.py](../../sources/azure/defender_attack_path_notifications_properly_configured/check.py)
- Source Metadata Path：`sources/azure/defender_attack_path_notifications_properly_configured/metadata.json`
- Source Code Path：`sources/azure/defender_attack_path_notifications_properly_configured/check.py`
