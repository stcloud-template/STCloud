# Check if RDS clusters have multi-AZ enabled.

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `rds_cluster_multi_az` |
| 云平台 | AWS |
| 服务 | rds |
| 严重等级 | medium |
| 类别 | redundancy |
| 资源类型 | AwsRdsDbCluster |
| 资源组 | database |

## 描述

Check if RDS clusters have multi-AZ enabled.

## 风险

In case of failure, with a single-AZ deployment configuration, should an availability zone specific database failure occur, Amazon RDS can not automatically fail over to the standby availability zone.

## 推荐措施

Enable multi-AZ deployment for production databases.

- 推荐链接：[https://aws.amazon.com/rds/features/multi-az/](https://aws.amazon.com/rds/features/multi-az/)

## 修复步骤


### CLI

```text
aws rds create-db-cluster --db-cluster-identifier <db_cluster_id> --multi-az true
```

### Native IaC

[https://docs.ST Cloud.com/checks/aws/general-policies/general_73#cloudformation](https://docs.ST Cloud.com/checks/aws/general-policies/general_73#cloudformation)

### Terraform

[https://docs.ST Cloud.com/checks/aws/general-policies/general_73#terraform](https://docs.ST Cloud.com/checks/aws/general-policies/general_73#terraform)

### Other

[https://docs.aws.amazon.com/securityhub/latest/userguide/rds-controls.html#rds-15](https://docs.aws.amazon.com/securityhub/latest/userguide/rds-controls.html#rds-15)

## 参考资料

- [https://aws.amazon.com/rds/features/multi-az/](https://aws.amazon.com/rds/features/multi-az/)

## 技术信息

- Source Metadata：[sources/aws/rds_cluster_multi_az/metadata.json](../../sources/aws/rds_cluster_multi_az/metadata.json)
- Source Code：[sources/aws/rds_cluster_multi_az/check.py](../../sources/aws/rds_cluster_multi_az/check.py)
- Source Metadata Path：`sources/aws/rds_cluster_multi_az/metadata.json`
- Source Code Path：`sources/aws/rds_cluster_multi_az/check.py`
