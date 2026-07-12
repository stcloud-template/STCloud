# ElastiCache Redis replication group has Multi-AZ enabled

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `elasticache_redis_cluster_multi_az_enabled` |
| クラウドプラットフォーム | AWS |
| サービス | elasticache |
| 重大度 | medium |
| カテゴリ | resilience |
| チェックタイプ | Software and Configuration Checks/AWS Security Best Practices, Effects/Denial of Service |
| リソースタイプ | Other |
| リソースグループ | database |

## 説明

**ElastiCache for Redis replication groups** have **Multi-AZ automatic failover** enabled, distributing primary and replicas across distinct Availability Zones

## リスク

Without **Multi-AZ failover**, a node or AZ outage can make Redis endpoints unreachable, reducing **availability**. Cold-cache rebuilds shift load to databases, risking saturation and cascading timeouts. Recent writes may be lost during failures, impacting **integrity**.

## 推奨事項

Enable **Multi-AZ with automatic failover** (`MultiAZ: enabled`) on Redis replication groups and place replicas in separate AZs. Use clients that follow primary/reader endpoints, monitor replication lag, and regularly test failover. Pair with snapshots for recovery; this enforces high **availability** and **resilience**.

## 修正手順


### CLI

```text
aws elasticache modify-replication-group --replication-group-id <example_resource_id> --multi-az-enabled --automatic-failover-enabled --apply-immediately
```

### Native IaC

```yaml
# CloudFormation: Enable Multi-AZ on an ElastiCache Redis replication group
Resources:
  <example_resource_name>:
    Type: AWS::ElastiCache::ReplicationGroup
    Properties:
      ReplicationGroupDescription: "<description>"
      Engine: redis
      CacheNodeType: cache.t4g.small
      NumCacheClusters: 2
      MultiAZEnabled: true  # CRITICAL: Enables Multi-AZ for the replication group
```

### Terraform

```hcl
# Enable Multi-AZ on an ElastiCache Redis replication group
resource "aws_elasticache_replication_group" "<example_resource_name>" {
  replication_group_id  = "<example_resource_id>"
  description           = "<description>"
  engine                = "redis"
  node_type             = "cache.t4g.small"
  number_cache_clusters = 2

  multi_az_enabled           = true  # CRITICAL: Enables Multi-AZ
  automatic_failover_enabled = true  # Required for Multi-AZ failover
}
```

### Other

1. In the AWS Console, go to ElastiCache > Redis
2. Select the target replication group
3. Click Modify
4. Enable Multi-AZ (and Automatic failover if prompted)
5. Check Apply immediately and click Modify

## 参考資料

- [https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/AutoFailover.html](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/AutoFailover.html)
- [https://repost.aws/knowledge-center/multi-az-replication-redis](https://repost.aws/knowledge-center/multi-az-replication-redis)
- [https://www.trendmicro.com/cloudoneconformity-staging/knowledge-base/aws/ElastiCache/elasticache-multi-az.html#](https://www.trendmicro.com/cloudoneconformity-staging/knowledge-base/aws/ElastiCache/elasticache-multi-az.html#)

## 技術情報

- Source Metadata：[sources/aws/elasticache_redis_cluster_multi_az_enabled/metadata.json](../../sources/aws/elasticache_redis_cluster_multi_az_enabled/metadata.json)
- Source Code：[sources/aws/elasticache_redis_cluster_multi_az_enabled/check.py](../../sources/aws/elasticache_redis_cluster_multi_az_enabled/check.py)
- Source Metadata Path：`sources/aws/elasticache_redis_cluster_multi_az_enabled/metadata.json`
- Source Code Path：`sources/aws/elasticache_redis_cluster_multi_az_enabled/check.py`
