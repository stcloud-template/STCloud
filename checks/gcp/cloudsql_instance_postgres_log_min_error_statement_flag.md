# Ensure that the Log_min_error_statement Flag for a Cloud SQL PostgreSQL Instance Is Set Appropriately

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `cloudsql_instance_postgres_log_min_error_statement_flag` |
| 云平台 | GCP |
| 服务 | cloudsql |
| 严重等级 | medium |
| 类别 | Uncategorized |
| 资源类型 | DatabaseInstance |
| 资源组 | database |

## 描述

Ensure that the Log_min_error_statement Flag for a Cloud SQL PostgreSQL Instance Is Set Appropriately

## 风险

The log_min_error_statement flag defines the minimum message severity level that are considered as an error statement. Messages for error statements are logged with the SQL statement. Valid values include DEBUG5, DEBUG4, DEBUG3, DEBUG2, DEBUG1, INFO, NOTICE, WARNING, ERROR, LOG, FATAL, and PANIC. Each severity level includes the subsequent levels mentioned above. Ensure a value of ERROR or stricter is set.

## 推荐措施

Auditing helps in troubleshooting operational problems and also permits forensic analysis. If log_min_error_statement is not set to the correct value, messages may not be classified as error messages appropriately. Considering general log messages as error messages would make is difficult to find actual errors and considering only stricter severity levels as error messages may skip actual errors to log their SQL statements. The log_min_error_statement flag should be set to ERROR or stricter.

- 推荐链接：[https://cloud.google.com/sql/docs/postgres/flags](https://cloud.google.com/sql/docs/postgres/flags)

## 修复步骤


### CLI

```text
gcloud sql instances patch INSTANCE_NAME --database-flags log_min_error_statement=error
```

### Other

[https://www.trendmicro.com/cloudoneconformity/knowledge-base/gcp/CloudSQL/configure-log-min-error-statement-flag.html](https://www.trendmicro.com/cloudoneconformity/knowledge-base/gcp/CloudSQL/configure-log-min-error-statement-flag.html)

## 参考资料

- [https://cloud.google.com/sql/docs/postgres/flags](https://cloud.google.com/sql/docs/postgres/flags)

## 技术信息

- Source Metadata：[sources/gcp/cloudsql_instance_postgres_log_min_error_statement_flag/metadata.json](../../sources/gcp/cloudsql_instance_postgres_log_min_error_statement_flag/metadata.json)
- Source Code：[sources/gcp/cloudsql_instance_postgres_log_min_error_statement_flag/check.py](../../sources/gcp/cloudsql_instance_postgres_log_min_error_statement_flag/check.py)
- Source Metadata Path：`sources/gcp/cloudsql_instance_postgres_log_min_error_statement_flag/metadata.json`
- Source Code Path：`sources/gcp/cloudsql_instance_postgres_log_min_error_statement_flag/check.py`
