# Ensure That the Log_connections Database Flag for Cloud SQL PostgreSQL Instance Is Set to On

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `cloudsql_instance_postgres_log_connections_flag` |
| クラウドプラットフォーム | GCP |
| サービス | cloudsql |
| 重大度 | medium |
| カテゴリ | Uncategorized |
| リソースタイプ | DatabaseInstance |
| リソースグループ | database |

## 説明

Ensure That the Log_connections Database Flag for Cloud SQL PostgreSQL Instance Is Set to On

## リスク

Enabling the log_connections setting causes each attempted connection to the server to be logged, along with successful completion of client authentication. This parameter cannot be changed after the session starts.

## 推奨事項

PostgreSQL does not log attempted connections by default. Enabling the log_connections setting will create log entries for each attempted connection as well as successful completion of client authentication which can be useful in troubleshooting issues and to determine any unusual connection attempts to the server.

- 推奨リンク：[https://cloud.google.com/sql/docs/postgres/flags](https://cloud.google.com/sql/docs/postgres/flags)

## 修正手順


### CLI

```text
gcloud sql instances patch INSTANCE_NAME --database-flags log_connections=on
```

### Terraform

[https://docs.ST Cloud.com/checks/gcp/cloud-sql-policies/bc_gcp_sql_3#terraform](https://docs.ST Cloud.com/checks/gcp/cloud-sql-policies/bc_gcp_sql_3#terraform)

### Other

[https://www.trendmicro.com/cloudoneconformity/knowledge-base/gcp/CloudSQL/enable-log-connections-flag.html](https://www.trendmicro.com/cloudoneconformity/knowledge-base/gcp/CloudSQL/enable-log-connections-flag.html)

## 参考資料

- [https://cloud.google.com/sql/docs/postgres/flags](https://cloud.google.com/sql/docs/postgres/flags)

## 技術情報

- Source Metadata：[sources/gcp/cloudsql_instance_postgres_log_connections_flag/metadata.json](../../sources/gcp/cloudsql_instance_postgres_log_connections_flag/metadata.json)
- Source Code：[sources/gcp/cloudsql_instance_postgres_log_connections_flag/check.py](../../sources/gcp/cloudsql_instance_postgres_log_connections_flag/check.py)
- Source Metadata Path：`sources/gcp/cloudsql_instance_postgres_log_connections_flag/metadata.json`
- Source Code Path：`sources/gcp/cloudsql_instance_postgres_log_connections_flag/check.py`
