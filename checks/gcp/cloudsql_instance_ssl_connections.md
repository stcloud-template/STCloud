# Ensure That the Cloud SQL Database Instance Requires All Incoming Connections To Use SSL

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `cloudsql_instance_ssl_connections` |
| 云平台 | GCP |
| 服务 | cloudsql |
| 严重等级 | medium |
| 类别 | Uncategorized |
| 资源类型 | DatabaseInstance |
| 资源组 | database |

## 描述

Ensure That the Cloud SQL Database Instance Requires All Incoming Connections To Use SSL

## 风险

SQL database connections if successfully trapped (MITM), can reveal sensitive data like credentials, database queries, query outputs etc. For security, it is recommended to always use SSL encryption when connecting to your instance. This recommendation is applicable for Postgresql, MySql generation 1, MySql generation 2 and SQL Server 2017 instances.

## 推荐措施

It is recommended to enforce all incoming connections to SQL database instance to use SSL.

- 推荐链接：[https://cloud.google.com/sql/docs/postgres/configure-ssl-instance/](https://cloud.google.com/sql/docs/postgres/configure-ssl-instance/)

## 修复步骤


### CLI

```text
gcloud sql instances patch <INSTANCE_NAME> --require-ssl
```

### Other

[https://www.trendmicro.com/cloudoneconformity/knowledge-base/gcp/CloudSQL/enable-ssl-for-incoming-connections.html](https://www.trendmicro.com/cloudoneconformity/knowledge-base/gcp/CloudSQL/enable-ssl-for-incoming-connections.html)

## 参考资料

- [https://cloud.google.com/sql/docs/postgres/configure-ssl-instance/](https://cloud.google.com/sql/docs/postgres/configure-ssl-instance/)

## 技术信息

- Source Metadata：[sources/gcp/cloudsql_instance_ssl_connections/metadata.json](../../sources/gcp/cloudsql_instance_ssl_connections/metadata.json)
- Source Code：[sources/gcp/cloudsql_instance_ssl_connections/check.py](../../sources/gcp/cloudsql_instance_ssl_connections/check.py)
- Source Metadata Path：`sources/gcp/cloudsql_instance_ssl_connections/metadata.json`
- Source Code Path：`sources/gcp/cloudsql_instance_ssl_connections/check.py`
