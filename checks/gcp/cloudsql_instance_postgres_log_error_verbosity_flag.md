# Ensure Log_error_verbosity Database Flag for Cloud SQL PostgreSQL Instance Is Set to DEFAULT or Stricter

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `cloudsql_instance_postgres_log_error_verbosity_flag` |
| クラウドプラットフォーム | GCP |
| サービス | cloudsql |
| 重大度 | medium |
| カテゴリ | Uncategorized |
| リソースタイプ | DatabaseInstance |
| リソースグループ | database |

## 説明

Ensure Log_error_verbosity Database Flag for Cloud SQL PostgreSQL Instance Is Set to DEFAULT or Stricter

## リスク

The log_error_verbosity flag controls the verbosity/details of messages logged.TERSE excludes the logging of DETAIL, HINT, QUERY, and CONTEXT error information. VERBOSE output includes the SQLSTATE error code, source code file name, function name, and line number that generated the error. Ensure an appropriate value is set to 'DEFAULT' or stricter.

## 推奨事項

Auditing helps in troubleshooting operational problems and also permits forensic analysis. If log_error_verbosity is not set to the correct value, too many details or too few details may be logged. This flag should be configured with a value of 'DEFAULT' or stricter. This recommendation is applicable to PostgreSQL database instances.

- 推奨リンク：[https://cloud.google.com/sql/docs/postgres/flags](https://cloud.google.com/sql/docs/postgres/flags)

## 修正手順


### CLI

```text
gcloud sql instances patch INSTANCE_NAME --database-flags log_error_verbosity=default
```

## 参考資料

- [https://cloud.google.com/sql/docs/postgres/flags](https://cloud.google.com/sql/docs/postgres/flags)

## 技術情報

- Source Metadata：[sources/gcp/cloudsql_instance_postgres_log_error_verbosity_flag/metadata.json](../../sources/gcp/cloudsql_instance_postgres_log_error_verbosity_flag/metadata.json)
- Source Code：[sources/gcp/cloudsql_instance_postgres_log_error_verbosity_flag/check.py](../../sources/gcp/cloudsql_instance_postgres_log_error_verbosity_flag/check.py)
- Source Metadata Path：`sources/gcp/cloudsql_instance_postgres_log_error_verbosity_flag/metadata.json`
- Source Code Path：`sources/gcp/cloudsql_instance_postgres_log_error_verbosity_flag/check.py`
