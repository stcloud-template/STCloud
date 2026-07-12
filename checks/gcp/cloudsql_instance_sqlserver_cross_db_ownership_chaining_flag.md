# Ensure that the 'cross db ownership chaining' database flag for Cloud SQL SQL Server instance is set to 'off'

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `cloudsql_instance_sqlserver_cross_db_ownership_chaining_flag` |
| クラウドプラットフォーム | GCP |
| サービス | cloudsql |
| 重大度 | medium |
| カテゴリ | Uncategorized |
| リソースタイプ | DatabaseInstance |
| リソースグループ | database |

## 説明

Ensure that the 'cross db ownership chaining' database flag for Cloud SQL SQL Server instance is set to 'off'

## リスク

Use the cross db ownership for chaining option to configure cross-database ownership chaining for an instance of Microsoft SQL Server. This server option allows you to control cross-database ownership chaining at the database level or to allow cross- database ownership chaining for all databases. Enabling cross db ownership is not recommended unless all of the databases hosted by the instance of SQL Server must participate in cross-database ownership chaining and you are aware of the security implications of this setting.

## 推奨事項

It is recommended to set cross db ownership chaining database flag for Cloud SQL SQL Server instance to off.

- 推奨リンク：[https://cloud.google.com/sql/docs/sqlserver/flags](https://cloud.google.com/sql/docs/sqlserver/flags)

## 修正手順


### CLI

```text
gcloud sql instances patch INSTANCE_NAME --database-flags cross db ownership=off
```

### Other

[https://www.trendmicro.com/cloudoneconformity/knowledge-base/gcp/CloudSQL/disable-cross-db-ownership-chaining-flag.html](https://www.trendmicro.com/cloudoneconformity/knowledge-base/gcp/CloudSQL/disable-cross-db-ownership-chaining-flag.html)

## 参考資料

- [https://cloud.google.com/sql/docs/sqlserver/flags](https://cloud.google.com/sql/docs/sqlserver/flags)

## 技術情報

- Source Metadata：[sources/gcp/cloudsql_instance_sqlserver_cross_db_ownership_chaining_flag/metadata.json](../../sources/gcp/cloudsql_instance_sqlserver_cross_db_ownership_chaining_flag/metadata.json)
- Source Code：[sources/gcp/cloudsql_instance_sqlserver_cross_db_ownership_chaining_flag/check.py](../../sources/gcp/cloudsql_instance_sqlserver_cross_db_ownership_chaining_flag/check.py)
- Source Metadata Path：`sources/gcp/cloudsql_instance_sqlserver_cross_db_ownership_chaining_flag/metadata.json`
- Source Code Path：`sources/gcp/cloudsql_instance_sqlserver_cross_db_ownership_chaining_flag/check.py`
