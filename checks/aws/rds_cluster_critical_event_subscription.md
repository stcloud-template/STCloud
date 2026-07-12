# Check if RDS Cluster critical events are subscribed.

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `rds_cluster_critical_event_subscription` |
| クラウドプラットフォーム | AWS |
| サービス | rds |
| 重大度 | low |
| カテゴリ | Uncategorized |
| チェックタイプ | Software and Configuration Checks, AWS Security Best Practices |
| リソースタイプ | AwsAccount |
| リソースグループ | governance |

## 説明

Ensure that Amazon RDS event notification subscriptions are enabled for database cluster events, particularly maintenance and failure.

## リスク

Without event subscriptions for critical events, such as maintenance and failures, you may not be aware of issues affecting your RDS clusters, leading to downtime or security vulnerabilities.

## 推奨事項

To subscribe to RDS cluster event notifications, see Subscribing to Amazon RDS event notification in the Amazon RDS User Guide.

- 推奨リンク：[https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_Events.Subscribing.html](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_Events.Subscribing.html)

## 修正手順


### CLI

```text
aws rds create-event-subscription --source-type db-cluster --event-categories 'failure' 'maintenance' --sns-topic-arn <sns-topic-arn>
```

### Other

[https://docs.aws.amazon.com/securityhub/latest/userguide/rds-controls.html#rds-19](https://docs.aws.amazon.com/securityhub/latest/userguide/rds-controls.html#rds-19)

## 参考資料

- [https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_Events.html](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_Events.html)
- [https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_Events.Subscribing.html](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_Events.Subscribing.html)

## 技術情報

- Source Metadata：[sources/aws/rds_cluster_critical_event_subscription/metadata.json](../../sources/aws/rds_cluster_critical_event_subscription/metadata.json)
- Source Code：[sources/aws/rds_cluster_critical_event_subscription/check.py](../../sources/aws/rds_cluster_critical_event_subscription/check.py)
- Source Metadata Path：`sources/aws/rds_cluster_critical_event_subscription/metadata.json`
- Source Code Path：`sources/aws/rds_cluster_critical_event_subscription/check.py`
