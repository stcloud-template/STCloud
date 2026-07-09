# Ensure 'external scripts enabled' database flag for Cloud SQL SQL Server instance is set to 'off'

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `cloudsql_instance_sqlserver_external_scripts_enabled_flag` |
| 云平台 | GCP |
| 服务 | cloudsql |
| 严重等级 | high |
| 类别 | Uncategorized |
| 资源类型 | DatabaseInstance |
| 资源组 | database |

## 描述

Ensure 'external scripts enabled' database flag for Cloud SQL SQL Server instance is set to 'off'

## 风险

external scripts enabled enable the execution of scripts with certain remote language extensions. This property is OFF by default. When Advanced Analytics Services is installed, setup can optionally set this property to true. As the External Scripts Enabled feature allows scripts external to SQL such as files located in an R library to be executed, which could adversely affect the security of the system, hence this should be disabled.

## 推荐措施

It is recommended to set external scripts enabled database flag for Cloud SQL SQL Server instance to off

- 推荐链接：[https://cloud.google.com/sql/docs/sqlserver/flags](https://cloud.google.com/sql/docs/sqlserver/flags)

## 修复步骤


### CLI

```text
gcloud sql instances patch INSTANCE_NAME --database-flags external scripts enabled=off
```

### Other

[https://www.trendmicro.com/cloudoneconformity/knowledge-base/gcp/CloudSQL/disable-external-scripts-enabled-flag.html](https://www.trendmicro.com/cloudoneconformity/knowledge-base/gcp/CloudSQL/disable-external-scripts-enabled-flag.html)

## 参考资料

- [https://cloud.google.com/sql/docs/sqlserver/flags](https://cloud.google.com/sql/docs/sqlserver/flags)

## 技术信息

- Source Metadata：[sources/gcp/cloudsql_instance_sqlserver_external_scripts_enabled_flag/metadata.json](../../sources/gcp/cloudsql_instance_sqlserver_external_scripts_enabled_flag/metadata.json)
- Source Code：[sources/gcp/cloudsql_instance_sqlserver_external_scripts_enabled_flag/check.py](../../sources/gcp/cloudsql_instance_sqlserver_external_scripts_enabled_flag/check.py)
- Source Metadata Path：`sources/gcp/cloudsql_instance_sqlserver_external_scripts_enabled_flag/metadata.json`
- Source Code Path：`sources/gcp/cloudsql_instance_sqlserver_external_scripts_enabled_flag/check.py`
