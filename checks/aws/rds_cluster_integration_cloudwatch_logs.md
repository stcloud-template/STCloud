# Check if RDS cluster is integrated with CloudWatch Logs.

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `rds_cluster_integration_cloudwatch_logs` |
| 云平台 | AWS |
| 服务 | rds |
| 严重等级 | medium |
| 类别 | logging |
| 资源类型 | AwsRdsDbCluster |
| 资源组 | database |

## 描述

Check if RDS cluster is integrated with CloudWatch Logs. The types valid are Aurora MySQL, Aurora PostgreSQL, MySQL, PostgreSQL.

## 风险

If logs are not enabled, monitoring of service use and threat analysis is not possible.

## 推荐措施

Use CloudWatch Logs to perform real-time analysis of the log data. Create alarms and view metrics.

- 推荐链接：[https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/publishing_cloudwatchlogs.html](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/publishing_cloudwatchlogs.html)

## 修复步骤


### CLI

```text
aws rds modify-db-cluster --db-cluster-identifier <db_cluster_id> --cloudwatch-logs-export-configuration {'EnableLogTypes':['audit',error','general','slowquery']} --apply-immediately
```

### Other

[https://docs.aws.amazon.com/securityhub/latest/userguide/rds-controls.html#rds-34](https://docs.aws.amazon.com/securityhub/latest/userguide/rds-controls.html#rds-34)

## 参考资料

- [https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_LogAccess.html](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_LogAccess.html)
- [https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/publishing_cloudwatchlogs.html](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/publishing_cloudwatchlogs.html)

## 技术信息

- Source Metadata：[sources/aws/rds_cluster_integration_cloudwatch_logs/metadata.json](../../sources/aws/rds_cluster_integration_cloudwatch_logs/metadata.json)
- Source Code：[sources/aws/rds_cluster_integration_cloudwatch_logs/check.py](../../sources/aws/rds_cluster_integration_cloudwatch_logs/check.py)
- Source Metadata Path：`sources/aws/rds_cluster_integration_cloudwatch_logs/metadata.json`
- Source Code Path：`sources/aws/rds_cluster_integration_cloudwatch_logs/check.py`
