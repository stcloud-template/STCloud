# Ensure that the 'contained database authentication' database flag for Cloud SQL on the SQL Server instance is set to 'off'

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `cloudsql_instance_sqlserver_contained_database_authentication_flag` |
| クラウドプラットフォーム | GCP |
| サービス | cloudsql |
| 重大度 | medium |
| カテゴリ | Uncategorized |
| リソースタイプ | DatabaseInstance |
| リソースグループ | database |

## 説明

Ensure that the 'contained database authentication' database flag for Cloud SQL on the SQL Server instance is set to 'off'

## リスク

A contained database includes all database settings and metadata required to define the database and has no configuration dependencies on the instance of the Database Engine where the database is installed. Users can connect to the database without authenticating a login at the Database Engine level. Isolating the database from the Database Engine makes it possible to easily move the database to another instance of SQL Server. Contained databases have some unique threats that should be understood and mitigated by SQL Server Database Engine administrators. Most of the threats are related to the USER WITH PASSWORD authentication process, which moves the authentication boundary from the Database Engine level to the database level, hence this is recommended to disable this flag. This recommendation is applicable to SQL Server database instances.

## 推奨事項

It is recommended to set contained database authentication database flag for Cloud SQL on the SQL Server instance to off.

- 推奨リンク：[https://cloud.google.com/sql/docs/sqlserver/flags](https://cloud.google.com/sql/docs/sqlserver/flags)

## 修正手順


### CLI

```text
gcloud sql instances patch <INSTANCE_NAME> --database-flags contained database authentication=off
```

### Terraform

[https://docs.ST Cloud.com/checks/gcp/cloud-sql-policies/bc_gcp_sql_10#terraform](https://docs.ST Cloud.com/checks/gcp/cloud-sql-policies/bc_gcp_sql_10#terraform)

### Other

[https://www.trendmicro.com/cloudoneconformity/knowledge-base/gcp/CloudSQL/disable-contained-database-authentication-flag.html](https://www.trendmicro.com/cloudoneconformity/knowledge-base/gcp/CloudSQL/disable-contained-database-authentication-flag.html)

## 参考資料

- [https://cloud.google.com/sql/docs/sqlserver/flags](https://cloud.google.com/sql/docs/sqlserver/flags)

## 技術情報

- Source Metadata：[sources/gcp/cloudsql_instance_sqlserver_contained_database_authentication_flag/metadata.json](../../sources/gcp/cloudsql_instance_sqlserver_contained_database_authentication_flag/metadata.json)
- Source Code：[sources/gcp/cloudsql_instance_sqlserver_contained_database_authentication_flag/check.py](../../sources/gcp/cloudsql_instance_sqlserver_contained_database_authentication_flag/check.py)
- Source Metadata Path：`sources/gcp/cloudsql_instance_sqlserver_contained_database_authentication_flag/metadata.json`
- Source Code Path：`sources/gcp/cloudsql_instance_sqlserver_contained_database_authentication_flag/check.py`
