# DynamoDB Accelerator (DAX) cluster has encryption in transit enabled

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `dynamodb_accelerator_cluster_in_transit_encryption_enabled` |
| クラウドプラットフォーム | AWS |
| サービス | dynamodb |
| 重大度 | medium |
| カテゴリ | encryption |
| チェックタイプ | Software and Configuration Checks/AWS Security Best Practices, Effects/Data Exposure |
| リソースタイプ | Other |
| リソースグループ | database |

## 説明

**DAX clusters** have endpoint encryption set to `TLS`, enforcing **encryption in transit** for client connections to the cluster

## リスク

Missing **TLS** enables interception and manipulation of DAX traffic, impacting: - Confidentiality: exposure of queries, data, or credentials - Integrity: tampered requests/responses and cache poisoning - Availability: session hijacking or replay causing service disruption

## 推奨事項

Enforce **TLS** for all DAX endpoints and clients (`encryption in transit`). If an existing cluster lacks it, create a new TLS-enabled cluster and migrate. Apply **defense in depth**: restrict network paths, keep access private, and use **least privilege** IAM to reduce blast radius.

## 修正手順


### CLI

```text
aws dax create-cluster --cluster-name <cluster-name> --node-type <node-type> --replication-factor <replication-factor> --cluster-endpoint-encryption-type TLS
```

### Native IaC

```yaml
# CloudFormation: Create DAX cluster with TLS (encryption in transit)
Resources:
  <example_resource_name>:
    Type: AWS::DAX::Cluster
    Properties:
      ClusterName: <example_resource_name>
      IAMRoleARN: <example_resource_id>
      NodeType: <example_node_type>
      ReplicationFactor: 1
      ClusterEndpointEncryptionType: TLS  # Critical: Enables TLS for in-transit encryption
```

### Terraform

```hcl
# DAX cluster with encryption in transit enabled
resource "aws_dax_cluster" "<example_resource_name>" {
  cluster_name                      = "<example_resource_name>"
  node_type                         = "<example_node_type>"
  replication_factor                = 1
  iam_role_arn                      = "<example_resource_id>"
  cluster_endpoint_encryption_type  = "TLS"  # Critical: Enables TLS for in-transit encryption
}
```

### Other

1. In the AWS Console, go to DynamoDB > DAX
2. Click Create cluster
3. Set Cluster name, Node type, Replication factor, and IAM role
4. Enable Encryption in transit (TLS)
5. Create the cluster and wait until ACTIVE
6. Update your application to use the new DAX cluster endpoint
7. Delete the old non-TLS DAX cluster

## 参考資料

- [https://docs.aws.amazon.com/securityhub/latest/userguide/dynamodb-controls.html#dynamodb-7](https://docs.aws.amazon.com/securityhub/latest/userguide/dynamodb-controls.html#dynamodb-7)
- [https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/DAXEncryptionInTransit.html](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/DAXEncryptionInTransit.html)

## 技術情報

- Source Metadata：[sources/aws/dynamodb_accelerator_cluster_in_transit_encryption_enabled/metadata.json](../../sources/aws/dynamodb_accelerator_cluster_in_transit_encryption_enabled/metadata.json)
- Source Code：[sources/aws/dynamodb_accelerator_cluster_in_transit_encryption_enabled/check.py](../../sources/aws/dynamodb_accelerator_cluster_in_transit_encryption_enabled/check.py)
- Source Metadata Path：`sources/aws/dynamodb_accelerator_cluster_in_transit_encryption_enabled/metadata.json`
- Source Code Path：`sources/aws/dynamodb_accelerator_cluster_in_transit_encryption_enabled/check.py`
