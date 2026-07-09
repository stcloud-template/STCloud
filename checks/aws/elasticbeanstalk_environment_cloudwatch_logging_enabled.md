# Elastic Beanstalk environment streams logs to CloudWatch Logs

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `elasticbeanstalk_environment_cloudwatch_logging_enabled` |
| 云平台 | AWS |
| 服务 | elasticbeanstalk |
| 严重等级 | high |
| 类别 | logging |
| 检查类型 | Software and Configuration Checks/AWS Security Best Practices/Runtime Behavior Analysis, TTPs/Defense Evasion |
| 资源类型 | AwsElasticBeanstalkEnvironment |
| 资源组 | compute |

## 描述

**Elastic Beanstalk environments** are configured to stream instance and proxy logs to **Amazon CloudWatch Logs** via the `StreamLogs` setting

## 风险

Without **centralized logging** to CloudWatch, logs may be lost during rotation or instance termination, delaying detection and response. Attackers can delete local logs to evade audits, hiding evidence of web attacks or config tampering and undermining **confidentiality**, **integrity**, and **availability**.

## 推荐措施

Enable streaming to **CloudWatch Logs**. Set sensible retention, avoid deletion on termination, and restrict access with least-privilege IAM. Add metric filters and alerts for early detection, and retain archives to support **forensics**, **accountability**, and **defense in depth**.

## 修复步骤


### CLI

```text
aws elasticbeanstalk update-environment --environment-name <example_resource_name> --option-settings Namespace=aws:elasticbeanstalk:cloudwatch:logs,OptionName=StreamLogs,Value=true
```

### Native IaC

```yaml
Resources:
  <example_resource_name>:
    Type: AWS::ElasticBeanstalk::Environment
    Properties:
      ApplicationName: "<example_resource_name>"
      PlatformArn: "<platform_arn>"
      OptionSettings:
        - Namespace: aws:elasticbeanstalk:cloudwatch:logs
          OptionName: StreamLogs
          Value: "true"  # Critical: Enables instance log streaming to CloudWatch Logs
```

### Terraform

```hcl
resource "aws_elastic_beanstalk_environment" "<example_resource_name>" {
  name         = "<example_resource_name>"
  application  = "<example_resource_name>"
  platform_arn = "<platform_arn>"

  # Critical: Enables instance log streaming to CloudWatch Logs
  setting {
    namespace = "aws:elasticbeanstalk:cloudwatch:logs"
    name      = "StreamLogs"
    value     = "true"
  }
}
```

### Other

1. Open the AWS Elastic Beanstalk console and select your environment
2. Go to Configuration > Updates, monitoring, and logging > Edit
3. Under "Instance log streaming to CloudWatch Logs", set Log streaming to Activated
4. Click Apply to save

## 参考资料

- [https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/AWSHowTo.cloudwatchlogs.html](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/AWSHowTo.cloudwatchlogs.html)
- [https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/environments-cfg-logging.html](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/environments-cfg-logging.html)
- [https://docs.aws.amazon.com/securityhub/latest/userguide/elasticbeanstalk-controls.html#elasticbeanstalk-3](https://docs.aws.amazon.com/securityhub/latest/userguide/elasticbeanstalk-controls.html#elasticbeanstalk-3)

## 技术信息

- Source Metadata：[sources/aws/elasticbeanstalk_environment_cloudwatch_logging_enabled/metadata.json](../../sources/aws/elasticbeanstalk_environment_cloudwatch_logging_enabled/metadata.json)
- Source Code：[sources/aws/elasticbeanstalk_environment_cloudwatch_logging_enabled/check.py](../../sources/aws/elasticbeanstalk_environment_cloudwatch_logging_enabled/check.py)
- Source Metadata Path：`sources/aws/elasticbeanstalk_environment_cloudwatch_logging_enabled/metadata.json`
- Source Code Path：`sources/aws/elasticbeanstalk_environment_cloudwatch_logging_enabled/check.py`
