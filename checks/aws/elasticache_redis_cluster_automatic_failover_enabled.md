# ElastiCache Redis cluster has automatic failover enabled

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `elasticache_redis_cluster_automatic_failover_enabled` |
| クラウドプラットフォーム | AWS |
| サービス | elasticache |
| 重大度 | medium |
| カテゴリ | resilience |
| チェックタイプ | Software and Configuration Checks/AWS Security Best Practices, Software and Configuration Checks/Industry and Regulatory Standards/AWS Foundational Security Best Practices |
| リソースタイプ | Other |
| リソースグループ | database |

## 説明

**Amazon ElastiCache (Redis OSS) replication groups** have **automatic failover** set to `enabled`, allowing a replica to be promoted when the primary becomes unavailable

## リスク

**Missing automatic failover** reduces **availability**: a primary or AZ outage can stop writes and require manual recovery, prolonging downtime. As Redis replication is asynchronous, delayed promotion increases chances of **lost or stale writes**, affecting **data integrity** and causing client timeouts.

## 推奨事項

Enable **automatic failover** with **Multi-AZ**, keeping at least one replica per shard in a different AZ. Regularly *test failover* and monitor replication lag. Architect clients for resilience with retries and backoff to tolerate brief role changes, aligning with **fault tolerance** and **defense in depth**.

## 修正手順


### CLI

```text
aws elasticache modify-replication-group --replication-group-id <example_resource_id> --automatic-failover-enabled --apply-immediately
```

### Native IaC

```yaml
# CloudFormation: enable automatic failover for a Redis replication group
Resources:
  <example_resource_name>:
    Type: AWS::ElastiCache::ReplicationGroup
    Properties:
      ReplicationGroupId: <example_resource_id>
      ReplicationGroupDescription: "<description>"
      NumCacheClusters: 2
      AutomaticFailoverEnabled: true  # Critical: turns on automatic failover so the check passes
      Engine: redis
```

### Terraform

```hcl
# Terraform: enable automatic failover for a Redis replication group
resource "aws_elasticache_replication_group" "<example_resource_name>" {
  replication_group_id          = "<example_resource_id>"
  replication_group_description = "<description>"
  node_type                     = "cache.t3.small"
  number_cache_clusters         = 2
  automatic_failover_enabled    = true  # Critical: turns on automatic failover so the check passes
}
```

### Other

1. Open the AWS Console and go to ElastiCache
2. Select your Redis replication group (<example_resource_id>)
3. Click Modify
4. Set Auto failover to Enabled
5. Check Apply immediately
6. Click Save changes

## 参考資料

- [https://aws.amazon.com/blogs/database/testing-automatic-failover-to-a-read-replica-on-amazon-elasticache-for-redis/](https://aws.amazon.com/blogs/database/testing-automatic-failover-to-a-read-replica-on-amazon-elasticache-for-redis/)
- [https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/AutoFailover.html](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/AutoFailover.html)

## 技術情報

- Source Metadata：[sources/aws/elasticache_redis_cluster_automatic_failover_enabled/metadata.json](../../sources/aws/elasticache_redis_cluster_automatic_failover_enabled/metadata.json)
- Source Code：[sources/aws/elasticache_redis_cluster_automatic_failover_enabled/check.py](../../sources/aws/elasticache_redis_cluster_automatic_failover_enabled/check.py)
- Source Metadata Path：`sources/aws/elasticache_redis_cluster_automatic_failover_enabled/metadata.json`
- Source Code Path：`sources/aws/elasticache_redis_cluster_automatic_failover_enabled/check.py`
