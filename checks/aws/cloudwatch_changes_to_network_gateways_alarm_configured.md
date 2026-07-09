# CloudWatch Logs metric filter and alarm exist for changes to network gateways

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `cloudwatch_changes_to_network_gateways_alarm_configured` |
| 云平台 | AWS |
| 服务 | cloudwatch |
| 严重等级 | medium |
| 类别 | logging |
| 检查类型 | Software and Configuration Checks/Industry and Regulatory Standards/CIS AWS Foundations Benchmark, Software and Configuration Checks/AWS Security Best Practices/Runtime Behavior Analysis, Software and Configuration Checks/AWS Security Best Practices/Network Reachability, TTPs/Command and Control |
| 资源类型 | AwsCloudWatchAlarm |
| 资源组 | monitoring |

## 描述

CloudWatch log metric filters and alarms for **network gateway changes** are identified by matching CloudTrail events such as `CreateCustomerGateway`, `DeleteCustomerGateway`, `AttachInternetGateway`, `CreateInternetGateway`, `DeleteInternetGateway`, and `DetachInternetGateway` in log groups that receive trail logs.

## 风险

Without this monitoring, gateway changes can expose private networks to the Internet or break connectivity. Adversaries or mistakes can enable data exfiltration, bypass network inspection, and trigger outages via deletions or detachments, impacting **confidentiality** and **availability**.

## 推荐措施

Send CloudTrail to CloudWatch Logs and create a metric filter for the listed gateway events with an alarm that notifies responders. Enforce **least privilege** for gateway modifications, require change approvals, and route alerts to monitored channels as part of **defense in depth**.

## 修复步骤


### Native IaC

```yaml
# CloudFormation: Create metric filter and alarm for network gateway changes
Resources:
  NetworkGatewayMetricFilter:
    Type: AWS::Logs::MetricFilter
    Properties:
      LogGroupName: <example_resource_name>
      FilterPattern: '{ ($.eventName = CreateCustomerGateway) || ($.eventName = DeleteCustomerGateway) || ($.eventName = AttachInternetGateway) || ($.eventName = CreateInternetGateway) || ($.eventName = DeleteInternetGateway) || ($.eventName = DetachInternetGateway) }'  # Critical: matches gateway change events
      MetricTransformations:
        - MetricName: <example_resource_name>
          MetricNamespace: <example_resource_name>
          MetricValue: "1"

  NetworkGatewayAlarm:
    Type: AWS::CloudWatch::Alarm
    Properties:
      ComparisonOperator: GreaterThanOrEqualToThreshold
      EvaluationPeriods: 1
      MetricName: <example_resource_name>  # Critical: alarm targets the metric created by the filter
      Namespace: <example_resource_name>
      Period: 300
      Statistic: Sum
      Threshold: 1
```

### Terraform

```hcl
# CloudWatch Logs metric filter for network gateway changes
resource "aws_cloudwatch_log_metric_filter" "<example_resource_name>" {
  name           = "<example_resource_name>"
  log_group_name = "<example_resource_name>"
  pattern        = "{ ($.eventName = CreateCustomerGateway) || ($.eventName = DeleteCustomerGateway) || ($.eventName = AttachInternetGateway) || ($.eventName = CreateInternetGateway) || ($.eventName = DeleteInternetGateway) || ($.eventName = DetachInternetGateway) }" # Critical: matches gateway change events

  metric_transformation {
    name      = "<example_resource_name>"
    namespace = "<example_resource_name>"
    value     = "1"
  }
}

# Alarm on the metric filter
resource "aws_cloudwatch_metric_alarm" "<example_resource_name>" {
  alarm_name          = "<example_resource_name>"
  comparison_operator = "GreaterThanOrEqualToThreshold"
  evaluation_periods  = 1
  metric_name         = "<example_resource_name>"   # Critical: must match metric from the filter
  namespace           = "<example_resource_name>"
  period              = 300
  statistic           = "Sum"
  threshold           = 1
}
```

### Other

1. In the AWS Console, go to CloudWatch > Logs > Log groups and open the CloudTrail log group
2. Create metric filter:
   - Filter pattern: { ($.eventName = CreateCustomerGateway) || ($.eventName = DeleteCustomerGateway) || ($.eventName = AttachInternetGateway) || ($.eventName = CreateInternetGateway) || ($.eventName = DeleteInternetGateway) || ($.eventName = DetachInternetGateway) }
   - Metric name: <example_resource_name>
   - Metric namespace: <example_resource_name>
   - Metric value: 1
3. From the filter, choose Create alarm:
   - Statistic: Sum, Period: 5 minutes, Threshold: >= 1, Evaluation periods: 1
   - Create the alarm (actions optional)

## 参考资料

- [https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudwatch-alarms-for-cloudtrail.html](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudwatch-alarms-for-cloudtrail.html)
- [https://support.icompaas.com/support/solutions/articles/62000083807-ensure-a-log-metric-filter-and-alarm-exist-for-changes-to-network-gateways](https://support.icompaas.com/support/solutions/articles/62000083807-ensure-a-log-metric-filter-and-alarm-exist-for-changes-to-network-gateways)
- [https://docs.aws.amazon.com/securityhub/latest/userguide/cloudwatch-controls.html#cloudwatch-12](https://docs.aws.amazon.com/securityhub/latest/userguide/cloudwatch-controls.html#cloudwatch-12)
- [https://paper.bobylive.com/Security/CIS/CIS_Amazon_Web_Services_Foundations_Benchmark_v1_3_0.pdf](https://paper.bobylive.com/Security/CIS/CIS_Amazon_Web_Services_Foundations_Benchmark_v1_3_0.pdf)

## 技术信息

- Source Metadata：[sources/aws/cloudwatch_changes_to_network_gateways_alarm_configured/metadata.json](../../sources/aws/cloudwatch_changes_to_network_gateways_alarm_configured/metadata.json)
- Source Code：[sources/aws/cloudwatch_changes_to_network_gateways_alarm_configured/check.py](../../sources/aws/cloudwatch_changes_to_network_gateways_alarm_configured/check.py)
- Source Metadata Path：`sources/aws/cloudwatch_changes_to_network_gateways_alarm_configured/metadata.json`
- Source Code Path：`sources/aws/cloudwatch_changes_to_network_gateways_alarm_configured/check.py`
