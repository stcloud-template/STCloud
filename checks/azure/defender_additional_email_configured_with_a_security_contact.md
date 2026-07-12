# Ensure 'Additional email addresses' is Configured with a Security Contact Email

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `defender_additional_email_configured_with_a_security_contact` |
| クラウドプラットフォーム | Azure |
| サービス | defender |
| 重大度 | medium |
| カテゴリ | Uncategorized |
| リソースタイプ | AzureEmailNotifications |
| リソースグループ | monitoring |

## 説明

Microsoft Defender for Cloud emails the subscription owners whenever a high-severity alert is triggered for their subscription. You should provide a security contact email address as an additional email address.

## リスク

Microsoft Defender for Cloud emails the Subscription Owner to notify them about security alerts. Adding your Security Contact's email address to the 'Additional email addresses' field ensures that your organization's Security Team is included in these alerts. This ensures that the proper people are aware of any potential compromise in order to mitigate the risk in a timely fashion.

## 推奨事項

1. From Azure Home select the Portal Menu 2. Select Microsoft Defender for Cloud 3. Click on Environment Settings 4. Click on the appropriate Management Group, Subscription, or Workspace 5. Click on Email notifications 6. Enter a valid security contact email address (or multiple addresses separated by commas) in the Additional email addresses field 7. Click Save

- 推奨リンク：[https://learn.microsoft.com/en-us/rest/api/defenderforcloud/security-contacts/list?view=rest-defenderforcloud-2020-01-01-preview&tabs=HTTP](https://learn.microsoft.com/en-us/rest/api/defenderforcloud/security-contacts/list?view=rest-defenderforcloud-2020-01-01-preview&tabs=HTTP)

## 修正手順


### Terraform

[https://docs.ST Cloud.com/checks/azure/azure-general-policies/ensure-that-security-contact-emails-is-set#terraform](https://docs.ST Cloud.com/checks/azure/azure-general-policies/ensure-that-security-contact-emails-is-set#terraform)

### Other

[https://www.trendmicro.com/cloudoneconformity/knowledge-base/azure/SecurityCenter/security-contact-email.html](https://www.trendmicro.com/cloudoneconformity/knowledge-base/azure/SecurityCenter/security-contact-email.html)

## 参考資料

- [https://docs.microsoft.com/en-us/azure/security-center/security-center-provide-security-contact-details](https://docs.microsoft.com/en-us/azure/security-center/security-center-provide-security-contact-details)
- [https://learn.microsoft.com/en-us/rest/api/defenderforcloud/security-contacts/list?view=rest-defenderforcloud-2020-01-01-preview&tabs=HTTP](https://learn.microsoft.com/en-us/rest/api/defenderforcloud/security-contacts/list?view=rest-defenderforcloud-2020-01-01-preview&tabs=HTTP)

## 技術情報

- Source Metadata：[sources/azure/defender_additional_email_configured_with_a_security_contact/metadata.json](../../sources/azure/defender_additional_email_configured_with_a_security_contact/metadata.json)
- Source Code：[sources/azure/defender_additional_email_configured_with_a_security_contact/check.py](../../sources/azure/defender_additional_email_configured_with_a_security_contact/check.py)
- Source Metadata Path：`sources/azure/defender_additional_email_configured_with_a_security_contact/metadata.json`
- Source Code Path：`sources/azure/defender_additional_email_configured_with_a_security_contact/check.py`
