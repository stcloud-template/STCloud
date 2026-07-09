# Amazon Athena workgroup has CloudWatch logging enabled

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `athena_workgroup_logging_enabled` |
| 云平台 | AWS |
| 服务 | athena |
| 严重等级 | medium |
| 类别 | logging |
| 检查类型 | Software and Configuration Checks/AWS Security Best Practices, Software and Configuration Checks/Industry and Regulatory Standards/AWS Foundational Security Best Practices, TTPs/Defense Evasion |
| 资源类型 | AwsAthenaWorkGroup |
| 资源组 | analytics |

## 描述

**Athena workgroups** publish **query metrics** to CloudWatch. This evaluation determines whether each workgroup has query activity logging enabled in CloudWatch.

## 风险

Without CloudWatch query logging, risky or anomalous queries go unobserved, weakening **confidentiality** and **integrity**. Compromised or insider accounts can exfiltrate data and alter datasets without timely detection, hampering forensics and containment.

## 推荐措施

Enable and enforce **CloudWatch query logging** for all workgroups (`PublishCloudWatchMetricsEnabled`). - Apply least privilege to logs and encrypt at rest - Set retention and anomaly alerts - Correlate with **CloudTrail** for user attribution - Centralize logs to a monitoring account

## 修复步骤


### CLI

```text
aws athena update-work-group --work-group <WORKGROUP_NAME> --configuration-updates PublishCloudWatchMetricsEnabled=true
```

### Native IaC

```yaml
# CloudFormation to enable CloudWatch logging for an Athena workgroup
Resources:
  AthenaWorkGroup:
    Type: AWS::Athena::WorkGroup
    Properties:
      Name: <example_resource_name>
      WorkGroupConfiguration:
        PublishCloudWatchMetricsEnabled: true  # Critical: Enables CloudWatch logging for the workgroup
```

### Terraform

```hcl
# Enable CloudWatch logging for an Athena workgroup
resource "aws_athena_workgroup" "example" {
  name = "<example_resource_name>"

  configuration {
    publish_cloudwatch_metrics_enabled = true  # Critical: Enables CloudWatch logging
  }
}
```

### Other

1. Open the AWS Management Console and go to Amazon Athena
2. In the left pane, click Workgroups and select the target workgroup
3. Click Edit
4. Check Publish query metrics to AWS CloudWatch
5. Click Save

## 参考资料

- [https://docs.aws.amazon.com/athena/latest/ug/security-logging-monitoring.html](https://docs.aws.amazon.com/athena/latest/ug/security-logging-monitoring.html)
- [https://docs.aws.amazon.com/athena/latest/ug/athena-cloudwatch-metrics-enable.html](https://docs.aws.amazon.com/athena/latest/ug/athena-cloudwatch-metrics-enable.html)
- [https://stackoverflow.com/questions/68896809/how-to-save-queries-executed-by-athena-in-logsgroup-cloudwatch](https://stackoverflow.com/questions/68896809/how-to-save-queries-executed-by-athena-in-logsgroup-cloudwatch)
- [https://support.icompaas.com/support/solutions/articles/62000233405-ensure-that-logging-is-enabled-for-amazon-athena-workgroups-to-capture-query-activity-](https://support.icompaas.com/support/solutions/articles/62000233405-ensure-that-logging-is-enabled-for-amazon-athena-workgroups-to-capture-query-activity-)
- [https://docs.aws.amazon.com/securityhub/latest/userguide/athena-controls.html#athena-4](https://docs.aws.amazon.com/securityhub/latest/userguide/athena-controls.html#athena-4)

## 技术信息

- Source Metadata：[sources/aws/athena_workgroup_logging_enabled/metadata.json](../../sources/aws/athena_workgroup_logging_enabled/metadata.json)
- Source Code：[sources/aws/athena_workgroup_logging_enabled/check.py](../../sources/aws/athena_workgroup_logging_enabled/check.py)
- Source Metadata Path：`sources/aws/athena_workgroup_logging_enabled/metadata.json`
- Source Code Path：`sources/aws/athena_workgroup_logging_enabled/check.py`
