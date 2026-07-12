# Ensure 'user options' database flag for Cloud SQL SQL Server instance is not configured

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `cloudsql_instance_sqlserver_user_options_flag` |
| クラウドプラットフォーム | GCP |
| サービス | cloudsql |
| 重大度 | medium |
| カテゴリ | Uncategorized |
| リソースタイプ | DatabaseInstance |
| リソースグループ | database |

## 説明

Ensure 'user options' database flag for Cloud SQL SQL Server instance is not configured

## リスク

The user options option specifies global defaults for all users. A list of default query processing options is established for the duration of a user's work session. The user options option allows you to change the default values of the SET options (if the server's default settings are not appropriate). A user can override these defaults by using the SET statement. You can configure user options dynamically for new logins. After you change the setting of user options, new login sessions use the new setting, current login sessions are not affected.

## 推奨事項

It is recommended that, user options database flag for Cloud SQL SQL Server instance should not be configured.

- 推奨リンク：[https://cloud.google.com/sql/docs/sqlserver/flags](https://cloud.google.com/sql/docs/sqlserver/flags)

## 修正手順


### Other

[https://www.trendmicro.com/cloudoneconformity/knowledge-base/gcp/CloudSQL/user-options-flag-not-configured.html](https://www.trendmicro.com/cloudoneconformity/knowledge-base/gcp/CloudSQL/user-options-flag-not-configured.html)

## 参考資料

- [https://cloud.google.com/sql/docs/sqlserver/flags](https://cloud.google.com/sql/docs/sqlserver/flags)

## 技術情報

- Source Metadata：[sources/gcp/cloudsql_instance_sqlserver_user_options_flag/metadata.json](../../sources/gcp/cloudsql_instance_sqlserver_user_options_flag/metadata.json)
- Source Code：[sources/gcp/cloudsql_instance_sqlserver_user_options_flag/check.py](../../sources/gcp/cloudsql_instance_sqlserver_user_options_flag/check.py)
- Source Metadata Path：`sources/gcp/cloudsql_instance_sqlserver_user_options_flag/metadata.json`
- Source Code Path：`sources/gcp/cloudsql_instance_sqlserver_user_options_flag/check.py`
