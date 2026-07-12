# CloudWatch Logs metric filter and alarm exist for IAM policy changes

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `cloudwatch_log_metric_filter_policy_changes` |
| クラウドプラットフォーム | AWS |
| サービス | cloudwatch |
| 重大度 | medium |
| カテゴリ | logging |
| チェックタイプ | Software and Configuration Checks/Industry and Regulatory Standards/CIS AWS Foundations Benchmark, TTPs/Privilege Escalation |
| リソースタイプ | AwsCloudWatchAlarm |
| リソースグループ | monitoring |

## 説明

CloudWatch uses a metric filter and alarm to track **IAM policy changes** recorded by CloudTrail (e.g., `CreatePolicy`, `DeletePolicy`, version changes, inline policy edits, policy attach/detach). This finding reflects whether that filter and an associated alarm are present on the trail's log group.

## リスク

Absent alerting on **IAM policy changes**, privilege modifications can go unnoticed, enabling **privilege escalation**, hidden backdoors, or permission revocations. This threatens **confidentiality** and **integrity**, and may impact **availability** if critical access is removed or misconfigured.

## 推奨事項

Create a metric filter for IAM policy create/update/delete and attach/detach events with an **alarm** to notify responders. - Enforce **least privilege** and separation of duties for policy changes - Require approvals and central logging across Regions/accounts - Integrate alerts with incident response

## 修正手順


### Native IaC

```yaml
# CloudFormation: Create metric filter and alarm for IAM policy changes
Resources:
  IAMPolicyChangeMetricFilter:
    Type: AWS::Logs::MetricFilter
    Properties:
      LogGroupName: <example_resource_name>  # IMPORTANT: CloudTrail log group to monitor
      # CRITICAL: Pattern matching IAM policy change events required by the check
      FilterPattern: '{($.eventName=DeleteGroupPolicy)||($.eventName=DeleteRolePolicy)||($.eventName=DeleteUserPolicy)||($.eventName=PutGroupPolicy)||($.eventName=PutRolePolicy)||($.eventName=PutUserPolicy)||($.eventName=CreatePolicy)||($.eventName=DeletePolicy)||($.eventName=CreatePolicyVersion)||($.eventName=DeletePolicyVersion)||($.eventName=AttachRolePolicy)||($.eventName=DetachRolePolicy)||($.eventName=AttachUserPolicy)||($.eventName=DetachUserPolicy)||($.eventName=AttachGroupPolicy)||($.eventName=DetachGroupPolicy)}'
      MetricTransformations:
        - MetricName: <example_resource_name>   # CRITICAL: Metric created from filter
          MetricNamespace: CISBenchmark        # CRITICAL: Namespace for the metric
          MetricValue: "1"

  IAMPolicyChangeAlarm:
    Type: AWS::CloudWatch::Alarm
    Properties:
      AlarmName: <example_resource_name>
      # CRITICAL: Alarm on the metric created above when >= 1 event occurs
      MetricName: <example_resource_name>
      Namespace: CISBenchmark
      Statistic: Sum
      Period: 300
      EvaluationPeriods: 1
      Threshold: 1
      ComparisonOperator: GreaterThanOrEqualToThreshold
```

### Terraform

```hcl
# Terraform: Metric filter and alarm for IAM policy changes
resource "aws_cloudwatch_log_metric_filter" "<example_resource_name>" {
  name           = "<example_resource_name>"
  log_group_name = "<example_resource_name>"  # CloudTrail log group

  # CRITICAL: Pattern matching IAM policy change events required by the check
  pattern = "{($.eventName=DeleteGroupPolicy)||($.eventName=DeleteRolePolicy)||($.eventName=DeleteUserPolicy)||($.eventName=PutGroupPolicy)||($.eventName=PutRolePolicy)||($.eventName=PutUserPolicy)||($.eventName=CreatePolicy)||($.eventName=DeletePolicy)||($.eventName=CreatePolicyVersion)||($.eventName=DeletePolicyVersion)||($.eventName=AttachRolePolicy)||($.eventName=DetachRolePolicy)||($.eventName=AttachUserPolicy)||($.eventName=DetachUserPolicy)||($.eventName=AttachGroupPolicy)||($.eventName=DetachGroupPolicy)}"

  metric_transformation {
    name      = "<example_resource_name>"      # CRITICAL: Metric created from filter
    namespace = "CISBenchmark"                 # CRITICAL: Namespace for the metric
    value     = "1"
  }
}

resource "aws_cloudwatch_metric_alarm" "<example_resource_name>" {
  alarm_name          = "<example_resource_name>"
  # CRITICAL: Alarm on the metric when >= 1 event occurs
  metric_name         = aws_cloudwatch_log_metric_filter.<example_resource_name>.metric_transformation[0].name
  namespace           = aws_cloudwatch_log_metric_filter.<example_resource_name>.metric_transformation[0].namespace
  statistic           = "Sum"
  period              = 300
  evaluation_periods  = 1
  threshold           = 1
  comparison_operator = "GreaterThanOrEqualToThreshold"
}
```

### Other

1. Open the CloudWatch console > Logs > Log groups and select the CloudTrail log group
2. Create metric filter:
   - Filter pattern: {($.eventName=DeleteGroupPolicy)||($.eventName=DeleteRolePolicy)||($.eventName=DeleteUserPolicy)||($.eventName=PutGroupPolicy)||($.eventName=PutRolePolicy)||($.eventName=PutUserPolicy)||($.eventName=CreatePolicy)||($.eventName=DeletePolicy)||($.eventName=CreatePolicyVersion)||($.eventName=DeletePolicyVersion)||($.eventName=AttachRolePolicy)||($.eventName=DetachRolePolicy)||($.eventName=AttachUserPolicy)||($.eventName=DetachUserPolicy)||($.eventName=AttachGroupPolicy)||($.eventName=DetachGroupPolicy)}
   - Metric name: <example_resource_name>
   - Namespace: CISBenchmark
   - Metric value: 1
3. On the Metric filters tab, select the new filter and choose Create alarm
4. Set: Statistic=Sum, Period=5 minutes, Threshold type=Static, Greater/Equal, Threshold=1, Evaluation periods=1
5. Create the alarm

## 参考資料

- [https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudwatch-alarms-for-cloudtrail.html](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudwatch-alarms-for-cloudtrail.html)
- [https://www.clouddefense.ai/compliance-rules/cis-v140/monitoring/cis-v140-4-4](https://www.clouddefense.ai/compliance-rules/cis-v140/monitoring/cis-v140-4-4)
- [https://www.intelligentdiscovery.io/controls/cloudwatch/cloudwatch-alarm-iam-policy-change](https://www.intelligentdiscovery.io/controls/cloudwatch/cloudwatch-alarm-iam-policy-change)

## 技術情報

- Source Metadata：[sources/aws/cloudwatch_log_metric_filter_policy_changes/metadata.json](../../sources/aws/cloudwatch_log_metric_filter_policy_changes/metadata.json)
- Source Code：[sources/aws/cloudwatch_log_metric_filter_policy_changes/check.py](../../sources/aws/cloudwatch_log_metric_filter_policy_changes/check.py)
- Source Metadata Path：`sources/aws/cloudwatch_log_metric_filter_policy_changes/metadata.json`
- Source Code Path：`sources/aws/cloudwatch_log_metric_filter_policy_changes/check.py`
