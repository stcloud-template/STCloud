# OpenSearch domain has at least 3 data nodes and Zone Awareness enabled

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `opensearch_service_domains_fault_tolerant_data_nodes` |
| 云平台 | AWS |
| 服务 | opensearch |
| 严重等级 | medium |
| 类别 | resilience |
| 检查类型 | Software and Configuration Checks/AWS Security Best Practices, Effects/Denial of Service |
| 资源类型 | AwsOpenSearchServiceDomain |
| 资源组 | database |

## 描述

**Amazon OpenSearch domains** are assessed for fault tolerance: **>= 3 data nodes** (`instance_count >= 3`) and **Zone Awareness** (`zone_awareness_enabled = true`) to distribute data across Availability Zones.

## 风险

**Insufficient data nodes** or disabled **Zone Awareness** reduces availability and durability. A node or AZ failure can trigger shard unavailability, write failures, or cluster outage, increasing risk of data inconsistency during rebalancing and blocking reads/writes until recovery.

## 推荐措施

Configure OpenSearch with **>= 3 data nodes** and enable **Zone Awareness** to spread nodes across AZs. - Prefer Multi-AZ with Standby for resilient failover - Use node counts in multiples of three and set index replicas (`>= 1`) - Practice capacity planning and failure testing as **defense in depth**

## 修复步骤


### CLI

```text
aws opensearch update-domain-config --domain-name <example_resource_name> --cluster-config InstanceCount=3,ZoneAwarenessEnabled=true
```

### Native IaC

```yaml
# CloudFormation: Ensure at least 3 data nodes and enable Zone Awareness
Resources:
  <example_resource_name>:
    Type: AWS::OpenSearchService::Domain
    Properties:
      DomainName: <example_resource_name>
      ClusterConfig:
        InstanceType: m5.large.search
        InstanceCount: 3            # Critical: sets at least 3 data nodes for fault tolerance
        ZoneAwarenessEnabled: true  # Critical: enables cross-AZ (Zone Awareness)
```

### Terraform

```hcl
# Terraform: Ensure at least 3 data nodes and enable Zone Awareness
resource "aws_opensearch_domain" "<example_resource_name>" {
  domain_name = "<example_resource_name>"

  cluster_config {
    instance_type          = "m5.large.search"
    instance_count         = 3     # Critical: sets at least 3 data nodes for fault tolerance
    zone_awareness_enabled = true  # Critical: enables cross-AZ (Zone Awareness)
  }
}
```

### Other

1. Open the AWS Console and go to Amazon OpenSearch Service
2. Select your domain and click Edit domain
3. Under Cluster configuration:
   - Set Number of data nodes to 3 (or more)
   - Enable Zone awareness
4. Click Submit to apply the changes

## 参考资料

- [https://docs.aws.amazon.com/opensearch-service/latest/developerguide/managedomains-multiaz.html](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/managedomains-multiaz.html)
- [https://docs.aws.amazon.com/securityhub/latest/userguide/es-controls.html#es-6](https://docs.aws.amazon.com/securityhub/latest/userguide/es-controls.html#es-6)

## 技术信息

- Source Metadata：[sources/aws/opensearch_service_domains_fault_tolerant_data_nodes/metadata.json](../../sources/aws/opensearch_service_domains_fault_tolerant_data_nodes/metadata.json)
- Source Code：[sources/aws/opensearch_service_domains_fault_tolerant_data_nodes/check.py](../../sources/aws/opensearch_service_domains_fault_tolerant_data_nodes/check.py)
- Source Metadata Path：`sources/aws/opensearch_service_domains_fault_tolerant_data_nodes/metadata.json`
- Source Code Path：`sources/aws/opensearch_service_domains_fault_tolerant_data_nodes/check.py`
