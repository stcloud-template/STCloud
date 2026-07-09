# ElastiCache cluster is not using public subnets

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `elasticache_cluster_uses_public_subnet` |
| 云平台 | AWS |
| 服务 | elasticache |
| 严重等级 | medium |
| 类别 | internet-exposed |
| 检查类型 | Software and Configuration Checks/AWS Security Best Practices/Network Reachability, Industry and Regulatory Standards/AWS Foundational Security Best Practices, Effects/Data Exposure |
| 资源类型 | Other |
| 资源组 | database |

## 描述

**ElastiCache resources** (Redis nodes and Memcached clusters) are assessed for placement in **public subnets**. The finding identifies cache subnet groups that include subnets configured with Internet routing instead of private-only subnets.

## 风险

Hosting caches in **public subnets** can permit direct or misconfigured Internet access, impacting CIA: - Confidentiality: unauthorized reads and key dumps - Integrity: cache poisoning or key tampering - Availability: scanning and DDoS Attackers may pivot from the cache to **lateral movement** within the VPC.

## 推荐措施

Place caches in **private subnets** only and ensure route tables lack Internet egress. Apply **least privilege** with tight **security groups** limited to required ports and trusted sources. For external access, use **VPC peering**, **VPN**, or **PrivateLink**. Enable encryption in transit and Redis `AUTH` for layered controls.

## 修复步骤


### CLI

```text
aws elasticache modify-cache-cluster --cache-cluster-id <example_resource_id> --cache-subnet-group-name <example_resource_name> --apply-immediately
```

### Native IaC

```yaml
# CloudFormation: move ElastiCache into private subnets via a private subnet group
Resources:
  PrivateCacheSubnetGroup:
    Type: AWS::ElastiCache::SubnetGroup
    Properties:
      Description: Private subnets only
      SubnetIds:
        - <example_resource_id>  # private subnet
        - <example_resource_id>  # private subnet

  CacheCluster:
    Type: AWS::ElastiCache::CacheCluster
    Properties:
      CacheClusterId: <example_resource_id>
      Engine: redis
      CacheNodeType: cache.t3.micro
      NumCacheNodes: 1
      CacheSubnetGroupName: !Ref PrivateCacheSubnetGroup  # CRITICAL: forces the cluster to use only private subnets
```

### Terraform

```hcl
# Terraform: ensure the cluster uses a subnet group with only private subnets
resource "aws_elasticache_subnet_group" "private" {
  name       = "<example_resource_name>"
  subnet_ids = ["<example_resource_id>", "<example_resource_id>"] # private subnets only
}

resource "aws_elasticache_cluster" "cache" {
  cluster_id      = "<example_resource_id>"
  engine          = "redis"
  node_type       = "cache.t3.micro"
  num_cache_nodes = 1
  subnet_group_name = aws_elasticache_subnet_group.private.name  # CRITICAL: restricts cluster to private subnets
}
```

### Other

1. In the AWS Console, go to ElastiCache > Subnet groups
2. Click Create cache subnet group and select only private subnets (no route to an Internet Gateway)
3. Go to ElastiCache > Redis or Memcached, select your cluster
4. Click Modify, set Subnet group to the private subnet group
5. Check Apply immediately and click Modify to save

## 参考资料

- [https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/SubnetGroups.html](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/SubnetGroups.html)
- [https://docs.aws.amazon.com/AmazonElastiCache/latest/red-ug/VPCs.html](https://docs.aws.amazon.com/AmazonElastiCache/latest/red-ug/VPCs.html)

## 技术信息

- Source Metadata：[sources/aws/elasticache_cluster_uses_public_subnet/metadata.json](../../sources/aws/elasticache_cluster_uses_public_subnet/metadata.json)
- Source Code：[sources/aws/elasticache_cluster_uses_public_subnet/check.py](../../sources/aws/elasticache_cluster_uses_public_subnet/check.py)
- Source Metadata Path：`sources/aws/elasticache_cluster_uses_public_subnet/metadata.json`
- Source Code Path：`sources/aws/elasticache_cluster_uses_public_subnet/check.py`
