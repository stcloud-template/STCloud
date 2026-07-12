# Kafka cluster is not publicly accessible

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `kafka_cluster_is_public` |
| クラウドプラットフォーム | AWS |
| サービス | kafka |
| 重大度 | critical |
| カテゴリ | internet-exposed |
| チェックタイプ | Software and Configuration Checks/AWS Security Best Practices/Network Reachability, TTPs/Initial Access, Effects/Data Exposure |
| リソースタイプ | AwsMskCluster |
| リソースグループ | messaging |

## 説明

**Amazon MSK clusters** with broker endpoints **exposed to the public Internet**. Serverless clusters are private by default; provisioned clusters are evaluated for their `public access` configuration.

## リスク

Public brokers erode **CIA**: - **Confidentiality**: unauthorized consumers can read topics - **Integrity**: rogue producers inject or alter events - **Availability**: floods or scans strain brokers This enables metadata enumeration, data exfiltration, stream poisoning, and costly egress.

## 推奨事項

Keep brokers private within the VPC by disabling public access and limiting exposure to trusted networks. Enforce strong auth (SASL/IAM, SASL/SCRAM, or mTLS), require TLS, and apply Kafka ACLs. Provide access via VPN, bastion, or private networking (peering/Transit Gateway). Apply **least privilege** and monitor broker connections.

## 修正手順


### CLI

```text
aws kafka update-connectivity --cluster-arn <CLUSTER_ARN> --current-version <CURRENT_CLUSTER_VERSION> --connectivity-info '{"PublicAccess":{"Type":"DISABLED"}}'
```

### Native IaC

```yaml
# CloudFormation: ensure MSK cluster is not publicly accessible
Resources:
  <example_resource_name>:
    Type: AWS::MSK::Cluster
    Properties:
      ClusterName: <example_resource_name>
      KafkaVersion: "2.8.1"
      NumberOfBrokerNodes: 2
      BrokerNodeGroupInfo:
        ClientSubnets:
          - <example_subnet_id_1>
          - <example_subnet_id_2>
        InstanceType: kafka.t3.small
        ConnectivityInfo:
          PublicAccess:
            Type: DISABLED  # Critical: disables public access to brokers
```

### Terraform

```hcl
# Terraform: ensure MSK cluster is not publicly accessible
resource "aws_msk_cluster" "<example_resource_name>" {
  cluster_name           = "<example_resource_name>"
  kafka_version          = "2.8.1"
  number_of_broker_nodes = 2

  broker_node_group_info {
    client_subnets = [
      "<example_subnet_id_1>",
      "<example_subnet_id_2>",
    ]
    instance_type = "kafka.t3.small"

    connectivity_info {
      public_access {
        type = "DISABLED"  # Critical: disables public access to brokers
      }
    }
  }
}
```

### Other

1. Open the Amazon MSK console
2. Select your cluster and go to the Properties tab
3. In Network settings, click Edit public access
4. Set Public access to Disabled (Off)
5. Click Save changes

## 参考資料

- [https://docs.aws.amazon.com/msk/latest/developerguide/public-access.html](https://docs.aws.amazon.com/msk/latest/developerguide/public-access.html)
- [https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/MSK/public-access-msk-cluster.html](https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/MSK/public-access-msk-cluster.html)
- [https://docs.aws.amazon.com/msk/latest/developerguide/client-access.html](https://docs.aws.amazon.com/msk/latest/developerguide/client-access.html)

## 技術情報

- Source Metadata：[sources/aws/kafka_cluster_is_public/metadata.json](../../sources/aws/kafka_cluster_is_public/metadata.json)
- Source Code：[sources/aws/kafka_cluster_is_public/check.py](../../sources/aws/kafka_cluster_is_public/check.py)
- Source Metadata Path：`sources/aws/kafka_cluster_is_public/metadata.json`
- Source Code Path：`sources/aws/kafka_cluster_is_public/check.py`
