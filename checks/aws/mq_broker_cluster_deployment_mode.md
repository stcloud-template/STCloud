# MQ RabbitMQ broker has cluster (multi-AZ) deployment mode

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `mq_broker_cluster_deployment_mode` |
| 云平台 | AWS |
| 服务 | mq |
| 严重等级 | medium |
| 类别 | resilience |
| 检查类型 | Software and Configuration Checks/AWS Security Best Practices, Software and Configuration Checks/Industry and Regulatory Standards/NIST 800-53 Controls, Effects/Denial of Service |
| 资源类型 | AwsAmazonMQBroker |
| 资源组 | messaging |

## 描述

**Amazon MQ RabbitMQ brokers** are assessed for **cluster deployment mode** (`CLUSTER_MULTI_AZ`) with nodes spread across multiple AZs and shared state. Brokers configured otherwise are identified.

## 风险

Without **clustered RabbitMQ**, the broker is a **single point of failure**. An instance or AZ outage can halt queues, cause message loss or duplication, and break ordering, reducing **availability** and **integrity** of workloads that depend on the broker.

## 推荐措施

Use **cluster deployment** (`CLUSTER_MULTI_AZ`) for RabbitMQ to remove single-instance risk. Apply **resiliency by design**: clients auto-reconnect, retries with backoff, and idempotent processing; test failover, size for node loss, and enforce **least privilege** with monitoring for defense in depth.

## 修复步骤


### CLI

```text
aws mq create-broker --broker-name <example_resource_name> --engine-type RABBITMQ --deployment-mode CLUSTER_MULTI_AZ --host-instance-type mq.m5.large --publicly-accessible --auto-minor-version-upgrade --users '[{"Username":"<example_username>","Password":"<example_password>"}]'
```

### Native IaC

```yaml
# CloudFormation: create a RabbitMQ broker in cluster (Multi-AZ) mode
Resources:
  ExampleBroker:
    Type: AWS::AmazonMQ::Broker
    Properties:
      BrokerName: "<example_resource_name>"
      EngineType: RABBITMQ            # Critical: ensures the broker is RabbitMQ
      DeploymentMode: CLUSTER_MULTI_AZ # Critical: sets cluster (Multi-AZ) to pass the check
      HostInstanceType: mq.m5.large
      PubliclyAccessible: true
      Users:
        - Username: "<example_username>"
          Password: "<example_password>"
```

### Terraform

```hcl
# Terraform: create a RabbitMQ broker in cluster (Multi-AZ) mode
resource "aws_mq_broker" "example" {
  broker_name         = "<example_resource_name>"
  engine_type         = "RabbitMQ"         # Critical: RabbitMQ engine
  deployment_mode     = "CLUSTER_MULTI_AZ" # Critical: cluster (Multi-AZ) to pass the check
  host_instance_type  = "mq.m5.large"
  publicly_accessible = true

  user {
    username = "<example_username>"
    password = "<example_password>"
  }
}
```

### Other

1. Open the AWS Console and go to Amazon MQ
2. Click Brokers > Create broker
3. Select RabbitMQ as the engine
4. Set Deployment mode to Cluster (Multi-AZ)
5. Enter a broker name, choose an instance type, set Public access as needed, and create one admin user
6. Click Create broker
7. Migrate applications to the new broker endpoint, then delete the old single-instance broker

Note: Deployment mode cannot be changed on an existing broker; you must create a new cluster broker.

## 参考资料

- [https://docs.aws.amazon.com/amazon-mq/latest/developer-guide/rabbitmq-basic-elements.html](https://docs.aws.amazon.com/amazon-mq/latest/developer-guide/rabbitmq-basic-elements.html)
- [https://docs.aws.amazon.com/securityhub/latest/userguide/mq-controls.html#mq-6](https://docs.aws.amazon.com/securityhub/latest/userguide/mq-controls.html#mq-6)
- [https://docs.aws.amazon.com/amazon-mq/latest/developer-guide/rabbitmq-broker-architecture.html#rabbitmq-broker-architecture-cluster](https://docs.aws.amazon.com/amazon-mq/latest/developer-guide/rabbitmq-broker-architecture.html#rabbitmq-broker-architecture-cluster)
- [https://docs.amazonaws.cn/en_us/AWSCloudFormation/latest/TemplateReference/aws-resource-amazonmq-broker.html](https://docs.amazonaws.cn/en_us/AWSCloudFormation/latest/TemplateReference/aws-resource-amazonmq-broker.html)
- [https://docs.aws.amazon.com/controltower/latest/controlreference/mq-rules.html](https://docs.aws.amazon.com/controltower/latest/controlreference/mq-rules.html)

## 技术信息

- Source Metadata：[sources/aws/mq_broker_cluster_deployment_mode/metadata.json](../../sources/aws/mq_broker_cluster_deployment_mode/metadata.json)
- Source Code：[sources/aws/mq_broker_cluster_deployment_mode/check.py](../../sources/aws/mq_broker_cluster_deployment_mode/check.py)
- Source Metadata Path：`sources/aws/mq_broker_cluster_deployment_mode/metadata.json`
- Source Code Path：`sources/aws/mq_broker_cluster_deployment_mode/check.py`
