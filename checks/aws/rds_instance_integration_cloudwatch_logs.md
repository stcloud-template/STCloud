# Check if RDS instances is integrated with CloudWatch Logs.

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `rds_instance_integration_cloudwatch_logs` |
| クラウドプラットフォーム | AWS |
| サービス | rds |
| 重大度 | medium |
| カテゴリ | logging |
| リソースタイプ | AwsRdsDbInstance |
| リソースグループ | database |

## 説明

Check if RDS instances is integrated with CloudWatch Logs.

## リスク

If logs are not enabled, monitoring of service use and threat analysis is not possible.

## 推奨事項

Use CloudWatch Logs to perform real-time analysis of the log data. Create alarms and view metrics.

- 推奨リンク：[https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/publishing_cloudwatchlogs.html](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/publishing_cloudwatchlogs.html)

## 修正手順


### CLI

```text
aws rds modify-db-instance --db-instance-identifier <db_instance_id> --cloudwatch-logs-export-configuration {'EnableLogTypes':['audit',error','general','slowquery']} --apply-immediately
```

### Terraform

[https://docs.ST Cloud.com/checks/aws/iam-policies/ensure-that-respective-logs-of-amazon-relational-database-service-amazon-rds-are-enabled#terraform](https://docs.ST Cloud.com/checks/aws/iam-policies/ensure-that-respective-logs-of-amazon-relational-database-service-amazon-rds-are-enabled#terraform)

### Other

[https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/RDS/log-exports.html](https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/RDS/log-exports.html)

## 参考資料

- [https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/publishing_cloudwatchlogs.html](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/publishing_cloudwatchlogs.html)

## 技術情報

- Source Metadata：[sources/aws/rds_instance_integration_cloudwatch_logs/metadata.json](../../sources/aws/rds_instance_integration_cloudwatch_logs/metadata.json)
- Source Code：[sources/aws/rds_instance_integration_cloudwatch_logs/check.py](../../sources/aws/rds_instance_integration_cloudwatch_logs/check.py)
- Source Metadata Path：`sources/aws/rds_instance_integration_cloudwatch_logs/metadata.json`
- Source Code Path：`sources/aws/rds_instance_integration_cloudwatch_logs/check.py`
