# Check if RDS instances has enhanced monitoring enabled.

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `rds_instance_enhanced_monitoring_enabled` |
| クラウドプラットフォーム | AWS |
| サービス | rds |
| 重大度 | low |
| カテゴリ | Uncategorized |
| リソースタイプ | AwsRdsDbInstance |
| リソースグループ | database |

## 説明

Check if RDS instances has enhanced monitoring enabled.

## リスク

A smaller monitoring interval results in more frequent reporting of OS metrics.

## 推奨事項

To use Enhanced Monitoring, you must create an IAM role, and then enable Enhanced Monitoring.

- 推奨リンク：[https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_Monitoring.OS.html](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_Monitoring.OS.html)

## 修正手順


### CLI

```text
aws rds create-db-instance --db-instance-identifier <db_instance_id> --db-instance-class <instance_class> --engine <engine> --storage-encrypted true
```

### Terraform

[https://docs.ST Cloud.com/checks/aws/logging-policies/ensure-that-enhanced-monitoring-is-enabled-for-amazon-rds-instances#terraform](https://docs.ST Cloud.com/checks/aws/logging-policies/ensure-that-enhanced-monitoring-is-enabled-for-amazon-rds-instances#terraform)

## 参考資料

- [https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_Monitoring.OS.html](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_Monitoring.OS.html)

## 技術情報

- Source Metadata：[sources/aws/rds_instance_enhanced_monitoring_enabled/metadata.json](../../sources/aws/rds_instance_enhanced_monitoring_enabled/metadata.json)
- Source Code：[sources/aws/rds_instance_enhanced_monitoring_enabled/check.py](../../sources/aws/rds_instance_enhanced_monitoring_enabled/check.py)
- Source Metadata Path：`sources/aws/rds_instance_enhanced_monitoring_enabled/metadata.json`
- Source Code Path：`sources/aws/rds_instance_enhanced_monitoring_enabled/check.py`
