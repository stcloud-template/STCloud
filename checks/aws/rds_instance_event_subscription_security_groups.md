# Check if RDS Security Group events are subscribed.

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `rds_instance_event_subscription_security_groups` |
| クラウドプラットフォーム | AWS |
| サービス | rds |
| 重大度 | medium |
| カテゴリ | Uncategorized |
| リソースタイプ | AwsRdsEventSubscription |
| リソースグループ | database |

## 説明

Ensure that Amazon RDS event notification subscriptions are enabled for database security groups events.

## リスク

Amazon RDS event subscriptions for database security groups are designed to provide incident notification of events that may affect the security, availability, and reliability of the RDS database instances associated with these security groups.

## 推奨事項

To subscribe to RDS instance event notifications, see Subscribing to Amazon RDS event notification in the Amazon RDS User Guide.

- 推奨リンク：[https://docs.aws.amazon.com/securityhub/latest/userguide/rds-controls.html#rds-22](https://docs.aws.amazon.com/securityhub/latest/userguide/rds-controls.html#rds-22)

## 修正手順


### Native IaC

[https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/RDS/rds-db-security-groups-events.html#](https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/RDS/rds-db-security-groups-events.html#)

### Terraform

[https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/RDS/rds-db-security-groups-events.html#](https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/RDS/rds-db-security-groups-events.html#)

### Other

[https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/RDS/rds-db-security-groups-events.html#](https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/RDS/rds-db-security-groups-events.html#)

## 参考資料

- [https://docs.aws.amazon.com/securityhub/latest/userguide/rds-controls.html#rds-22](https://docs.aws.amazon.com/securityhub/latest/userguide/rds-controls.html#rds-22)

## 技術情報

- Source Metadata：[sources/aws/rds_instance_event_subscription_security_groups/metadata.json](../../sources/aws/rds_instance_event_subscription_security_groups/metadata.json)
- Source Code：[sources/aws/rds_instance_event_subscription_security_groups/check.py](../../sources/aws/rds_instance_event_subscription_security_groups/check.py)
- Source Metadata Path：`sources/aws/rds_instance_event_subscription_security_groups/metadata.json`
- Source Code Path：`sources/aws/rds_instance_event_subscription_security_groups/check.py`
