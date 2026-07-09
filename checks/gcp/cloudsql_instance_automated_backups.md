# Ensure That Cloud SQL Database Instances Are Configured With Automated Backups

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `cloudsql_instance_automated_backups` |
| 云平台 | GCP |
| 服务 | cloudsql |
| 严重等级 | medium |
| 类别 | Uncategorized |
| 资源类型 | DatabaseInstance |
| 资源组 | database |

## 描述

Ensure That Cloud SQL Database Instances Are Configured With Automated Backups

## 风险

Backups provide a way to restore a Cloud SQL instance to recover lost data or recover from a problem with that instance. Automated backups need to be set for any instance that contains data that should be protected from loss or damage. This recommendation is applicable for SQL Server, PostgreSql, MySql generation 1 and MySql generation 2 instances.

## 推荐措施

It is recommended to have all SQL database instances set to enable automated backups.

- 推荐链接：[https://cloud.google.com/sql/docs/postgres/configure-ssl-instance/](https://cloud.google.com/sql/docs/postgres/configure-ssl-instance/)

## 修复步骤


### CLI

```text
gcloud sql instances patch <INSTANCE_NAME> --backup-start-time <[HH:MM]>
```

### Other

[https://www.trendmicro.com/cloudoneconformity/knowledge-base/gcp/CloudSQL/enable-automated-backups.html](https://www.trendmicro.com/cloudoneconformity/knowledge-base/gcp/CloudSQL/enable-automated-backups.html)

## 参考资料

- [https://cloud.google.com/sql/docs/postgres/configure-ssl-instance/](https://cloud.google.com/sql/docs/postgres/configure-ssl-instance/)

## 技术信息

- Source Metadata：[sources/gcp/cloudsql_instance_automated_backups/metadata.json](../../sources/gcp/cloudsql_instance_automated_backups/metadata.json)
- Source Code：[sources/gcp/cloudsql_instance_automated_backups/check.py](../../sources/gcp/cloudsql_instance_automated_backups/check.py)
- Source Metadata Path：`sources/gcp/cloudsql_instance_automated_backups/metadata.json`
- Source Code Path：`sources/gcp/cloudsql_instance_automated_backups/check.py`
