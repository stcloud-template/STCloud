# Ensure Log Metric Filter and Alerts Exist for Project Ownership Assignments/Changes.

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `logging_log_metric_filter_and_alert_for_project_ownership_changes_enabled` |
| クラウドプラットフォーム | GCP |
| サービス | logging |
| 重大度 | medium |
| カテゴリ | Uncategorized |
| リソースタイプ | MetricFilter |
| リソースグループ | monitoring |

## 説明

Ensure Log Metric Filter and Alerts Exist for Project Ownership Assignments/Changes.

## リスク

Project ownership has the highest level of privileges on a GCP project. These privileges include viewer permissions on all GCP services inside the project, permission to modify the state of all GCP services within the project, set up billing and manage roles and permissions for the project and all the resources inside the project.

## 推奨事項

Using Google Cloud alerting policies to detect ownership assignments/changes will help you maintain the right access permissions for each IAM member created within your project, follow the security principle of least privilege, and prevent any accidental or intentional changes that may lead to unauthorized actions.

- 推奨リンク：[https://cloud.google.com/monitoring/alerts](https://cloud.google.com/monitoring/alerts)

## 修正手順


### Other

[https://www.trendmicro.com/cloudoneconformity/knowledge-base/gcp/CloudLogging/enable-ownership-assignments-monitoring.html](https://www.trendmicro.com/cloudoneconformity/knowledge-base/gcp/CloudLogging/enable-ownership-assignments-monitoring.html)

## 参考資料

- [https://cloud.google.com/monitoring/alerts](https://cloud.google.com/monitoring/alerts)

## 技術情報

- Source Metadata：[sources/gcp/logging_log_metric_filter_and_alert_for_project_ownership_changes_enabled/metadata.json](../../sources/gcp/logging_log_metric_filter_and_alert_for_project_ownership_changes_enabled/metadata.json)
- Source Code：[sources/gcp/logging_log_metric_filter_and_alert_for_project_ownership_changes_enabled/check.py](../../sources/gcp/logging_log_metric_filter_and_alert_for_project_ownership_changes_enabled/check.py)
- Source Metadata Path：`sources/gcp/logging_log_metric_filter_and_alert_for_project_ownership_changes_enabled/metadata.json`
- Source Code Path：`sources/gcp/logging_log_metric_filter_and_alert_for_project_ownership_changes_enabled/check.py`
