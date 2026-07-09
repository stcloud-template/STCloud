# CloudWatch Logs metric filter and alarm exist for security group changes

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `cloudwatch_log_metric_filter_security_group_changes` |
| 云平台 | AWS |
| 服务 | cloudwatch |
| 严重等级 | medium |
| 类别 | logging |
| 检查类型 | Software and Configuration Checks/Industry and Regulatory Standards/CIS AWS Foundations Benchmark, Software and Configuration Checks/AWS Security Best Practices/Runtime Behavior Analysis |
| 资源类型 | AwsCloudWatchAlarm |
| 资源组 | monitoring |

## 描述

**CloudTrail** events for **security group configuration changes** are monitored using a **CloudWatch Logs metric filter** with an associated **alarm**. The filter targets actions like `AuthorizeSecurityGroupIngress/Egress`, `RevokeSecurityGroupIngress/Egress`, `CreateSecurityGroup`, and `DeleteSecurityGroup` to surface any security group modifications.

## 风险

Without alerting on **security group changes**, unauthorized or mistaken rules can expose services to the Internet, enabling brute force and lateral movement (**confidentiality, integrity**). Deletions or restrictive edits can break connectivity (**availability**). Delayed detection increases attacker dwell time and impact.

## 推荐措施

Establish real-time alerts for **security group modifications** by sending CloudTrail to CloudWatch, creating metric filters and alarms, and notifying responders. - Enforce **least privilege** on SG changes - Use change management and tagging - Centralize logs, test alarms, and maintain runbooks - Layer with NACLs and WAF for **defense in depth**

## 修复步骤


### Native IaC

```yaml
# CloudFormation: Create metric filter and alarm for Security Group changes
Resources:
  MetricFilter:
    Type: AWS::Logs::MetricFilter
    Properties:
      LogGroupName: <example_log_group_name>
      # Critical: Matches Security Group change events required by the check
      # This publishes a metric when these events appear in CloudTrail logs
      FilterPattern: '{ ($.eventName = AuthorizeSecurityGroupIngress) || ($.eventName = AuthorizeSecurityGroupEgress) || ($.eventName = RevokeSecurityGroupIngress) || ($.eventName = RevokeSecurityGroupEgress) || ($.eventName = CreateSecurityGroup) || ($.eventName = DeleteSecurityGroup) }'
      MetricTransformations:
        - MetricName: <example_metric_name>
          MetricNamespace: <example_metric_namespace>
          MetricValue: "1"

  Alarm:
    Type: AWS::CloudWatch::Alarm
    Properties:
      # Critical: Alarm on the metric to satisfy the requirement
      MetricName: <example_metric_name>
      Namespace: <example_metric_namespace>
      Statistic: Sum
      Period: 300
      EvaluationPeriods: 1
      Threshold: 1
      ComparisonOperator: GreaterThanOrEqualToThreshold
```

### Terraform

```hcl
# Metric filter for Security Group changes
resource "aws_cloudwatch_log_metric_filter" "sg" {
  name           = "<example_resource_name>"
  log_group_name = "<example_log_group_name>"
  # Critical: Matches Security Group change events required by the check
  pattern = "{ ($.eventName = AuthorizeSecurityGroupIngress) || ($.eventName = AuthorizeSecurityGroupEgress) || ($.eventName = RevokeSecurityGroupIngress) || ($.eventName = RevokeSecurityGroupEgress) || ($.eventName = CreateSecurityGroup) || ($.eventName = DeleteSecurityGroup) }"

  metric_transformation {
    name      = "<example_metric_name>"
    namespace = "<example_metric_namespace>"
    value     = "1"
  }
}

# Alarm for the above metric
resource "aws_cloudwatch_metric_alarm" "sg" {
  alarm_name          = "<example_resource_name>"
  # Critical: Alarm on the SG change metric to pass the control
  metric_name         = "<example_metric_name>"
  namespace           = "<example_metric_namespace>"
  statistic           = "Sum"
  period              = 300
  evaluation_periods  = 1
  threshold           = 1
  comparison_operator = "GreaterThanOrEqualToThreshold"
}
```

### Other

1. Open the CloudWatch console > Logs > Log groups, and select the CloudTrail log group
2. Create metric filter with this pattern:
   { ($.eventName = AuthorizeSecurityGroupIngress) || ($.eventName = AuthorizeSecurityGroupEgress) || ($.eventName = RevokeSecurityGroupIngress) || ($.eventName = RevokeSecurityGroupEgress) || ($.eventName = CreateSecurityGroup) || ($.eventName = DeleteSecurityGroup) }
3. Assign metric: name <example_metric_name>, namespace <example_metric_namespace>, value 1, then create the filter
4. From the metric filter, choose Create alarm and set: Statistic Sum, Period 5 minutes, Threshold type Static, Greater/Equal 1, Evaluation periods 1, then create the alarm

## 参考资料

- [https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudwatch-alarms-for-cloudtrail.html](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudwatch-alarms-for-cloudtrail.html)
- [https://support.icompaas.com/support/solutions/articles/62000084030-ensure-a-log-metric-filter-and-alarm-exist-for-security-group-changes](https://support.icompaas.com/support/solutions/articles/62000084030-ensure-a-log-metric-filter-and-alarm-exist-for-security-group-changes)
- [https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Alarm-On-Logs.html](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Alarm-On-Logs.html)
- [https://asecure.cloud/a/cwalarm_securitygroup_changes/](https://asecure.cloud/a/cwalarm_securitygroup_changes/)

## 技术信息

- Source Metadata：[sources/aws/cloudwatch_log_metric_filter_security_group_changes/metadata.json](../../sources/aws/cloudwatch_log_metric_filter_security_group_changes/metadata.json)
- Source Code：[sources/aws/cloudwatch_log_metric_filter_security_group_changes/check.py](../../sources/aws/cloudwatch_log_metric_filter_security_group_changes/check.py)
- Source Metadata Path：`sources/aws/cloudwatch_log_metric_filter_security_group_changes/metadata.json`
- Source Code Path：`sources/aws/cloudwatch_log_metric_filter_security_group_changes/check.py`
