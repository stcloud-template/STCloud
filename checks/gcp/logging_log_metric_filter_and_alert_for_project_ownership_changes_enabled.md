# Ensure Log Metric Filter and Alerts Exist for Project Ownership Assignments/Changes.

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `logging_log_metric_filter_and_alert_for_project_ownership_changes_enabled` |
| 云平台 | GCP |
| 服务 | logging |
| 严重等级 | medium |
| 类别 | Uncategorized |
| 资源类型 | MetricFilter |
| 资源组 | monitoring |

## 描述

Ensure Log Metric Filter and Alerts Exist for Project Ownership Assignments/Changes.

## 风险

Project ownership has the highest level of privileges on a GCP project. These privileges include viewer permissions on all GCP services inside the project, permission to modify the state of all GCP services within the project, set up billing and manage roles and permissions for the project and all the resources inside the project.

## 推荐措施

Using Google Cloud alerting policies to detect ownership assignments/changes will help you maintain the right access permissions for each IAM member created within your project, follow the security principle of least privilege, and prevent any accidental or intentional changes that may lead to unauthorized actions.

- 推荐链接：[https://cloud.google.com/monitoring/alerts](https://cloud.google.com/monitoring/alerts)

## 修复步骤


### Other

[https://www.trendmicro.com/cloudoneconformity/knowledge-base/gcp/CloudLogging/enable-ownership-assignments-monitoring.html](https://www.trendmicro.com/cloudoneconformity/knowledge-base/gcp/CloudLogging/enable-ownership-assignments-monitoring.html)

## 参考资料

- [https://cloud.google.com/monitoring/alerts](https://cloud.google.com/monitoring/alerts)

## 技术信息

- Source Metadata：[sources/gcp/logging_log_metric_filter_and_alert_for_project_ownership_changes_enabled/metadata.json](../../sources/gcp/logging_log_metric_filter_and_alert_for_project_ownership_changes_enabled/metadata.json)
- Source Code：[sources/gcp/logging_log_metric_filter_and_alert_for_project_ownership_changes_enabled/check.py](../../sources/gcp/logging_log_metric_filter_and_alert_for_project_ownership_changes_enabled/check.py)
- Source Metadata Path：`sources/gcp/logging_log_metric_filter_and_alert_for_project_ownership_changes_enabled/metadata.json`
- Source Code Path：`sources/gcp/logging_log_metric_filter_and_alert_for_project_ownership_changes_enabled/check.py`
