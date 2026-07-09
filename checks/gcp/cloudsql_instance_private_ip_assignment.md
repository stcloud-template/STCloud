# Ensure Instance IP assignment is set to private

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `cloudsql_instance_private_ip_assignment` |
| 云平台 | GCP |
| 服务 | cloudsql |
| 严重等级 | medium |
| 类别 | Uncategorized |
| 资源类型 | DatabaseInstance |
| 资源组 | database |

## 描述

Ensure Instance IP assignment is set to private

## 风险

Instance addresses can be public IP or private IP. Public IP means that the instance is accessible through the public internet. In contrast, instances using only private IP are not accessible through the public internet, but are accessible through a Virtual Private Cloud (VPC). Limiting network access to your database will limit potential attacks.

## 推荐措施

Setting databases access only to private will reduce attack surface.

- 推荐链接：[https://cloud.google.com/sql/docs/mysql/configure-private-ip](https://cloud.google.com/sql/docs/mysql/configure-private-ip)

## 修复步骤

No remediation steps available.

## 参考资料

- [https://cloud.google.com/sql/docs/mysql/configure-private-ip](https://cloud.google.com/sql/docs/mysql/configure-private-ip)

## 技术信息

- Source Metadata：[sources/gcp/cloudsql_instance_private_ip_assignment/metadata.json](../../sources/gcp/cloudsql_instance_private_ip_assignment/metadata.json)
- Source Code：[sources/gcp/cloudsql_instance_private_ip_assignment/check.py](../../sources/gcp/cloudsql_instance_private_ip_assignment/check.py)
- Source Metadata Path：`sources/gcp/cloudsql_instance_private_ip_assignment/metadata.json`
- Source Code Path：`sources/gcp/cloudsql_instance_private_ip_assignment/check.py`
