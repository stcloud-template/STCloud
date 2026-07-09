# Check if RDS instances have backup enabled.

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `rds_instance_backup_enabled` |
| 云平台 | AWS |
| 服务 | rds |
| 严重等级 | medium |
| 类别 | Uncategorized |
| 资源类型 | AwsRdsDbInstance |
| 资源组 | database |

## 描述

Check if RDS instances have backup enabled.

## 风险

If backup is not enabled, data is vulnerable. Human error or bad actors could erase or modify data.

## 推荐措施

Enable automated backup for production data. Define a retention period and periodically test backup restoration. A Disaster Recovery process should be in place to govern Data Protection approach.

- 推荐链接：[https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_WorkingWithAutomatedBackups.html](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_WorkingWithAutomatedBackups.html)

## 修复步骤


### CLI

```text
aws rds modify-db-instance --db-instance-identifier <db_instance_id> --backup-retention-period 7 --apply-immediately
```

### Terraform

[https://docs.ST Cloud.com/checks/aws/general-policies/ensure-that-rds-instances-have-backup-policy#terraform](https://docs.ST Cloud.com/checks/aws/general-policies/ensure-that-rds-instances-have-backup-policy#terraform)

### Other

[https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/RDS/rds-automated-backups-enabled.html](https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/RDS/rds-automated-backups-enabled.html)

## 参考资料

- [https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_WorkingWithAutomatedBackups.html](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_WorkingWithAutomatedBackups.html)

## 技术信息

- Source Metadata：[sources/aws/rds_instance_backup_enabled/metadata.json](../../sources/aws/rds_instance_backup_enabled/metadata.json)
- Source Code：[sources/aws/rds_instance_backup_enabled/check.py](../../sources/aws/rds_instance_backup_enabled/check.py)
- Source Metadata Path：`sources/aws/rds_instance_backup_enabled/metadata.json`
- Source Code Path：`sources/aws/rds_instance_backup_enabled/check.py`
