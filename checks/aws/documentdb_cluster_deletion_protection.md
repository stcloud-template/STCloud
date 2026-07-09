# DocumentDB cluster has deletion protection enabled

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `documentdb_cluster_deletion_protection` |
| 云平台 | AWS |
| 服务 | documentdb |
| 严重等级 | medium |
| 类别 | resilience |
| 检查类型 | Software and Configuration Checks/AWS Security Best Practices, Software and Configuration Checks/Industry and Regulatory Standards/AWS Foundational Security Best Practices |
| 资源类型 | AwsRdsDbCluster |
| 资源组 | database |

## 描述

**Amazon DocumentDB clusters** are evaluated for the `deletion_protection` setting on the cluster configuration. The finding highlights clusters where this protection is not enabled.

## 风险

Without **deletion protection**, clusters can be deleted by mistake or misuse, causing sudden outage and loss of recovery points, impacting **availability** and **data integrity**. Compromised accounts or faulty automation can remove databases or skip final snapshots, hindering restoration.

## 推荐措施

Enable **deletion protection** on all non-ephemeral clusters, prioritizing production. Enforce **least privilege** for delete and modify actions, require change control to toggle protection, and implement **defense in depth** with automation that continuously enforces this setting. *Before decommissioning*, take a final snapshot.

## 修复步骤


### CLI

```text
aws docdb modify-db-cluster --db-cluster-identifier <DB_CLUSTER_ID> --deletion-protection --apply-immediately
```

### Native IaC

```yaml
# CloudFormation: Enable deletion protection on a DocumentDB cluster
Resources:
  <example_resource_name>:
    Type: AWS::DocDB::DBCluster
    Properties:
      MasterUsername: "<MASTER_USERNAME>"
      MasterUserPassword: "<MASTER_USER_PASSWORD>"
      DeletionProtection: true  # CRITICAL: Prevents cluster deletion until disabled
```

### Terraform

```hcl
# Terraform: Enable deletion protection on a DocumentDB cluster
resource "aws_docdb_cluster" "<example_resource_name>" {
  master_username     = "<MASTER_USERNAME>"
  master_password     = "<MASTER_USER_PASSWORD>"
  deletion_protection = true  # CRITICAL: Prevents cluster deletion until disabled
}
```

### Other

1. In the AWS Console, go to Amazon DocumentDB > Clusters
2. Select the target cluster and click Modify
3. Enable Deletion protection
4. Check Apply immediately and click Save changes

## 参考资料

- [https://support.icompaas.com/support/solutions/articles/62000233689-ensure-documentdb-clusters-has-deletion-protection-enabled](https://support.icompaas.com/support/solutions/articles/62000233689-ensure-documentdb-clusters-has-deletion-protection-enabled)
- [https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/DocumentDB/deletion-protection.html](https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/DocumentDB/deletion-protection.html)
- [https://docs.aws.amazon.com/documentdb/latest/developerguide/db-cluster-delete.html](https://docs.aws.amazon.com/documentdb/latest/developerguide/db-cluster-delete.html)
- [https://docs.aws.amazon.com/securityhub/latest/userguide/documentdb-controls.html#documentdb-5](https://docs.aws.amazon.com/securityhub/latest/userguide/documentdb-controls.html#documentdb-5)

## 技术信息

- Source Metadata：[sources/aws/documentdb_cluster_deletion_protection/metadata.json](../../sources/aws/documentdb_cluster_deletion_protection/metadata.json)
- Source Code：[sources/aws/documentdb_cluster_deletion_protection/check.py](../../sources/aws/documentdb_cluster_deletion_protection/check.py)
- Source Metadata Path：`sources/aws/documentdb_cluster_deletion_protection/metadata.json`
- Source Code Path：`sources/aws/documentdb_cluster_deletion_protection/check.py`
