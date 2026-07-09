# Check if RDS Cluster critical events are subscribed.

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `rds_cluster_critical_event_subscription` |
| 云平台 | AWS |
| 服务 | rds |
| 严重等级 | low |
| 类别 | Uncategorized |
| 检查类型 | Software and Configuration Checks, AWS Security Best Practices |
| 资源类型 | AwsAccount |
| 资源组 | governance |

## 描述

Ensure that Amazon RDS event notification subscriptions are enabled for database cluster events, particularly maintenance and failure.

## 风险

Without event subscriptions for critical events, such as maintenance and failures, you may not be aware of issues affecting your RDS clusters, leading to downtime or security vulnerabilities.

## 推荐措施

To subscribe to RDS cluster event notifications, see Subscribing to Amazon RDS event notification in the Amazon RDS User Guide.

- 推荐链接：[https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_Events.Subscribing.html](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_Events.Subscribing.html)

## 修复步骤


### CLI

```text
aws rds create-event-subscription --source-type db-cluster --event-categories 'failure' 'maintenance' --sns-topic-arn <sns-topic-arn>
```

### Other

[https://docs.aws.amazon.com/securityhub/latest/userguide/rds-controls.html#rds-19](https://docs.aws.amazon.com/securityhub/latest/userguide/rds-controls.html#rds-19)

## 参考资料

- [https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_Events.html](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_Events.html)
- [https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_Events.Subscribing.html](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_Events.Subscribing.html)

## 技术信息

- Source Metadata：[sources/aws/rds_cluster_critical_event_subscription/metadata.json](../../sources/aws/rds_cluster_critical_event_subscription/metadata.json)
- Source Code：[sources/aws/rds_cluster_critical_event_subscription/check.py](../../sources/aws/rds_cluster_critical_event_subscription/check.py)
- Source Metadata Path：`sources/aws/rds_cluster_critical_event_subscription/metadata.json`
- Source Code Path：`sources/aws/rds_cluster_critical_event_subscription/check.py`
