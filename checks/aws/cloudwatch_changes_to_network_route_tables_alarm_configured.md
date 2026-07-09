# Account monitors VPC route table changes with a CloudWatch Logs metric filter and alarm

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `cloudwatch_changes_to_network_route_tables_alarm_configured` |
| 云平台 | AWS |
| 服务 | cloudwatch |
| 严重等级 | medium |
| 类别 | logging |
| 检查类型 | Software and Configuration Checks/Industry and Regulatory Standards/CIS AWS Foundations Benchmark, Software and Configuration Checks/AWS Security Best Practices, TTPs/Defense Evasion, Effects/Data Exfiltration |
| 资源类型 | AwsCloudWatchAlarm |
| 资源组 | monitoring |

## 描述

**VPC route table changes** are captured from **CloudTrail logs** by a **CloudWatch Logs metric filter** with an associated **alarm** for events like `CreateRoute`, `CreateRouteTable`, `ReplaceRoute`, `ReplaceRouteTableAssociation`, `DeleteRoute`, `DeleteRouteTable`, and `DisassociateRouteTable`.

## 风险

Without monitoring of **route table changes**, unauthorized or accidental edits can redirect traffic, bypass inspection, or blackhole routes, impacting **confidentiality** (exfiltration), **integrity** (tampered paths), and **availability** (outages from misrouted traffic).

## 推荐措施

Implement a **CloudWatch Logs metric filter and alarm** on CloudTrail for these route table events and notify responders. Enforce **least privilege** for route modifications, require **change control**, and apply **defense in depth** with VPC Flow Logs and guardrails to prevent and quickly contain unsafe routing changes.

## 修复步骤


### Native IaC

```yaml
# CloudFormation: Metric filter + alarm for VPC route table changes
Resources:
  RouteTableChangeMetricFilter:
    Type: AWS::Logs::MetricFilter
    Properties:
      LogGroupName: "<example_resource_name>"
      # CRITICAL: Detect EC2 route table change events in CloudTrail logs
      # Includes eventSource and the required eventNames
      FilterPattern: '{($.eventSource = ec2.amazonaws.com) && (($.eventName = CreateRoute) || ($.eventName = CreateRouteTable) || ($.eventName = ReplaceRoute) || ($.eventName = ReplaceRouteTableAssociation) || ($.eventName = DeleteRouteTable) || ($.eventName = DeleteRoute) || ($.eventName = DisassociateRouteTable))}'
      MetricTransformations:
        - MetricValue: "1"
          MetricNamespace: "<example_resource_name>"
          MetricName: "<example_resource_name>"

  RouteTableChangeAlarm:
    Type: AWS::CloudWatch::Alarm
    Properties:
      # CRITICAL: Alarm on the metric from the filter above
      Namespace: "<example_resource_name>"
      MetricName: "<example_resource_name>"
      ComparisonOperator: GreaterThanOrEqualToThreshold
      EvaluationPeriods: 1
      Period: 300
      Statistic: Sum
      Threshold: 1
```

### Terraform

```hcl
# Metric filter + alarm for VPC route table changes
resource "aws_cloudwatch_log_metric_filter" "routes" {
  name           = "<example_resource_name>"
  log_group_name = "<example_resource_name>"
  # CRITICAL: Detect EC2 route table change events in CloudTrail logs
  pattern = "{($.eventSource = ec2.amazonaws.com) && (($.eventName = CreateRoute) || ($.eventName = CreateRouteTable) || ($.eventName = ReplaceRoute) || ($.eventName = ReplaceRouteTableAssociation) || ($.eventName = DeleteRouteTable) || ($.eventName = DeleteRoute) || ($.eventName = DisassociateRouteTable))}"

  metric_transformation {
    name      = "<example_resource_name>"
    namespace = "<example_resource_name>"
    value     = "1"
  }
}

resource "aws_cloudwatch_metric_alarm" "routes" {
  alarm_name          = "<example_resource_name>"
  # CRITICAL: Alarm targets the metric from the filter above
  metric_name         = "<example_resource_name>"
  namespace           = "<example_resource_name>"
  comparison_operator = "GreaterThanOrEqualToThreshold"
  evaluation_periods  = 1
  period              = 300
  statistic           = "Sum"
  threshold           = 1
}
```

### Other

1. In the AWS console, open CloudWatch > Log groups and select your CloudTrail log group
2. Go to Metric filters > Create metric filter
3. Set Filter pattern to:
   {($.eventSource = ec2.amazonaws.com) && (($.eventName = CreateRoute) || ($.eventName = CreateRouteTable) || ($.eventName = ReplaceRoute) || ($.eventName = ReplaceRouteTableAssociation) || ($.eventName = DeleteRouteTable) || ($.eventName = DeleteRoute) || ($.eventName = DisassociateRouteTable))}
4. Name the metric and set Metric value to 1; choose any namespace/name
5. Create the filter
6. From the filter, click Create alarm
7. Set Statistic: Sum, Period: 5 minutes, Threshold type: Static, Threshold: 1, Whenever: Greater/Equal
8. Create the alarm (notifications optional)

## 参考资料

- [https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudwatch-alarms-for-cloudtrail.html](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudwatch-alarms-for-cloudtrail.html)

## 技术信息

- Source Metadata：[sources/aws/cloudwatch_changes_to_network_route_tables_alarm_configured/metadata.json](../../sources/aws/cloudwatch_changes_to_network_route_tables_alarm_configured/metadata.json)
- Source Code：[sources/aws/cloudwatch_changes_to_network_route_tables_alarm_configured/check.py](../../sources/aws/cloudwatch_changes_to_network_route_tables_alarm_configured/check.py)
- Source Metadata Path：`sources/aws/cloudwatch_changes_to_network_route_tables_alarm_configured/metadata.json`
- Source Code Path：`sources/aws/cloudwatch_changes_to_network_route_tables_alarm_configured/check.py`
