# Ensure Essential Contacts is Configured for Organization

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `iam_organization_essential_contacts_configured` |
| クラウドプラットフォーム | GCP |
| サービス | iam |
| 重大度 | medium |
| カテゴリ | Uncategorized |
| リソースタイプ | Organization |
| リソースグループ | governance |

## 説明

It is recommended that Essential Contacts is configured to designate email addresses for Google Cloud services to notify of important technical or security information.

## リスク

Google Cloud Platform (GCP) services, such as Cloud Billing, send out billing notifications to share important information with the cloud platform users. By default, these types of notifications are sent to members with certain Identity and Access Management (IAM) roles such as 'roles/owner' and 'roles/billing.admin'. With Essential Contacts, you can specify exactly who receives important notifications by providing your own list of contacts (i.e. email addresses).

## 推奨事項

It is recommended that Essential Contacts is configured to designate email addresses for Google Cloud services to notify of important technical or security information.

- 推奨リンク：[https://cloud.google.com/resource-manager/docs/managing-notification-contacts](https://cloud.google.com/resource-manager/docs/managing-notification-contacts)

## 修正手順


### CLI

```text
gcloud essential-contacts create --email=<EMAIL> --notification-categories=<NOTIFICATION_CATEGORIES> --organization=<ORGANIZATION_ID>
```

### Other

[https://www.trendmicro.com/cloudoneconformity/knowledge-base/gcp/CloudIAM/essential-contacts.html](https://www.trendmicro.com/cloudoneconformity/knowledge-base/gcp/CloudIAM/essential-contacts.html)

## 参考資料

- [https://cloud.google.com/resource-manager/docs/managing-notification-contacts](https://cloud.google.com/resource-manager/docs/managing-notification-contacts)

## 技術情報

- Source Metadata：[sources/gcp/iam_organization_essential_contacts_configured/metadata.json](../../sources/gcp/iam_organization_essential_contacts_configured/metadata.json)
- Source Code：[sources/gcp/iam_organization_essential_contacts_configured/check.py](../../sources/gcp/iam_organization_essential_contacts_configured/check.py)
- Source Metadata Path：`sources/gcp/iam_organization_essential_contacts_configured/metadata.json`
- Source Code Path：`sources/gcp/iam_organization_essential_contacts_configured/check.py`
