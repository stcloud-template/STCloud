# Ensure That the Log_statement Database Flag for Cloud SQL PostgreSQL Instance Is Set Appropriately

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `cloudsql_instance_postgres_log_statement_flag` |
| 云平台 | GCP |
| 服务 | cloudsql |
| 严重等级 | medium |
| 类别 | Uncategorized |
| 资源类型 | DatabaseInstance |
| 资源组 | database |

## 描述

Ensure That the Log_statement Database Flag for Cloud SQL PostgreSQL Instance Is Set Appropriately

## 风险

Auditing helps in forensic analysis. If log_statement is not set to the correct value, too many statements may be logged leading to issues in finding the relevant information from the logs, or too few statements may be logged with relevant information missing from the logs.

## 推荐措施

The value ddl logs all data definition statements. A value of 'ddl' is recommended unless otherwise directed by your organization's logging policy.

- 推荐链接：[https://cloud.google.com/sql/docs/postgres/flags](https://cloud.google.com/sql/docs/postgres/flags)

## 修复步骤


### CLI

```text
gcloud sql instances patch INSTANCE_NAME --database-flags log_statement=ddl
```

## 参考资料

- [https://cloud.google.com/sql/docs/postgres/flags](https://cloud.google.com/sql/docs/postgres/flags)

## 技术信息

- Source Metadata：[sources/gcp/cloudsql_instance_postgres_log_statement_flag/metadata.json](../../sources/gcp/cloudsql_instance_postgres_log_statement_flag/metadata.json)
- Source Code：[sources/gcp/cloudsql_instance_postgres_log_statement_flag/check.py](../../sources/gcp/cloudsql_instance_postgres_log_statement_flag/check.py)
- Source Metadata Path：`sources/gcp/cloudsql_instance_postgres_log_statement_flag/metadata.json`
- Source Code Path：`sources/gcp/cloudsql_instance_postgres_log_statement_flag/check.py`
