# Ensure That the log_disconnections Database Flag for Cloud SQL PostgreSQL Instance Is Set to On

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `cloudsql_instance_postgres_log_disconnections_flag` |
| 云平台 | GCP |
| 服务 | cloudsql |
| 严重等级 | medium |
| 类别 | Uncategorized |
| 资源类型 | DatabaseInstance |
| 资源组 | database |

## 描述

Ensure That the log_disconnections Database Flag for Cloud SQL PostgreSQL Instance Is Set to On

## 风险

PostgreSQL does not log session details such as duration and session end by default. Enabling the log_disconnections setting will create log entries at the end of each session which can be useful in troubleshooting issues and determine any unusual activity across a time period.

## 推荐措施

Enabling the log_disconnections setting logs the end of each session, including the session duration.

- 推荐链接：[https://cloud.google.com/sql/docs/postgres/flags](https://cloud.google.com/sql/docs/postgres/flags)

## 修复步骤


### CLI

```text
gcloud sql instances patch INSTANCE_NAME --database-flags log_disconnections=on
```

### Terraform

[https://docs.ST Cloud.com/checks/gcp/cloud-sql-policies/bc_gcp_sql_4#terraform](https://docs.ST Cloud.com/checks/gcp/cloud-sql-policies/bc_gcp_sql_4#terraform)

### Other

[https://www.trendmicro.com/cloudoneconformity/knowledge-base/gcp/CloudSQL/enable-log-connections-flag.html](https://www.trendmicro.com/cloudoneconformity/knowledge-base/gcp/CloudSQL/enable-log-connections-flag.html)

## 参考资料

- [https://cloud.google.com/sql/docs/postgres/flags](https://cloud.google.com/sql/docs/postgres/flags)

## 技术信息

- Source Metadata：[sources/gcp/cloudsql_instance_postgres_log_disconnections_flag/metadata.json](../../sources/gcp/cloudsql_instance_postgres_log_disconnections_flag/metadata.json)
- Source Code：[sources/gcp/cloudsql_instance_postgres_log_disconnections_flag/check.py](../../sources/gcp/cloudsql_instance_postgres_log_disconnections_flag/check.py)
- Source Metadata Path：`sources/gcp/cloudsql_instance_postgres_log_disconnections_flag/metadata.json`
- Source Code Path：`sources/gcp/cloudsql_instance_postgres_log_disconnections_flag/check.py`
