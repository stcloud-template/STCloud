# Ensure That the Log Metric Filter and Alerts Exist for Audit Configuration Changes.

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `logging_log_metric_filter_and_alert_for_audit_configuration_changes_enabled` |
| クラウドプラットフォーム | GCP |
| サービス | logging |
| 重大度 | medium |
| カテゴリ | Uncategorized |
| リソースタイプ | MetricFilter |
| リソースグループ | monitoring |

## 説明

Ensure That the Log Metric Filter and Alerts Exist for Audit Configuration Changes.

## リスク

Admin Activity audit logs and Data Access audit logs produced by the Google Cloud Audit Logs service can be extremely useful for security analysis, resource change tracking, and compliance auditing.

## 推奨事項

By using Google Cloud alerting policies to detect audit configuration changes, you make sure that the recommended state of audit configuration is well maintained so that all the activities performed within your GCP project are available for security analysis and auditing at any point in time.

- 推奨リンク：[https://cloud.google.com/monitoring/alerts](https://cloud.google.com/monitoring/alerts)

## 修正手順


### Other

[https://www.trendmicro.com/cloudoneconformity/knowledge-base/gcp/CloudLogging/enable-audit-configuration-changes-monitoring.html](https://www.trendmicro.com/cloudoneconformity/knowledge-base/gcp/CloudLogging/enable-audit-configuration-changes-monitoring.html)

## 参考資料

- [https://cloud.google.com/monitoring/alerts](https://cloud.google.com/monitoring/alerts)

## 技術情報

- Source Metadata：[sources/gcp/logging_log_metric_filter_and_alert_for_audit_configuration_changes_enabled/metadata.json](../../sources/gcp/logging_log_metric_filter_and_alert_for_audit_configuration_changes_enabled/metadata.json)
- Source Code：[sources/gcp/logging_log_metric_filter_and_alert_for_audit_configuration_changes_enabled/check.py](../../sources/gcp/logging_log_metric_filter_and_alert_for_audit_configuration_changes_enabled/check.py)
- Source Metadata Path：`sources/gcp/logging_log_metric_filter_and_alert_for_audit_configuration_changes_enabled/metadata.json`
- Source Code Path：`sources/gcp/logging_log_metric_filter_and_alert_for_audit_configuration_changes_enabled/check.py`
