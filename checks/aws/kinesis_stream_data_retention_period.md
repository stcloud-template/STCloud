# Kinesis stream retains data for at least the required minimum hours

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `kinesis_stream_data_retention_period` |
| クラウドプラットフォーム | AWS |
| サービス | kinesis |
| 重大度 | medium |
| カテゴリ | resilience |
| チェックタイプ | Software and Configuration Checks/AWS Security Best Practices, Software and Configuration Checks/Industry and Regulatory Standards/AWS Foundational Security Best Practices, Effects/Data Destruction |
| リソースタイプ | AwsKinesisStream |
| リソースグループ | messaging |

## 説明

**Kinesis Data Streams** retention window is evaluated to confirm records are kept for at least the configured minimum duration (default `168` hours).

## リスク

Insufficient retention causes records to expire before consumers read or reprocess them, undermining **availability** and analytics **integrity**. Backlogs or outages can create irreversible data gaps, hinder investigations and recovery, and enable denial-of-service-by-lag against event pipelines.

## 推奨事項

Set the **retention period** to exceed worst-case consumer lag, replay needs, and compliance windows; use at least `168` hours by default (or customize as necessary) and raise as required. Enforce **change control** and least privilege on retention changes, monitor consumer lag, and maintain **secondary durability** (e.g., archival) for critical streams.

## 修正手順


### CLI

```text
aws kinesis increase-stream-retention-period --stream-name <example_resource_name> --retention-period-hours 168
```

### Native IaC

```yaml
# CloudFormation: set Kinesis stream retention to minimum required hours
Resources:
  <example_resource_name>:
    Type: AWS::Kinesis::Stream
    Properties:
      ShardCount: 1
      RetentionPeriodHours: 168  # critical: sets retention to >= 168 hours to pass the check
```

### Terraform

```hcl
# Kinesis stream with adequate retention period
resource "aws_kinesis_stream" "<example_resource_name>" {
  name             = "<example_resource_name>"
  shard_count      = 1
  retention_period = 168  # critical: sets retention to >= 168 hours to pass the check
}
```

### Other

1. Sign in to the AWS Console and open Amazon Kinesis
2. Go to Data streams and select <example_resource_name>
3. Click Edit
4. Set Retention period to 168 hours (or higher, per your policy)
5. Click Save changes

## 参考資料

- [https://docs.aws.amazon.com/streams/latest/dev/kinesis-extended-retention.html](https://docs.aws.amazon.com/streams/latest/dev/kinesis-extended-retention.html)
- [https://docs.aws.amazon.com/securityhub/latest/userguide/kinesis-controls.html#kinesis-3](https://docs.aws.amazon.com/securityhub/latest/userguide/kinesis-controls.html#kinesis-3)

## 技術情報

- Source Metadata：[sources/aws/kinesis_stream_data_retention_period/metadata.json](../../sources/aws/kinesis_stream_data_retention_period/metadata.json)
- Source Code：[sources/aws/kinesis_stream_data_retention_period/check.py](../../sources/aws/kinesis_stream_data_retention_period/check.py)
- Source Metadata Path：`sources/aws/kinesis_stream_data_retention_period/metadata.json`
- Source Code Path：`sources/aws/kinesis_stream_data_retention_period/check.py`
