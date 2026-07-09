# Ensure That 'cloudsql.enable_pgaudit' Database Flag for each Cloud Sql Postgresql Instance Is Set to 'on' For Centralized Logging

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `cloudsql_instance_postgres_enable_pgaudit_flag` |
| 云平台 | GCP |
| 服务 | cloudsql |
| 严重等级 | medium |
| 类别 | Uncategorized |
| 资源类型 | DatabaseInstance |
| 资源组 | database |

## 描述

Ensure That 'cloudsql.enable_pgaudit' Database Flag for each Cloud Sql Postgresql Instance Is Set to 'on' For Centralized Logging

## 风险

Ensure cloudsql.enable_pgaudit database flag for Cloud SQL PostgreSQL instance is set to on to allow for centralized logging.

## 推荐措施

As numerous other recommendations in this section consist of turning on flags for logging purposes, your organization will need a way to manage these logs. You may have a solution already in place. If you do not, consider installing and enabling the open source pgaudit extension within PostgreSQL and enabling its corresponding flag of cloudsql.enable_pgaudit. This flag and installing the extension enables database auditing in PostgreSQL through the open-source pgAudit extension. This extension provides detailed session and object logging to comply with government, financial, & ISO standards and provides auditing capabilities to mitigate threats by monitoring security events on the instance. Enabling the flag and settings later in this recommendation will send these logs to Google Logs Explorer so that you can access them in a central location.

- 推荐链接：[https://cloud.google.com/sql/docs/postgres/flags](https://cloud.google.com/sql/docs/postgres/flags)

## 修复步骤


### CLI

```text
gcloud sql instances patch INSTANCE_NAME --database-flags cloudsql.enable_pgaudit=On
```

### Other

[https://www.trendmicro.com/cloudoneconformity/knowledge-base/gcp/CloudSQL/postgre-sql-audit-flag.html](https://www.trendmicro.com/cloudoneconformity/knowledge-base/gcp/CloudSQL/postgre-sql-audit-flag.html)

## 参考资料

- [https://cloud.google.com/sql/docs/postgres/flags](https://cloud.google.com/sql/docs/postgres/flags)

## 技术信息

- Source Metadata：[sources/gcp/cloudsql_instance_postgres_enable_pgaudit_flag/metadata.json](../../sources/gcp/cloudsql_instance_postgres_enable_pgaudit_flag/metadata.json)
- Source Code：[sources/gcp/cloudsql_instance_postgres_enable_pgaudit_flag/check.py](../../sources/gcp/cloudsql_instance_postgres_enable_pgaudit_flag/check.py)
- Source Metadata Path：`sources/gcp/cloudsql_instance_postgres_enable_pgaudit_flag/metadata.json`
- Source Code Path：`sources/gcp/cloudsql_instance_postgres_enable_pgaudit_flag/check.py`
