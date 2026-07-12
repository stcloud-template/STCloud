# Elastic Beanstalk environment streams logs to CloudWatch Logs

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `elasticbeanstalk_environment_cloudwatch_logging_enabled` |
| クラウドプラットフォーム | AWS |
| サービス | elasticbeanstalk |
| 重大度 | high |
| カテゴリ | logging |
| チェックタイプ | Software and Configuration Checks/AWS Security Best Practices/Runtime Behavior Analysis, TTPs/Defense Evasion |
| リソースタイプ | AwsElasticBeanstalkEnvironment |
| リソースグループ | compute |

## 説明

**Elastic Beanstalk environments** are configured to stream instance and proxy logs to **Amazon CloudWatch Logs** via the `StreamLogs` setting

## リスク

Without **centralized logging** to CloudWatch, logs may be lost during rotation or instance termination, delaying detection and response. Attackers can delete local logs to evade audits, hiding evidence of web attacks or config tampering and undermining **confidentiality**, **integrity**, and **availability**.

## 推奨事項

Enable streaming to **CloudWatch Logs**. Set sensible retention, avoid deletion on termination, and restrict access with least-privilege IAM. Add metric filters and alerts for early detection, and retain archives to support **forensics**, **accountability**, and **defense in depth**.

## 修正手順


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

## 参考資料

- [https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/AWSHowTo.cloudwatchlogs.html](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/AWSHowTo.cloudwatchlogs.html)
- [https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/environments-cfg-logging.html](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/environments-cfg-logging.html)
- [https://docs.aws.amazon.com/securityhub/latest/userguide/elasticbeanstalk-controls.html#elasticbeanstalk-3](https://docs.aws.amazon.com/securityhub/latest/userguide/elasticbeanstalk-controls.html#elasticbeanstalk-3)

## 技術情報

- Source Metadata：[sources/aws/elasticbeanstalk_environment_cloudwatch_logging_enabled/metadata.json](../../sources/aws/elasticbeanstalk_environment_cloudwatch_logging_enabled/metadata.json)
- Source Code：[sources/aws/elasticbeanstalk_environment_cloudwatch_logging_enabled/check.py](../../sources/aws/elasticbeanstalk_environment_cloudwatch_logging_enabled/check.py)
- Source Metadata Path：`sources/aws/elasticbeanstalk_environment_cloudwatch_logging_enabled/metadata.json`
- Source Code Path：`sources/aws/elasticbeanstalk_environment_cloudwatch_logging_enabled/check.py`
