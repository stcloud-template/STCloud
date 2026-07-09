# Ensure 'remote access' database flag for Cloud SQL SQL Server instance is set to 'off'

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `cloudsql_instance_sqlserver_remote_access_flag` |
| 云平台 | GCP |
| 服务 | cloudsql |
| 严重等级 | high |
| 类别 | Uncategorized |
| 资源类型 | DatabaseInstance |
| 资源组 | database |

## 描述

Ensure 'remote access' database flag for Cloud SQL SQL Server instance is set to 'off'

## 风险

The remote access option controls the execution of stored procedures from local or remote servers on which instances of SQL Server are running. This default value for this option is 1. This grants permission to run local stored procedures from remote servers or remote stored procedures from the local server. To prevent local stored procedures from being run from a remote server or remote stored procedures from being run on the local server, this must be disabled. The Remote Access option controls the execution of local stored procedures on remote servers or remote stored procedures on local server. 'Remote access' functionality can be abused to launch a Denial-of- Service (DoS) attack on remote servers by off-loading query processing to a target, hence this should be disabled. This recommendation is applicable to SQL Server database instances.

## 推荐措施

It is recommended to set remote access database flag for Cloud SQL SQL Server instance to off.

- 推荐链接：[https://cloud.google.com/sql/docs/sqlserver/flags](https://cloud.google.com/sql/docs/sqlserver/flags)

## 修复步骤


### Other

[https://www.trendmicro.com/cloudoneconformity/knowledge-base/gcp/CloudSQL/disable-remote-access-flag.html](https://www.trendmicro.com/cloudoneconformity/knowledge-base/gcp/CloudSQL/disable-remote-access-flag.html)

## 参考资料

- [https://cloud.google.com/sql/docs/sqlserver/flags](https://cloud.google.com/sql/docs/sqlserver/flags)

## 技术信息

- Source Metadata：[sources/gcp/cloudsql_instance_sqlserver_remote_access_flag/metadata.json](../../sources/gcp/cloudsql_instance_sqlserver_remote_access_flag/metadata.json)
- Source Code：[sources/gcp/cloudsql_instance_sqlserver_remote_access_flag/check.py](../../sources/gcp/cloudsql_instance_sqlserver_remote_access_flag/check.py)
- Source Metadata Path：`sources/gcp/cloudsql_instance_sqlserver_remote_access_flag/metadata.json`
- Source Code Path：`sources/gcp/cloudsql_instance_sqlserver_remote_access_flag/check.py`
