# DynamoDB DAX cluster has encryption at rest enabled

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `dynamodb_accelerator_cluster_encryption_enabled` |
| 云平台 | AWS |
| 服务 | dynamodb |
| 严重等级 | medium |
| 类别 | encryption |
| 检查类型 | Software and Configuration Checks/AWS Security Best Practices, Software and Configuration Checks/Industry and Regulatory Standards/AWS Foundational Security Best Practices, Software and Configuration Checks/Industry and Regulatory Standards/CIS AWS Foundations Benchmark |
| 资源类型 | Other |
| 资源组 | database |

## 描述

**Amazon DynamoDB Accelerator (DAX) clusters** are evaluated for **server-side `encryption at rest`**. The finding indicates whether the cluster's on-disk cache, configuration, and logs are encrypted using service-managed keys.

## 风险

Without **encryption at rest**, DAX on-disk cache and logs can be extracted from underlying storage by those with low-level access, compromising **confidentiality** and enabling offline data mining. Threats: - Compromised host or admin - Lost/retired media - Unauthorized backups or snapshots

## 推荐措施

Provision DAX clusters with **`encryption at rest`** enabled. Apply **least privilege** for DAX administration and data access, and monitor with logging. Adopt **defense in depth**: enable encryption in transit, restrict network exposure, and avoid caching highly sensitive data. Re-create unencrypted clusters to enforce this setting.

## 修复步骤


### CLI

```text
aws dax create-cluster --cluster-name <example_resource_name> --node-type <NODE_TYPE> --replication-factor 1 --iam-role-arn <example_resource_id> --sse-specification Enabled=true
```

### Native IaC

```yaml
Resources:
  DaxCluster:
    Type: AWS::DAX::Cluster
    Properties:
      ClusterName: <example_resource_name>
      NodeType: <NODE_TYPE>
      ReplicationFactor: 1
      IAMRoleARN: <example_resource_id>
      SSESpecification:           # Critical: enables encryption at rest
        SSEEnabled: true          # Encrypts DAX cluster data at rest
```

### Terraform

```hcl
resource "aws_dax_cluster" "example" {
  cluster_name       = "<example_resource_name>"
  node_type          = "<NODE_TYPE>"
  replication_factor = 1
  iam_role_arn       = "<example_resource_id>"

  # Critical: enables encryption at rest
  server_side_encryption {
    enabled = true  # Encrypts DAX cluster data at rest
  }
}
```

### Other

1. In the AWS console, open **DynamoDB** > under **DAX**, choose **Clusters** > **Create cluster**
2. Enter a name and choose a node type
3. In **Encryption**, select **Enable encryption**
4. Choose the IAM role and required networking, then click **Launch cluster**
5. If replacing an existing unencrypted cluster: point your application to the new cluster endpoint, then delete the old cluster

## 参考资料

- [https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/DAXEncryptionAtRest.html](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/DAXEncryptionAtRest.html)
- [https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/DAX/encryption-enabled.html](https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/DAX/encryption-enabled.html)
- [https://docs.aws.amazon.com/prescriptive-guidance/latest/encryption-best-practices/dynamodb.html](https://docs.aws.amazon.com/prescriptive-guidance/latest/encryption-best-practices/dynamodb.html)

## 技术信息

- Source Metadata：[sources/aws/dynamodb_accelerator_cluster_encryption_enabled/metadata.json](../../sources/aws/dynamodb_accelerator_cluster_encryption_enabled/metadata.json)
- Source Code：[sources/aws/dynamodb_accelerator_cluster_encryption_enabled/check.py](../../sources/aws/dynamodb_accelerator_cluster_encryption_enabled/check.py)
- Source Metadata Path：`sources/aws/dynamodb_accelerator_cluster_encryption_enabled/metadata.json`
- Source Code Path：`sources/aws/dynamodb_accelerator_cluster_encryption_enabled/check.py`
