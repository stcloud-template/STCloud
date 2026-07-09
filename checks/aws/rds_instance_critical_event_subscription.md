# Check if RDS Instances events are subscribed.

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `rds_instance_critical_event_subscription` |
| 云平台 | AWS |
| 服务 | rds |
| 严重等级 | low |
| 类别 | Uncategorized |
| 检查类型 | Software and Configuration Checks, AWS Security Best Practices |
| 资源类型 | AwsRdsEventSubscription |
| 资源组 | database |

## 描述

Ensure that Amazon RDS event notification subscriptions are enabled for database database events, particularly maintenance, configuration change and failure.

## 风险

Without event subscriptions for critical events, such as maintenance, configuration changes and failures, you may not be aware of issues affecting your RDS instances, leading to downtime or security vulnerabilities.

## 推荐措施

To subscribe to RDS instance event notifications, see Subscribing to Amazon RDS event notification in the Amazon RDS User Guide.

- 推荐链接：[https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_Events.Subscribing.html](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_Events.Subscribing.html)

## 修复步骤


### CLI

```text
aws rds create-event-subscription --source-type db-instance --event-categories 'failure' 'maintenance' 'configuration change' --sns-topic-arn <sns-topic-arn>
```

### Other

[https://docs.aws.amazon.com/securityhub/latest/userguide/rds-controls.html#rds-20](https://docs.aws.amazon.com/securityhub/latest/userguide/rds-controls.html#rds-20)

## 参考资料

- [https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_Events.html](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_Events.html)
- [https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_Events.Subscribing.html](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_Events.Subscribing.html)

## 技术信息

- Source Metadata：[sources/aws/rds_instance_critical_event_subscription/metadata.json](../../sources/aws/rds_instance_critical_event_subscription/metadata.json)
- Source Code：[sources/aws/rds_instance_critical_event_subscription/check.py](../../sources/aws/rds_instance_critical_event_subscription/check.py)
- Source Metadata Path：`sources/aws/rds_instance_critical_event_subscription/metadata.json`
- Source Code Path：`sources/aws/rds_instance_critical_event_subscription/check.py`
