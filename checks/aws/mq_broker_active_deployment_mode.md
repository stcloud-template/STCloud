# Apache ActiveMQ broker is configured in active/standby Multi-AZ deployment mode

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `mq_broker_active_deployment_mode` |
| 云平台 | AWS |
| 服务 | mq |
| 严重等级 | low |
| 类别 | resilience |
| 检查类型 | Software and Configuration Checks/AWS Security Best Practices, Software and Configuration Checks/Industry and Regulatory Standards/AWS Foundational Security Best Practices, Software and Configuration Checks/Industry and Regulatory Standards/NIST 800-53 Controls, Effects/Denial of Service |
| 资源类型 | AwsAmazonMQBroker |
| 资源组 | messaging |

## 描述

**ActiveMQ broker deployment mode** is configured as **active/standby** (`ACTIVE_STANDBY_MULTI_AZ`), indicating a redundant pair operating across Availability Zones

## 风险

Without **active/standby**, a single-instance broker becomes a **single point of failure**, degrading **availability** and risking **message loss or duplication** during outages or maintenance. This can stall message flows, grow backlogs, and cause inconsistent processing across dependent services.

## 推荐措施

Adopt **active/standby deployment** for ActiveMQ brokers to provide multi-AZ resilience. Design clients for **failover** with retries and idempotent processing, validate recovery through regular **failover testing**, monitor broker health, and apply **least privilege** to limit blast radius.

## 修复步骤


### Native IaC

```yaml
# CloudFormation: Create an ActiveMQ broker in active/standby Multi-AZ
Resources:
  <example_resource_name>:
    Type: AWS::AmazonMQ::Broker
    Properties:
      BrokerName: <example_resource_name>
      EngineType: ACTIVEMQ
      EngineVersion: <example_resource_name>
      HostInstanceType: mq.t3.micro
      PubliclyAccessible: false
      DeploymentMode: ACTIVE_STANDBY_MULTI_AZ  # Critical: sets active/standby Multi-AZ to pass the check
      SubnetIds:
        - <example_resource_id>
        - <example_resource_id>  # Critical: two subnets in different AZs required for active/standby
      SecurityGroups:
        - <example_resource_id>
      Users:
        - Username: <example_resource_name>
          Password: <example_resource_id>
```

### Terraform

```hcl
# Create an ActiveMQ broker in active/standby Multi-AZ
resource "aws_mq_broker" "<example_resource_name>" {
  broker_name         = "<example_resource_name>"
  engine_type         = "ActiveMQ"
  engine_version      = "<example_resource_name>"
  host_instance_type  = "mq.t3.micro"
  publicly_accessible = false
  deployment_mode     = "ACTIVE_STANDBY_MULTI_AZ"  # Critical: enables active/standby Multi-AZ to pass the check

  subnet_ids      = ["<example_resource_id>", "<example_resource_id>"]  # Critical: two subnets in different AZs
  security_groups = ["<example_resource_id>"]

  user {
    username = "<example_resource_name>"
    password = "<example_resource_id>"
  }
}
```

### Other

1. In the AWS Console, go to Amazon MQ > Brokers > Create broker
2. Select Engine: ActiveMQ
3. Set Deployment mode to Active/standby broker (Multi-AZ)
4. Choose two subnets in different AZs and a security group
5. Enter a broker name, instance type, and create a user (username/password)
6. Create the broker, update clients to use the new endpoints, then delete the old single-instance broker

## 参考资料

- [https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/MQ/deployment-mode.html](https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/MQ/deployment-mode.html)
- [https://docs.aws.amazon.com/amazon-mq/latest/developer-guide/amazon-mq-basic-elements.html](https://docs.aws.amazon.com/amazon-mq/latest/developer-guide/amazon-mq-basic-elements.html)
- [https://docs.aws.amazon.com/securityhub/latest/userguide/mq-controls.html#mq-5](https://docs.aws.amazon.com/securityhub/latest/userguide/mq-controls.html#mq-5)
- [https://docs.aws.amazon.com/amazon-mq/latest/developer-guide/amazon-mq-broker-architecture.html#active-standby-broker-deployment](https://docs.aws.amazon.com/amazon-mq/latest/developer-guide/amazon-mq-broker-architecture.html#active-standby-broker-deployment)

## 技术信息

- Source Metadata：[sources/aws/mq_broker_active_deployment_mode/metadata.json](../../sources/aws/mq_broker_active_deployment_mode/metadata.json)
- Source Code：[sources/aws/mq_broker_active_deployment_mode/check.py](../../sources/aws/mq_broker_active_deployment_mode/check.py)
- Source Metadata Path：`sources/aws/mq_broker_active_deployment_mode/metadata.json`
- Source Code Path：`sources/aws/mq_broker_active_deployment_mode/check.py`
