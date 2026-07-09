# Ensure Log_error_verbosity Database Flag for Cloud SQL PostgreSQL Instance Is Set to DEFAULT or Stricter

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `cloudsql_instance_postgres_log_error_verbosity_flag` |
| 云平台 | GCP |
| 服务 | cloudsql |
| 严重等级 | medium |
| 类别 | Uncategorized |
| 资源类型 | DatabaseInstance |
| 资源组 | database |

## 描述

Ensure Log_error_verbosity Database Flag for Cloud SQL PostgreSQL Instance Is Set to DEFAULT or Stricter

## 风险

The log_error_verbosity flag controls the verbosity/details of messages logged.TERSE excludes the logging of DETAIL, HINT, QUERY, and CONTEXT error information. VERBOSE output includes the SQLSTATE error code, source code file name, function name, and line number that generated the error. Ensure an appropriate value is set to 'DEFAULT' or stricter.

## 推荐措施

Auditing helps in troubleshooting operational problems and also permits forensic analysis. If log_error_verbosity is not set to the correct value, too many details or too few details may be logged. This flag should be configured with a value of 'DEFAULT' or stricter. This recommendation is applicable to PostgreSQL database instances.

- 推荐链接：[https://cloud.google.com/sql/docs/postgres/flags](https://cloud.google.com/sql/docs/postgres/flags)

## 修复步骤


### CLI

```text
gcloud sql instances patch INSTANCE_NAME --database-flags log_error_verbosity=default
```

## 参考资料

- [https://cloud.google.com/sql/docs/postgres/flags](https://cloud.google.com/sql/docs/postgres/flags)

## 技术信息

- Source Metadata：[sources/gcp/cloudsql_instance_postgres_log_error_verbosity_flag/metadata.json](../../sources/gcp/cloudsql_instance_postgres_log_error_verbosity_flag/metadata.json)
- Source Code：[sources/gcp/cloudsql_instance_postgres_log_error_verbosity_flag/check.py](../../sources/gcp/cloudsql_instance_postgres_log_error_verbosity_flag/check.py)
- Source Metadata Path：`sources/gcp/cloudsql_instance_postgres_log_error_verbosity_flag/metadata.json`
- Source Code Path：`sources/gcp/cloudsql_instance_postgres_log_error_verbosity_flag/check.py`
