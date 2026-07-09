# MSK cluster uses the latest Kafka version or is serverless with AWS-managed version

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `kafka_cluster_uses_latest_version` |
| 云平台 | AWS |
| 服务 | kafka |
| 严重等级 | medium |
| 类别 | vulnerabilities |
| 检查类型 | Software and Configuration Checks/Patch Management, Software and Configuration Checks/AWS Security Best Practices, Software and Configuration Checks/Industry and Regulatory Standards/AWS Foundational Security Best Practices |
| 资源类型 | AwsMskCluster |
| 资源组 | messaging |

## 描述

**Amazon MSK clusters** are evaluated for use of the latest supported **Apache Kafka version**. Provisioned clusters are compared to the most recent release, while **serverless clusters** are treated as automatically managed for versioning.

## 风险

Outdated Kafka enables exploitation of known flaws and weak cryptography, risking data exposure or tampering (**confidentiality/integrity**). Missing fixes increase broker crashes and partition instability (**availability**). After end of support, silent auto-upgrades can trigger unexpected behavior and compatibility issues.

## 推荐措施

Adopt a controlled upgrade strategy: - Track MSK version support and upgrade before end of support - Test in staging and schedule maintenance windows - Use blue/green or rolling upgrades to reduce downtime - Validate client compatibility and security settings - Consider serverless MSK if automatic versioning fits your risk model

## 修复步骤


### CLI

```text
aws kafka update-cluster-kafka-version --cluster-arn <example_resource_id> --current-version <current_version> --target-kafka-version <latest_version>
```

### Native IaC

```yaml
# CloudFormation: Upgrade MSK cluster to latest Kafka version
Resources:
  <example_resource_name>:
    Type: AWS::MSK::Cluster
    Properties:
      ClusterName: <example_resource_name>
      KafkaVersion: <latest_version>  # CRITICAL: set to the latest Kafka version to pass the check
      NumberOfBrokerNodes: 2
      BrokerNodeGroupInfo:
        InstanceType: kafka.m5.large
        ClientSubnets:
          - <example_resource_id>
          - <example_resource_id>
```

### Terraform

```hcl
# Terraform: Upgrade MSK cluster to latest Kafka version
resource "aws_msk_cluster" "<example_resource_name>" {
  cluster_name           = "<example_resource_name>"
  kafka_version          = "<latest_version>"  # CRITICAL: set to the latest Kafka version to pass the check
  number_of_broker_nodes = 2

  broker_node_group_info {
    instance_type  = "kafka.m5.large"
    client_subnets = ["<example_resource_id>", "<example_resource_id>"]

    storage_info {
      ebs_storage_info { volume_size = 1000 }
    }
  }
}
```

### Other

1. Open the AWS Management Console and go to Amazon MSK
2. Select your cluster and choose Actions > Update cluster
3. In Kafka version, select the latest available version
4. Review and start the upgrade (Update/Start upgrade)
5. Wait until the operation completes and the cluster status returns to Active

## 参考资料

- [https://docs.aws.amazon.com/msk/latest/developerguide/version-support.html#version-upgrades](https://docs.aws.amazon.com/msk/latest/developerguide/version-support.html#version-upgrades)
- [https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-databases.html](https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-databases.html)
- [https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/MSK/enable-apache-kafka-latest-security-features.html](https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/MSK/enable-apache-kafka-latest-security-features.html)

## 技术信息

- Source Metadata：[sources/aws/kafka_cluster_uses_latest_version/metadata.json](../../sources/aws/kafka_cluster_uses_latest_version/metadata.json)
- Source Code：[sources/aws/kafka_cluster_uses_latest_version/check.py](../../sources/aws/kafka_cluster_uses_latest_version/check.py)
- Source Metadata Path：`sources/aws/kafka_cluster_uses_latest_version/metadata.json`
- Source Code Path：`sources/aws/kafka_cluster_uses_latest_version/check.py`
