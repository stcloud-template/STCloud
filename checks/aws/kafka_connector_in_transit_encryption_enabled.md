# MSK Connect connector has encryption in transit enabled

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `kafka_connector_in_transit_encryption_enabled` |
| 云平台 | AWS |
| 服务 | kafka |
| 严重等级 | high |
| 类别 | encryption |
| 检查类型 | Software and Configuration Checks/AWS Security Best Practices, Software and Configuration Checks/Industry and Regulatory Standards/AWS Foundational Security Best Practices |
| 资源类型 | Other |
| 资源组 | messaging |

## 描述

**MSK Connect connectors** are evaluated for **in-transit encryption** using `TLS` on client connections to Kafka brokers and connected systems.

## 风险

Without **TLS**, data streams can be **intercepted** or **modified** in transit. Attackers on the path can perform **man-in-the-middle**, replay, or message **tampering**, exposing records and secrets. This degrades **confidentiality** and **integrity** and can enable unauthorized access to downstream systems.

## 推荐措施

Require **TLS** for all connector communications and disallow plaintext. Prefer private connectivity, validate certificates, and use modern cipher suites. Pair with **mutual authentication** and **least privilege** roles for defense-in-depth. Regularly review connector configs to avoid non-TLS endpoints.

## 修复步骤


### Native IaC

```yaml
# CloudFormation: MSK Connect connector with in-transit encryption enabled
Resources:
  <example_resource_name>:
    Type: AWS::KafkaConnect::Connector
    Properties:
      ConnectorName: <example_resource_name>
      KafkaCluster:
        ApacheKafkaCluster:
          BootstrapServers: <BOOTSTRAP_SERVERS>
          Vpc:
            SecurityGroups: [<example_resource_id>]
            Subnets: [<example_resource_id>]
      KafkaClusterClientAuthentication:
        AuthenticationType: NONE
      KafkaClusterEncryptionInTransit:
        EncryptionType: TLS  # Critical: enables TLS encryption in transit
      KafkaConnectVersion: <KAFKA_CONNECT_VERSION>
      Plugins:
        - CustomPlugin:
            CustomPluginArn: <example_resource_id>
            Revision: 1
      Capacity:
        ProvisionedCapacity:
          McuCount: 1
          WorkerCount: 1
      ServiceExecutionRoleArn: <example_resource_id>
      ConnectorConfiguration:
        connector.class: <CONNECTOR_CLASS>
        tasks.max: "1"
```

### Terraform

```hcl
# Terraform: MSK Connect connector with in-transit encryption enabled
resource "aws_mskconnect_connector" "<example_resource_name>" {
  name                  = "<example_resource_name>"
  kafkaconnect_version  = "<KAFKA_CONNECT_VERSION>"

  kafka_cluster {
    apache_kafka_cluster {
      bootstrap_servers = "<BOOTSTRAP_SERVERS>"
      vpc {
        security_groups = ["<example_resource_id>"]
        subnets         = ["<example_resource_id>"]
      }
    }
  }

  kafka_cluster_client_authentication {
    authentication_type = "NONE"
  }

  kafka_cluster_encryption_in_transit {
    encryption_type = "TLS"  # Critical: enables TLS encryption in transit
  }

  capacity {
    provisioned_capacity {
      mcu_count    = 1
      worker_count = 1
    }
  }

  service_execution_role_arn = "<example_resource_id>"

  connector_configuration = {
    "connector.class" = "<CONNECTOR_CLASS>"
    "tasks.max"       = "1"
  }

  plugin {
    custom_plugin {
      arn      = "<example_resource_id>"
      revision = 1
    }
  }
}
```

### Other

1. In the AWS console, go to Amazon MSK > MSK Connect > Connectors
2. Select the non-TLS connector and choose Delete (encryption setting can't be changed)
3. Choose Create connector and select your custom plugin and cluster
4. In the Security section, set Encryption in transit to TLS (required)
5. Complete other required fields and Create the connector

## 参考资料

- [https://docs.aws.amazon.com/msk/latest/developerguide/msk-connect.html](https://docs.aws.amazon.com/msk/latest/developerguide/msk-connect.html)
- [https://docs.aws.amazon.com/msk/latest/developerguide/mkc-create-connector-intro.html](https://docs.aws.amazon.com/msk/latest/developerguide/mkc-create-connector-intro.html)

## 技术信息

- Source Metadata：[sources/aws/kafka_connector_in_transit_encryption_enabled/metadata.json](../../sources/aws/kafka_connector_in_transit_encryption_enabled/metadata.json)
- Source Code：[sources/aws/kafka_connector_in_transit_encryption_enabled/check.py](../../sources/aws/kafka_connector_in_transit_encryption_enabled/check.py)
- Source Metadata Path：`sources/aws/kafka_connector_in_transit_encryption_enabled/metadata.json`
- Source Code Path：`sources/aws/kafka_connector_in_transit_encryption_enabled/check.py`
