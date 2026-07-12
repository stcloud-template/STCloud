# Configure Google Cloud Audit Logs to Track All Activities

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `iam_audit_logs_enabled` |
| クラウドプラットフォーム | GCP |
| サービス | iam |
| サブサービス | Audit Logs |
| 重大度 | medium |
| カテゴリ | Uncategorized |
| リソースタイプ | GCPProject |
| リソースグループ | governance |

## 説明

Ensure that Google Cloud Audit Logs feature is configured to track Data Access logs for all Google Cloud Platform (GCP) services and users, in order to enhance overall access security and meet compliance requirements. Once configured, the feature can record all admin related activities, as well as all the read and write access requests to user data.

## リスク

In order to maintain an effective Google Cloud audit configuration for your project, folder, and organization, all 3 types of Data Access logs (ADMIN_READ, DATA_READ and DATA_WRITE) must be enabled for all supported GCP services. Also, Data Access logs should be captured for all IAM users, without exempting any of them. Exemptions let you control which users generate audit logs. When you add an exempted user to your log configuration, audit logs are not created for that user, for the selected log type(s). Data Access audit logs are disabled by default and must be explicitly enabled based on your business requirements.

## 推奨事項

It is recommended that Cloud Audit Logging is configured to track all admin activities and read, write access to user data.

- 推奨リンク：[https://cloud.google.com/logging/docs/audit/](https://cloud.google.com/logging/docs/audit/)

## 修正手順


### Terraform

[https://docs.ST Cloud.com/checks/gcp/logging-policies-1/ensure-that-cloud-audit-logging-is-configured-properly-across-all-services-and-all-users-from-a-project#terraform](https://docs.ST Cloud.com/checks/gcp/logging-policies-1/ensure-that-cloud-audit-logging-is-configured-properly-across-all-services-and-all-users-from-a-project#terraform)

### Other

[https://www.trendmicro.com/cloudoneconformity/knowledge-base/gcp/CloudIAM/record-all-activities.html](https://www.trendmicro.com/cloudoneconformity/knowledge-base/gcp/CloudIAM/record-all-activities.html)

## 参考資料

- [https://cloud.google.com/logging/docs/audit/](https://cloud.google.com/logging/docs/audit/)

## 技術情報

- Source Metadata：[sources/gcp/iam_audit_logs_enabled/metadata.json](../../sources/gcp/iam_audit_logs_enabled/metadata.json)
- Source Code：[sources/gcp/iam_audit_logs_enabled/check.py](../../sources/gcp/iam_audit_logs_enabled/check.py)
- Source Metadata Path：`sources/gcp/iam_audit_logs_enabled/metadata.json`
- Source Code Path：`sources/gcp/iam_audit_logs_enabled/check.py`
