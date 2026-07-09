# ElastiCache Redis replication group with engine version < 6.0 has Redis OSS AUTH enabled

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `elasticache_redis_replication_group_auth_enabled` |
| 云平台 | AWS |
| 服务 | elasticache |
| 严重等级 | medium |
| 类别 | identity-access |
| 检查类型 | Software and Configuration Checks/AWS Security Best Practices, Software and Configuration Checks/Industry and Regulatory Standards/NIST 800-53 Controls, TTPs/Initial Access/Unauthorized Access, Effects/Data Exposure |
| 资源类型 | Other |
| 资源组 | database |

## 描述

Amazon ElastiCache Redis replication groups running versions prior to `6.0` are evaluated for the use of **AUTH tokens**. For `6.0+`, the finding indicates **ACL/RBAC** configuration should be reviewed instead of token-based AUTH.

## 风险

Without **AUTH** on pre-`6.0` clusters, clients can run unauthenticated commands, enabling data reads/writes, key deletion, and cache poisoning. This threatens **confidentiality** and **integrity**, and can facilitate lateral movement via stolen or injected session data.

## 推荐措施

Apply defense in depth: - For versions < `6.0`, enable **AUTH** with strong, rotated tokens and require in-transit encryption. - For `6.0+`, prefer **RBAC/ACLs** with least-privilege, deny-by-default roles. - Restrict network access to trusted sources and audit access regularly.

## 修复步骤


### CLI

```text
aws elasticache modify-replication-group --replication-group-id <example_resource_id> --auth-token <AUTH_TOKEN> --auth-token-update-strategy SET --apply-immediately
```

### Native IaC

```yaml
# CloudFormation: enable Redis AUTH on an existing replication group
Resources:
  <example_resource_name>:
    Type: AWS::ElastiCache::ReplicationGroup
    Properties:
      ReplicationGroupId: <example_resource_id>
      ReplicationGroupDescription: enable-auth
      TransitEncryptionEnabled: true   # CRITICAL: required to use AUTH
      AuthToken: <AUTH_TOKEN>          # CRITICAL: enables Redis AUTH
      AuthTokenUpdateStrategy: SET  # CRITICAL: adds token; enables AUTH
```

### Terraform

```hcl
# Terraform: enable Redis AUTH on an existing replication group
resource "aws_elasticache_replication_group" "<example_resource_name>" {
  replication_group_id       = "<example_resource_id>"
  description                = "enable-auth"
  transit_encryption_enabled = true            # CRITICAL: required to use AUTH
  auth_token                 = "<AUTH_TOKEN>" # CRITICAL: enables Redis AUTH
  auth_token_update_strategy = "SET"       # CRITICAL: adds token; enables AUTH
}
```

### Other

1. In the AWS Console, go to ElastiCache > Redis replication groups
2. Select the replication group <example_resource_id> and click Modify
3. Under Access control, choose Redis OSS AUTH and enter <AUTH_TOKEN>
4. Check Apply immediately and click Modify
5. Wait for status to return to Available; AUTH is now enabled

## 参考资料

- [https://docs.aws.amazon.com/securityhub/latest/userguide/elasticache-controls.html#elasticache-6](https://docs.aws.amazon.com/securityhub/latest/userguide/elasticache-controls.html#elasticache-6)
- [https://docs.aws.amazon.com/AmazonElastiCache/latest/red-ug/auth.html#auth-modifyng-token](https://docs.aws.amazon.com/AmazonElastiCache/latest/red-ug/auth.html#auth-modifyng-token)
- [https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/auth.html](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/auth.html)

## 技术信息

- Source Metadata：[sources/aws/elasticache_redis_replication_group_auth_enabled/metadata.json](../../sources/aws/elasticache_redis_replication_group_auth_enabled/metadata.json)
- Source Code：[sources/aws/elasticache_redis_replication_group_auth_enabled/check.py](../../sources/aws/elasticache_redis_replication_group_auth_enabled/check.py)
- Source Metadata Path：`sources/aws/elasticache_redis_replication_group_auth_enabled/metadata.json`
- Source Code Path：`sources/aws/elasticache_redis_replication_group_auth_enabled/check.py`
