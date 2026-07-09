# Check if RDS Parameter Group events are subscribed.

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `rds_instance_event_subscription_parameter_groups` |
| 云平台 | AWS |
| 服务 | rds |
| 严重等级 | low |
| 类别 | Uncategorized |
| 资源类型 | AwsAccount |
| 资源组 | governance |

## 描述

Ensure that Amazon RDS event notification subscriptions are enabled for database parameter groups events.

## 风险

Amazon RDS event subscriptions for database parameter groups are designed to provide incident notification of events that may affect the security, availability, and reliability of the RDS database instances associated with these parameter groups.

## 推荐措施

To subscribe to RDS instance event notifications, see Subscribing to Amazon RDS event notification in the Amazon RDS User Guide.

- 推荐链接：[https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_Events.Subscribing.html](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_Events.Subscribing.html)

## 修复步骤


### CLI

```text
aws rds create-event-subscription --source-type db-instance --event-categories 'configuration change' --sns-topic-arn <sns-topic-arn>
```

### Other

[https://docs.aws.amazon.com/securityhub/latest/userguide/rds-controls.html#rds-21](https://docs.aws.amazon.com/securityhub/latest/userguide/rds-controls.html#rds-21)

## 参考资料

- [https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_Events.html](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_Events.html)
- [https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_Events.Subscribing.html](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_Events.Subscribing.html)

## 技术信息

- Source Metadata：[sources/aws/rds_instance_event_subscription_parameter_groups/metadata.json](../../sources/aws/rds_instance_event_subscription_parameter_groups/metadata.json)
- Source Code：[sources/aws/rds_instance_event_subscription_parameter_groups/check.py](../../sources/aws/rds_instance_event_subscription_parameter_groups/check.py)
- Source Metadata Path：`sources/aws/rds_instance_event_subscription_parameter_groups/metadata.json`
- Source Code Path：`sources/aws/rds_instance_event_subscription_parameter_groups/check.py`
