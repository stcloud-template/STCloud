# Check if RDS Aurora MySQL Clusters have backtrack enabled.

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `rds_cluster_backtrack_enabled` |
| 云平台 | AWS |
| 服务 | rds |
| 严重等级 | medium |
| 类别 | Uncategorized |
| 资源类型 | AwsRdsDbCluster |
| 资源组 | database |

## 描述

Ensure that the Backtrack feature is enabled for your Amazon Aurora (with MySQL compatibility) database clusters in order to backtrack your clusters to a specific time, without using backups. Backtrack is an Amazon RDS feature that allows you to specify the amount of time that an Aurora MySQL database cluster needs to retain change records, in order to have a fast way to recover from user errors, such as dropping the wrong table or deleting the wrong row by moving your MySQL database to a prior point in time without the need to restore from a recent backup.

## 风险

Once the Backtrack feature is enabled, Amazon RDS can quickly 'rewind' your Aurora MySQL database cluster to a point in time that you specify. In contrast to the backup and restore method, with Backtrack you can easily undo a destructive action, such as a DELETE query without a WHERE clause, with minimal downtime, you can rewind your Aurora cluster in just few minutes, and you can repeatedly backtrack a database cluster back and forth in time to help determine when a particular data change occurred.

## 推荐措施

Backups help you to recover more quickly from a security incident. They also strengthens the resilience of your systems. Aurora backtracking reduces the time to recover a database to a point in time. It does not require a database restore to do so. You cannot enable backtracking on an existing cluster. Instead, you can create a clone that has backtracking enabled.

- 推荐链接：[https://docs.aws.amazon.com/securityhub/latest/userguide/rds-controls.html#rds-14](https://docs.aws.amazon.com/securityhub/latest/userguide/rds-controls.html#rds-14)

## 修复步骤


### CLI

```text
aws rds restore-db-cluster-to-point-in-time --region <REGION> --source-db-cluster-identifier <SOURCE_DB_CLUSTER_ID> --db-cluster-identifier <DB_CLUSTER_ID> --restore-type copy-on-write --use-latest-restorable-time --backtrack-window 86400
```

### Native IaC

[https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/RDS/backtrack.html#](https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/RDS/backtrack.html#)

### Terraform

[https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/RDS/backtrack.html#](https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/RDS/backtrack.html#)

### Other

[https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/RDS/backtrack.html#](https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/RDS/backtrack.html#)

## 参考资料

- [https://docs.aws.amazon.com/securityhub/latest/userguide/rds-controls.html#rds-14](https://docs.aws.amazon.com/securityhub/latest/userguide/rds-controls.html#rds-14)

## 技术信息

- Source Metadata：[sources/aws/rds_cluster_backtrack_enabled/metadata.json](../../sources/aws/rds_cluster_backtrack_enabled/metadata.json)
- Source Code：[sources/aws/rds_cluster_backtrack_enabled/check.py](../../sources/aws/rds_cluster_backtrack_enabled/check.py)
- Source Metadata Path：`sources/aws/rds_cluster_backtrack_enabled/metadata.json`
- Source Code Path：`sources/aws/rds_cluster_backtrack_enabled/check.py`
