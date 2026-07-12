# Check if RDS cluster is integrated with CloudWatch Logs.

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `rds_cluster_integration_cloudwatch_logs` |
| クラウドプラットフォーム | AWS |
| サービス | rds |
| 重大度 | medium |
| カテゴリ | logging |
| リソースタイプ | AwsRdsDbCluster |
| リソースグループ | database |

## 説明

Check if RDS cluster is integrated with CloudWatch Logs. The types valid are Aurora MySQL, Aurora PostgreSQL, MySQL, PostgreSQL.

## リスク

If logs are not enabled, monitoring of service use and threat analysis is not possible.

## 推奨事項

Use CloudWatch Logs to perform real-time analysis of the log data. Create alarms and view metrics.

- 推奨リンク：[https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/publishing_cloudwatchlogs.html](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/publishing_cloudwatchlogs.html)

## 修正手順


### CLI

```text
aws rds modify-db-cluster --db-cluster-identifier <db_cluster_id> --cloudwatch-logs-export-configuration {'EnableLogTypes':['audit',error','general','slowquery']} --apply-immediately
```

### Other

[https://docs.aws.amazon.com/securityhub/latest/userguide/rds-controls.html#rds-34](https://docs.aws.amazon.com/securityhub/latest/userguide/rds-controls.html#rds-34)

## 参考資料

- [https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_LogAccess.html](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_LogAccess.html)
- [https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/publishing_cloudwatchlogs.html](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/publishing_cloudwatchlogs.html)

## 技術情報

- Source Metadata：[sources/aws/rds_cluster_integration_cloudwatch_logs/metadata.json](../../sources/aws/rds_cluster_integration_cloudwatch_logs/metadata.json)
- Source Code：[sources/aws/rds_cluster_integration_cloudwatch_logs/check.py](../../sources/aws/rds_cluster_integration_cloudwatch_logs/check.py)
- Source Metadata Path：`sources/aws/rds_cluster_integration_cloudwatch_logs/metadata.json`
- Source Code Path：`sources/aws/rds_cluster_integration_cloudwatch_logs/check.py`
