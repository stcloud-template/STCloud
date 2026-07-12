# ElastiCache Redis cache cluster has at rest encryption enabled

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `elasticache_redis_cluster_rest_encryption_enabled` |
| クラウドプラットフォーム | AWS |
| サービス | elasticache |
| 重大度 | medium |
| カテゴリ | encryption |
| チェックタイプ | Software and Configuration Checks/AWS Security Best Practices, Software and Configuration Checks/Industry and Regulatory Standards/AWS Foundational Security Best Practices, Effects/Data Exposure |
| リソースタイプ | Other |
| リソースグループ | database |

## 説明

**ElastiCache for Redis replication groups** are evaluated for **encryption at rest** of on-disk cache data and backups. The finding pinpoints groups where this protection is not enabled.

## リスク

Without at-rest encryption, cache files and snapshots can be read if storage or backups are accessed via compromise or misconfiguration. Secrets, tokens, and PII may be exposed, breaking **confidentiality** and aiding **lateral movement** through offline analysis of cached data.

## 推奨事項

Enable **encryption at rest** on all Redis replication groups. Use **customer-managed KMS keys**, apply least-privilege access to keys, and audit key usage. Plan a controlled migration since at-rest encryption is enabled at creation (backup, restore, replace). Pair with **in-transit encryption** and authentication for defense in depth.

## 修正手順


### Native IaC

```yaml
# CloudFormation: enable at-rest encryption for an ElastiCache Redis replication group
Resources:
  <example_resource_name>:
    Type: AWS::ElastiCache::ReplicationGroup
    Properties:
      ReplicationGroupId: <example_resource_id>
      ReplicationGroupDescription: Enable at-rest encryption
      Engine: redis
      CacheNodeType: cache.t3.micro
      NumCacheClusters: 1
      AtRestEncryptionEnabled: true  # CRITICAL: turns on encryption at rest for the replication group
```

### Terraform

```hcl
# Terraform: enable at-rest encryption for an ElastiCache Redis replication group
resource "aws_elasticache_replication_group" "<example_resource_name>" {
  replication_group_id  = "<example_resource_id>"
  description           = "Enable at-rest encryption"
  node_type             = "cache.t3.micro"
  number_cache_clusters = 1
  at_rest_encryption_enabled = true  # CRITICAL: turns on encryption at rest for the replication group
}
```

### Other

1. In the AWS Console, go to ElastiCache > Redis
2. Select the non-encrypted replication group, click Actions > Backup and create a manual backup
3. After the backup completes, click Backups, select it, then Restore
4. In restore settings, check/enable Encryption at rest (use default KMS key) and create the new replication group
5. Update your application to use the new replication group endpoint
6. Verify connectivity and data, then delete the old (non-encrypted) replication group

## 参考資料

- [https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/ElastiCache/in-transit-and-at-rest-encryption.html](https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/ElastiCache/in-transit-and-at-rest-encryption.html)
- [https://docs.aws.amazon.com/AmazonElastiCache/latest/red-ug/at-rest-encryption.html#at-rest-encryption-enable](https://docs.aws.amazon.com/AmazonElastiCache/latest/red-ug/at-rest-encryption.html#at-rest-encryption-enable)
- [https://aws.amazon.com/blogs/security/amazon-elasticache-now-supports-encryption-for-elasticache-for-redis/](https://aws.amazon.com/blogs/security/amazon-elasticache-now-supports-encryption-for-elasticache-for-redis/)

## 技術情報

- Source Metadata：[sources/aws/elasticache_redis_cluster_rest_encryption_enabled/metadata.json](../../sources/aws/elasticache_redis_cluster_rest_encryption_enabled/metadata.json)
- Source Code：[sources/aws/elasticache_redis_cluster_rest_encryption_enabled/check.py](../../sources/aws/elasticache_redis_cluster_rest_encryption_enabled/check.py)
- Source Metadata Path：`sources/aws/elasticache_redis_cluster_rest_encryption_enabled/metadata.json`
- Source Code Path：`sources/aws/elasticache_redis_cluster_rest_encryption_enabled/check.py`
