# Ensure That Cloud SQL Database Instances Are Configured With Automated Backups

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `cloudsql_instance_automated_backups` |
| クラウドプラットフォーム | GCP |
| サービス | cloudsql |
| 重大度 | medium |
| カテゴリ | Uncategorized |
| リソースタイプ | DatabaseInstance |
| リソースグループ | database |

## 説明

Ensure That Cloud SQL Database Instances Are Configured With Automated Backups

## リスク

Backups provide a way to restore a Cloud SQL instance to recover lost data or recover from a problem with that instance. Automated backups need to be set for any instance that contains data that should be protected from loss or damage. This recommendation is applicable for SQL Server, PostgreSql, MySql generation 1 and MySql generation 2 instances.

## 推奨事項

It is recommended to have all SQL database instances set to enable automated backups.

- 推奨リンク：[https://cloud.google.com/sql/docs/postgres/configure-ssl-instance/](https://cloud.google.com/sql/docs/postgres/configure-ssl-instance/)

## 修正手順


### CLI

```text
gcloud sql instances patch <INSTANCE_NAME> --backup-start-time <[HH:MM]>
```

### Other

[https://www.trendmicro.com/cloudoneconformity/knowledge-base/gcp/CloudSQL/enable-automated-backups.html](https://www.trendmicro.com/cloudoneconformity/knowledge-base/gcp/CloudSQL/enable-automated-backups.html)

## 参考資料

- [https://cloud.google.com/sql/docs/postgres/configure-ssl-instance/](https://cloud.google.com/sql/docs/postgres/configure-ssl-instance/)

## 技術情報

- Source Metadata：[sources/gcp/cloudsql_instance_automated_backups/metadata.json](../../sources/gcp/cloudsql_instance_automated_backups/metadata.json)
- Source Code：[sources/gcp/cloudsql_instance_automated_backups/check.py](../../sources/gcp/cloudsql_instance_automated_backups/check.py)
- Source Metadata Path：`sources/gcp/cloudsql_instance_automated_backups/metadata.json`
- Source Code Path：`sources/gcp/cloudsql_instance_automated_backups/check.py`
