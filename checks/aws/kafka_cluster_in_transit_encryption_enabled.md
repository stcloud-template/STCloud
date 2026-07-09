# Kafka cluster has encryption in transit enabled

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `kafka_cluster_in_transit_encryption_enabled` |
| 云平台 | AWS |
| 服务 | kafka |
| 严重等级 | high |
| 类别 | encryption |
| 检查类型 | Software and Configuration Checks/AWS Security Best Practices, Software and Configuration Checks/Industry and Regulatory Standards/AWS Foundational Security Best Practices |
| 资源类型 | AwsMskCluster |
| 资源组 | messaging |

## 描述

**Amazon MSK clusters** are evaluated for **encryption in transit** on both paths: **clientbroker** set to `TLS` only and **inter-broker** encryption enabled. *Serverless clusters provide this by default*. The finding highlights clusters where client-broker traffic isn't `TLS`-only or inter-broker encryption is turned off.

## 风险

Unencrypted or mixed (`TLS_PLAINTEXT`/`PLAINTEXT`) traffic enables interception of records, credentials, and metadata, supporting **MITM**, replay, and message tampering. Plaintext inter-broker links expose replication data within the VPC, enabling **lateral movement** and topic poisoning, degrading data **confidentiality** and **integrity**.

## 推荐措施

Enforce end-to-end transport protection: - Require `client_broker=TLS` for all clients - Enable `in_cluster=true` for broker-to-broker links Apply **defense in depth**: restrict network paths, prefer private connectivity, and use strong client authentication with **least privilege** authorization to limit blast radius.

## 修复步骤


### Native IaC

```yaml
# CloudFormation: MSK cluster with encryption in transit enforced
Resources:
  <example_resource_name>:
    Type: AWS::MSK::Cluster
    Properties:
      ClusterName: <example_resource_name>
      KafkaVersion: <VERSION>
      NumberOfBrokerNodes: 3
      BrokerNodeGroupInfo:
        ClientSubnets:
          - <example_resource_id>
          - <example_resource_id>
        InstanceType: kafka.m5.large
      EncryptionInfo:
        EncryptionInTransit:
          ClientBroker: TLS  # Critical: forces client-to-broker TLS only
          InCluster: true    # Critical: enables inter-broker encryption
```

### Terraform

```hcl
# Terraform: MSK cluster with encryption in transit enforced
resource "aws_msk_cluster" "<example_resource_name>" {
  cluster_name           = "<example_resource_name>"
  kafka_version          = "<VERSION>"
  number_of_broker_nodes = 3

  broker_node_group_info {
    instance_type  = "kafka.m5.large"
    client_subnets = [
      "subnet-<example_resource_id>",
      "subnet-<example_resource_id>",
    ]
  }

  encryption_info {
    encryption_in_transit {
      client_broker = "TLS"  # Critical: forces client-to-broker TLS only
      in_cluster    = true    # Critical: enables inter-broker encryption
    }
  }
}
```

### Other

1. In the AWS Console, go to Amazon MSK > Clusters and select your cluster
2. Click Edit (Security)
3. Under Encryption in transit, set Client-broker to TLS only
4. Save changes
5. Verify Inter-broker (in-cluster) encryption is enabled; if it is disabled (immutable), create a new cluster with:
   - Encryption in transit: Client-broker = TLS only, Inter-broker encryption = Enabled
   - Migrate clients to the new cluster, then decommission the old one

## 参考资料

- [https://docs.aws.amazon.com/msk/latest/developerguide/msk-encryption.html](https://docs.aws.amazon.com/msk/latest/developerguide/msk-encryption.html)
- [https://docs.aws.amazon.com/msk/latest/developerguide/msk-working-with-encryption.html](https://docs.aws.amazon.com/msk/latest/developerguide/msk-working-with-encryption.html)
- [https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/MSK/encryption-in-transit-for-msk.html](https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/MSK/encryption-in-transit-for-msk.html)

## 技术信息

- Source Metadata：[sources/aws/kafka_cluster_in_transit_encryption_enabled/metadata.json](../../sources/aws/kafka_cluster_in_transit_encryption_enabled/metadata.json)
- Source Code：[sources/aws/kafka_cluster_in_transit_encryption_enabled/check.py](../../sources/aws/kafka_cluster_in_transit_encryption_enabled/check.py)
- Source Metadata Path：`sources/aws/kafka_cluster_in_transit_encryption_enabled/metadata.json`
- Source Code Path：`sources/aws/kafka_cluster_in_transit_encryption_enabled/check.py`
