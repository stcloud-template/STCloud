# Ensure That 'All users with the following roles' is set to 'Owner'

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `defender_ensure_notify_emails_to_owners` |
| クラウドプラットフォーム | Azure |
| サービス | defender |
| 重大度 | medium |
| カテゴリ | Uncategorized |
| リソースタイプ | AzureEmailNotifications |
| リソースグループ | monitoring |

## 説明

Enable security alert emails to subscription owners.

## リスク

Enabling security alert emails to subscription owners ensures that they receive security alert emails from Microsoft. This ensures that they are aware of any potential security issues and can mitigate the risk in a timely fashion.

## 推奨事項

1. From Azure Home select the Portal Menu 2. Select Microsoft Defender for Cloud 3. Click on Environment Settings 4. Click on the appropriate Management Group, Subscription, or Workspace 5. Click on Email notifications 6. In the drop down of the All users with the following roles field select Owner 7. Click Save

- 推奨リンク：[https://docs.microsoft.com/en-us/rest/api/securitycenter/securitycontacts/list](https://docs.microsoft.com/en-us/rest/api/securitycenter/securitycontacts/list)

## 修正手順


### Other

[https://www.trendmicro.com/cloudoneconformity/knowledge-base/azure/SecurityCenter/email-to-subscription-owners.html](https://www.trendmicro.com/cloudoneconformity/knowledge-base/azure/SecurityCenter/email-to-subscription-owners.html)

## 参考資料

- [https://docs.microsoft.com/en-us/azure/security-center/security-center-provide-security-contact-details](https://docs.microsoft.com/en-us/azure/security-center/security-center-provide-security-contact-details)
- [https://docs.microsoft.com/en-us/rest/api/securitycenter/securitycontacts/list](https://docs.microsoft.com/en-us/rest/api/securitycenter/securitycontacts/list)

## 技術情報

- Source Metadata：[sources/azure/defender_ensure_notify_emails_to_owners/metadata.json](../../sources/azure/defender_ensure_notify_emails_to_owners/metadata.json)
- Source Code：[sources/azure/defender_ensure_notify_emails_to_owners/check.py](../../sources/azure/defender_ensure_notify_emails_to_owners/check.py)
- Source Metadata Path：`sources/azure/defender_ensure_notify_emails_to_owners/metadata.json`
- Source Code Path：`sources/azure/defender_ensure_notify_emails_to_owners/check.py`
