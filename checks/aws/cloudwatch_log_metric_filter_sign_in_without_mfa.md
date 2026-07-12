# CloudWatch log metric filter and alarm exist for Management Console sign-in without MFA

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `cloudwatch_log_metric_filter_sign_in_without_mfa` |
| クラウドプラットフォーム | AWS |
| サービス | cloudwatch |
| 重大度 | medium |
| カテゴリ | logging |
| チェックタイプ | Software and Configuration Checks/AWS Security Best Practices, Software and Configuration Checks/Industry and Regulatory Standards/CIS AWS Foundations Benchmark, TTPs/Initial Access, Unusual Behaviors/User |
| リソースタイプ | AwsCloudWatchAlarm |
| リソースグループ | monitoring |

## 説明

**CloudTrail logs** in CloudWatch are assessed for a metric filter and alarm that detect console logins where `$.eventName = ConsoleLogin` and `$.additionalEventData.MFAUsed != \"Yes\"`. This reflects whether alerting exists for sign-ins that occur without **MFA**.

## リスク

Without alerting on non-MFA console logins, successful use of stolen passwords can go **undetected**, enabling: - Unauthorized console access and IAM changes - Data exfiltration or deletion Impacts: loss of **confidentiality** and **integrity**, and potential **availability** disruption.

## 推奨事項

Enforce **MFA** for all console-capable identities and maintain alerts for `ConsoleLogin` with `MFAUsed != \"Yes\"`. Apply **least privilege**, route alarms to monitored channels, and tune for SSO to reduce noise. Test alarms regularly and review coverage as part of **defense in depth**.

## 修正手順


### Native IaC

```yaml
# CloudFormation: Create metric filter and alarm for console sign-in without MFA
Resources:
  NoMFAConsoleSigninMetricFilter:
    Type: AWS::Logs::MetricFilter
    Properties:
      LogGroupName: "<example_resource_name>"
      FilterPattern: '{ ($.eventName = "ConsoleLogin") && ($.additionalEventData.MFAUsed != "Yes") }' # CRITICAL: detects ConsoleLogin events without MFA
      MetricTransformations:
        - MetricName: "<example_resource_name>"
          MetricNamespace: "<example_resource_name>"
          MetricValue: "1"  # CRITICAL: emits a metric on each match

  NoMFAConsoleSigninAlarm:
    Type: AWS::CloudWatch::Alarm
    Properties:
      MetricName: "<example_resource_name>"   # CRITICAL: alarm uses the metric from the filter
      Namespace: "<example_resource_name>"
      ComparisonOperator: GreaterThanOrEqualToThreshold
      EvaluationPeriods: 1
      Period: 300
      Statistic: Sum
      Threshold: 1  # CRITICAL: alarm on first occurrence
```

### Terraform

```hcl
# Create metric filter for console sign-in without MFA
resource "aws_cloudwatch_log_metric_filter" "nomfa" {
  name           = "<example_resource_name>"
  log_group_name = "<example_resource_name>"
  pattern        = "{ ($.eventName = \"ConsoleLogin\") && ($.additionalEventData.MFAUsed != \"Yes\") }"  # CRITICAL: detects ConsoleLogin without MFA

  metric_transformation {
    name      = "<example_resource_name>"
    namespace = "<example_resource_name>"
    value     = "1"  # CRITICAL: emits a count per match
  }
}

# Alarm on the emitted metric
resource "aws_cloudwatch_metric_alarm" "nomfa" {
  alarm_name          = "<example_resource_name>"
  metric_name         = aws_cloudwatch_log_metric_filter.nomfa.metric_transformation[0].name  # CRITICAL: ties alarm to the metric
  namespace           = aws_cloudwatch_log_metric_filter.nomfa.metric_transformation[0].namespace
  comparison_operator = "GreaterThanOrEqualToThreshold"
  evaluation_periods  = 1
  period              = 300
  statistic           = "Sum"
  threshold           = 1  # CRITICAL: alarm on first event
}
```

### Other

1. In AWS Console, go to CloudWatch > Logs > Log groups and open the CloudTrail log group
2. Go to Metric filters > Create metric filter
3. Set Filter pattern to: { ($.eventName = "ConsoleLogin") && ($.additionalEventData.MFAUsed != "Yes") }
4. Next > set Filter name, Metric namespace, Metric name; set Metric value = 1; Create metric filter
5. Select the new filter > Create alarm
6. Set Statistic = Sum, Period = 5 minutes, Threshold type = Static, Threshold = 1, Whenever >= 1; Next
7. Skip actions if not needed, Name the alarm, Create alarm

## 参考資料

- [https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudwatch-alarms-for-cloudtrail.html](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudwatch-alarms-for-cloudtrail.html)
- [https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/CloudWatchLogs/console-sign-in-without-mfa.html](https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/CloudWatchLogs/console-sign-in-without-mfa.html)
- [https://www.tenable.com/audits/items/CIS_Amazon_Web_Services_Foundations_v3.0.0_L1.audit:1957056ee174cc38502d5f5f1864333b](https://www.tenable.com/audits/items/CIS_Amazon_Web_Services_Foundations_v3.0.0_L1.audit:1957056ee174cc38502d5f5f1864333b)
- [https://www.clouddefense.ai/compliance-rules/gdpr/data-protection/log-metric-filter-console-login-mfa](https://www.clouddefense.ai/compliance-rules/gdpr/data-protection/log-metric-filter-console-login-mfa)
- [https://www.intelligentdiscovery.io/controls/cloudwatch/cloudwatch-alarm-no-mfa](https://www.intelligentdiscovery.io/controls/cloudwatch/cloudwatch-alarm-no-mfa)
- [https://support.icompaas.com/support/solutions/articles/62000083605-ensure-a-log-metric-filter-and-alarm-exist-for-management-console-sign-in-without-mfa](https://support.icompaas.com/support/solutions/articles/62000083605-ensure-a-log-metric-filter-and-alarm-exist-for-management-console-sign-in-without-mfa)

## 技術情報

- Source Metadata：[sources/aws/cloudwatch_log_metric_filter_sign_in_without_mfa/metadata.json](../../sources/aws/cloudwatch_log_metric_filter_sign_in_without_mfa/metadata.json)
- Source Code：[sources/aws/cloudwatch_log_metric_filter_sign_in_without_mfa/check.py](../../sources/aws/cloudwatch_log_metric_filter_sign_in_without_mfa/check.py)
- Source Metadata Path：`sources/aws/cloudwatch_log_metric_filter_sign_in_without_mfa/metadata.json`
- Source Code Path：`sources/aws/cloudwatch_log_metric_filter_sign_in_without_mfa/check.py`
