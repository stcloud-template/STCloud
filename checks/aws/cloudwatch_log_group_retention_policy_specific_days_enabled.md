# CloudWatch log group has a retention policy of at least the configured minimum days or never expires

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `cloudwatch_log_group_retention_policy_specific_days_enabled` |
| 云平台 | AWS |
| 服务 | cloudwatch |
| 严重等级 | medium |
| 类别 | logging, forensics-ready |
| 检查类型 | Software and Configuration Checks/AWS Security Best Practices, Software and Configuration Checks/Industry and Regulatory Standards/AWS Foundational Security Best Practices, Software and Configuration Checks/Industry and Regulatory Standards/NIST 800-53 Controls (USA), Software and Configuration Checks/Industry and Regulatory Standards/PCI-DSS, Software and Configuration Checks/Industry and Regulatory Standards/SOC 2 |
| 资源类型 | AwsLogsLogGroup |
| 资源组 | monitoring |

## 描述

**CloudWatch Log Groups** are assessed for a retention period at or above the configured threshold (e.g., `365` days) or for being set to **never expire**. Log groups with shorter retention are identified.

## 风险

Short log retention erodes audit evidence. Adversaries can wait out the window, creating gaps in detection, forensics, and compliance reporting. This degrades the **availability** of historical logs and the **integrity** of incident timelines.

## 推荐措施

Define a minimum retention baseline (e.g., `>=365` days) aligned to legal and investigative needs. Apply it consistently with documented exceptions. Automate enforcement, monitor changes, and restrict who can modify retention under **least privilege** and **defense in depth**.

## 修复步骤


### CLI

```text
aws logs put-retention-policy --log-group-name <LOG_GROUP_NAME> --retention-in-days <DAYS>
```

### Native IaC

```yaml
# CloudFormation: set retention on a CloudWatch Log Group
Resources:
  <example_resource_name>:
    Type: AWS::Logs::LogGroup
    Properties:
      LogGroupName: "<example_resource_name>"
      RetentionInDays: <DAYS>  # Critical: sets log retention to the required minimum to pass the check
```

### Terraform

```hcl
# Set retention on a CloudWatch Log Group
resource "aws_cloudwatch_log_group" "<example_resource_name>" {
  name              = "<example_resource_name>"
  retention_in_days = <DAYS> # Critical: set to at least the required minimum to pass the check
}
```

### Other

1. In the AWS Console, go to CloudWatch > Log groups
2. Select the target log group
3. In the Expire events after/Retention column, click the current value
4. Choose a retention value >= <DAYS> or select Never expire
5. Click Save

## 参考资料

- [https://trendmicro.com/cloudoneconformity/knowledge-base/aws/CloudWatchLogs/cloudwatch-logs-retention-period.html](https://trendmicro.com/cloudoneconformity/knowledge-base/aws/CloudWatchLogs/cloudwatch-logs-retention-period.html)
- [https://boto3.amazonaws.com/v1/documentation/api/1.26.93/reference/services/logs/client/put_retention_policy.html](https://boto3.amazonaws.com/v1/documentation/api/1.26.93/reference/services/logs/client/put_retention_policy.html)
- [https://medium.com/pareture/aws-cloudwatch-log-group-retention-periods-bb8a2fb9c358](https://medium.com/pareture/aws-cloudwatch-log-group-retention-periods-bb8a2fb9c358)
- [https://www.blinkops.com/blog/cloudwatch-retention](https://www.blinkops.com/blog/cloudwatch-retention)
- [https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_Logs.html](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_Logs.html)

## 技术信息

- Source Metadata：[sources/aws/cloudwatch_log_group_retention_policy_specific_days_enabled/metadata.json](../../sources/aws/cloudwatch_log_group_retention_policy_specific_days_enabled/metadata.json)
- Source Code：[sources/aws/cloudwatch_log_group_retention_policy_specific_days_enabled/check.py](../../sources/aws/cloudwatch_log_group_retention_policy_specific_days_enabled/check.py)
- Source Metadata Path：`sources/aws/cloudwatch_log_group_retention_policy_specific_days_enabled/metadata.json`
- Source Code Path：`sources/aws/cloudwatch_log_group_retention_policy_specific_days_enabled/check.py`
