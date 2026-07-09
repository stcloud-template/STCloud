# Account has a CloudWatch Logs metric filter and alarm for root account usage

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `cloudwatch_log_metric_filter_root_usage` |
| 云平台 | AWS |
| 服务 | cloudwatch |
| 严重等级 | medium |
| 类别 | logging |
| 检查类型 | Software and Configuration Checks/Industry and Regulatory Standards/CIS AWS Foundations Benchmark, Software and Configuration Checks/Industry and Regulatory Standards/AWS Foundational Security Best Practices, Software and Configuration Checks/AWS Security Best Practices, TTPs/Privilege Escalation |
| 资源类型 | AwsCloudWatchAlarm |
| 资源组 | monitoring |

## 描述

**CloudTrail** logs in CloudWatch include a metric filter for **root account activity** (`{ $.userIdentity.type = "Root" && $.userIdentity.invokedBy NOT EXISTS && $.eventType != "AwsServiceEvent" }`) and a linked CloudWatch alarm that triggers when the filter matches.

## 风险

Without alerting on **root activity**, full-privilege actions can proceed unnoticed, impacting: - confidentiality via data access/exfiltration - integrity via policy/config tampering - availability via deletions or shutdowns Delayed detection increases blast radius and persistence.

## 推荐措施

Enable real-time alerts for **root activity** using a log metric filter and a high-priority alarm with notifications. Reduce exposure: enforce **least privilege**, keep root for *break-glass* with MFA, disable root access keys, and route alerts into incident response for **defense in depth**.

## 修复步骤


### Native IaC

```yaml
# CloudFormation: Create metric filter and alarm for root account usage
Resources:
  RootUsageMetricFilter:
    Type: AWS::Logs::MetricFilter
    Properties:
      LogGroupName: "<example_resource_name>"
      FilterPattern: '{ $.userIdentity.type = "Root" && $.userIdentity.invokedBy NOT EXISTS && $.eventType != "AwsServiceEvent" }'  # CRITICAL: detects root user actions not invoked by services
      MetricTransformations:
        - MetricValue: "1"
          MetricNamespace: "<example_resource_name>"  # CRITICAL: metric namespace used by the alarm
          MetricName: "<example_resource_name>"       # CRITICAL: metric name used by the alarm

  RootUsageAlarm:
    Type: AWS::CloudWatch::Alarm
    Properties:
      ComparisonOperator: GreaterThanOrEqualToThreshold
      EvaluationPeriods: 1
      MetricName: "<example_resource_name>"   # CRITICAL: alarms on the metric created by the filter
      Namespace: "<example_resource_name>"
      Period: 300
      Statistic: Sum
      Threshold: 1
```

### Terraform

```hcl
# CloudWatch Logs metric filter for root account usage
resource "aws_cloudwatch_log_metric_filter" "<example_resource_name>" {
  name           = "<example_resource_name>"
  log_group_name = "<example_resource_name>"
  pattern        = "{ $.userIdentity.type = \"Root\" && $.userIdentity.invokedBy NOT EXISTS && $.eventType != \"AwsServiceEvent\" }" # CRITICAL: detects root user actions

  metric_transformation {
    name      = "<example_resource_name>"     # CRITICAL: metric used by the alarm
    namespace = "<example_resource_name>"
    value     = "1"
  }
}

# Alarm on the root usage metric
resource "aws_cloudwatch_metric_alarm" "<example_resource_name>" {
  comparison_operator = "GreaterThanOrEqualToThreshold"
  evaluation_periods  = 1
  metric_name         = "<example_resource_name>"   # CRITICAL: matches metric filter
  namespace           = "<example_resource_name>"
  period              = 300
  statistic           = "Sum"
  threshold           = 1
}
```

### Other

1. In the AWS console, open CloudWatch > Logs > Log groups and select the CloudTrail log group
2. Go to Metric filters > Create metric filter
3. For Filter pattern, enter: { $.userIdentity.type = "Root" && $.userIdentity.invokedBy NOT EXISTS && $.eventType != "AwsServiceEvent" }
4. Click Next, set any Filter name, set Metric namespace and Metric name, set Metric value to 1, then Create metric filter
5. Select the new metric filter and click Create alarm
6. Set Period to 5 minutes, Statistic to Sum, Threshold type Static with value 1, Evaluation periods 1, then Create alarm

## 参考资料

- [https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudwatch-alarms-for-cloudtrail.html](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudwatch-alarms-for-cloudtrail.html)
- [https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/CloudWatchLogs/root-account-usage-alarm.html](https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/CloudWatchLogs/root-account-usage-alarm.html)
- [https://asecure.cloud/a/root_account_login/](https://asecure.cloud/a/root_account_login/)
- [https://support.icompaas.com/support/solutions/articles/62000083624-ensure-a-log-metric-filter-and-alarm-exist-for-usage-of-root-account](https://support.icompaas.com/support/solutions/articles/62000083624-ensure-a-log-metric-filter-and-alarm-exist-for-usage-of-root-account)
- [https://www.intelligentdiscovery.io/controls/cloudwatch/cloudwatch-alarm-root-account-usage](https://www.intelligentdiscovery.io/controls/cloudwatch/cloudwatch-alarm-root-account-usage)
- [https://aws.amazon.com/blogs/security/how-to-receive-notifications-when-your-aws-accounts-root-access-keys-are-used/](https://aws.amazon.com/blogs/security/how-to-receive-notifications-when-your-aws-accounts-root-access-keys-are-used/)
- [https://www.tenable.com/audits/items/CIS_Amazon_Web_Services_Foundations_v1.5.0_L1.audit:000adfb028a1475075a6b5d2117f53f4](https://www.tenable.com/audits/items/CIS_Amazon_Web_Services_Foundations_v1.5.0_L1.audit:000adfb028a1475075a6b5d2117f53f4)

## 技术信息

- Source Metadata：[sources/aws/cloudwatch_log_metric_filter_root_usage/metadata.json](../../sources/aws/cloudwatch_log_metric_filter_root_usage/metadata.json)
- Source Code：[sources/aws/cloudwatch_log_metric_filter_root_usage/check.py](../../sources/aws/cloudwatch_log_metric_filter_root_usage/check.py)
- Source Metadata Path：`sources/aws/cloudwatch_log_metric_filter_root_usage/metadata.json`
- Source Code Path：`sources/aws/cloudwatch_log_metric_filter_root_usage/check.py`
