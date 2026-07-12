# ElastiCache Redis cache cluster has in-transit encryption enabled

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `elasticache_redis_cluster_in_transit_encryption_enabled` |
| クラウドプラットフォーム | AWS |
| サービス | elasticache |
| 重大度 | medium |
| カテゴリ | encryption |
| チェックタイプ | Software and Configuration Checks/AWS Security Best Practices/Network Security, Software and Configuration Checks/Industry and Regulatory Standards/AWS Foundational Security Best Practices, Effects/Data Exposure |
| リソースタイプ | Other |
| リソースグループ | database |

## 説明

**ElastiCache for Redis** replication groups have **in-transit encryption (TLS)** enabled for client and inter-node traffic (`TransitEncryptionEnabled=true`).

## リスク

Absent **in-transit encryption**, traffic between apps and Redis or between nodes can be **eavesdropped** or **tampered**. This exposes keys, tokens, and cached sensitive data, enables **MITM** and session hijacking, and can corrupt replication, harming **confidentiality** and **integrity**.

## 推奨事項

Enable **TLS** by setting `TransitEncryptionEnabled=true` and enforce a strict mode (require TLS 1.2+). Ensure clients validate certificates, restrict network paths, and pair with **least privilege** plus Redis AUTH/RBAC for defense in depth.

## 修正手順


### CLI

```text
aws elasticache modify-replication-group --replication-group-id <example_resource_id> --transit-encryption-enabled --transit-encryption-mode preferred --apply-immediately
```

### Native IaC

```yaml
# CloudFormation: enable in-transit encryption for a Redis replication group
Resources:
  <example_resource_name>:
    Type: AWS::ElastiCache::ReplicationGroup
    Properties:
      ReplicationGroupId: "<example_resource_id>"
      ReplicationGroupDescription: "<example_description>"
      NumCacheClusters: 1
      CacheSubnetGroupName: "<example_resource_name>"
      TransitEncryptionEnabled: true  # CRITICAL: enables TLS in-transit to pass the check
```

### Terraform

```hcl
# Enable in-transit encryption for a Redis replication group
resource "aws_elasticache_replication_group" "<example_resource_name>" {
  replication_group_id       = "<example_resource_id>"
  description                = "<example_description>"
  node_type                  = "cache.t3.micro"
  num_cache_clusters         = 1
  subnet_group_name          = "<example_resource_name>"
  transit_encryption_enabled = true  # CRITICAL: enables TLS in-transit to pass the check
}
```

### Other

1. In the AWS Console, go to ElastiCache > Redis OSS (or Valkey) replication groups
2. Select the replication group and click Actions > Modify
3. Under Security, enable Encryption in transit and set Transit encryption mode to Preferred
4. Check Apply immediately and Save changes

## 参考資料

- [https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/ElastiCache/in-transit-and-at-rest-encryption.html](https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/ElastiCache/in-transit-and-at-rest-encryption.html)
- [https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/in-transit-encryption-enable.html](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/in-transit-encryption-enable.html)
- [https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/in-transit-encryption.html](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/in-transit-encryption.html)

## 技術情報

- Source Metadata：[sources/aws/elasticache_redis_cluster_in_transit_encryption_enabled/metadata.json](../../sources/aws/elasticache_redis_cluster_in_transit_encryption_enabled/metadata.json)
- Source Code：[sources/aws/elasticache_redis_cluster_in_transit_encryption_enabled/check.py](../../sources/aws/elasticache_redis_cluster_in_transit_encryption_enabled/check.py)
- Source Metadata Path：`sources/aws/elasticache_redis_cluster_in_transit_encryption_enabled/metadata.json`
- Source Code Path：`sources/aws/elasticache_redis_cluster_in_transit_encryption_enabled/check.py`
