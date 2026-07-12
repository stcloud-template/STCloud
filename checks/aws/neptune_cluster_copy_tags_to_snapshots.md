# Neptune DB cluster is configured to copy tags to snapshots.

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `neptune_cluster_copy_tags_to_snapshots` |
| クラウドプラットフォーム | AWS |
| サービス | neptune |
| 重大度 | low |
| カテゴリ | Uncategorized |
| チェックタイプ | Software and Configuration Checks/AWS Security Best Practices |
| リソースタイプ | AwsRdsDbCluster |
| リソースグループ | database |

## 説明

Neptune DB cluster is configured to copy all tags to snapshots when snapshots are created.

## リスク

**Missing snapshot tags** weakens governance across confidentiality, integrity, and availability. - **Access control**: Tag-based IAM conditions may not apply to snapshots, enabling unauthorized restore or copy - **Operational**: Recovery, retention, and cost tracking can fail due to unidentifiable or orphaned snapshots

## 推奨事項

Preserve metadata by enabling tag inheritance for snapshots and enforcing a consistent tagging strategy. - Adopt a standardized tag taxonomy - Use tag-based access controls and apply least privilege - Automate tagging and policy checks in provisioning to prevent untagged snapshots

## 修正手順


### CLI

```text
aws neptune modify-db-cluster --db-cluster-identifier <DB_CLUSTER_ID> --copy-tags-to-snapshot --apply-immediately
```

### Native IaC

```yaml
Resources:
  NeptuneCluster:
    Type: AWS::RDS::DBCluster
    Properties:
      DBClusterIdentifier: <DB_CLUSTER_ID>
      EngineVersion: neptune
      CopyTagsToSnapshot: true  # Inherit tags for snapshot governance and access control
```

### Terraform

```hcl
resource "aws_neptune_cluster" "example_resource" {
  cluster_identifier     = "<DB_CLUSTER_ID>"
  copy_tags_to_snapshot  = true  # Inherit tags for snapshot governance and access control
}
```

### Other

1. Sign in to the AWS Management Console and open Amazon Neptune
2. Click Clusters and select the cluster
3. Click Modify
4. In Backup, enable "Copy tags to snapshots"
5. Check "Apply immediately"
6. Click Modify Cluster

## 参考資料

- [https://docs.aws.amazon.com/neptune/latest/userguide/tagging.html#tagging-overview](https://docs.aws.amazon.com/neptune/latest/userguide/tagging.html#tagging-overview)
- [https://www.cloudanix.com/docs/aws/audit/rdsmonitoring/rules/neptune_cluster_copy_tags_to_snapshot_enabled](https://www.cloudanix.com/docs/aws/audit/rdsmonitoring/rules/neptune_cluster_copy_tags_to_snapshot_enabled)
- [https://docs.aws.amazon.com/securityhub/latest/userguide/neptune-controls.html#neptune-8](https://docs.aws.amazon.com/securityhub/latest/userguide/neptune-controls.html#neptune-8)
- [https://docs.prismacloud.io/en/enterprise-edition/policy-reference/aws-policies/aws-general-policies/bc-aws-2-60](https://docs.prismacloud.io/en/enterprise-edition/policy-reference/aws-policies/aws-general-policies/bc-aws-2-60)

## 技術情報

- Source Metadata：[sources/aws/neptune_cluster_copy_tags_to_snapshots/metadata.json](../../sources/aws/neptune_cluster_copy_tags_to_snapshots/metadata.json)
- Source Code：[sources/aws/neptune_cluster_copy_tags_to_snapshots/check.py](../../sources/aws/neptune_cluster_copy_tags_to_snapshots/check.py)
- Source Metadata Path：`sources/aws/neptune_cluster_copy_tags_to_snapshots/metadata.json`
- Source Code Path：`sources/aws/neptune_cluster_copy_tags_to_snapshots/check.py`
