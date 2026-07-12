# Kafka cluster has TLS authentication enabled

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `kafka_cluster_mutual_tls_authentication_enabled` |
| クラウドプラットフォーム | AWS |
| サービス | kafka |
| 重大度 | high |
| カテゴリ | encryption |
| チェックタイプ | Software and Configuration Checks/AWS Security Best Practices, Software and Configuration Checks/Industry and Regulatory Standards/AWS Foundational Security Best Practices, TTPs/Initial Access |
| リソースタイプ | AwsMskCluster |
| リソースグループ | messaging |

## 説明

Amazon MSK clusters enforce **client authentication** on client-to-broker connections. Serverless clusters use TLS-based authentication by default; provisioned clusters must have **mutual TLS (mTLS)** explicitly enabled.

## リスク

Without **mTLS**, adversaries can impersonate clients or intercept sessions, compromising **confidentiality** and **integrity**. Unauthorized producers/consumers can read or alter topics, poison data streams, and flood brokers, degrading **availability** and impacting downstream systems.

## 推奨事項

Enable **mutual TLS** for client-broker traffic and disable `PLAINTEXT` listeners. Issue short-lived client certificates from a managed CA with rotation. Apply **least privilege** using Kafka ACLs, restrict network access to trusted sources, and monitor authentication events as part of **defense in depth**.

## 修正手順


### CLI

```text
aws kafka update-security --cluster-arn <CLUSTER_ARN> --current-version <CURRENT_VERSION> --client-authentication 'Tls={CertificateAuthorityArnList=["<ACM_PCA_ARN>"]}' --encryption-info 'EncryptionInTransit={ClientBroker=TLS}'
```

### Native IaC

```yaml
# CloudFormation: Enable mTLS for an MSK cluster
Resources:
  <example_resource_name>:
    Type: AWS::MSK::Cluster
    Properties:
      ClusterName: <example_resource_name>
      KafkaVersion: <example_kafka_version>
      NumberOfBrokerNodes: 2
      BrokerNodeGroupInfo:
        InstanceType: kafka.m5.large
        ClientSubnets:
          - <subnet_id_1>
          - <subnet_id_2>
      ClientAuthentication:
        Tls:
          CertificateAuthorityArnList:
            - <acm_pca_arn>  # CRITICAL: Enables mutual TLS using this Private CA
      EncryptionInfo:
        EncryptionInTransit:
          ClientBroker: TLS  # CRITICAL: Required when enabling mTLS
```

### Terraform

```hcl
# Terraform: Enable mTLS for an MSK cluster
resource "aws_msk_cluster" "<example_resource_name>" {
  cluster_name           = "<example_resource_name>"
  kafka_version          = "<example_kafka_version>"
  number_of_broker_nodes = 2

  broker_node_group_info {
    instance_type  = "kafka.m5.large"
    client_subnets = ["<subnet_id_1>", "<subnet_id_2>"]
  }

  client_authentication {
    tls {
      certificate_authority_arns = ["<acm_pca_arn>"]  # CRITICAL: Enables mutual TLS with this Private CA
    }
  }

  encryption_info {
    encryption_in_transit {
      client_broker = "TLS"  # CRITICAL: Required when enabling mTLS
    }
  }
}
```

### Other

1. In the AWS Console, go to Amazon MSK > Clusters and select the provisioned cluster (state must be ACTIVE)
2. Choose Actions > Update security (or Security > Edit)
3. Under Client authentication, enable TLS and add your AWS Private CA ARN(s)
4. Under Encryption in transit, set Client-broker to TLS
5. Save/Update and wait for the update to complete

## 参考資料

- [https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/MSK/enable-mutual-tls-authentication-for-kafka-clients.html](https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/MSK/enable-mutual-tls-authentication-for-kafka-clients.html)
- [https://docs.aws.amazon.com/msk/latest/developerguide/msk-update-security.html](https://docs.aws.amazon.com/msk/latest/developerguide/msk-update-security.html)
- [https://docs.aws.amazon.com/msk/latest/developerguide/msk-authentication.html](https://docs.aws.amazon.com/msk/latest/developerguide/msk-authentication.html)

## 技術情報

- Source Metadata：[sources/aws/kafka_cluster_mutual_tls_authentication_enabled/metadata.json](../../sources/aws/kafka_cluster_mutual_tls_authentication_enabled/metadata.json)
- Source Code：[sources/aws/kafka_cluster_mutual_tls_authentication_enabled/check.py](../../sources/aws/kafka_cluster_mutual_tls_authentication_enabled/check.py)
- Source Metadata Path：`sources/aws/kafka_cluster_mutual_tls_authentication_enabled/metadata.json`
- Source Code Path：`sources/aws/kafka_cluster_mutual_tls_authentication_enabled/check.py`
