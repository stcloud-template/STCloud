# Amazon MQ broker is not publicly accessible

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `mq_broker_not_publicly_accessible` |
| 云平台 | AWS |
| 服务 | mq |
| 严重等级 | high |
| 类别 | internet-exposed |
| 检查类型 | Software and Configuration Checks/AWS Security Best Practices/Network Reachability, Software and Configuration Checks/Industry and Regulatory Standards/AWS Foundational Security Best Practices, Software and Configuration Checks/Industry and Regulatory Standards/NIST 800-53 Controls, TTPs/Initial Access, Effects/Data Exposure |
| 资源类型 | AwsAmazonMQBroker |
| 资源组 | messaging |

## 描述

**Amazon MQ brokers** are evaluated for **public accessibility**, determining whether a broker exposes a public endpoint or is restricted to VPC-only connectivity via its `publicly accessible` setting.

## 风险

**Publicly reachable brokers** expand exposure: internet hosts can probe protocols and consoles, attempt credential spraying, publish/consume messages, and flood connections. This threatens **confidentiality** (data leakage), **integrity** (message tampering), and **availability** (DoS/resource exhaustion).

## 推荐措施

Prefer private deployment: set `publicly_accessible=false`, place brokers in private subnets, and restrict security groups to trusted producers/consumers. Use private connectivity (VPC endpoints, peering, VPN/Direct Connect). Enforce strong authn and authorization maps, and allow only required protocol ports. Apply **least privilege**.

## 修复步骤


### Native IaC

```yaml
# CloudFormation: Amazon MQ broker without public accessibility
Resources:
  <example_resource_name>:
    Type: AWS::AmazonMQ::Broker
    Properties:
      BrokerName: <example_resource_name>
      EngineType: ACTIVEMQ
      EngineVersion: <example_engine_version>
      HostInstanceType: <example_instance_type>
      PubliclyAccessible: false  # Critical: disables public internet access
      Users:
        - Username: <example_username>
          Password: <example_password>
      SubnetIds:
        - <example_subnet_id>
      SecurityGroups:
        - <example_security_group_id>
      AutoMinorVersionUpgrade: true
```

### Terraform

```hcl
# Amazon MQ broker without public accessibility
resource "aws_mq_broker" "<example_resource_name>" {
  broker_name         = "<example_resource_name>"
  engine_type         = "ActiveMQ"
  engine_version      = "<example_engine_version>"
  host_instance_type  = "<example_instance_type>"
  publicly_accessible = false # Critical: disables public internet access
  security_groups     = ["<example_security_group_id>"]
  subnet_ids          = ["<example_subnet_id>"]

  user {
    username = "<example_username>"
    password = "<example_password>"
  }
}
```

### Other

1. Open the AWS Console and go to Amazon MQ
2. Create a new broker and set Public accessibility to Disabled/No
3. Point your clients to the new broker's private endpoints
4. Delete the old publicly accessible broker

## 参考资料

- [https://docs.aws.amazon.com/amazon-mq/latest/developer-guide/using-amazon-mq-securely.html#prefer-brokers-without-public-accessibility](https://docs.aws.amazon.com/amazon-mq/latest/developer-guide/using-amazon-mq-securely.html#prefer-brokers-without-public-accessibility)
- [https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/MQ/publicly-accessible.html#](https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/MQ/publicly-accessible.html#)

## 技术信息

- Source Metadata：[sources/aws/mq_broker_not_publicly_accessible/metadata.json](../../sources/aws/mq_broker_not_publicly_accessible/metadata.json)
- Source Code：[sources/aws/mq_broker_not_publicly_accessible/check.py](../../sources/aws/mq_broker_not_publicly_accessible/check.py)
- Source Metadata Path：`sources/aws/mq_broker_not_publicly_accessible/metadata.json`
- Source Code Path：`sources/aws/mq_broker_not_publicly_accessible/check.py`
