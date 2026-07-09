# Ensure that the Log_min_duration_statement Flag for a Cloud SQL PostgreSQL Instance Is Set to -1

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `cloudsql_instance_postgres_log_min_duration_statement_flag` |
| 云平台 | GCP |
| 服务 | cloudsql |
| 严重等级 | medium |
| 类别 | Uncategorized |
| 资源类型 | DatabaseInstance |
| 资源组 | database |

## 描述

Ensure that the Log_min_duration_statement Flag for a Cloud SQL PostgreSQL Instance Is Set to -1

## 风险

The log_min_duration_statement flag defines the minimum amount of execution time of a statement in milliseconds where the total duration of the statement is logged. Ensure that log_min_duration_statement is disabled, i.e., a value of -1 is set.

## 推荐措施

Logging SQL statements may include sensitive information that should not be recorded in logs. This recommendation is applicable to PostgreSQL database instances.

- 推荐链接：[https://cloud.google.com/sql/docs/postgres/flags](https://cloud.google.com/sql/docs/postgres/flags)

## 修复步骤


### CLI

```text
gcloud sql instances patch INSTANCE_NAME --database-flags log_min_duration_statement=-1
```

### Other

[https://www.trendmicro.com/cloudoneconformity/knowledge-base/gcp/CloudSQL/configure-log-min-error-statement-flag.html](https://www.trendmicro.com/cloudoneconformity/knowledge-base/gcp/CloudSQL/configure-log-min-error-statement-flag.html)

## 参考资料

- [https://cloud.google.com/sql/docs/postgres/flags](https://cloud.google.com/sql/docs/postgres/flags)

## 技术信息

- Source Metadata：[sources/gcp/cloudsql_instance_postgres_log_min_duration_statement_flag/metadata.json](../../sources/gcp/cloudsql_instance_postgres_log_min_duration_statement_flag/metadata.json)
- Source Code：[sources/gcp/cloudsql_instance_postgres_log_min_duration_statement_flag/check.py](../../sources/gcp/cloudsql_instance_postgres_log_min_duration_statement_flag/check.py)
- Source Metadata Path：`sources/gcp/cloudsql_instance_postgres_log_min_duration_statement_flag/metadata.json`
- Source Code Path：`sources/gcp/cloudsql_instance_postgres_log_min_duration_statement_flag/check.py`
