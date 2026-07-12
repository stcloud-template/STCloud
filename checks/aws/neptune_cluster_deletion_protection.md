# Neptune cluster has deletion protection enabled

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `neptune_cluster_deletion_protection` |
| クラウドプラットフォーム | AWS |
| サービス | neptune |
| 重大度 | medium |
| カテゴリ | resilience |
| チェックタイプ | Software and Configuration Checks/AWS Security Best Practices, Industry and Regulatory Standards/AWS Foundational Security Best Practices, Effects/Data Destruction |
| リソースタイプ | Other |
| リソースグループ | database |

## 説明

Neptune DB cluster has **deletion protection** enabled.

## リスク

Absence of **deletion protection** weakens **availability** and **integrity**: clusters can be removed by accidental admin actions, rogue automation, or compromised credentials. Cluster deletion causes immediate service outage, potential permanent data loss, and extended recovery time if backups or restores are insufficient.

## 推奨事項

Enable **deletion protection** for production Neptune clusters and apply the principles of **least privilege** and **separation of duties** for delete operations. Enforce change-control approvals, restrict delete permissions to audited roles, and limit automated workflows that can perform destructive actions to prevent accidental or malicious deletions.

## 修正手順


### CLI

```text
aws neptune modify-db-cluster --db-cluster-identifier <DB_CLUSTER_IDENTIFIER> --deletion-protection --apply-immediately
```

### Native IaC

```yaml
Resources:
  NeptuneCluster:
    Type: AWS::Neptune::DBCluster
    Properties:
      DBClusterIdentifier: <CLUSTER_ID>
      DeletionProtection: true  # Prevent accidental or malicious cluster deletion
```

### Terraform

```hcl
resource "aws_neptune_cluster" "example_resource" {
  cluster_identifier  = "<CLUSTER_ID>"
  deletion_protection = true  # Prevent accidental or malicious cluster deletion
}
```

### Other

1. Sign in to the AWS Management Console and open Amazon Neptune
2. In the navigation pane, choose Databases
3. Select the DB cluster and choose Modify
4. Enable Deletion protection
5. Choose Apply immediately (if shown) and then Modify DB cluster

## 参考資料

- [https://docs.aws.amazon.com/securityhub/latest/userguide/neptune-controls.html#neptune-4](https://docs.aws.amazon.com/securityhub/latest/userguide/neptune-controls.html#neptune-4)

## 技術情報

- Source Metadata：[sources/aws/neptune_cluster_deletion_protection/metadata.json](../../sources/aws/neptune_cluster_deletion_protection/metadata.json)
- Source Code：[sources/aws/neptune_cluster_deletion_protection/check.py](../../sources/aws/neptune_cluster_deletion_protection/check.py)
- Source Metadata Path：`sources/aws/neptune_cluster_deletion_protection/metadata.json`
- Source Code Path：`sources/aws/neptune_cluster_deletion_protection/check.py`
