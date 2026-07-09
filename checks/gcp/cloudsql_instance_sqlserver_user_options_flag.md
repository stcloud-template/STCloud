# Ensure 'user options' database flag for Cloud SQL SQL Server instance is not configured

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `cloudsql_instance_sqlserver_user_options_flag` |
| 云平台 | GCP |
| 服务 | cloudsql |
| 严重等级 | medium |
| 类别 | Uncategorized |
| 资源类型 | DatabaseInstance |
| 资源组 | database |

## 描述

Ensure 'user options' database flag for Cloud SQL SQL Server instance is not configured

## 风险

The user options option specifies global defaults for all users. A list of default query processing options is established for the duration of a user's work session. The user options option allows you to change the default values of the SET options (if the server's default settings are not appropriate). A user can override these defaults by using the SET statement. You can configure user options dynamically for new logins. After you change the setting of user options, new login sessions use the new setting, current login sessions are not affected.

## 推荐措施

It is recommended that, user options database flag for Cloud SQL SQL Server instance should not be configured.

- 推荐链接：[https://cloud.google.com/sql/docs/sqlserver/flags](https://cloud.google.com/sql/docs/sqlserver/flags)

## 修复步骤


### Other

[https://www.trendmicro.com/cloudoneconformity/knowledge-base/gcp/CloudSQL/user-options-flag-not-configured.html](https://www.trendmicro.com/cloudoneconformity/knowledge-base/gcp/CloudSQL/user-options-flag-not-configured.html)

## 参考资料

- [https://cloud.google.com/sql/docs/sqlserver/flags](https://cloud.google.com/sql/docs/sqlserver/flags)

## 技术信息

- Source Metadata：[sources/gcp/cloudsql_instance_sqlserver_user_options_flag/metadata.json](../../sources/gcp/cloudsql_instance_sqlserver_user_options_flag/metadata.json)
- Source Code：[sources/gcp/cloudsql_instance_sqlserver_user_options_flag/check.py](../../sources/gcp/cloudsql_instance_sqlserver_user_options_flag/check.py)
- Source Metadata Path：`sources/gcp/cloudsql_instance_sqlserver_user_options_flag/metadata.json`
- Source Code Path：`sources/gcp/cloudsql_instance_sqlserver_user_options_flag/check.py`
