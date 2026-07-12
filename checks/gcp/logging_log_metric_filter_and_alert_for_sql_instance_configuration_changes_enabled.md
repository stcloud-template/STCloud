# Ensure that the log metric filter and alerts exist for SQL instance configuration changes.

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `logging_log_metric_filter_and_alert_for_sql_instance_configuration_changes_enabled` |
| クラウドプラットフォーム | GCP |
| サービス | logging |
| 重大度 | medium |
| カテゴリ | Uncategorized |
| リソースタイプ | MetricFilter |
| リソースグループ | monitoring |

## 説明

Ensure that the log metric filter and alerts exist for SQL instance configuration changes.

## リスク

SQL instance configuration changes can affect availability, security and data protection. Alerting on these changes helps detect unauthorized or unexpected modifications.

## 推奨事項

Create a log metric filter for Cloud SQL instance update events and associate it with a monitoring alert policy.

- 推奨リンク：[https://cloud.google.com/monitoring/alerts](https://cloud.google.com/monitoring/alerts)

## 修正手順

No remediation steps available.

## 参考資料

- [https://cloud.google.com/monitoring/alerts](https://cloud.google.com/monitoring/alerts)

## 技術情報

- Source Metadata：[sources/gcp/logging_log_metric_filter_and_alert_for_sql_instance_configuration_changes_enabled/metadata.json](../../sources/gcp/logging_log_metric_filter_and_alert_for_sql_instance_configuration_changes_enabled/metadata.json)
- Source Code：[sources/gcp/logging_log_metric_filter_and_alert_for_sql_instance_configuration_changes_enabled/check.py](../../sources/gcp/logging_log_metric_filter_and_alert_for_sql_instance_configuration_changes_enabled/check.py)
- Source Metadata Path：`sources/gcp/logging_log_metric_filter_and_alert_for_sql_instance_configuration_changes_enabled/metadata.json`
- Source Code Path：`sources/gcp/logging_log_metric_filter_and_alert_for_sql_instance_configuration_changes_enabled/check.py`
