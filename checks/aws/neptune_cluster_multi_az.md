# Neptune cluster has Multi-AZ enabled

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `neptune_cluster_multi_az` |
| クラウドプラットフォーム | AWS |
| サービス | neptune |
| 重大度 | medium |
| カテゴリ | resilience |
| チェックタイプ | Software and Configuration Checks/AWS Security Best Practices, Software and Configuration Checks/Industry and Regulatory Standards/AWS Foundational Security Best Practices, Effects/Denial of Service |
| リソースタイプ | AwsRdsDbCluster |
| リソースグループ | database |

## 説明

Amazon Neptune DB clusters are evaluated for `Multi-AZ` deployment by checking whether the cluster has read-replica instances distributed across multiple Availability Zones. A failing result indicates the cluster is deployed in a single AZ and lacks read-replicas that enable automatic promotion and cross-AZ failover.

## リスク

**Single-AZ deployment** creates a clear availability single point of failure. - **Availability**: AZ outage or maintenance can cause prolonged downtime until the primary is rebuilt. - **Integrity/Recovery**: Manual recovery increases risk of configuration errors and longer RTOs, impacting operations and compliance.

## 推奨事項

Adopt a **high availability** deployment model for production Neptune clusters by placing read-replicas in separate Availability Zones to avoid single points of failure. Regularly test automated failover and combine HA with robust backup and recovery practices as part of a defense-in-depth strategy.

## 修正手順


### Native IaC

```yaml
Resources:
 NeptuneCluster:
 Type: AWS::Neptune::DBCluster
 Properties:
 DBClusterIdentifier: "<DB_CLUSTER_IDENTIFIER>"
 # Deploy across multiple AZs for high availability and failover
 AvailabilityZones:
 - "<AZ_1>"
 - "<AZ_2>"
 - "<AZ_3>"
```

### Terraform

```hcl
resource "aws_neptune_cluster" "example" {
 cluster_identifier = "<db_cluster_identifier>"
 availability_zones = ["<AZ_1>", "<AZ_2>", "<AZ_3>"]  # Deploy across multiple AZs for high availability
}
```

## 参考資料

- [https://docs.aws.amazon.com/securityhub/latest/userguide/neptune-controls.html#neptune-9](https://docs.aws.amazon.com/securityhub/latest/userguide/neptune-controls.html#neptune-9)
- [https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/Neptune/multi-az.html#](https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/Neptune/multi-az.html#)

## 技術情報

- Source Metadata：[sources/aws/neptune_cluster_multi_az/metadata.json](../../sources/aws/neptune_cluster_multi_az/metadata.json)
- Source Code：[sources/aws/neptune_cluster_multi_az/check.py](../../sources/aws/neptune_cluster_multi_az/check.py)
- Source Metadata Path：`sources/aws/neptune_cluster_multi_az/metadata.json`
- Source Code Path：`sources/aws/neptune_cluster_multi_az/check.py`
