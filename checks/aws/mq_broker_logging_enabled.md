# MQ broker has general logging enabled and, for ActiveMQ, audit logging enabled

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `mq_broker_logging_enabled` |
| クラウドプラットフォーム | AWS |
| サービス | mq |
| 重大度 | low |
| カテゴリ | logging |
| チェックタイプ | Software and Configuration Checks/AWS Security Best Practices, Software and Configuration Checks/Industry and Regulatory Standards/NIST 800-53 Controls, Software and Configuration Checks/Industry and Regulatory Standards/AWS Foundational Security Best Practices |
| リソースタイプ | AwsAmazonMQBroker |
| リソースグループ | messaging |

## 説明

**Amazon MQ brokers** have logging to **CloudWatch Logs** enabled per engine type: **ActiveMQ** requires both `general` and `audit` logs; **RabbitMQ** requires `general` logs.

## リスク

Missing broker logs creates blind spots in authentication events, administrative changes, and broker failures. Adversaries can act without detection, enabling unauthorized access and message tampering (confidentiality/integrity) and hindering incident response and root-cause analysis (availability).

## 推奨事項

Enable centralized **CloudWatch Logs** for brokers. For **ActiveMQ**, turn on both `general` and `audit` logs; for **RabbitMQ**, enable `general` logs. Apply **least privilege** to log access, set retention, and create alerts for anomalous events to strengthen **defense in depth**.

## 修正手順


### CLI

```text
aws mq update-broker --broker-id <example_resource_id> --logs Audit=true,General=true
```

### Native IaC

```yaml
# CloudFormation: Enable Amazon MQ logging
Resources:
  <example_resource_name>:
    Type: AWS::AmazonMQ::Broker
    Properties:
      BrokerName: <example_resource_name>
      EngineType: ACTIVEMQ
      HostInstanceType: mq.t3.micro
      DeploymentMode: SINGLE_INSTANCE
      PubliclyAccessible: true
      Users:
        - Username: <example_user>
          Password: <example_password>
      Logs:
        General: true  # Critical: enables general logs to CloudWatch
        Audit: true    # Critical: enables audit logs (required for ActiveMQ)
```

### Terraform

```hcl
# Terraform: Enable Amazon MQ logging
resource "aws_mq_broker" "<example_resource_name>" {
  broker_name         = "<example_resource_name>"
  engine_type         = "ActiveMQ"
  host_instance_type  = "mq.t3.micro"
  deployment_mode     = "SINGLE_INSTANCE"
  publicly_accessible = true

  user {
    username = "<example_user>"
    password = "<example_password>"
  }

  logs {
    general = true  # Critical: enables general logs
    audit   = true  # Critical: enables audit logs (ActiveMQ)
  }
}
```

### Other

1. In the AWS Console, go to Amazon MQ > Brokers
2. Select <example_resource_name> and choose Edit
3. In Log settings:
   - For ActiveMQ: enable General logs and Audit logs
   - For RabbitMQ: enable General logs only
4. Save changes and reboot if prompted

## 参考資料

- [https://docs.aws.amazon.com/amazon-mq/latest/developer-guide/configure-logging-monitoring-activemq.html](https://docs.aws.amazon.com/amazon-mq/latest/developer-guide/configure-logging-monitoring-activemq.html)
- [https://docs.aws.amazon.com/securityhub/latest/userguide/mq-controls.html#mq-2](https://docs.aws.amazon.com/securityhub/latest/userguide/mq-controls.html#mq-2)
- [https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/MQ/log-exports.html](https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/MQ/log-exports.html)
- [https://docs.aws.amazon.com/cli/latest/reference/mq/create-broker.html](https://docs.aws.amazon.com/cli/latest/reference/mq/create-broker.html)
- [https://docs.aws.amazon.com/amazon-mq/latest/developer-guide/security-logging-monitoring.html](https://docs.aws.amazon.com/amazon-mq/latest/developer-guide/security-logging-monitoring.html)

## 技術情報

- Source Metadata：[sources/aws/mq_broker_logging_enabled/metadata.json](../../sources/aws/mq_broker_logging_enabled/metadata.json)
- Source Code：[sources/aws/mq_broker_logging_enabled/check.py](../../sources/aws/mq_broker_logging_enabled/check.py)
- Source Metadata Path：`sources/aws/mq_broker_logging_enabled/metadata.json`
- Source Code Path：`sources/aws/mq_broker_logging_enabled/check.py`
