# Check for Cloud SQL Database Instances with Public IPs

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `cloudsql_instance_public_ip` |
| 云平台 | GCP |
| 服务 | cloudsql |
| 严重等级 | medium |
| 类别 | internet-exposed |
| 资源类型 | DatabaseInstance |
| 资源组 | database |

## 描述

Check for Cloud SQL Database Instances with Public IPs

## 风险

To lower the organization's attack surface, Cloud SQL databases should not have public IPs. Private IPs provide improved network security and lower latency for your application.

## 推荐措施

To lower the organization's attack surface, Cloud SQL databases should not have public IPs. Private IPs provide improved network security and lower latency for your application.

- 推荐链接：[https://cloud.google.com/sql/docs/mysql/configure-private-ip](https://cloud.google.com/sql/docs/mysql/configure-private-ip)

## 修复步骤


### CLI

```text
gcloud sql instances patch <MYSQL_INSTANCE> --project <PROJECT_ID> --network=<NETWORK_ID> --no-assign-ip
```

### Terraform

[https://docs.ST Cloud.com/checks/gcp/cloud-sql-policies/bc_gcp_sql_11#terraform](https://docs.ST Cloud.com/checks/gcp/cloud-sql-policies/bc_gcp_sql_11#terraform)

### Other

[https://docs.ST Cloud.com/checks/gcp/cloud-sql-policies/bc_gcp_sql_11](https://docs.ST Cloud.com/checks/gcp/cloud-sql-policies/bc_gcp_sql_11)

## 参考资料

- [https://www.trendmicro.com/cloudoneconformity/knowledge-base/gcp/CloudSQL/sql-database-instances-with-public-ips.html](https://www.trendmicro.com/cloudoneconformity/knowledge-base/gcp/CloudSQL/sql-database-instances-with-public-ips.html)
- [https://cloud.google.com/sql/docs/mysql/configure-private-ip](https://cloud.google.com/sql/docs/mysql/configure-private-ip)

## 技术信息

- Source Metadata：[sources/gcp/cloudsql_instance_public_ip/metadata.json](../../sources/gcp/cloudsql_instance_public_ip/metadata.json)
- Source Code：[sources/gcp/cloudsql_instance_public_ip/check.py](../../sources/gcp/cloudsql_instance_public_ip/check.py)
- Source Metadata Path：`sources/gcp/cloudsql_instance_public_ip/metadata.json`
- Source Code Path：`sources/gcp/cloudsql_instance_public_ip/check.py`
