# Check if RDS Parameter Group events are subscribed.

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `rds_instance_event_subscription_parameter_groups` |
| クラウドプラットフォーム | AWS |
| サービス | rds |
| 重大度 | low |
| カテゴリ | Uncategorized |
| リソースタイプ | AwsAccount |
| リソースグループ | governance |

## 説明

Ensure that Amazon RDS event notification subscriptions are enabled for database parameter groups events.

## リスク

Amazon RDS event subscriptions for database parameter groups are designed to provide incident notification of events that may affect the security, availability, and reliability of the RDS database instances associated with these parameter groups.

## 推奨事項

To subscribe to RDS instance event notifications, see Subscribing to Amazon RDS event notification in the Amazon RDS User Guide.

- 推奨リンク：[https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_Events.Subscribing.html](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_Events.Subscribing.html)

## 修正手順


### CLI

```text
aws rds create-event-subscription --source-type db-instance --event-categories 'configuration change' --sns-topic-arn <sns-topic-arn>
```

### Other

[https://docs.aws.amazon.com/securityhub/latest/userguide/rds-controls.html#rds-21](https://docs.aws.amazon.com/securityhub/latest/userguide/rds-controls.html#rds-21)

## 参考資料

- [https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_Events.html](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_Events.html)
- [https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_Events.Subscribing.html](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_Events.Subscribing.html)

## 技術情報

- Source Metadata：[sources/aws/rds_instance_event_subscription_parameter_groups/metadata.json](../../sources/aws/rds_instance_event_subscription_parameter_groups/metadata.json)
- Source Code：[sources/aws/rds_instance_event_subscription_parameter_groups/check.py](../../sources/aws/rds_instance_event_subscription_parameter_groups/check.py)
- Source Metadata Path：`sources/aws/rds_instance_event_subscription_parameter_groups/metadata.json`
- Source Code Path：`sources/aws/rds_instance_event_subscription_parameter_groups/check.py`
