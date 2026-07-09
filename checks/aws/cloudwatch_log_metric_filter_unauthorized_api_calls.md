# CloudWatch Logs metric filter and alarm exist for unauthorized API calls

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `cloudwatch_log_metric_filter_unauthorized_api_calls` |
| 云平台 | AWS |
| 服务 | cloudwatch |
| 严重等级 | medium |
| 类别 | logging |
| 检查类型 | Software and Configuration Checks/Industry and Regulatory Standards/CIS AWS Foundations Benchmark, Software and Configuration Checks/AWS Security Best Practices/Runtime Behavior Analysis, TTPs/Initial Access/Unauthorized Access |
| 资源类型 | AwsCloudWatchAlarm |
| 资源组 | monitoring |

## 描述

**CloudWatch Logs** for CloudTrail include a metric filter that matches unauthorized API errors (`$.errorCode="*UnauthorizedOperation"` or `$.errorCode="AccessDenied*"`) and a linked alarm that triggers when events match the filter.

## 风险

Without alerting on **unauthorized API calls**, permission probing and failed access by compromised identities can go unnoticed. Attackers can enumerate services, pivot, and attempt privilege escalation, threatening data **confidentiality** and **integrity**.

## 推荐措施

Enable real-time **alerting** by adding a CloudWatch Logs metric filter for unauthorized errors (`*UnauthorizedOperation`, `AccessDenied*`) and associating it with an alarm that notifies responders. - Enforce **least privilege** to reduce noise - Integrate with IR tooling for **defense in depth**

## 修复步骤


### Native IaC

```yaml
# CloudFormation: Create metric filter and alarm for unauthorized API calls
Resources:
  MetricFilterUnauthorized:
    Type: AWS::Logs::MetricFilter
    Properties:
      LogGroupName: <example_resource_name>
      FilterPattern: '{($.errorCode = "*UnauthorizedOperation") || ($.errorCode = "AccessDenied*")}'  # Critical: detects unauthorized/denied API calls
      MetricTransformations:
        - MetricName: unauthorized_api_calls_metric
          MetricNamespace: CISBenchmark
          MetricValue: "1"

  AlarmUnauthorized:
    Type: AWS::CloudWatch::Alarm
    Properties:
      ComparisonOperator: GreaterThanOrEqualToThreshold
      EvaluationPeriods: 1
      MetricName: unauthorized_api_calls_metric  # Critical: alarm on the metric from the filter
      Namespace: CISBenchmark
      Period: 300
      Statistic: Sum
      Threshold: 1
```

### Terraform

```hcl
# Terraform: Metric filter and alarm for unauthorized API calls
resource "aws_cloudwatch_log_metric_filter" "unauthorized" {
  name           = "unauthorized_api_calls_metric"
  log_group_name = "<example_resource_name>"
  pattern        = "{($.errorCode = \"*UnauthorizedOperation\") || ($.errorCode = \"AccessDenied*\")}"  # Critical: detects unauthorized/denied API calls

  metric_transformation {
    name      = "unauthorized_api_calls_metric"
    namespace = "CISBenchmark"
    value     = "1"
  }
}

resource "aws_cloudwatch_metric_alarm" "unauthorized" {
  comparison_operator = "GreaterThanOrEqualToThreshold"
  evaluation_periods  = 1
  metric_name         = "unauthorized_api_calls_metric"   # Critical: alarm on the metric from the filter
  namespace           = "CISBenchmark"
  period              = 300
  statistic           = "Sum"
  threshold           = 1
}
```

### Other

1. In the AWS Console, open CloudWatch > Logs > Log groups and select the CloudTrail log group
2. Go to Metric filters > Create metric filter
3. Set Filter pattern to: {($.errorCode = "*UnauthorizedOperation") || ($.errorCode = "AccessDenied*")}
4. Name the metric unauthorized_api_calls_metric, set Namespace to CISBenchmark, Value to 1, then create
5. Select the new metric filter and click Create alarm
6. Set Statistic: Sum, Period: 5 minutes, Threshold type: Static, Threshold: 1, Evaluation periods: 1
7. Create the alarm

## 参考资料

- [https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudwatch-alarms-for-cloudtrail.html](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudwatch-alarms-for-cloudtrail.html)
- [https://asecure.cloud/a/unauthorized_api_calls/](https://asecure.cloud/a/unauthorized_api_calls/)
- [https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/CloudWatchLogs/authorization-failures-alarm.html](https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/CloudWatchLogs/authorization-failures-alarm.html)
- [https://www.tenable.com/policies/[type]/AC_AWS_0559](https://www.tenable.com/policies/[type]/AC_AWS_0559)
- [https://www.intelligentdiscovery.io/controls/cloudwatch/cloudwatch-unauthorized-api-calls](https://www.intelligentdiscovery.io/controls/cloudwatch/cloudwatch-unauthorized-api-calls)
- [https://support.icompaas.com/support/solutions/articles/62000083561-ensure-a-log-metric-filter-and-alarm-exist-for-unauthorized-api-calls](https://support.icompaas.com/support/solutions/articles/62000083561-ensure-a-log-metric-filter-and-alarm-exist-for-unauthorized-api-calls)

## 技术信息

- Source Metadata：[sources/aws/cloudwatch_log_metric_filter_unauthorized_api_calls/metadata.json](../../sources/aws/cloudwatch_log_metric_filter_unauthorized_api_calls/metadata.json)
- Source Code：[sources/aws/cloudwatch_log_metric_filter_unauthorized_api_calls/check.py](../../sources/aws/cloudwatch_log_metric_filter_unauthorized_api_calls/check.py)
- Source Metadata Path：`sources/aws/cloudwatch_log_metric_filter_unauthorized_api_calls/metadata.json`
- Source Code Path：`sources/aws/cloudwatch_log_metric_filter_unauthorized_api_calls/check.py`
