# Check if RDS Security Group events are subscribed.

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `rds_instance_event_subscription_security_groups` |
| 云平台 | AWS |
| 服务 | rds |
| 严重等级 | medium |
| 类别 | Uncategorized |
| 资源类型 | AwsRdsEventSubscription |
| 资源组 | database |

## 描述

Ensure that Amazon RDS event notification subscriptions are enabled for database security groups events.

## 风险

Amazon RDS event subscriptions for database security groups are designed to provide incident notification of events that may affect the security, availability, and reliability of the RDS database instances associated with these security groups.

## 推荐措施

To subscribe to RDS instance event notifications, see Subscribing to Amazon RDS event notification in the Amazon RDS User Guide.

- 推荐链接：[https://docs.aws.amazon.com/securityhub/latest/userguide/rds-controls.html#rds-22](https://docs.aws.amazon.com/securityhub/latest/userguide/rds-controls.html#rds-22)

## 修复步骤


### Native IaC

[https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/RDS/rds-db-security-groups-events.html#](https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/RDS/rds-db-security-groups-events.html#)

### Terraform

[https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/RDS/rds-db-security-groups-events.html#](https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/RDS/rds-db-security-groups-events.html#)

### Other

[https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/RDS/rds-db-security-groups-events.html#](https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/RDS/rds-db-security-groups-events.html#)

## 参考资料

- [https://docs.aws.amazon.com/securityhub/latest/userguide/rds-controls.html#rds-22](https://docs.aws.amazon.com/securityhub/latest/userguide/rds-controls.html#rds-22)

## 技术信息

- Source Metadata：[sources/aws/rds_instance_event_subscription_security_groups/metadata.json](../../sources/aws/rds_instance_event_subscription_security_groups/metadata.json)
- Source Code：[sources/aws/rds_instance_event_subscription_security_groups/check.py](../../sources/aws/rds_instance_event_subscription_security_groups/check.py)
- Source Metadata Path：`sources/aws/rds_instance_event_subscription_security_groups/metadata.json`
- Source Code Path：`sources/aws/rds_instance_event_subscription_security_groups/check.py`
