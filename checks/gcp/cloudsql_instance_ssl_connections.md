# Ensure That the Cloud SQL Database Instance Requires All Incoming Connections To Use SSL

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `cloudsql_instance_ssl_connections` |
| クラウドプラットフォーム | GCP |
| サービス | cloudsql |
| 重大度 | medium |
| カテゴリ | Uncategorized |
| リソースタイプ | DatabaseInstance |
| リソースグループ | database |

## 説明

Ensure That the Cloud SQL Database Instance Requires All Incoming Connections To Use SSL

## リスク

SQL database connections if successfully trapped (MITM), can reveal sensitive data like credentials, database queries, query outputs etc. For security, it is recommended to always use SSL encryption when connecting to your instance. This recommendation is applicable for Postgresql, MySql generation 1, MySql generation 2 and SQL Server 2017 instances.

## 推奨事項

It is recommended to enforce all incoming connections to SQL database instance to use SSL.

- 推奨リンク：[https://cloud.google.com/sql/docs/postgres/configure-ssl-instance/](https://cloud.google.com/sql/docs/postgres/configure-ssl-instance/)

## 修正手順


### CLI

```text
gcloud sql instances patch <INSTANCE_NAME> --require-ssl
```

### Other

[https://www.trendmicro.com/cloudoneconformity/knowledge-base/gcp/CloudSQL/enable-ssl-for-incoming-connections.html](https://www.trendmicro.com/cloudoneconformity/knowledge-base/gcp/CloudSQL/enable-ssl-for-incoming-connections.html)

## 参考資料

- [https://cloud.google.com/sql/docs/postgres/configure-ssl-instance/](https://cloud.google.com/sql/docs/postgres/configure-ssl-instance/)

## 技術情報

- Source Metadata：[sources/gcp/cloudsql_instance_ssl_connections/metadata.json](../../sources/gcp/cloudsql_instance_ssl_connections/metadata.json)
- Source Code：[sources/gcp/cloudsql_instance_ssl_connections/check.py](../../sources/gcp/cloudsql_instance_ssl_connections/check.py)
- Source Metadata Path：`sources/gcp/cloudsql_instance_ssl_connections/metadata.json`
- Source Code Path：`sources/gcp/cloudsql_instance_ssl_connections/check.py`
