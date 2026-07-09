# Ensure that the 'cross db ownership chaining' database flag for Cloud SQL SQL Server instance is set to 'off'

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `cloudsql_instance_sqlserver_cross_db_ownership_chaining_flag` |
| 云平台 | GCP |
| 服务 | cloudsql |
| 严重等级 | medium |
| 类别 | Uncategorized |
| 资源类型 | DatabaseInstance |
| 资源组 | database |

## 描述

Ensure that the 'cross db ownership chaining' database flag for Cloud SQL SQL Server instance is set to 'off'

## 风险

Use the cross db ownership for chaining option to configure cross-database ownership chaining for an instance of Microsoft SQL Server. This server option allows you to control cross-database ownership chaining at the database level or to allow cross- database ownership chaining for all databases. Enabling cross db ownership is not recommended unless all of the databases hosted by the instance of SQL Server must participate in cross-database ownership chaining and you are aware of the security implications of this setting.

## 推荐措施

It is recommended to set cross db ownership chaining database flag for Cloud SQL SQL Server instance to off.

- 推荐链接：[https://cloud.google.com/sql/docs/sqlserver/flags](https://cloud.google.com/sql/docs/sqlserver/flags)

## 修复步骤


### CLI

```text
gcloud sql instances patch INSTANCE_NAME --database-flags cross db ownership=off
```

### Other

[https://www.trendmicro.com/cloudoneconformity/knowledge-base/gcp/CloudSQL/disable-cross-db-ownership-chaining-flag.html](https://www.trendmicro.com/cloudoneconformity/knowledge-base/gcp/CloudSQL/disable-cross-db-ownership-chaining-flag.html)

## 参考资料

- [https://cloud.google.com/sql/docs/sqlserver/flags](https://cloud.google.com/sql/docs/sqlserver/flags)

## 技术信息

- Source Metadata：[sources/gcp/cloudsql_instance_sqlserver_cross_db_ownership_chaining_flag/metadata.json](../../sources/gcp/cloudsql_instance_sqlserver_cross_db_ownership_chaining_flag/metadata.json)
- Source Code：[sources/gcp/cloudsql_instance_sqlserver_cross_db_ownership_chaining_flag/check.py](../../sources/gcp/cloudsql_instance_sqlserver_cross_db_ownership_chaining_flag/check.py)
- Source Metadata Path：`sources/gcp/cloudsql_instance_sqlserver_cross_db_ownership_chaining_flag/metadata.json`
- Source Code Path：`sources/gcp/cloudsql_instance_sqlserver_cross_db_ownership_chaining_flag/check.py`
