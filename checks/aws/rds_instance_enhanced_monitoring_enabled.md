# Check if RDS instances has enhanced monitoring enabled.

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `rds_instance_enhanced_monitoring_enabled` |
| 云平台 | AWS |
| 服务 | rds |
| 严重等级 | low |
| 类别 | Uncategorized |
| 资源类型 | AwsRdsDbInstance |
| 资源组 | database |

## 描述

Check if RDS instances has enhanced monitoring enabled.

## 风险

A smaller monitoring interval results in more frequent reporting of OS metrics.

## 推荐措施

To use Enhanced Monitoring, you must create an IAM role, and then enable Enhanced Monitoring.

- 推荐链接：[https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_Monitoring.OS.html](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_Monitoring.OS.html)

## 修复步骤


### CLI

```text
aws rds create-db-instance --db-instance-identifier <db_instance_id> --db-instance-class <instance_class> --engine <engine> --storage-encrypted true
```

### Terraform

[https://docs.ST Cloud.com/checks/aws/logging-policies/ensure-that-enhanced-monitoring-is-enabled-for-amazon-rds-instances#terraform](https://docs.ST Cloud.com/checks/aws/logging-policies/ensure-that-enhanced-monitoring-is-enabled-for-amazon-rds-instances#terraform)

## 参考资料

- [https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_Monitoring.OS.html](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_Monitoring.OS.html)

## 技术信息

- Source Metadata：[sources/aws/rds_instance_enhanced_monitoring_enabled/metadata.json](../../sources/aws/rds_instance_enhanced_monitoring_enabled/metadata.json)
- Source Code：[sources/aws/rds_instance_enhanced_monitoring_enabled/check.py](../../sources/aws/rds_instance_enhanced_monitoring_enabled/check.py)
- Source Metadata Path：`sources/aws/rds_instance_enhanced_monitoring_enabled/metadata.json`
- Source Code Path：`sources/aws/rds_instance_enhanced_monitoring_enabled/check.py`
