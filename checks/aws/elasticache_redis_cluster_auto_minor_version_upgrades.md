# ElastiCache Redis cache cluster has automatic minor version upgrades enabled

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `elasticache_redis_cluster_auto_minor_version_upgrades` |
| クラウドプラットフォーム | AWS |
| サービス | elasticache |
| 重大度 | high |
| カテゴリ | Uncategorized |
| チェックタイプ | Software and Configuration Checks/Patch Management, Software and Configuration Checks/AWS Security Best Practices |
| リソースタイプ | Other |
| リソースグループ | database |

## 説明

**ElastiCache for Redis** replication groups are configured to apply **automatic minor engine upgrades** using `AutoMinorVersionUpgrade`

## リスク

Without **automatic minor upgrades**, Redis nodes may run versions with known CVEs and stability bugs, enabling unauthorized access, replication inconsistencies, or crashes. Delayed patching widens the attack window and lengthens maintenance, degrading confidentiality, integrity, and availability.

## 推奨事項

Enable `AutoMinorVersionUpgrade` for Redis replication groups and govern updates with a maintenance window. Apply **patch management** and **defense in depth**: validate in staging, keep recent backups, use Multi-AZ for resilience, and monitor release notes to ensure timely, low-impact updates.

## 修正手順


### CLI

```text
aws elasticache modify-replication-group --replication-group-id <replication_group_id> --auto-minor-version-upgrade --apply-immediately
```

### Native IaC

```yaml
# CloudFormation: enable auto minor version upgrades on a Replication Group
Resources:
  <example_resource_name>:
    Type: AWS::ElastiCache::ReplicationGroup
    Properties:
      ReplicationGroupDescription: "<example_description>"
      CacheNodeType: "<example_node_type>"
      NumCacheClusters: 1
      AutoMinorVersionUpgrade: true  # CRITICAL: turns on automatic minor version upgrades
      # This ensures new minor engine versions are applied automatically
```

### Terraform

```hcl
# Enable auto minor version upgrades on an ElastiCache replication group
resource "aws_elasticache_replication_group" "<example_resource_name>" {
  replication_group_id       = "<example_resource_id>"
  description                = "<example_description>"
  node_type                  = "<example_node_type>"
  num_cache_clusters         = 1
  auto_minor_version_upgrade = true  # CRITICAL: automatically applies minor engine upgrades
}
```

### Other

1. Open the AWS console and go to ElastiCache
2. Select Replication groups, choose the target group
3. Click Modify
4. Enable Automatic minor version upgrade
5. Check Apply immediately and click Modify to save

## 参考資料

- [https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/VersionManagementConsiderations.html](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/VersionManagementConsiderations.html)
- [https://support.icompaas.com/support/solutions/articles/62000233595-ensure-elasticache-redis-cache-clusters-have-automatic-minor-upgrades-enabled](https://support.icompaas.com/support/solutions/articles/62000233595-ensure-elasticache-redis-cache-clusters-have-automatic-minor-upgrades-enabled)
- [https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/engine-versions.html](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/engine-versions.html)
- [https://docs.aws.amazon.com/AmazonElastiCache/latest/red-ug/VersionManagement.html](https://docs.aws.amazon.com/AmazonElastiCache/latest/red-ug/VersionManagement.html)

## 技術情報

- Source Metadata：[sources/aws/elasticache_redis_cluster_auto_minor_version_upgrades/metadata.json](../../sources/aws/elasticache_redis_cluster_auto_minor_version_upgrades/metadata.json)
- Source Code：[sources/aws/elasticache_redis_cluster_auto_minor_version_upgrades/check.py](../../sources/aws/elasticache_redis_cluster_auto_minor_version_upgrades/check.py)
- Source Metadata Path：`sources/aws/elasticache_redis_cluster_auto_minor_version_upgrades/metadata.json`
- Source Code Path：`sources/aws/elasticache_redis_cluster_auto_minor_version_upgrades/check.py`
