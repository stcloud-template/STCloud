# Ensure That Cloud SQL Database Instances Do Not Implicitly Whitelist All Public IP Addresses

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `cloudsql_instance_public_access` |
| 云平台 | GCP |
| 服务 | cloudsql |
| 严重等级 | high |
| 类别 | internet-exposed |
| 资源类型 | DatabaseInstance |
| 资源组 | database |

## 描述

Ensure That Cloud SQL Database Instances Do Not Implicitly Whitelist All Public IP Addresses

## 风险

To minimize attack surface on a Database server instance, only trusted/known and required IP(s) should be white-listed to connect to it. An authorized network should not have IPs/networks configured to 0.0.0.0/0 which will allow access to the instance from anywhere in the world. Note that authorized networks apply only to instances with public IPs.

## 推荐措施

Database Server should accept connections only from trusted Network(s)/IP(s) and restrict access from public IP addresses.

- 推荐链接：[https://cloud.google.com/sql/docs/mysql/connection-org-policy](https://cloud.google.com/sql/docs/mysql/connection-org-policy)

## 修复步骤


### CLI

```text
gcloud sql instances patch <INSTANCE_NAME> --authorized-networks=IP_ADDR1,IP_ADDR2...
```

### Other

[https://www.trendmicro.com/cloudoneconformity/knowledge-base/gcp/CloudSQL/publicly-accessible-cloud-sql-instances.html](https://www.trendmicro.com/cloudoneconformity/knowledge-base/gcp/CloudSQL/publicly-accessible-cloud-sql-instances.html)

## 参考资料

- [https://cloud.google.com/sql/docs/mysql/connection-org-policy](https://cloud.google.com/sql/docs/mysql/connection-org-policy)

## 技术信息

- Source Metadata：[sources/gcp/cloudsql_instance_public_access/metadata.json](../../sources/gcp/cloudsql_instance_public_access/metadata.json)
- Source Code：[sources/gcp/cloudsql_instance_public_access/check.py](../../sources/gcp/cloudsql_instance_public_access/check.py)
- Source Metadata Path：`sources/gcp/cloudsql_instance_public_access/metadata.json`
- Source Code Path：`sources/gcp/cloudsql_instance_public_access/check.py`
