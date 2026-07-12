# Ensure 'user Connections' Database Flag for Cloud Sql Sql Server Instance Is Set to a Non-limiting Value

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `cloudsql_instance_sqlserver_user_connections_flag` |
| クラウドプラットフォーム | GCP |
| サービス | cloudsql |
| 重大度 | medium |
| カテゴリ | Uncategorized |
| リソースタイプ | DatabaseInstance |
| リソースグループ | database |

## 説明

Ensure 'user Connections' Database Flag for Cloud Sql Sql Server Instance Is Set to a Non-limiting Value

## リスク

The user connections option specifies the maximum number of simultaneous user connections that are allowed on an instance of SQL Server. The actual number of user connections allowed also depends on the version of SQL Server that you are using, and also the limits of your application or applications and hardware. SQL Server allows a maximum of 32,767 user connections. Because user connections is by default a self- configuring value, with SQL Server adjusting the maximum number of user connections automatically as needed, up to the maximum value allowable. For example, if only 10 users are logged in, 10 user connection objects are allocated. In most cases, you do not have to change the value for this option. The default is 0, which means that the maximum (32,767) user connections are allowed. However if there is a number defined here that limits connections, SQL Server will not allow anymore above this limit. If the connections are at the limit, any new requests will be dropped, potentially causing lost data or outages for those using the database.

## 推奨事項

It is recommended to check the user connections for a Cloud SQL SQL Server instance to ensure that it is not artificially limiting connections.

- 推奨リンク：[https://cloud.google.com/sql/docs/sqlserver/flags](https://cloud.google.com/sql/docs/sqlserver/flags)

## 修正手順


### CLI

```text
gcloud sql instances patch INSTANCE_NAME --database-flags user connections=0
```

### Other

[https://www.trendmicro.com/cloudoneconformity/knowledge-base/gcp/CloudSQL/configure-user-connection-flag.html](https://www.trendmicro.com/cloudoneconformity/knowledge-base/gcp/CloudSQL/configure-user-connection-flag.html)

## 参考資料

- [https://cloud.google.com/sql/docs/sqlserver/flags](https://cloud.google.com/sql/docs/sqlserver/flags)

## 技術情報

- Source Metadata：[sources/gcp/cloudsql_instance_sqlserver_user_connections_flag/metadata.json](../../sources/gcp/cloudsql_instance_sqlserver_user_connections_flag/metadata.json)
- Source Code：[sources/gcp/cloudsql_instance_sqlserver_user_connections_flag/check.py](../../sources/gcp/cloudsql_instance_sqlserver_user_connections_flag/check.py)
- Source Metadata Path：`sources/gcp/cloudsql_instance_sqlserver_user_connections_flag/metadata.json`
- Source Code Path：`sources/gcp/cloudsql_instance_sqlserver_user_connections_flag/check.py`
