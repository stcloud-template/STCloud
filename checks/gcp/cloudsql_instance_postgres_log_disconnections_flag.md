# Ensure That the log_disconnections Database Flag for Cloud SQL PostgreSQL Instance Is Set to On

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `cloudsql_instance_postgres_log_disconnections_flag` |
| クラウドプラットフォーム | GCP |
| サービス | cloudsql |
| 重大度 | medium |
| カテゴリ | Uncategorized |
| リソースタイプ | DatabaseInstance |
| リソースグループ | database |

## 説明

Ensure That the log_disconnections Database Flag for Cloud SQL PostgreSQL Instance Is Set to On

## リスク

PostgreSQL does not log session details such as duration and session end by default. Enabling the log_disconnections setting will create log entries at the end of each session which can be useful in troubleshooting issues and determine any unusual activity across a time period.

## 推奨事項

Enabling the log_disconnections setting logs the end of each session, including the session duration.

- 推奨リンク：[https://cloud.google.com/sql/docs/postgres/flags](https://cloud.google.com/sql/docs/postgres/flags)

## 修正手順


### CLI

```text
gcloud sql instances patch INSTANCE_NAME --database-flags log_disconnections=on
```

### Terraform

[https://docs.ST Cloud.com/checks/gcp/cloud-sql-policies/bc_gcp_sql_4#terraform](https://docs.ST Cloud.com/checks/gcp/cloud-sql-policies/bc_gcp_sql_4#terraform)

### Other

[https://www.trendmicro.com/cloudoneconformity/knowledge-base/gcp/CloudSQL/enable-log-connections-flag.html](https://www.trendmicro.com/cloudoneconformity/knowledge-base/gcp/CloudSQL/enable-log-connections-flag.html)

## 参考資料

- [https://cloud.google.com/sql/docs/postgres/flags](https://cloud.google.com/sql/docs/postgres/flags)

## 技術情報

- Source Metadata：[sources/gcp/cloudsql_instance_postgres_log_disconnections_flag/metadata.json](../../sources/gcp/cloudsql_instance_postgres_log_disconnections_flag/metadata.json)
- Source Code：[sources/gcp/cloudsql_instance_postgres_log_disconnections_flag/check.py](../../sources/gcp/cloudsql_instance_postgres_log_disconnections_flag/check.py)
- Source Metadata Path：`sources/gcp/cloudsql_instance_postgres_log_disconnections_flag/metadata.json`
- Source Code Path：`sources/gcp/cloudsql_instance_postgres_log_disconnections_flag/check.py`
