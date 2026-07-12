# DocumentDB cluster has Multi-AZ enabled

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `documentdb_cluster_multi_az_enabled` |
| クラウドプラットフォーム | AWS |
| サービス | documentdb |
| 重大度 | medium |
| カテゴリ | resilience |
| チェックタイプ | Software and Configuration Checks/AWS Security Best Practices |
| リソースタイプ | AwsRdsDbCluster |
| リソースグループ | database |

## 説明

**Amazon DocumentDB clusters** with **Multi-AZ** (`multi_az`) indicate deployment of a primary and one or more replicas across Availability Zones.

## リスク

Without Multi-AZ, the cluster depends on a single AZ/instance. An AZ or node failure-or maintenance-can stop reads and writes, causing downtime, timeouts, and SLA breaches. Availability degrades, RTO rises, and applications may experience failed or retried transactions until replacement capacity is created.

## 推奨事項

Enable **Multi-AZ** for DocumentDB and distribute instances across distinct AZs. - Maintain at least one replica - Set promotion priorities to guide failover - Test failover regularly and use resilient client retries This builds **fault tolerance** and preserves service availability.

## 修正手順


### CLI

```text
aws docdb create-db-instance --db-instance-identifier <example_resource_id> --db-cluster-identifier <example_resource_id> --db-instance-class <INSTANCE_CLASS> --engine docdb --availability-zone <OTHER_AZ>
```

### Native IaC

```yaml
# CloudFormation: add a replica to enable Multi-AZ for an existing DocumentDB cluster
Resources:
  DocDBReplica:
    Type: AWS::DocDB::DBInstance
    Properties:
      DBClusterIdentifier: "<example_resource_id>"  # CRITICAL: adds a new instance to the cluster to achieve Multi-AZ
      DBInstanceClass: "<INSTANCE_CLASS>"
      AvailabilityZone: "<OTHER_AZ>"                # CRITICAL: place in a different AZ to provide Multi-AZ failover
```

### Terraform

```hcl
# Add a replica to enable Multi-AZ for an existing DocumentDB cluster
resource "aws_docdb_cluster_instance" "<example_resource_name>" {
  cluster_identifier = "<example_resource_id>"  # CRITICAL: adds a new instance to the cluster to achieve Multi-AZ
  instance_class     = "<INSTANCE_CLASS>"
  availability_zone  = "<OTHER_AZ>"             # CRITICAL: different AZ ensures Multi-AZ failover
}
```

### Other

1. In the AWS Console, go to Amazon DocumentDB and open your cluster
2. Click Create instance
3. Set Instance class and choose an Availability Zone different from the primary
4. Click Create to add the replica
5. Verify the cluster now shows Multi-AZ enabled

## 参考資料

- [https://docs.aws.amazon.com/documentdb/latest/developerguide/failover.html](https://docs.aws.amazon.com/documentdb/latest/developerguide/failover.html)
- [https://support.icompaas.com/support/solutions/articles/62000233690-ensure-documentdb-cluster-have-multi-az-enabled](https://support.icompaas.com/support/solutions/articles/62000233690-ensure-documentdb-cluster-have-multi-az-enabled)

## 技術情報

- Source Metadata：[sources/aws/documentdb_cluster_multi_az_enabled/metadata.json](../../sources/aws/documentdb_cluster_multi_az_enabled/metadata.json)
- Source Code：[sources/aws/documentdb_cluster_multi_az_enabled/check.py](../../sources/aws/documentdb_cluster_multi_az_enabled/check.py)
- Source Metadata Path：`sources/aws/documentdb_cluster_multi_az_enabled/metadata.json`
- Source Code Path：`sources/aws/documentdb_cluster_multi_az_enabled/check.py`
