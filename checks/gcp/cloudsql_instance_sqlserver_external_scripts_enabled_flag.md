# Ensure 'external scripts enabled' database flag for Cloud SQL SQL Server instance is set to 'off'

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `cloudsql_instance_sqlserver_external_scripts_enabled_flag` |
| クラウドプラットフォーム | GCP |
| サービス | cloudsql |
| 重大度 | high |
| カテゴリ | Uncategorized |
| リソースタイプ | DatabaseInstance |
| リソースグループ | database |

## 説明

Ensure 'external scripts enabled' database flag for Cloud SQL SQL Server instance is set to 'off'

## リスク

external scripts enabled enable the execution of scripts with certain remote language extensions. This property is OFF by default. When Advanced Analytics Services is installed, setup can optionally set this property to true. As the External Scripts Enabled feature allows scripts external to SQL such as files located in an R library to be executed, which could adversely affect the security of the system, hence this should be disabled.

## 推奨事項

It is recommended to set external scripts enabled database flag for Cloud SQL SQL Server instance to off

- 推奨リンク：[https://cloud.google.com/sql/docs/sqlserver/flags](https://cloud.google.com/sql/docs/sqlserver/flags)

## 修正手順


### CLI

```text
gcloud sql instances patch INSTANCE_NAME --database-flags external scripts enabled=off
```

### Other

[https://www.trendmicro.com/cloudoneconformity/knowledge-base/gcp/CloudSQL/disable-external-scripts-enabled-flag.html](https://www.trendmicro.com/cloudoneconformity/knowledge-base/gcp/CloudSQL/disable-external-scripts-enabled-flag.html)

## 参考資料

- [https://cloud.google.com/sql/docs/sqlserver/flags](https://cloud.google.com/sql/docs/sqlserver/flags)

## 技術情報

- Source Metadata：[sources/gcp/cloudsql_instance_sqlserver_external_scripts_enabled_flag/metadata.json](../../sources/gcp/cloudsql_instance_sqlserver_external_scripts_enabled_flag/metadata.json)
- Source Code：[sources/gcp/cloudsql_instance_sqlserver_external_scripts_enabled_flag/check.py](../../sources/gcp/cloudsql_instance_sqlserver_external_scripts_enabled_flag/check.py)
- Source Metadata Path：`sources/gcp/cloudsql_instance_sqlserver_external_scripts_enabled_flag/metadata.json`
- Source Code Path：`sources/gcp/cloudsql_instance_sqlserver_external_scripts_enabled_flag/check.py`
