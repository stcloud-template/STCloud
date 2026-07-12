# Ensure That the Log_statement Database Flag for Cloud SQL PostgreSQL Instance Is Set Appropriately

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `cloudsql_instance_postgres_log_statement_flag` |
| クラウドプラットフォーム | GCP |
| サービス | cloudsql |
| 重大度 | medium |
| カテゴリ | Uncategorized |
| リソースタイプ | DatabaseInstance |
| リソースグループ | database |

## 説明

Ensure That the Log_statement Database Flag for Cloud SQL PostgreSQL Instance Is Set Appropriately

## リスク

Auditing helps in forensic analysis. If log_statement is not set to the correct value, too many statements may be logged leading to issues in finding the relevant information from the logs, or too few statements may be logged with relevant information missing from the logs.

## 推奨事項

The value ddl logs all data definition statements. A value of 'ddl' is recommended unless otherwise directed by your organization's logging policy.

- 推奨リンク：[https://cloud.google.com/sql/docs/postgres/flags](https://cloud.google.com/sql/docs/postgres/flags)

## 修正手順


### CLI

```text
gcloud sql instances patch INSTANCE_NAME --database-flags log_statement=ddl
```

## 参考資料

- [https://cloud.google.com/sql/docs/postgres/flags](https://cloud.google.com/sql/docs/postgres/flags)

## 技術情報

- Source Metadata：[sources/gcp/cloudsql_instance_postgres_log_statement_flag/metadata.json](../../sources/gcp/cloudsql_instance_postgres_log_statement_flag/metadata.json)
- Source Code：[sources/gcp/cloudsql_instance_postgres_log_statement_flag/check.py](../../sources/gcp/cloudsql_instance_postgres_log_statement_flag/check.py)
- Source Metadata Path：`sources/gcp/cloudsql_instance_postgres_log_statement_flag/metadata.json`
- Source Code Path：`sources/gcp/cloudsql_instance_postgres_log_statement_flag/check.py`
