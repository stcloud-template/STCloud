# AWS account has a CloudWatch Logs metric filter and alarm for VPC changes

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `cloudwatch_changes_to_vpcs_alarm_configured` |
| 云平台 | AWS |
| 服务 | cloudwatch |
| 严重等级 | medium |
| 类别 | logging |
| 检查类型 | Software and Configuration Checks/Industry and Regulatory Standards/CIS AWS Foundations Benchmark |
| 资源类型 | AwsCloudWatchAlarm |
| 资源组 | monitoring |

## 描述

**CloudTrail events** for **VPC configuration changes** are captured in CloudWatch Logs with a metric filter and an associated alarm. The filter targets actions like `CreateVpc`, `DeleteVpc`, `ModifyVpcAttribute`, and VPC peering operations to surface when network topology is altered.

## 风险

Without alerting on VPC changes, unauthorized or accidental edits to routes, peering, or attributes can go unnoticed, exposing private networks and enabling data exfiltration (C), lateral movement and traffic tampering (I), and outages from misrouted or bridged networks (A).

## 推荐措施

Create a CloudWatch Logs metric filter and alarm on CloudTrail for critical **VPC change events**, and notify responders. Apply **least privilege** to network changes, require change approvals, and use **defense in depth** (segmentation, route controls) to prevent and contain unauthorized modifications.

## 修复步骤


### Native IaC

```yaml
# CloudFormation: Create a metric filter and alarm for VPC changes
Resources:
  VPCChangesMetricFilter:
    Type: AWS::Logs::MetricFilter
    Properties:
      LogGroupName: <example_log_group_name>
      FilterPattern: '{ ($.eventName = CreateVpc) || ($.eventName = DeleteVpc) || ($.eventName = ModifyVpcAttribute) || ($.eventName = AcceptVpcPeeringConnection) || ($.eventName = CreateVpcPeeringConnection) || ($.eventName = DeleteVpcPeeringConnection) || ($.eventName = RejectVpcPeeringConnection) || ($.eventName = AttachClassicLinkVpc) || ($.eventName = DetachClassicLinkVpc) || ($.eventName = DisableVpcClassicLink) || ($.eventName = EnableVpcClassicLink) }' # Critical: matches VPC change events
      MetricTransformations:
        - MetricName: vpc_changes_metric
          MetricNamespace: CISBenchmark
          MetricValue: "1"  # Critical: emits a metric on matching events

  VPCChangesAlarm:
    Type: AWS::CloudWatch::Alarm
    Properties:
      MetricName: vpc_changes_metric  # Critical: alarm monitors the metric above
      Namespace: CISBenchmark
      Statistic: Sum
      Period: 300
      EvaluationPeriods: 1
      Threshold: 1
      ComparisonOperator: GreaterThanOrEqualToThreshold
```

### Terraform

```hcl
# Metric filter for VPC changes
resource "aws_cloudwatch_log_metric_filter" "<example_resource_name>" {
  name           = "<example_resource_name>"
  log_group_name = "<example_log_group_name>"
  pattern        = "{ ($.eventName = CreateVpc) || ($.eventName = DeleteVpc) || ($.eventName = ModifyVpcAttribute) || ($.eventName = AcceptVpcPeeringConnection) || ($.eventName = CreateVpcPeeringConnection) || ($.eventName = DeleteVpcPeeringConnection) || ($.eventName = RejectVpcPeeringConnection) || ($.eventName = AttachClassicLinkVpc) || ($.eventName = DetachClassicLinkVpc) || ($.eventName = DisableVpcClassicLink) || ($.eventName = EnableVpcClassicLink) }" # Critical: matches VPC change events

  metric_transformation {
    name      = "<example_resource_name>"   # Critical: metric created by the filter
    namespace = "CISBenchmark"
    value     = "1"
  }
}

# Alarm on the VPC changes metric
resource "aws_cloudwatch_metric_alarm" "<example_resource_name>" {
  metric_name        = "<example_resource_name>"  # Critical: alarm monitors the filter's metric
  namespace          = "CISBenchmark"
  statistic          = "Sum"
  period             = 300
  evaluation_periods = 1
  threshold          = 1
  comparison_operator = "GreaterThanOrEqualToThreshold"
}
```

### Other

1. In the AWS Console, go to CloudWatch > Log groups and open the CloudTrail log group
2. Choose Create metric filter
3. For Filter pattern, paste:
   { ($.eventName = CreateVpc) || ($.eventName = DeleteVpc) || ($.eventName = ModifyVpcAttribute) || ($.eventName = AcceptVpcPeeringConnection) || ($.eventName = CreateVpcPeeringConnection) || ($.eventName = DeleteVpcPeeringConnection) || ($.eventName = RejectVpcPeeringConnection) || ($.eventName = AttachClassicLinkVpc) || ($.eventName = DetachClassicLinkVpc) || ($.eventName = DisableVpcClassicLink) || ($.eventName = EnableVpcClassicLink) }
4. Name the filter and set Metric namespace to CISBenchmark, Metric name to vpc_changes_metric, Metric value to 1; create the filter
5. Select the new filter and choose Create alarm
6. Set Statistic to Sum, Period 5 minutes, Threshold type Static, Whenever Greater/Equal 1, Evaluation periods 1
7. Create the alarm (actions/notifications are optional and not required for pass)

## 参考资料

- [https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudwatch-alarms-for-cloudtrail.html](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudwatch-alarms-for-cloudtrail.html)

## 技术信息

- Source Metadata：[sources/aws/cloudwatch_changes_to_vpcs_alarm_configured/metadata.json](../../sources/aws/cloudwatch_changes_to_vpcs_alarm_configured/metadata.json)
- Source Code：[sources/aws/cloudwatch_changes_to_vpcs_alarm_configured/check.py](../../sources/aws/cloudwatch_changes_to_vpcs_alarm_configured/check.py)
- Source Metadata Path：`sources/aws/cloudwatch_changes_to_vpcs_alarm_configured/metadata.json`
- Source Code Path：`sources/aws/cloudwatch_changes_to_vpcs_alarm_configured/check.py`
