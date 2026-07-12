# Ensure Skip_show_database Database Flag for Cloud SQL MySQL Instance Is Set to On

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `cloudsql_instance_mysql_skip_show_database_flag` |
| クラウドプラットフォーム | GCP |
| サービス | cloudsql |
| 重大度 | medium |
| カテゴリ | Uncategorized |
| リソースタイプ | DatabaseInstance |
| リソースグループ | database |

## 説明

Ensure Skip_show_database Database Flag for Cloud SQL MySQL Instance Is Set to On

## リスク

'skip_show_database' database flag prevents people from using the SHOW DATABASES statement if they do not have the SHOW DATABASES privilege.

## 推奨事項

It is recommended to set skip_show_database database flag for Cloud SQL Mysql instance to on.

- 推奨リンク：[https://cloud.google.com/sql/docs/mysql/flags](https://cloud.google.com/sql/docs/mysql/flags)

## 修正手順


### CLI

```text
gcloud sql instances patch INSTANCE_NAME --database-flags skip_show_database=on
```

### Other

[https://www.trendmicro.com/cloudoneconformity/knowledge-base/gcp/CloudSQL/enable-skip-show-database-flag.html](https://www.trendmicro.com/cloudoneconformity/knowledge-base/gcp/CloudSQL/enable-skip-show-database-flag.html)

## 参考資料

- [https://cloud.google.com/sql/docs/mysql/flags](https://cloud.google.com/sql/docs/mysql/flags)

## 技術情報

- Source Metadata：[sources/gcp/cloudsql_instance_mysql_skip_show_database_flag/metadata.json](../../sources/gcp/cloudsql_instance_mysql_skip_show_database_flag/metadata.json)
- Source Code：[sources/gcp/cloudsql_instance_mysql_skip_show_database_flag/check.py](../../sources/gcp/cloudsql_instance_mysql_skip_show_database_flag/check.py)
- Source Metadata Path：`sources/gcp/cloudsql_instance_mysql_skip_show_database_flag/metadata.json`
- Source Code Path：`sources/gcp/cloudsql_instance_mysql_skip_show_database_flag/check.py`
