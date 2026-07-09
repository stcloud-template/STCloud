# Check if RDS clusters are protected by a backup plan.

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `rds_cluster_protected_by_backup_plan` |
| 云平台 | AWS |
| 服务 | rds |
| 严重等级 | medium |
| 类别 | Uncategorized |
| 检查类型 | Software and Configuration Checks, AWS Security Best Practices |
| 资源类型 | AwsRdsDbInstance |
| 资源组 | database |

## 描述

Check if RDS clusters are protected by a backup plan.

## 风险

Without a backup plan, RDS clusters are vulnerable to data loss, accidental deletion, or corruption. This could lead to significant operational disruptions or loss of critical data.

## 推荐措施

Create a backup plan for the RDS cluster to protect it from data loss, accidental deletion, or corruption.

- 推荐链接：[https://docs.aws.amazon.com/aws-backup/latest/devguide/assigning-resources.html](https://docs.aws.amazon.com/aws-backup/latest/devguide/assigning-resources.html)

## 修复步骤


### CLI

```text
aws backup create-backup-plan --backup-plan , aws backup tag-resource --resource-arn <rds-cluster-arn> --tags Key=backup,Value=true
```

### Other

[https://docs.aws.amazon.com/securityhub/latest/userguide/rds-controls.html#rds-26](https://docs.aws.amazon.com/securityhub/latest/userguide/rds-controls.html#rds-26)

## 参考资料

- [https://docs.aws.amazon.com/aws-backup/latest/devguide/assigning-resources.html](https://docs.aws.amazon.com/aws-backup/latest/devguide/assigning-resources.html)

## 技术信息

- Source Metadata：[sources/aws/rds_cluster_protected_by_backup_plan/metadata.json](../../sources/aws/rds_cluster_protected_by_backup_plan/metadata.json)
- Source Code：[sources/aws/rds_cluster_protected_by_backup_plan/check.py](../../sources/aws/rds_cluster_protected_by_backup_plan/check.py)
- Source Metadata Path：`sources/aws/rds_cluster_protected_by_backup_plan/metadata.json`
- Source Code Path：`sources/aws/rds_cluster_protected_by_backup_plan/check.py`
