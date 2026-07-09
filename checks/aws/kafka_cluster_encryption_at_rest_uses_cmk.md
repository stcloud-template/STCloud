# Kafka cluster has encryption at rest enabled with a customer managed key (CMK) or is serverless

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `kafka_cluster_encryption_at_rest_uses_cmk` |
| 云平台 | AWS |
| 服务 | kafka |
| 严重等级 | medium |
| 类别 | encryption |
| 检查类型 | Software and Configuration Checks/AWS Security Best Practices/Data Encryption, Industry and Regulatory Standards/AWS Foundational Security Best Practices, Industry and Regulatory Standards/NIST 800-53 Controls (USA), Industry and Regulatory Standards/PCI-DSS, Effects/Data Exposure |
| 资源类型 | AwsMskCluster |
| 资源组 | messaging |

## 描述

Amazon MSK clusters are inspected for **encryption at rest** using a **customer-managed KMS key** for data volumes. Serverless clusters are inherently encrypted. Provisioned clusters are recognized only when the configured `DataVolumeKMSKeyId` corresponds to a customer-managed key.

## 风险

Relying on service-managed keys weakens **confidentiality** and **accountability**: you can't enforce granular key policies, separation of duties, or independent rotation. This limits incident response (e.g., disabling the key for crypto-shredding) and reduces auditability, increasing impact of credential misuse or broker compromise.

## 推荐措施

Use a **customer-managed KMS key** for MSK at-rest encryption. Apply **least privilege** in key policies and grants, enable **key rotation**, and log key use for auditing. Enforce **separation of duties** between MSK admins and KMS key custodians, and regularly review access, aliases, and pending-deletion states.

## 修复步骤


### Native IaC

```yaml
# CloudFormation: MSK cluster using a customer managed KMS key for encryption at rest
Resources:
  <example_resource_name>:
    Type: AWS::MSK::Cluster
    Properties:
      ClusterName: <example_resource_name>
      KafkaVersion: <KAFKA_VERSION>
      NumberOfBrokerNodes: 2
      BrokerNodeGroupInfo:
        InstanceType: kafka.m5.large
        ClientSubnets:
          - <example_subnet_id_a>
          - <example_subnet_id_b>
        SecurityGroups:
          - <example_security_group_id>
      EncryptionInfo:
        EncryptionAtRest:
          DataVolumeKMSKeyId: <example_kms_key_arn>  # Critical: use a customer managed KMS key ARN to enable CMK encryption at rest
```

### Terraform

```hcl
# MSK cluster using a customer managed KMS key for encryption at rest
resource "aws_msk_cluster" "<example_resource_name>" {
  cluster_name           = "<example_resource_name>"
  kafka_version          = "<KAFKA_VERSION>"
  number_of_broker_nodes = 2

  broker_node_group_info {
    instance_type  = "kafka.m5.large"
    client_subnets = ["<example_subnet_id_a>", "<example_subnet_id_b>"]
    security_groups = ["<example_security_group_id>"]
  }

  encryption_info {
    encryption_at_rest_kms_key_arn = "<example_kms_key_arn>" # Critical: customer managed KMS key to pass the check
  }
}
```

### Other

1. In the AWS Console, go to Amazon MSK > Clusters
2. Click Create cluster
3. Choose Provisioned (or choose Serverless to pass by default)
4. In Encryption settings, for At-rest encryption, select Customer managed key and choose your CMK (not alias/aws/kafka)
5. Create the cluster, migrate clients to it, then delete the old cluster that used the AWS managed key

## 参考资料

- [https://docs.aws.amazon.com/msk/latest/developerguide/msk-encryption.html](https://docs.aws.amazon.com/msk/latest/developerguide/msk-encryption.html)
- [https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/MSK/msk-encryption-at-rest-with-cmk.html](https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/MSK/msk-encryption-at-rest-with-cmk.html)
- [https://docs.aws.amazon.com/msk/latest/developerguide/msk-working-with-encryption.html](https://docs.aws.amazon.com/msk/latest/developerguide/msk-working-with-encryption.html)

## 技术信息

- Source Metadata：[sources/aws/kafka_cluster_encryption_at_rest_uses_cmk/metadata.json](../../sources/aws/kafka_cluster_encryption_at_rest_uses_cmk/metadata.json)
- Source Code：[sources/aws/kafka_cluster_encryption_at_rest_uses_cmk/check.py](../../sources/aws/kafka_cluster_encryption_at_rest_uses_cmk/check.py)
- Source Metadata Path：`sources/aws/kafka_cluster_encryption_at_rest_uses_cmk/metadata.json`
- Source Code Path：`sources/aws/kafka_cluster_encryption_at_rest_uses_cmk/check.py`
