# Ensure That the Log Metric Filter and Alerts Exist for Custom Role Changes.

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `logging_log_metric_filter_and_alert_for_custom_role_changes_enabled` |
| クラウドプラットフォーム | GCP |
| サービス | logging |
| 重大度 | medium |
| カテゴリ | Uncategorized |
| リソースタイプ | MetricFilter |
| リソースグループ | monitoring |

## 説明

Ensure That the Log Metric Filter and Alerts Exist for Custom Role Changes.

## リスク

Google Cloud IAM provides predefined roles that give granular access to specific Google Cloud Platform resources and prevent unwanted access to other resources.

## 推奨事項

It is recommended that a metric filter and alarm be established for changes to Identity and Access Management (IAM) role creation, deletion and updating activities.

- 推奨リンク：[https://cloud.google.com/monitoring/alerts](https://cloud.google.com/monitoring/alerts)

## 修正手順


### Other

[https://www.trendmicro.com/cloudoneconformity/knowledge-base/gcp/CloudLogging/enable-custom-role-changes-monitoring.html](https://www.trendmicro.com/cloudoneconformity/knowledge-base/gcp/CloudLogging/enable-custom-role-changes-monitoring.html)

## 参考資料

- [https://cloud.google.com/monitoring/alerts](https://cloud.google.com/monitoring/alerts)

## 技術情報

- Source Metadata：[sources/gcp/logging_log_metric_filter_and_alert_for_custom_role_changes_enabled/metadata.json](../../sources/gcp/logging_log_metric_filter_and_alert_for_custom_role_changes_enabled/metadata.json)
- Source Code：[sources/gcp/logging_log_metric_filter_and_alert_for_custom_role_changes_enabled/check.py](../../sources/gcp/logging_log_metric_filter_and_alert_for_custom_role_changes_enabled/check.py)
- Source Metadata Path：`sources/gcp/logging_log_metric_filter_and_alert_for_custom_role_changes_enabled/metadata.json`
- Source Code Path：`sources/gcp/logging_log_metric_filter_and_alert_for_custom_role_changes_enabled/check.py`
