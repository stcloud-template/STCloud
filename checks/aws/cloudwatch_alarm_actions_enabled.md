# CloudWatch metric alarm has actions enabled

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `cloudwatch_alarm_actions_enabled` |
| クラウドプラットフォーム | AWS |
| サービス | cloudwatch |
| 重大度 | high |
| カテゴリ | resilience |
| チェックタイプ | Software and Configuration Checks/AWS Security Best Practices, Industry and Regulatory Standards/AWS Foundational Security Best Practices, TTPs/Defense Evasion |
| リソースタイプ | AwsCloudWatchAlarm |
| リソースグループ | monitoring |

## 説明

**CloudWatch metric alarms** are evaluated for **alarm actions** activation (`actions_enabled: true`), enabling state changes to invoke configured notifications or automated responses.

## リスク

With alarm actions disabled, state changes neither notify nor remediate. Incidents can persist unnoticed, enabling unauthorized activity, configuration drift, or capacity exhaustion. Visibility drops, MTTR rises, and confidentiality, integrity, and availability are all at greater risk.

## 推奨事項

Enable `actions_enabled` on critical alarms and attach least-privilege actions (SNS, automation) for ALARM and recovery states. Use redundant targets, regularly test notifications, and integrate with incident response. Apply **defense in depth** with complementary detections to ensure timely, reliable alerting.

## 修正手順


### CLI

```text
aws cloudwatch enable-alarm-actions --alarm-names <alarm-name>
```

### Native IaC

```yaml
Resources:
  <example_resource_name>:
    Type: AWS::CloudWatch::Alarm
    Properties:
      ActionsEnabled: true  # FIX: activates alarm actions so the check passes
      ComparisonOperator: GreaterThanThreshold
      EvaluationPeriods: 1
      MetricName: <example_metric_name>
      Namespace: <example_metric_namespace>
      Period: 60
      Statistic: Average
      Threshold: 1
```

### Terraform

```hcl
resource "aws_cloudwatch_metric_alarm" "<example_resource_name>" {
  alarm_name          = "<example_resource_name>"
  comparison_operator = "GreaterThanThreshold"
  evaluation_periods  = 1
  metric_name         = "<example_metric_name>"
  namespace           = "<example_metric_namespace>"
  period              = 60
  statistic           = "Average"
  threshold           = 1

  actions_enabled = true  # FIX: activates alarm actions so the check passes
}
```

### Other

1. Open the CloudWatch console
2. Go to Alarms > All alarms and select the alarm
3. Choose Actions > Alarm actions - new > Enable
4. Confirm to activate actions

## 参考資料

- [https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/CloudWatch/cloudwatch-alarm-action-activated.html](https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/CloudWatch/cloudwatch-alarm-action-activated.html)
- [https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.html#alarms-and-actions](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.html#alarms-and-actions)
- [https://docs.aws.amazon.com/securityhub/latest/userguide/cloudwatch-controls.html#cloudwatch-17](https://docs.aws.amazon.com/securityhub/latest/userguide/cloudwatch-controls.html#cloudwatch-17)

## 技術情報

- Source Metadata：[sources/aws/cloudwatch_alarm_actions_enabled/metadata.json](../../sources/aws/cloudwatch_alarm_actions_enabled/metadata.json)
- Source Code：[sources/aws/cloudwatch_alarm_actions_enabled/check.py](../../sources/aws/cloudwatch_alarm_actions_enabled/check.py)
- Source Metadata Path：`sources/aws/cloudwatch_alarm_actions_enabled/metadata.json`
- Source Code Path：`sources/aws/cloudwatch_alarm_actions_enabled/check.py`
