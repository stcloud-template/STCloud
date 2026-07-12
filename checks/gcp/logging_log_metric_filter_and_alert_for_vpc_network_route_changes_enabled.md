# Ensure That the Log Metric Filter and Alerts Exist for VPC Network Route Changes.

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `logging_log_metric_filter_and_alert_for_vpc_network_route_changes_enabled` |
| クラウドプラットフォーム | GCP |
| サービス | logging |
| 重大度 | medium |
| カテゴリ | Uncategorized |
| リソースタイプ | MetricFilter |
| リソースグループ | monitoring |

## 説明

Ensure That the Log Metric Filter and Alerts Exist for VPC Network Route Changes.

## リスク

Monitoring changes to route tables will help ensure that all VPC traffic flows through an expected path.

## 推奨事項

It is recommended that a metric filter and alarm be established for Virtual Private Cloud (VPC) network route changes.

- 推奨リンク：[https://cloud.google.com/monitoring/alerts](https://cloud.google.com/monitoring/alerts)

## 修正手順


### Other

[https://www.trendmicro.com/cloudoneconformity/knowledge-base/gcp/CloudLogging/enable-network-route-changes-monitoring.html](https://www.trendmicro.com/cloudoneconformity/knowledge-base/gcp/CloudLogging/enable-network-route-changes-monitoring.html)

## 参考資料

- [https://cloud.google.com/monitoring/alerts](https://cloud.google.com/monitoring/alerts)

## 技術情報

- Source Metadata：[sources/gcp/logging_log_metric_filter_and_alert_for_vpc_network_route_changes_enabled/metadata.json](../../sources/gcp/logging_log_metric_filter_and_alert_for_vpc_network_route_changes_enabled/metadata.json)
- Source Code：[sources/gcp/logging_log_metric_filter_and_alert_for_vpc_network_route_changes_enabled/check.py](../../sources/gcp/logging_log_metric_filter_and_alert_for_vpc_network_route_changes_enabled/check.py)
- Source Metadata Path：`sources/gcp/logging_log_metric_filter_and_alert_for_vpc_network_route_changes_enabled/metadata.json`
- Source Code Path：`sources/gcp/logging_log_metric_filter_and_alert_for_vpc_network_route_changes_enabled/check.py`
