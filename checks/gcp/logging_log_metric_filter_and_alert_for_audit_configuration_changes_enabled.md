# Ensure That the Log Metric Filter and Alerts Exist for Audit Configuration Changes.

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `logging_log_metric_filter_and_alert_for_audit_configuration_changes_enabled` |
| 云平台 | GCP |
| 服务 | logging |
| 严重等级 | medium |
| 类别 | Uncategorized |
| 资源类型 | MetricFilter |
| 资源组 | monitoring |

## 描述

Ensure That the Log Metric Filter and Alerts Exist for Audit Configuration Changes.

## 风险

Admin Activity audit logs and Data Access audit logs produced by the Google Cloud Audit Logs service can be extremely useful for security analysis, resource change tracking, and compliance auditing.

## 推荐措施

By using Google Cloud alerting policies to detect audit configuration changes, you make sure that the recommended state of audit configuration is well maintained so that all the activities performed within your GCP project are available for security analysis and auditing at any point in time.

- 推荐链接：[https://cloud.google.com/monitoring/alerts](https://cloud.google.com/monitoring/alerts)

## 修复步骤


### Other

[https://www.trendmicro.com/cloudoneconformity/knowledge-base/gcp/CloudLogging/enable-audit-configuration-changes-monitoring.html](https://www.trendmicro.com/cloudoneconformity/knowledge-base/gcp/CloudLogging/enable-audit-configuration-changes-monitoring.html)

## 参考资料

- [https://cloud.google.com/monitoring/alerts](https://cloud.google.com/monitoring/alerts)

## 技术信息

- Source Metadata：[sources/gcp/logging_log_metric_filter_and_alert_for_audit_configuration_changes_enabled/metadata.json](../../sources/gcp/logging_log_metric_filter_and_alert_for_audit_configuration_changes_enabled/metadata.json)
- Source Code：[sources/gcp/logging_log_metric_filter_and_alert_for_audit_configuration_changes_enabled/check.py](../../sources/gcp/logging_log_metric_filter_and_alert_for_audit_configuration_changes_enabled/check.py)
- Source Metadata Path：`sources/gcp/logging_log_metric_filter_and_alert_for_audit_configuration_changes_enabled/metadata.json`
- Source Code Path：`sources/gcp/logging_log_metric_filter_and_alert_for_audit_configuration_changes_enabled/check.py`
