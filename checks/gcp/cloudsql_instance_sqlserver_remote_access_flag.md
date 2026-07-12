# Ensure 'remote access' database flag for Cloud SQL SQL Server instance is set to 'off'

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `cloudsql_instance_sqlserver_remote_access_flag` |
| クラウドプラットフォーム | GCP |
| サービス | cloudsql |
| 重大度 | high |
| カテゴリ | Uncategorized |
| リソースタイプ | DatabaseInstance |
| リソースグループ | database |

## 説明

Ensure 'remote access' database flag for Cloud SQL SQL Server instance is set to 'off'

## リスク

The remote access option controls the execution of stored procedures from local or remote servers on which instances of SQL Server are running. This default value for this option is 1. This grants permission to run local stored procedures from remote servers or remote stored procedures from the local server. To prevent local stored procedures from being run from a remote server or remote stored procedures from being run on the local server, this must be disabled. The Remote Access option controls the execution of local stored procedures on remote servers or remote stored procedures on local server. 'Remote access' functionality can be abused to launch a Denial-of- Service (DoS) attack on remote servers by off-loading query processing to a target, hence this should be disabled. This recommendation is applicable to SQL Server database instances.

## 推奨事項

It is recommended to set remote access database flag for Cloud SQL SQL Server instance to off.

- 推奨リンク：[https://cloud.google.com/sql/docs/sqlserver/flags](https://cloud.google.com/sql/docs/sqlserver/flags)

## 修正手順


### Other

[https://www.trendmicro.com/cloudoneconformity/knowledge-base/gcp/CloudSQL/disable-remote-access-flag.html](https://www.trendmicro.com/cloudoneconformity/knowledge-base/gcp/CloudSQL/disable-remote-access-flag.html)

## 参考資料

- [https://cloud.google.com/sql/docs/sqlserver/flags](https://cloud.google.com/sql/docs/sqlserver/flags)

## 技術情報

- Source Metadata：[sources/gcp/cloudsql_instance_sqlserver_remote_access_flag/metadata.json](../../sources/gcp/cloudsql_instance_sqlserver_remote_access_flag/metadata.json)
- Source Code：[sources/gcp/cloudsql_instance_sqlserver_remote_access_flag/check.py](../../sources/gcp/cloudsql_instance_sqlserver_remote_access_flag/check.py)
- Source Metadata Path：`sources/gcp/cloudsql_instance_sqlserver_remote_access_flag/metadata.json`
- Source Code Path：`sources/gcp/cloudsql_instance_sqlserver_remote_access_flag/check.py`
