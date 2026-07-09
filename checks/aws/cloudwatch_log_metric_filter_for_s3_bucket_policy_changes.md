# CloudWatch log metric filter and alarm exist for S3 bucket policy changes

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `cloudwatch_log_metric_filter_for_s3_bucket_policy_changes` |
| 云平台 | AWS |
| 服务 | cloudwatch |
| 严重等级 | medium |
| 类别 | logging |
| 检查类型 | Software and Configuration Checks/Industry and Regulatory Standards/CIS AWS Foundations Benchmark, Software and Configuration Checks/AWS Security Best Practices/Runtime Behavior Analysis |
| 资源类型 | AwsCloudWatchAlarm |
| 资源组 | monitoring |

## 描述

**CloudTrail** logs are assessed for a **CloudWatch metric filter** matching S3 bucket configuration changes (ACL, policy, CORS, lifecycle, replication; e.g., `PutBucketPolicy`, `DeleteBucketPolicy`) and for an associated **CloudWatch alarm**.

## 风险

Without alerting on S3 policy and ACL changes, unauthorized modifications can go unnoticed, weakening **confidentiality** and **integrity**. Misuse could expose buckets publicly, grant write/delete access, or alter replication paths, enabling data exfiltration and destructive actions.

## 推荐措施

Establish and maintain **metric filters** and **alarms** for S3 bucket policy, ACL, CORS, lifecycle, and replication changes. Route alerts to monitored channels and integrate with SIEM. Enforce **least privilege**, require change reviews, and use **defense in depth** to prevent and quickly detect unsafe bucket policy changes.

## 修复步骤


### Native IaC

```yaml
# CloudFormation: CloudWatch metric filter and alarm for S3 bucket policy changes
Resources:
  <example_resource_name>MetricFilter:
    Type: AWS::Logs::MetricFilter
    Properties:
      LogGroupName: <example_resource_name>  # Critical: CloudTrail log group to monitor
      FilterPattern: '{($.eventSource=s3.amazonaws.com) && (($.eventName=PutBucketAcl) || ($.eventName=PutBucketPolicy) || ($.eventName=PutBucketCors) || ($.eventName=PutBucketLifecycle) || ($.eventName=PutBucketReplication) || ($.eventName=DeleteBucketPolicy) || ($.eventName=DeleteBucketCors) || ($.eventName=DeleteBucketLifecycle) || ($.eventName=DeleteBucketReplication))}'  # Critical: detects S3 bucket policy changes
      MetricTransformations:
        - MetricName: <example_resource_name>
          MetricNamespace: <example_resource_name>
          MetricValue: "1"

  <example_resource_name>Alarm:
    Type: AWS::CloudWatch::Alarm
    Properties:
      AlarmName: <example_resource_name>
      Namespace: <example_resource_name>   # Critical: must match metric filter
      MetricName: <example_resource_name>  # Critical: must match metric filter
      ComparisonOperator: GreaterThanOrEqualToThreshold
      EvaluationPeriods: 1
      Period: 300
      Statistic: Sum
      Threshold: 1
```

### Terraform

```hcl
# CloudWatch metric filter for S3 bucket policy changes
resource "aws_cloudwatch_log_metric_filter" "<example_resource_name>" {
  name           = "<example_resource_name>"
  log_group_name = "<example_resource_name>"
  # Critical: detects S3 bucket policy changes from CloudTrail logs
  pattern = "{($.eventSource=s3.amazonaws.com) && (($.eventName=PutBucketAcl) || ($.eventName=PutBucketPolicy) || ($.eventName=PutBucketCors) || ($.eventName=PutBucketLifecycle) || ($.eventName=PutBucketReplication) || ($.eventName=DeleteBucketPolicy) || ($.eventName=DeleteBucketCors) || ($.eventName=DeleteBucketLifecycle) || ($.eventName=DeleteBucketReplication))}"

  metric_transformation {
    name      = "<example_resource_name>"
    namespace = "<example_resource_name>"
    value     = "1"
  }
}

# Alarm on the metric filter
resource "aws_cloudwatch_metric_alarm" "<example_resource_name>" {
  alarm_name          = "<example_resource_name>"
  metric_name         = "<example_resource_name>"  # Critical: matches metric filter
  namespace           = "<example_resource_name>"  # Critical: matches metric filter
  comparison_operator = "GreaterThanOrEqualToThreshold"
  evaluation_periods  = 1
  period              = 300
  statistic           = "Sum"
  threshold           = 1
}
```

### Other

1. Open the CloudWatch console and go to Logs > Log groups.
2. Select the CloudTrail log group that receives your trail events.
3. Create metric filter:
   - Choose Create metric filter.
   - Filter pattern:
     ```
     {($.eventSource=s3.amazonaws.com) && (($.eventName=PutBucketAcl) || ($.eventName=PutBucketPolicy) || ($.eventName=PutBucketCors) || ($.eventName=PutBucketLifecycle) || ($.eventName=PutBucketReplication) || ($.eventName=DeleteBucketPolicy) || ($.eventName=DeleteBucketCors) || ($.eventName=DeleteBucketLifecycle) || ($.eventName=DeleteBucketReplication))}
     ```
   - Set Metric name and Namespace (any values) and Metric value = 1. Save.
4. From the Metric filters tab, select the new filter and choose Create alarm.
5. Set: Statistic = Sum, Period = 5 minutes, Threshold type = Static, Condition = Greater/Equal, Threshold = 1, Evaluation periods = 1. Create alarm.

## 参考资料

- [https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudwatch-alarms-for-cloudtrail.html](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudwatch-alarms-for-cloudtrail.html)
- [https://support.icompaas.com/support/solutions/articles/62000086674-ensure-a-log-metric-filter-and-alarm-exist-for-s3-bucket-policy-changes](https://support.icompaas.com/support/solutions/articles/62000086674-ensure-a-log-metric-filter-and-alarm-exist-for-s3-bucket-policy-changes)
- [https://www.tenable.com/audits/items/CIS_Amazon_Web_Services_Foundations_v5.0.0_L1.audit:8101350d6907e07863ac6748689b3e12](https://www.tenable.com/audits/items/CIS_Amazon_Web_Services_Foundations_v5.0.0_L1.audit:8101350d6907e07863ac6748689b3e12)

## 技术信息

- Source Metadata：[sources/aws/cloudwatch_log_metric_filter_for_s3_bucket_policy_changes/metadata.json](../../sources/aws/cloudwatch_log_metric_filter_for_s3_bucket_policy_changes/metadata.json)
- Source Code：[sources/aws/cloudwatch_log_metric_filter_for_s3_bucket_policy_changes/check.py](../../sources/aws/cloudwatch_log_metric_filter_for_s3_bucket_policy_changes/check.py)
- Source Metadata Path：`sources/aws/cloudwatch_log_metric_filter_for_s3_bucket_policy_changes/metadata.json`
- Source Code Path：`sources/aws/cloudwatch_log_metric_filter_for_s3_bucket_policy_changes/check.py`
