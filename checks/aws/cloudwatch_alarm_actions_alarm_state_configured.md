# CloudWatch metric alarm has actions configured for the ALARM state

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `cloudwatch_alarm_actions_alarm_state_configured` |
| 云平台 | AWS |
| 服务 | cloudwatch |
| 严重等级 | high |
| 类别 | resilience |
| 检查类型 | Software and Configuration Checks/AWS Security Best Practices |
| 资源类型 | AwsCloudWatchAlarm |
| 资源组 | monitoring |

## 描述

Amazon CloudWatch metric alarms are evaluated for **actions** configured for the `ALARM` state. The finding flags alarms that have no action to execute when their monitored metric crosses its threshold.

## 风险

Without an **ALARM action**, threshold breaches trigger no **notification** or **automated response**. This delays detection and containment, risking: - Availability: prolonged outages or missed scale-out - Integrity/confidentiality: unchecked anomalies enabling tampering or data loss

## 推荐措施

Assign at least one **ALARM-state action** per alarm (e.g., notify via SNS or run automated remediation with Lambda/SSM). Keep actions enabled, apply **least privilege** to targets, and regularly test. *For critical metrics*, add redundant paths (EventBridge) for **defense in depth**.

## 修复步骤


### CLI

```text
aws cloudwatch put-metric-alarm --alarm-name <alarm-name> --metric-name <metric-name> --namespace <namespace> --statistic <statistic> --period <period-seconds> --evaluation-periods <evaluation-periods> --threshold <threshold> --comparison-operator <comparison-operator> --alarm-actions <action-arn>
```

### Native IaC

```yaml
# CloudFormation: add an ALARM action to a metric alarm
Resources:
  <example_resource_name>:
    Type: AWS::CloudWatch::Alarm
    Properties:
      AlarmName: <example_resource_name>
      MetricName: <metric-name>
      Namespace: <namespace>
      Statistic: Average
      Period: 60
      EvaluationPeriods: 1
      Threshold: 1
      ComparisonOperator: GreaterThanThreshold
      AlarmActions:
        - <action-arn>  # CRITICAL: adds an action for ALARM state so the check passes
```

### Terraform

```hcl
# Terraform: add an ALARM action to a metric alarm
resource "aws_cloudwatch_metric_alarm" "<example_resource_name>" {
  alarm_name          = "<example_resource_name>"
  metric_name         = "<metric-name>"
  namespace           = "<namespace>"
  statistic           = "Average"
  period              = 60
  evaluation_periods  = 1
  threshold           = 1
  comparison_operator = "GreaterThanThreshold"
  alarm_actions       = ["<action-arn>"] # CRITICAL: ensures an action is configured for ALARM state
}
```

### Other

1. Open the AWS Console and go to CloudWatch > Alarms
2. Select the target alarm and choose Edit (or Modify alarm)
3. In Actions, under When alarm state is ALARM, add an action (e.g., select an SNS topic or other supported action)
4. Click Save changes

## 参考资料

- [https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.html#alarms-and-actions](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.html#alarms-and-actions)
- [https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudwatch/client/put_metric_alarm.html](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudwatch/client/put_metric_alarm.html)
- [https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/cloudwatch_metric_alarm](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/cloudwatch_metric_alarm)
- [https://docs.aws.amazon.com/securityhub/latest/userguide/cloudwatch-controls.html#cloudwatch-15](https://docs.aws.amazon.com/securityhub/latest/userguide/cloudwatch-controls.html#cloudwatch-15)
- [https://support.icompaas.com/support/solutions/articles/62000233431-ensure-cloudwatch-alarms-have-specified-actions-configured-for-the-alarm-state](https://support.icompaas.com/support/solutions/articles/62000233431-ensure-cloudwatch-alarms-have-specified-actions-configured-for-the-alarm-state)
- [https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/CloudWatch/cloudwatch-alarm-action.html](https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/CloudWatch/cloudwatch-alarm-action.html)
- [https://awscli.amazonaws.com/v2/documentation/api/2.0.34/reference/cloudwatch/put-metric-alarm.html](https://awscli.amazonaws.com/v2/documentation/api/2.0.34/reference/cloudwatch/put-metric-alarm.html)

## 技术信息

- Source Metadata：[sources/aws/cloudwatch_alarm_actions_alarm_state_configured/metadata.json](../../sources/aws/cloudwatch_alarm_actions_alarm_state_configured/metadata.json)
- Source Code：[sources/aws/cloudwatch_alarm_actions_alarm_state_configured/check.py](../../sources/aws/cloudwatch_alarm_actions_alarm_state_configured/check.py)
- Source Metadata Path：`sources/aws/cloudwatch_alarm_actions_alarm_state_configured/metadata.json`
- Source Code Path：`sources/aws/cloudwatch_alarm_actions_alarm_state_configured/check.py`
