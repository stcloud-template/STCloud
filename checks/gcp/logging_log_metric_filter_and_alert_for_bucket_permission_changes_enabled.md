# Ensure That the Log Metric Filter and Alerts Exist for Cloud Storage IAM Permission Changes.

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `logging_log_metric_filter_and_alert_for_bucket_permission_changes_enabled` |
| クラウドプラットフォーム | GCP |
| サービス | logging |
| 重大度 | medium |
| カテゴリ | Uncategorized |
| リソースタイプ | MetricFilter |
| リソースグループ | monitoring |

## 説明

Ensure That the Log Metric Filter and Alerts Exist for Cloud Storage IAM Permission Changes.

## リスク

Monitoring changes to cloud storage bucket permissions may reduce the time needed to detect and correct permissions on sensitive cloud storage buckets and objects inside the bucket.

## 推奨事項

It is recommended that a metric filter and alarm be established for Cloud Storage Bucket IAM changes.

- 推奨リンク：[https://cloud.google.com/monitoring/alerts](https://cloud.google.com/monitoring/alerts)

## 修正手順


### Other

[https://www.trendmicro.com/cloudoneconformity/knowledge-base/gcp/CloudLogging/enable-bucket-permission-changes-monitoring.html](https://www.trendmicro.com/cloudoneconformity/knowledge-base/gcp/CloudLogging/enable-bucket-permission-changes-monitoring.html)

## 参考資料

- [https://cloud.google.com/monitoring/alerts](https://cloud.google.com/monitoring/alerts)

## 技術情報

- Source Metadata：[sources/gcp/logging_log_metric_filter_and_alert_for_bucket_permission_changes_enabled/metadata.json](../../sources/gcp/logging_log_metric_filter_and_alert_for_bucket_permission_changes_enabled/metadata.json)
- Source Code：[sources/gcp/logging_log_metric_filter_and_alert_for_bucket_permission_changes_enabled/check.py](../../sources/gcp/logging_log_metric_filter_and_alert_for_bucket_permission_changes_enabled/check.py)
- Source Metadata Path：`sources/gcp/logging_log_metric_filter_and_alert_for_bucket_permission_changes_enabled/metadata.json`
- Source Code Path：`sources/gcp/logging_log_metric_filter_and_alert_for_bucket_permission_changes_enabled/check.py`
