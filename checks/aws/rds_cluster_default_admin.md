# Ensure that your Amazon RDS clusters are not using the default master username.

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `rds_cluster_default_admin` |
| 云平台 | AWS |
| 服务 | rds |
| 严重等级 | medium |
| 类别 | Uncategorized |
| 资源类型 | AwsRdsDbCluster |
| 资源组 | database |

## 描述

Ensure that your Amazon RDS clusters are not using the default master username.

## 风险

Since admin is the Amazon's example for the RDS database master username and postgres is the default PostgreSQL master username. Many AWS customers will use this username for their RDS database instances in production. Malicious users can use this information to their advantage and frequently try to use default master username during brute-force attacks.

## 推荐措施

To change the master username configured for your Amazon RDS database clusters you must re-create them and migrate the existing data.

- 推荐链接：[https://docs.aws.amazon.com/securityhub/latest/userguide/rds-controls.html#rds-24](https://docs.aws.amazon.com/securityhub/latest/userguide/rds-controls.html#rds-24)

## 修复步骤


### Native IaC

[https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/RDS/rds-master-username.html#](https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/RDS/rds-master-username.html#)

### Terraform

[https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/RDS/rds-master-username.html#](https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/RDS/rds-master-username.html#)

### Other

[https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/RDS/rds-master-username.html#](https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/RDS/rds-master-username.html#)

## 参考资料

- [https://docs.aws.amazon.com/securityhub/latest/userguide/rds-controls.html#rds-24](https://docs.aws.amazon.com/securityhub/latest/userguide/rds-controls.html#rds-24)

## 技术信息

- Source Metadata：[sources/aws/rds_cluster_default_admin/metadata.json](../../sources/aws/rds_cluster_default_admin/metadata.json)
- Source Code：[sources/aws/rds_cluster_default_admin/check.py](../../sources/aws/rds_cluster_default_admin/check.py)
- Source Metadata Path：`sources/aws/rds_cluster_default_admin/metadata.json`
- Source Code Path：`sources/aws/rds_cluster_default_admin/check.py`
