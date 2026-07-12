# Amazon MSK cluster has enhanced monitoring enabled

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `kafka_cluster_enhanced_monitoring_enabled` |
| クラウドプラットフォーム | AWS |
| サービス | kafka |
| 重大度 | medium |
| カテゴリ | logging |
| チェックタイプ | Software and Configuration Checks/AWS Security Best Practices, Software and Configuration Checks/Industry and Regulatory Standards/AWS Foundational Security Best Practices |
| リソースタイプ | AwsMskCluster |
| リソースグループ | messaging |

## 説明

**Amazon MSK clusters** are assessed for **enhanced monitoring** levels beyond `DEFAULT` (e.g., `PER_BROKER`, `PER_TOPIC_PER_BROKER`, `PER_TOPIC_PER_PARTITION`). *Serverless clusters* include enhanced monitoring by design; provisioned clusters are evaluated by their configured monitoring level.

## リスク

Insufficient metrics limit visibility into **broker health**, **replication state**, and **consumer lag**, delaying response to incidents. This increases risk of **availability loss** (saturation, throttling) and can mask **integrity issues** such as under-replicated partitions, raising data-loss impact during failures.

## 推奨事項

Select an enhanced level (e.g., `PER_BROKER` or finer) and establish **observability**: prioritize telemetry for broker resources, replication health, and consumer lag. Configure alerts and dashboards aligned to SLOs to enable proactive scaling and rapid incident containment. *Balance granularity with cost*.

## 修正手順


### CLI

```text
aws kafka update-monitoring --cluster-arn <CLUSTER_ARN> --current-version <CURRENT_VERSION> --enhanced-monitoring PER_BROKER
```

### Native IaC

```yaml
# CloudFormation: Enable enhanced monitoring on an MSK cluster
Resources:
  <example_resource_name>:
    Type: AWS::MSK::Cluster
    Properties:
      ClusterName: <example_resource_name>
      KafkaVersion: <example_kafka_version>
      NumberOfBrokerNodes: 2
      BrokerNodeGroupInfo:
        ClientSubnets:
          - <example_subnet_id_1>
          - <example_subnet_id_2>
        InstanceType: kafka.t3.small
      EnhancedMonitoring: PER_BROKER  # Critical: sets enhanced monitoring above DEFAULT to pass the check
```

### Terraform

```hcl
# Terraform: Enable enhanced monitoring on an MSK cluster
resource "aws_msk_cluster" "<example_resource_name>" {
  cluster_name           = "<example_resource_name>"
  kafka_version          = "<example_kafka_version>"
  number_of_broker_nodes = 2

  broker_node_group_info {
    instance_type  = "kafka.t3.small"
    client_subnets = ["<example_subnet_id_1>", "<example_subnet_id_2>"]
  }

  enhanced_monitoring = "PER_BROKER" # Critical: sets monitoring above DEFAULT to pass the check
}
```

### Other

1. Open the AWS Console and go to Amazon MSK
2. Select your provisioned cluster
3. Click Edit
4. Under Monitoring, set Enhanced monitoring to PER_BROKER (or higher)
5. Save changes and wait for the update to complete

## 参考資料

- [https://docs.aws.amazon.com/msk/latest/developerguide/metrics-details.html](https://docs.aws.amazon.com/msk/latest/developerguide/metrics-details.html)
- [https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/MSK/enable-enhanced-monitoring-for-apache-kafka-brokers.html#](https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/MSK/enable-enhanced-monitoring-for-apache-kafka-brokers.html#)
- [https://docs.aws.amazon.com/msk/latest/developerguide/monitoring.html](https://docs.aws.amazon.com/msk/latest/developerguide/monitoring.html)

## 技術情報

- Source Metadata：[sources/aws/kafka_cluster_enhanced_monitoring_enabled/metadata.json](../../sources/aws/kafka_cluster_enhanced_monitoring_enabled/metadata.json)
- Source Code：[sources/aws/kafka_cluster_enhanced_monitoring_enabled/check.py](../../sources/aws/kafka_cluster_enhanced_monitoring_enabled/check.py)
- Source Metadata Path：`sources/aws/kafka_cluster_enhanced_monitoring_enabled/metadata.json`
- Source Code Path：`sources/aws/kafka_cluster_enhanced_monitoring_enabled/check.py`
