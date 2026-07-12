# Ensure that the Log_min_duration_statement Flag for a Cloud SQL PostgreSQL Instance Is Set to -1

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `cloudsql_instance_postgres_log_min_duration_statement_flag` |
| クラウドプラットフォーム | GCP |
| サービス | cloudsql |
| 重大度 | medium |
| カテゴリ | Uncategorized |
| リソースタイプ | DatabaseInstance |
| リソースグループ | database |

## 説明

Ensure that the Log_min_duration_statement Flag for a Cloud SQL PostgreSQL Instance Is Set to -1

## リスク

The log_min_duration_statement flag defines the minimum amount of execution time of a statement in milliseconds where the total duration of the statement is logged. Ensure that log_min_duration_statement is disabled, i.e., a value of -1 is set.

## 推奨事項

Logging SQL statements may include sensitive information that should not be recorded in logs. This recommendation is applicable to PostgreSQL database instances.

- 推奨リンク：[https://cloud.google.com/sql/docs/postgres/flags](https://cloud.google.com/sql/docs/postgres/flags)

## 修正手順


### CLI

```text
gcloud sql instances patch INSTANCE_NAME --database-flags log_min_duration_statement=-1
```

### Other

[https://www.trendmicro.com/cloudoneconformity/knowledge-base/gcp/CloudSQL/configure-log-min-error-statement-flag.html](https://www.trendmicro.com/cloudoneconformity/knowledge-base/gcp/CloudSQL/configure-log-min-error-statement-flag.html)

## 参考資料

- [https://cloud.google.com/sql/docs/postgres/flags](https://cloud.google.com/sql/docs/postgres/flags)

## 技術情報

- Source Metadata：[sources/gcp/cloudsql_instance_postgres_log_min_duration_statement_flag/metadata.json](../../sources/gcp/cloudsql_instance_postgres_log_min_duration_statement_flag/metadata.json)
- Source Code：[sources/gcp/cloudsql_instance_postgres_log_min_duration_statement_flag/check.py](../../sources/gcp/cloudsql_instance_postgres_log_min_duration_statement_flag/check.py)
- Source Metadata Path：`sources/gcp/cloudsql_instance_postgres_log_min_duration_statement_flag/metadata.json`
- Source Code Path：`sources/gcp/cloudsql_instance_postgres_log_min_duration_statement_flag/check.py`
