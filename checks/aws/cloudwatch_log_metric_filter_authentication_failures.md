# Account has a CloudWatch Logs metric filter and alarm for AWS Management Console authentication failures

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `cloudwatch_log_metric_filter_authentication_failures` |
| クラウドプラットフォーム | AWS |
| サービス | cloudwatch |
| 重大度 | medium |
| カテゴリ | logging |
| チェックタイプ | Software and Configuration Checks/Industry and Regulatory Standards/CIS AWS Foundations Benchmark, Software and Configuration Checks/Industry and Regulatory Standards/AWS Foundational Security Best Practices, Software and Configuration Checks/AWS Security Best Practices/Runtime Behavior Analysis, TTPs/Initial Access, TTPs/Credential Access |
| リソースタイプ | AwsCloudWatchAlarm |
| リソースグループ | monitoring |

## 説明

CloudWatch Logs metric filter and alarm for **AWS Management Console authentication failures**, sourced from CloudTrail (`eventName=ConsoleLogin`, `errorMessage="Failed authentication"`). Identifies whether these failures are converted into a metric and actively monitored by an alarm.

## リスク

Absent visibility into failed console logins enables undetected **brute-force** and **credential-stuffing** attempts, extending attacker dwell time. Successful guesses can grant console access, risking data confidentiality, configuration integrity, and availability through destructive changes.

## 推奨事項

Implement a log metric filter for `ConsoleLogin` failures and attach a **CloudWatch alarm** with actionable notifications. Tune thresholds to reduce noise and route alerts to incident response. Apply **least privilege** and enforce **MFA** to limit impact, and correlate alerts with source IP and user context.

## 修正手順


### Native IaC

```yaml
# CloudFormation: Metric filter and alarm for console authentication failures
Resources:
  MetricFilter:
    Type: AWS::Logs::MetricFilter
    Properties:
      LogGroupName: "<example_resource_name>"
      FilterPattern: '{ ($.eventName = ConsoleLogin) && ($.errorMessage = "Failed authentication") }'  # Critical: matches failed console login events
      MetricTransformations:
        - MetricValue: "1"
          MetricNamespace: "<example_resource_name>"  # Critical: creates metric namespace
          MetricName: "<example_resource_name>"       # Critical: creates metric name

  Alarm:
    Type: AWS::CloudWatch::Alarm
    Properties:
      MetricName: "<example_resource_name>"   # Critical: alarm targets metric from filter
      Namespace: "<example_resource_name>"    # Critical: must match metric's namespace
      ComparisonOperator: GreaterThanOrEqualToThreshold
      EvaluationPeriods: 1
      Period: 300
      Statistic: Sum
      Threshold: 1
```

### Terraform

```hcl
# Metric filter and alarm for console authentication failures
resource "aws_cloudwatch_log_metric_filter" "metric" {
  name           = "<example_resource_name>"
  log_group_name = "<example_resource_name>"
  pattern        = "{($.eventName = ConsoleLogin) && ($.errorMessage = \"Failed authentication\") }" # Critical: detects failed console logins

  metric_transformation {
    name      = "<example_resource_name>"   # Critical: metric created by filter
    namespace = "<example_resource_name>"   # Critical: metric namespace
    value     = "1"
  }
}

resource "aws_cloudwatch_metric_alarm" "alarm" {
  metric_name          = aws_cloudwatch_log_metric_filter.metric.metric_transformation[0].name   # Critical: alarm references the filter's metric
  namespace            = aws_cloudwatch_log_metric_filter.metric.metric_transformation[0].namespace # Critical: must match
  comparison_operator  = "GreaterThanOrEqualToThreshold"
  evaluation_periods   = 1
  period               = 300
  statistic            = "Sum"
  threshold            = 1
}
```

### Other

1. In the AWS Console, open CloudWatch
2. Go to Logs > Log groups and select the CloudTrail log group receiving events
3. Open the Metric filters tab > Create metric filter
   - Filter pattern: { ($.eventName = ConsoleLogin) && ($.errorMessage = "Failed authentication") }
   - Assign any metric name and namespace, value 1, then create
4. On the created metric filter, select it and choose Create alarm
   - Statistic: Sum, Period: 5 minutes, Threshold type: Static, Threshold: >= 1
   - Create the alarm

## 参考資料

- [https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudwatch-alarms-for-cloudtrail.html](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudwatch-alarms-for-cloudtrail.html)
- [https://www.intelligentdiscovery.io/controls/cloudwatch/cloudwatch-alarm-signin-failures](https://www.intelligentdiscovery.io/controls/cloudwatch/cloudwatch-alarm-signin-failures)
- [https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/CloudWatchLogs/console-sign-in-failures-alarm.html](https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/CloudWatchLogs/console-sign-in-failures-alarm.html)
- [https://newsletter.simpleaws.dev/p/cloudtrail-cloudwatch-logs-login-detection-alert](https://newsletter.simpleaws.dev/p/cloudtrail-cloudwatch-logs-login-detection-alert)

## 技術情報

- Source Metadata：[sources/aws/cloudwatch_log_metric_filter_authentication_failures/metadata.json](../../sources/aws/cloudwatch_log_metric_filter_authentication_failures/metadata.json)
- Source Code：[sources/aws/cloudwatch_log_metric_filter_authentication_failures/check.py](../../sources/aws/cloudwatch_log_metric_filter_authentication_failures/check.py)
- Source Metadata Path：`sources/aws/cloudwatch_log_metric_filter_authentication_failures/metadata.json`
- Source Code Path：`sources/aws/cloudwatch_log_metric_filter_authentication_failures/check.py`
