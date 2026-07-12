# CloudWatch log metric filter and alarm exist for Network ACL (NACL) change events

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `cloudwatch_changes_to_network_acls_alarm_configured` |
| クラウドプラットフォーム | AWS |
| サービス | cloudwatch |
| 重大度 | medium |
| カテゴリ | logging |
| チェックタイプ | Software and Configuration Checks/Industry and Regulatory Standards/CIS AWS Foundations Benchmark, Software and Configuration Checks/AWS Security Best Practices/Runtime Behavior Analysis |
| リソースタイプ | AwsCloudWatchAlarm |
| リソースグループ | monitoring |

## 説明

CloudTrail records for **Network ACL changes** are matched by a CloudWatch Logs metric filter with an associated alarm for events like `CreateNetworkAcl`, `CreateNetworkAclEntry`, `DeleteNetworkAcl`, `DeleteNetworkAclEntry`, `ReplaceNetworkAclEntry`, and `ReplaceNetworkAclAssociation`.

## リスク

Absent monitoring of **NACL changes** reduces detection of policy tampering, risking loss of **confidentiality** (opened ingress/egress), degraded network **integrity** (lateral movement, bypassed segmentation), and reduced **availability** (traffic blackholes or lockouts).

## 推奨事項

Implement a CloudWatch Logs metric filter and alarm for NACL change events from CloudTrail and route alerts to responders. Enforce **least privilege** on NACL management, require **change control**, and use **defense in depth** with configuration monitoring and flow logs to validate and monitor network posture.

## 修正手順


### Native IaC

```yaml
# CloudFormation to alert on NACL changes
Resources:
  MetricFilter:
    Type: AWS::Logs::MetricFilter
    Properties:
      LogGroupName: "<example_resource_name>"  # CRITICAL: CloudTrail log group to monitor
      FilterPattern: '{ ($.eventName = CreateNetworkAcl) || ($.eventName = CreateNetworkAclEntry) || ($.eventName = DeleteNetworkAcl) || ($.eventName = DeleteNetworkAclEntry) || ($.eventName = ReplaceNetworkAclEntry) || ($.eventName = ReplaceNetworkAclAssociation) }'  # CRITICAL: detects NACL changes
      MetricTransformations:
        - MetricValue: "1"
          MetricNamespace: "CISBenchmark"
          MetricName: "nacl_changes"

  NaclChangesAlarm:
    Type: AWS::CloudWatch::Alarm
    Properties:
      AlarmName: "nacl_changes"
      ComparisonOperator: GreaterThanOrEqualToThreshold
      EvaluationPeriods: 1
      MetricName: "nacl_changes"   # CRITICAL: alarm targets the metric from the filter
      Namespace: "CISBenchmark"
      Period: 300
      Statistic: Sum
      Threshold: 1
```

### Terraform

```hcl
# CloudWatch metric filter and alarm for NACL changes
resource "aws_cloudwatch_log_metric_filter" "nacl" {
  name           = "nacl_changes"
  log_group_name = "<example_resource_name>"  # CloudTrail log group
  pattern        = "{ ($.eventName = CreateNetworkAcl) || ($.eventName = CreateNetworkAclEntry) || ($.eventName = DeleteNetworkAcl) || ($.eventName = DeleteNetworkAclEntry) || ($.eventName = ReplaceNetworkAclEntry) || ($.eventName = ReplaceNetworkAclAssociation) }"  # CRITICAL: detects NACL changes

  metric_transformation {
    name      = "nacl_changes"
    namespace = "CISBenchmark"
    value     = "1"
  }
}

resource "aws_cloudwatch_metric_alarm" "nacl" {
  alarm_name          = "nacl_changes"
  comparison_operator = "GreaterThanOrEqualToThreshold"
  evaluation_periods  = 1
  metric_name         = "nacl_changes"   # CRITICAL: alarm targets the metric from the filter
  namespace           = "CISBenchmark"
  period              = 300
  statistic           = "Sum"
  threshold           = 1
}
```

### Other

1. In the AWS Console, go to CloudWatch > Log groups and open the CloudTrail log group
2. Metric filters tab > Create metric filter
3. Set Filter pattern to:
   { ($.eventName = CreateNetworkAcl) || ($.eventName = CreateNetworkAclEntry) || ($.eventName = DeleteNetworkAcl) || ($.eventName = DeleteNetworkAclEntry) || ($.eventName = ReplaceNetworkAclEntry) || ($.eventName = ReplaceNetworkAclAssociation) }
4. Next > Filter name: nacl_changes; Metric namespace: CISBenchmark; Metric name: nacl_changes; Metric value: 1 > Create metric filter
5. Select the new metric filter > Create alarm
6. Set Statistic: Sum, Period: 5 minutes, Threshold type: Static, Condition: Greater/Equal, Threshold: 1
7. Next through actions (optional) > Name: nacl_changes > Create alarm

## 参考資料

- [https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudwatch-alarms-for-cloudtrail.html](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudwatch-alarms-for-cloudtrail.html)
- [https://www.clouddefense.ai/compliance-rules/cis-v130/monitoring/cis-v130-4-11](https://www.clouddefense.ai/compliance-rules/cis-v130/monitoring/cis-v130-4-11)
- [https://support.icompaas.com/support/solutions/articles/62000084031-ensure-a-log-metric-filter-and-alarm-exist-for-changes-to-network-access-control-lists-nacl-](https://support.icompaas.com/support/solutions/articles/62000084031-ensure-a-log-metric-filter-and-alarm-exist-for-changes-to-network-access-control-lists-nacl-)
- [https://trendmicro.com/cloudoneconformity/knowledge-base/aws/CloudWatchLogs/network-acl-changes-alarm.html](https://trendmicro.com/cloudoneconformity/knowledge-base/aws/CloudWatchLogs/network-acl-changes-alarm.html)
- [https://support.icompaas.com/support/solutions/articles/62000233134-4-11-ensure-network-access-control-list-nacl-changes-are-monitored-manual-](https://support.icompaas.com/support/solutions/articles/62000233134-4-11-ensure-network-access-control-list-nacl-changes-are-monitored-manual-)

## 技術情報

- Source Metadata：[sources/aws/cloudwatch_changes_to_network_acls_alarm_configured/metadata.json](../../sources/aws/cloudwatch_changes_to_network_acls_alarm_configured/metadata.json)
- Source Code：[sources/aws/cloudwatch_changes_to_network_acls_alarm_configured/check.py](../../sources/aws/cloudwatch_changes_to_network_acls_alarm_configured/check.py)
- Source Metadata Path：`sources/aws/cloudwatch_changes_to_network_acls_alarm_configured/metadata.json`
- Source Code Path：`sources/aws/cloudwatch_changes_to_network_acls_alarm_configured/check.py`
