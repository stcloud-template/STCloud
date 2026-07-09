# Account has a CloudWatch log metric filter and alarm for disabling or scheduled deletion of customer-managed KMS keys

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `cloudwatch_log_metric_filter_disable_or_scheduled_deletion_of_kms_cmk` |
| 云平台 | AWS |
| 服务 | cloudwatch |
| 严重等级 | medium |
| 类别 | logging |
| 检查类型 | Software and Configuration Checks/Industry and Regulatory Standards/CIS AWS Foundations Benchmark, Software and Configuration Checks/AWS Security Best Practices, Effects/Denial of Service |
| 资源类型 | AwsCloudWatchAlarm |
| 资源组 | monitoring |

## 描述

CloudTrail events delivered to CloudWatch are evaluated for a **metric filter and alarm** that monitor **KMS CMK state changes**, specifically `DisableKey` and `ScheduleKeyDeletion` from `kms.amazonaws.com`.

## 风险

Missing alerts on **CMK disablement or scheduled deletion** undermines **availability** and **integrity**: encrypted data may become undecryptable, backups unusable, and recovery impossible. Attackers or insiders can change key states unnoticed, causing outages and irreversible data loss.

## 推荐措施

Establish **CloudWatch metric filters and alarms** for `DisableKey` and `ScheduleKeyDeletion` CloudTrail events to enable rapid response. - Apply **least privilege** to KMS administration - Enforce **change control** and separation of duties - Use deletion waiting periods and monitor all regions

## 修复步骤


### Native IaC

```yaml
# CloudFormation: Metric filter and alarm for KMS key disable/deletion
Resources:
  MetricFilter:
    Type: AWS::Logs::MetricFilter
    Properties:
      LogGroupName: <example_resource_name>
      # CRITICAL: Detect KMS DisableKey or ScheduleKeyDeletion events from CloudTrail logs
      # This pattern is what the check looks for
      FilterPattern: '{($.eventSource = kms.amazonaws.com) && (($.eventName=DisableKey)||($.eventName=ScheduleKeyDeletion)) }'
      MetricTransformations:
        - MetricValue: "1"
          MetricNamespace: CISBenchmark
          MetricName: disable_or_delete_cmk_changes_metric

  Alarm:
    Type: AWS::CloudWatch::Alarm
    Properties:
      # CRITICAL: Alarm on the metric created by the filter above
      MetricName: disable_or_delete_cmk_changes_metric
      Namespace: CISBenchmark
      Statistic: Sum
      Period: 300
      EvaluationPeriods: 1
      Threshold: 1
      ComparisonOperator: GreaterThanOrEqualToThreshold
```

### Terraform

```hcl
# Metric filter for KMS DisableKey or ScheduleKeyDeletion
resource "aws_cloudwatch_log_metric_filter" "cmk" {
  name           = "<example_resource_name>"
  log_group_name = "<example_resource_name>" # CRITICAL: CloudTrail log group
  # CRITICAL: Detect KMS key disable or scheduled deletion events
  pattern = "{($.eventSource = kms.amazonaws.com) && (($.eventName=DisableKey)||($.eventName=ScheduleKeyDeletion)) }"

  metric_transformation {
    name      = "disable_or_delete_cmk_changes_metric" # CRITICAL: metric used by alarm
    namespace = "CISBenchmark"
    value     = "1"
  }
}

# Alarm for the metric above
resource "aws_cloudwatch_metric_alarm" "cmk" {
  alarm_name          = "<example_resource_name>"
  comparison_operator = "GreaterThanOrEqualToThreshold"
  evaluation_periods  = 1
  metric_name         = "disable_or_delete_cmk_changes_metric" # CRITICAL: same metric name
  namespace           = "CISBenchmark"
  period              = 300
  statistic           = "Sum"
  threshold           = 1
}
```

### Other

1. Open the AWS Console and go to CloudWatch > Log groups
2. Select the CloudTrail log group that receives your trail events
3. Choose Create metric filter
4. In Filter pattern, paste: {($.eventSource = kms.amazonaws.com) && (($.eventName=DisableKey)||($.eventName=ScheduleKeyDeletion)) }
5. Name the metric (e.g., disable_or_delete_cmk_changes_metric), set Namespace to CISBenchmark, Value to 1, then Create
6. From the Metric filters tab, select the new filter and click Create alarm
7. Set Statistic: Sum, Period: 5 minutes, Threshold type: Static, Threshold: 1, Comparison: Greater/Equal
8. Create the alarm (notification actions optional and not required for pass)

## 参考资料

- [https://docs.aws.amazon.com/kms/latest/developerguide/deleting-keys-creating-cloudwatch-alarm.html](https://docs.aws.amazon.com/kms/latest/developerguide/deleting-keys-creating-cloudwatch-alarm.html)

## 技术信息

- Source Metadata：[sources/aws/cloudwatch_log_metric_filter_disable_or_scheduled_deletion_of_kms_cmk/metadata.json](../../sources/aws/cloudwatch_log_metric_filter_disable_or_scheduled_deletion_of_kms_cmk/metadata.json)
- Source Code：[sources/aws/cloudwatch_log_metric_filter_disable_or_scheduled_deletion_of_kms_cmk/check.py](../../sources/aws/cloudwatch_log_metric_filter_disable_or_scheduled_deletion_of_kms_cmk/check.py)
- Source Metadata Path：`sources/aws/cloudwatch_log_metric_filter_disable_or_scheduled_deletion_of_kms_cmk/metadata.json`
- Source Code Path：`sources/aws/cloudwatch_log_metric_filter_disable_or_scheduled_deletion_of_kms_cmk/check.py`
