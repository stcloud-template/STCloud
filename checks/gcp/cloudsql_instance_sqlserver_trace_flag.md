# Ensure '3625 (trace flag)' database flag for all Cloud SQL Server instances is set to 'on'

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `cloudsql_instance_sqlserver_trace_flag` |
| 云平台 | GCP |
| 服务 | cloudsql |
| 严重等级 | medium |
| 类别 | Uncategorized |
| 资源类型 | DatabaseInstance |
| 资源组 | database |

## 描述

Ensure '3625 (trace flag)' database flag for all Cloud SQL Server instances is set to 'on'

## 风险

Microsoft SQL Trace Flags are frequently used to diagnose performance issues or to debug stored procedures or complex computer systems, but they may also be recommended by Microsoft Support to address behavior that is negatively impacting a specific workload. All documented trace flags and those recommended by Microsoft Support are fully supported in a production environment when used as directed. 3625(trace log) Limits the amount of information returned to users who are not members of the sysadmin fixed server role, by masking the parameters of some error messages using '******'. Setting this in a Google Cloud flag for the instance allows for security through obscurity and prevents the disclosure of sensitive information, hence this is recommended to set this flag globally to on to prevent the flag having been left off, or changed by bad actors. This recommendation is applicable to SQL Server database instances.

## 推荐措施

It is recommended to set 3625 (trace flag) database flag for Cloud SQL SQL Server instance to on.

- 推荐链接：[https://cloud.google.com/sql/docs/sqlserver/flags](https://cloud.google.com/sql/docs/sqlserver/flags)

## 修复步骤


### CLI

```text
gcloud sql instances patch <INSTANCE_NAME> --database-flags 3625=on
```

### Other

[https://www.trendmicro.com/cloudoneconformity/knowledge-base/gcp/CloudSQL/disable-3625-trace-flag.html](https://www.trendmicro.com/cloudoneconformity/knowledge-base/gcp/CloudSQL/disable-3625-trace-flag.html)

## 参考资料

- [https://cloud.google.com/sql/docs/sqlserver/flags](https://cloud.google.com/sql/docs/sqlserver/flags)

## 技术信息

- Source Metadata：[sources/gcp/cloudsql_instance_sqlserver_trace_flag/metadata.json](../../sources/gcp/cloudsql_instance_sqlserver_trace_flag/metadata.json)
- Source Code：[sources/gcp/cloudsql_instance_sqlserver_trace_flag/check.py](../../sources/gcp/cloudsql_instance_sqlserver_trace_flag/check.py)
- Source Metadata Path：`sources/gcp/cloudsql_instance_sqlserver_trace_flag/metadata.json`
- Source Code Path：`sources/gcp/cloudsql_instance_sqlserver_trace_flag/check.py`
