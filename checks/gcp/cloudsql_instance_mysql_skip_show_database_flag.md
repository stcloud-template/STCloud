# Ensure Skip_show_database Database Flag for Cloud SQL MySQL Instance Is Set to On

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `cloudsql_instance_mysql_skip_show_database_flag` |
| 云平台 | GCP |
| 服务 | cloudsql |
| 严重等级 | medium |
| 类别 | Uncategorized |
| 资源类型 | DatabaseInstance |
| 资源组 | database |

## 描述

Ensure Skip_show_database Database Flag for Cloud SQL MySQL Instance Is Set to On

## 风险

'skip_show_database' database flag prevents people from using the SHOW DATABASES statement if they do not have the SHOW DATABASES privilege.

## 推荐措施

It is recommended to set skip_show_database database flag for Cloud SQL Mysql instance to on.

- 推荐链接：[https://cloud.google.com/sql/docs/mysql/flags](https://cloud.google.com/sql/docs/mysql/flags)

## 修复步骤


### CLI

```text
gcloud sql instances patch INSTANCE_NAME --database-flags skip_show_database=on
```

### Other

[https://www.trendmicro.com/cloudoneconformity/knowledge-base/gcp/CloudSQL/enable-skip-show-database-flag.html](https://www.trendmicro.com/cloudoneconformity/knowledge-base/gcp/CloudSQL/enable-skip-show-database-flag.html)

## 参考资料

- [https://cloud.google.com/sql/docs/mysql/flags](https://cloud.google.com/sql/docs/mysql/flags)

## 技术信息

- Source Metadata：[sources/gcp/cloudsql_instance_mysql_skip_show_database_flag/metadata.json](../../sources/gcp/cloudsql_instance_mysql_skip_show_database_flag/metadata.json)
- Source Code：[sources/gcp/cloudsql_instance_mysql_skip_show_database_flag/check.py](../../sources/gcp/cloudsql_instance_mysql_skip_show_database_flag/check.py)
- Source Metadata Path：`sources/gcp/cloudsql_instance_mysql_skip_show_database_flag/metadata.json`
- Source Code Path：`sources/gcp/cloudsql_instance_mysql_skip_show_database_flag/check.py`
