# Ensure That the Log Metric Filter and Alerts Exist for VPC Network Route Changes.

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `logging_log_metric_filter_and_alert_for_vpc_network_route_changes_enabled` |
| 云平台 | GCP |
| 服务 | logging |
| 严重等级 | medium |
| 类别 | Uncategorized |
| 资源类型 | MetricFilter |
| 资源组 | monitoring |

## 描述

Ensure That the Log Metric Filter and Alerts Exist for VPC Network Route Changes.

## 风险

Monitoring changes to route tables will help ensure that all VPC traffic flows through an expected path.

## 推荐措施

It is recommended that a metric filter and alarm be established for Virtual Private Cloud (VPC) network route changes.

- 推荐链接：[https://cloud.google.com/monitoring/alerts](https://cloud.google.com/monitoring/alerts)

## 修复步骤


### Other

[https://www.trendmicro.com/cloudoneconformity/knowledge-base/gcp/CloudLogging/enable-network-route-changes-monitoring.html](https://www.trendmicro.com/cloudoneconformity/knowledge-base/gcp/CloudLogging/enable-network-route-changes-monitoring.html)

## 参考资料

- [https://cloud.google.com/monitoring/alerts](https://cloud.google.com/monitoring/alerts)

## 技术信息

- Source Metadata：[sources/gcp/logging_log_metric_filter_and_alert_for_vpc_network_route_changes_enabled/metadata.json](../../sources/gcp/logging_log_metric_filter_and_alert_for_vpc_network_route_changes_enabled/metadata.json)
- Source Code：[sources/gcp/logging_log_metric_filter_and_alert_for_vpc_network_route_changes_enabled/check.py](../../sources/gcp/logging_log_metric_filter_and_alert_for_vpc_network_route_changes_enabled/check.py)
- Source Metadata Path：`sources/gcp/logging_log_metric_filter_and_alert_for_vpc_network_route_changes_enabled/metadata.json`
- Source Code Path：`sources/gcp/logging_log_metric_filter_and_alert_for_vpc_network_route_changes_enabled/check.py`
