# ElastiCache Redis cache cluster has automated snapshot backups enabled with retention of at least 7 days

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `elasticache_redis_cluster_backup_enabled` |
| 云平台 | AWS |
| 服务 | elasticache |
| 严重等级 | high |
| 类别 | resilience |
| 检查类型 | Software and Configuration Checks/AWS Security Best Practices, Software and Configuration Checks/Industry and Regulatory Standards/AWS Foundational Security Best Practices, Effects/Data Destruction |
| 资源类型 | Other |
| 资源组 | database |

## 描述

Amazon ElastiCache Redis replication groups have **automated snapshot backups** enabled with a **retention period** of at least `7` days. The evaluation focuses on whether backups are enabled and the configured retention meets the minimum threshold.

## 风险

Absent or short-retained backups degrade **availability** and heighten **data loss** risk. Hardware failures, corruption, or accidental deletes may not be recoverable to needed points, undermining **RPO/RTO**, prolonging outages, and limiting **forensics** on cache data.

## 推荐措施

Enable **automated backups** and set **retention** to meet RPO/RTO (typically `7` days). - Define a consistent `snapshot window` - Test restores regularly - Protect backup storage with **least privilege** and immutability - Monitor backup status for failures - Apply **defense in depth** with replicas/Multi-AZ

## 修复步骤


### CLI

```text
aws elasticache modify-replication-group --replication-group-id <REPLICATION_GROUP_ID> --snapshot-retention-limit 7 --apply-immediately
```

### Native IaC

```yaml
# CloudFormation: set automated snapshot retention for a Redis replication group
Resources:
  <example_resource_name>:
    Type: AWS::ElastiCache::ReplicationGroup
    Properties:
      ReplicationGroupDescription: example
      SnapshotRetentionLimit: 7  # Critical: enables automatic snapshots and retains them for >=7 days
```

### Terraform

```hcl
resource "aws_elasticache_replication_group" "<example_resource_name>" {
  replication_group_id       = "<example_resource_id>"
  replication_group_description = "<example_description>"
  snapshot_retention_limit   = 7  # Critical: enable automated backups and keep them for >=7 days
}
```

### Other

1. In the AWS Console, open ElastiCache
2. Go to Redis > Replication groups
3. Select <example_resource_id> and click Modify
4. Set Snapshot retention (days) to 7 or higher
5. Check Apply immediately
6. Click Modify to save

## 参考资料

- [https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/ElastiCache/enable-automatic-backups.html](https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/ElastiCache/enable-automatic-backups.html)
- [https://docs.aws.amazon.com/securityhub/latest/userguide/elasticache-controls.html#elasticache-1](https://docs.aws.amazon.com/securityhub/latest/userguide/elasticache-controls.html#elasticache-1)

## 技术信息

- Source Metadata：[sources/aws/elasticache_redis_cluster_backup_enabled/metadata.json](../../sources/aws/elasticache_redis_cluster_backup_enabled/metadata.json)
- Source Code：[sources/aws/elasticache_redis_cluster_backup_enabled/check.py](../../sources/aws/elasticache_redis_cluster_backup_enabled/check.py)
- Source Metadata Path：`sources/aws/elasticache_redis_cluster_backup_enabled/metadata.json`
- Source Code Path：`sources/aws/elasticache_redis_cluster_backup_enabled/check.py`
