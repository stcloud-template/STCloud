# CloudTrail trail has delivered logs to CloudWatch Logs in the last 24 hours

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `cloudtrail_cloudwatch_logging_enabled` |
| クラウドプラットフォーム | AWS |
| サービス | cloudtrail |
| 重大度 | low |
| カテゴリ | logging, forensics-ready |
| チェックタイプ | Software and Configuration Checks/AWS Security Best Practices, Software and Configuration Checks/Industry and Regulatory Standards/AWS Foundational Security Best Practices, Software and Configuration Checks/Industry and Regulatory Standards/CIS AWS Foundations Benchmark |
| リソースタイプ | AwsCloudTrailTrail |
| リソースグループ | monitoring |

## 説明

**CloudTrail trails** are configured to send events to **CloudWatch Logs**, and show recent delivery within the last `24h`. Trails without integration or without recent CloudWatch delivery are identified, across single-Region and multi-Region trails.

## リスク

Missing or stale CloudWatch delivery weakens visibility and delays detection, impacting confidentiality and integrity. Adversaries can: - Hide **privilege escalation** - Perform unauthorized **resource changes** - Exfiltrate data via API misuse

## 推奨事項

Integrate every trail with **CloudWatch Logs** and maintain continuous, near-real-time delivery. Enforce **least privilege** on the delivery role, prefer **multi-Region** coverage, and implement **metric filters and alerts** for sensitive actions. Centralize retention to support **defense in depth**.

## 修正手順


### CLI

```text
aws cloudtrail update-trail --name <trail_name> --cloud-watch-logs-log-group-arn <cloudwatch_log_group_arn> --cloud-watch-logs-role-arn <cloudwatch_logs_role_arn>
```

### Native IaC

```yaml
# CloudFormation: enable CloudTrail delivery to CloudWatch Logs
Resources:
  <example_resource_name>:
    Type: AWS::CloudTrail::Trail
    Properties:
      S3BucketName: "<example_resource_name>"
      CloudWatchLogsLogGroupArn: "<cloudwatch_log_group_arn>"  # CRITICAL: sends CloudTrail events to CloudWatch Logs
      CloudWatchLogsRoleArn: "<cloudwatch_logs_role_arn>"      # CRITICAL: role CloudTrail assumes to deliver events
```

### Terraform

```hcl
# Terraform: enable CloudTrail delivery to CloudWatch Logs
resource "aws_cloudtrail" "<example_resource_name>" {
  name                       = "<example_resource_name>"
  s3_bucket_name             = "<example_resource_name>"
  cloud_watch_logs_group_arn = "<cloudwatch_log_group_arn>"  # CRITICAL: sends CloudTrail events to CloudWatch Logs
  cloud_watch_logs_role_arn  = "<cloudwatch_logs_role_arn>"   # CRITICAL: role CloudTrail assumes to deliver events
}
```

### Other

1. In AWS Console, go to CloudTrail > Trails and select the trail
2. In the CloudWatch Logs section, click Edit
3. Set CloudWatch Logs to Enabled
4. Choose an existing Log group (or create new) and select an IAM role with permissions for CreateLogStream/PutLogEvents
5. Click Save changes
6. After a few minutes, verify events appear in the chosen CloudWatch Logs log group

## 参考資料

- [https://docs.aws.amazon.com/awscloudtrail/latest/userguide/send-cloudtrail-events-to-cloudwatch-logs.html](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/send-cloudtrail-events-to-cloudwatch-logs.html)

## 技術情報

- Source Metadata：[sources/aws/cloudtrail_cloudwatch_logging_enabled/metadata.json](../../sources/aws/cloudtrail_cloudwatch_logging_enabled/metadata.json)
- Source Code：[sources/aws/cloudtrail_cloudwatch_logging_enabled/check.py](../../sources/aws/cloudtrail_cloudwatch_logging_enabled/check.py)
- Source Metadata Path：`sources/aws/cloudtrail_cloudwatch_logging_enabled/metadata.json`
- Source Code Path：`sources/aws/cloudtrail_cloudwatch_logging_enabled/check.py`
