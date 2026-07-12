# DynamoDB Accelerator (DAX) cluster has nodes in multiple Availability Zones

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `dynamodb_accelerator_cluster_multi_az` |
| クラウドプラットフォーム | AWS |
| サービス | dynamodb |
| 重大度 | medium |
| カテゴリ | resilience |
| チェックタイプ | Software and Configuration Checks/AWS Security Best Practices, Effects/Denial of Service |
| リソースタイプ | Other |
| リソースグループ | database |

## 説明

**Amazon DynamoDB Accelerator (DAX)** cluster node placement across **Availability Zones** is evaluated. Clusters with nodes in more than one AZ within the Region are recognized as multi-AZ; clusters whose nodes reside in a single AZ are recognized as single-AZ.

## リスク

Without **multi-AZ DAX nodes**, an AZ outage or primary node failure can render the cache **unavailable**, harming **availability** and causing **latency spikes** and **throttling** as load shifts to DynamoDB. Loss of caching can drive higher costs and trigger **timeout cascades** in read-heavy workloads.

## 推奨事項

Deploy **DAX clusters** with at least `3` nodes spread across distinct **Availability Zones** to ensure fault tolerance. Use subnet groups spanning multiple AZs, access via the cluster endpoint, and validate **failover** regularly. Monitor capacity to avoid single-AZ or single-node dependencies.

## 修正手順


### CLI

```text
aws dax increase-replication-factor --cluster-name <example_resource_name> --new-replication-factor 2 --availability-zones <AZ_1> <AZ_2>
```

### Native IaC

```yaml
Resources:
  DAXCluster:
    Type: AWS::DAX::Cluster
    Properties:
      ClusterName: <example_resource_name>
      IAMRoleARN: <example_resource_id>
      NodeType: <NODE_TYPE>
      ReplicationFactor: 2  # CRITICAL: at least 2 nodes so nodes can be placed in multiple AZs
      SubnetGroupName: <example_resource_name>
      AvailabilityZones:     # CRITICAL: specify multiple AZs to ensure multi-AZ placement
        - <AZ_1>
        - <AZ_2>
```

### Terraform

```hcl
resource "aws_dax_cluster" "example" {
  cluster_name       = "<example_resource_name>"
  node_type          = "<NODE_TYPE>"
  replication_factor = 2  # CRITICAL: at least 2 nodes to allow multi-AZ
  iam_role_arn       = "<example_resource_id>"
  subnet_group_name  = "<example_resource_name>"
  availability_zones = ["<AZ_1>", "<AZ_2>"]  # CRITICAL: ensures nodes are in multiple AZs
}
```

### Other

1. In AWS Console, go to DynamoDB > DAX > Subnet groups and ensure the subnet group used by the cluster includes subnets from at least two Availability Zones; save if you add one.
2. Go to DynamoDB > DAX > Clusters, select <example_resource_name>, and choose Modify.
3. Set Cluster size to 2 or more.
4. In Availability Zones (or node placement), select at least two different AZs.
5. Save changes and wait until status is Available, then confirm nodes show multiple AZs in Cluster details.

## 参考資料

- [https://support.icompaas.com/support/solutions/articles/62000233618-ensure-dynamodb-accelerator-dax-clusters-have-nodes-in-multiple-availability-zones](https://support.icompaas.com/support/solutions/articles/62000233618-ensure-dynamodb-accelerator-dax-clusters-have-nodes-in-multiple-availability-zones)
- [https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/DAX.concepts.cluster.html#DAX.concepts.regions-and-azs](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/DAX.concepts.cluster.html#DAX.concepts.regions-and-azs)
- [https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/DAX.create-cluster.console.html](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/DAX.create-cluster.console.html)

## 技術情報

- Source Metadata：[sources/aws/dynamodb_accelerator_cluster_multi_az/metadata.json](../../sources/aws/dynamodb_accelerator_cluster_multi_az/metadata.json)
- Source Code：[sources/aws/dynamodb_accelerator_cluster_multi_az/check.py](../../sources/aws/dynamodb_accelerator_cluster_multi_az/check.py)
- Source Metadata Path：`sources/aws/dynamodb_accelerator_cluster_multi_az/metadata.json`
- Source Code Path：`sources/aws/dynamodb_accelerator_cluster_multi_az/check.py`
