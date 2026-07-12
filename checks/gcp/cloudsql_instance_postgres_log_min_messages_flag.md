# Ensure that the Log_min_messages Flag for a Cloud SQL PostgreSQL Instance Is Set Appropriately

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `cloudsql_instance_postgres_log_min_messages_flag` |
| クラウドプラットフォーム | GCP |
| サービス | cloudsql |
| 重大度 | medium |
| カテゴリ | Uncategorized |
| リソースタイプ | DatabaseInstance |
| リソースグループ | database |

## 説明

Ensure that the Log_min_messages Flag for a Cloud SQL PostgreSQL Instance Is Set Appropriately

## リスク

Auditing helps in troubleshooting operational problems and also permits forensic analysis. If log_min_messages is not set to the correct value, messages may not be classified as error messages appropriately. An organization will need to decide their own threshold for logging log_min_messages flag.

## 推奨事項

The log_min_messages flag defines the minimum message severity level that is considered as an error statement. Messages for error statements are logged with the SQL statement. Valid values include DEBUG5, DEBUG4, DEBUG3, DEBUG2, DEBUG1, INFO, NOTICE, WARNING, ERROR, LOG, FATAL, and PANIC. Each severity level includes the subsequent levels mentioned above. ERROR is considered the best practice setting. Changes should only be made in accordance with the organization's logging policy.

- 推奨リンク：[https://cloud.google.com/sql/docs/postgres/flags](https://cloud.google.com/sql/docs/postgres/flags)

## 修正手順


### CLI

```text
gcloud sql instances patch INSTANCE_NAME --database-flags log_min_messages=warning
```

### Terraform

[https://docs.ST Cloud.com/checks/gcp/cloud-sql-policies/bc_gcp_sql_4#terraform](https://docs.ST Cloud.com/checks/gcp/cloud-sql-policies/bc_gcp_sql_4#terraform)

## 参考資料

- [https://cloud.google.com/sql/docs/postgres/flags](https://cloud.google.com/sql/docs/postgres/flags)

## 技術情報

- Source Metadata：[sources/gcp/cloudsql_instance_postgres_log_min_messages_flag/metadata.json](../../sources/gcp/cloudsql_instance_postgres_log_min_messages_flag/metadata.json)
- Source Code：[sources/gcp/cloudsql_instance_postgres_log_min_messages_flag/check.py](../../sources/gcp/cloudsql_instance_postgres_log_min_messages_flag/check.py)
- Source Metadata Path：`sources/gcp/cloudsql_instance_postgres_log_min_messages_flag/metadata.json`
- Source Code Path：`sources/gcp/cloudsql_instance_postgres_log_min_messages_flag/check.py`
