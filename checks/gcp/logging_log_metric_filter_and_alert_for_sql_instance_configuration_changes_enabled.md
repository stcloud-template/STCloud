# Ensure that the log metric filter and alerts exist for SQL instance configuration changes.

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `logging_log_metric_filter_and_alert_for_sql_instance_configuration_changes_enabled` |
| 云平台 | GCP |
| 服务 | logging |
| 严重等级 | medium |
| 类别 | Uncategorized |
| 资源类型 | MetricFilter |
| 资源组 | monitoring |

## 描述

Ensure that the log metric filter and alerts exist for SQL instance configuration changes.

## 风险

SQL instance configuration changes can affect availability, security and data protection. Alerting on these changes helps detect unauthorized or unexpected modifications.

## 推荐措施

Create a log metric filter for Cloud SQL instance update events and associate it with a monitoring alert policy.

- 推荐链接：[https://cloud.google.com/monitoring/alerts](https://cloud.google.com/monitoring/alerts)

## 修复步骤

No remediation steps available.

## 参考资料

- [https://cloud.google.com/monitoring/alerts](https://cloud.google.com/monitoring/alerts)

## 技术信息

- Source Metadata：[sources/gcp/logging_log_metric_filter_and_alert_for_sql_instance_configuration_changes_enabled/metadata.json](../../sources/gcp/logging_log_metric_filter_and_alert_for_sql_instance_configuration_changes_enabled/metadata.json)
- Source Code：[sources/gcp/logging_log_metric_filter_and_alert_for_sql_instance_configuration_changes_enabled/check.py](../../sources/gcp/logging_log_metric_filter_and_alert_for_sql_instance_configuration_changes_enabled/check.py)
- Source Metadata Path：`sources/gcp/logging_log_metric_filter_and_alert_for_sql_instance_configuration_changes_enabled/metadata.json`
- Source Code Path：`sources/gcp/logging_log_metric_filter_and_alert_for_sql_instance_configuration_changes_enabled/check.py`
