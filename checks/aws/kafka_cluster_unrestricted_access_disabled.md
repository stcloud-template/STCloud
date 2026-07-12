# Kafka cluster requires authentication

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `kafka_cluster_unrestricted_access_disabled` |
| クラウドプラットフォーム | AWS |
| サービス | kafka |
| 重大度 | critical |
| カテゴリ | identity-access |
| チェックタイプ | Software and Configuration Checks/AWS Security Best Practices, Software and Configuration Checks/Industry and Regulatory Standards/AWS Foundational Security Best Practices, TTPs/Initial Access/Unauthorized Access, Effects/Data Exposure |
| リソースタイプ | AwsMskCluster |
| リソースグループ | messaging |

## 説明

Amazon MSK clusters are evaluated for **unauthenticated client access**. Serverless clusters inherently require authentication; provisioned clusters are checked for configurations that allow **unrestricted connections** rather than authenticated clients.

## リスク

Allowing **unauthenticated access** lets anyone connect and: - Read sensitive topics (confidentiality) - Publish or alter data (integrity) - Overload brokers and consumers (availability) This enables message exfiltration, stream poisoning, and abuse of trusted data pipelines.

## 推奨事項

Disable **unauthenticated access** and require **strong client authentication** (mTLS or IAM/SASL). - Enforce **least privilege** with scoped ACLs - Restrict network paths via private connectivity and tight security groups - Encrypt in transit, monitor access, and rotate credentials regularly

## 修正手順


### CLI

```text
aws kafka update-security --cluster-arn <example_resource_arn> --current-version <example_current_version> --client-authentication 'Unauthenticated={Enabled=false}'
```

### Native IaC

```yaml
# CloudFormation: Disable unauthenticated client access for MSK
Resources:
  <example_resource_name>:
    Type: AWS::MSK::Cluster
    Properties:
      ClusterName: <example_resource_name>
      KafkaVersion: <example_kafka_version>
      NumberOfBrokerNodes: 2
      BrokerNodeGroupInfo:
        InstanceType: <example_instance_type>
        ClientSubnets:
          - <subnet_id_1>
          - <subnet_id_2>
        StorageInfo:
          EbsStorageInfo:
            VolumeSize: 1000
      ClientAuthentication:
        Unauthenticated:
          Enabled: false  # CRITICAL: Disables unauthenticated client access
```

### Terraform

```hcl
# Terraform: Disable unauthenticated client access for MSK
resource "aws_msk_cluster" "<example_resource_name>" {
  cluster_name           = "<example_resource_name>"
  kafka_version          = "<example_kafka_version>"
  number_of_broker_nodes = 2

  broker_node_group_info {
    instance_type   = "<example_instance_type>"
    client_subnets  = ["<subnet_id_1>", "<subnet_id_2>"]
    ebs_volume_size = 1000
  }

  client_authentication {
    unauthenticated = false  # CRITICAL: Disables unauthenticated client access
  }
}
```

### Other

1. Open the AWS Console and go to Amazon MSK
2. Select your cluster and open the Security tab
3. Click Edit under Client authentication
4. Turn off/clear Unauthenticated access
5. Save changes to apply the update

## 参考資料

- [https://docs.aws.amazon.com/msk/latest/developerguide/msk-configure-security.html](https://docs.aws.amazon.com/msk/latest/developerguide/msk-configure-security.html)
- [https://docs.aws.amazon.com/msk/latest/developerguide/security.html](https://docs.aws.amazon.com/msk/latest/developerguide/security.html)
- [https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/MSK/unrestricted-access-to-brokers.html](https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/MSK/unrestricted-access-to-brokers.html)

## 技術情報

- Source Metadata：[sources/aws/kafka_cluster_unrestricted_access_disabled/metadata.json](../../sources/aws/kafka_cluster_unrestricted_access_disabled/metadata.json)
- Source Code：[sources/aws/kafka_cluster_unrestricted_access_disabled/check.py](../../sources/aws/kafka_cluster_unrestricted_access_disabled/check.py)
- Source Metadata Path：`sources/aws/kafka_cluster_unrestricted_access_disabled/metadata.json`
- Source Code Path：`sources/aws/kafka_cluster_unrestricted_access_disabled/check.py`
