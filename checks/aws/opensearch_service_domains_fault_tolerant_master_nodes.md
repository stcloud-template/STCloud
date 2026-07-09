# OpenSearch domain has at least 3 dedicated master nodes

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `opensearch_service_domains_fault_tolerant_master_nodes` |
| 云平台 | AWS |
| 服务 | opensearch |
| 严重等级 | medium |
| 类别 | resilience |
| 检查类型 | Software and Configuration Checks/AWS Security Best Practices, Effects/Denial of Service |
| 资源类型 | AwsOpenSearchServiceDomain |
| 资源组 | database |

## 描述

**Amazon OpenSearch domains** have **dedicated master nodes** enabled with a master node count of at least `3` to support stable cluster coordination and elections

## 风险

With fewer than `3` or disabled **dedicated master nodes**, the cluster can lose **quorum**, blocking leader election. Effects include stalled cluster state updates, failed reads/writes, shard allocation issues, and possible split-brain, reducing **availability** and **integrity**.

## 推荐措施

Enable **dedicated master nodes** and set the count to at least `3` (use an odd number) to maintain **quorum**. Use *Multi-AZ with standby* to distribute masters across zones. Right-size master instances and monitor cluster health to uphold high availability and resilience.

## 修复步骤


### CLI

```text
aws opensearch update-domain-config --domain-name <name> --cluster-config "DedicatedMasterEnabled=true,DedicatedMasterType=<instance_type>,DedicatedMasterCount=3"
```

### Native IaC

```yaml
# CloudFormation: set at least 3 dedicated master nodes
Resources:
  <example_resource_name>:
    Type: AWS::OpenSearchService::Domain
    Properties:
      ClusterConfig:
        DedicatedMasterEnabled: true  # Critical: enable dedicated master nodes
        DedicatedMasterCount: 3       # Critical: ensure minimum of 3 masters
        DedicatedMasterType: "<instance_type>"  # Critical: required when enabling masters
```

### Terraform

```hcl
# Terraform: set at least 3 dedicated master nodes
resource "aws_opensearch_domain" "<example_resource_name>" {
  domain_name = "<example_resource_name>"

  cluster_config {
    dedicated_master_enabled = true  # Critical: enable dedicated masters
    dedicated_master_count   = 3     # Critical: ensure minimum of 3 masters
    dedicated_master_type    = "<instance_type>"  # Critical: required when enabling masters
  }
}
```

### Other

1. Sign in to the AWS Console and open Amazon OpenSearch Service
2. Select your domain and choose Edit
3. In Cluster configuration:
   - Enable Dedicated master nodes
   - Set Dedicated master node count to 3
   - Select a Dedicated master instance type
4. Choose Save changes

## 参考资料

- [https://docs.aws.amazon.com/securityhub/latest/userguide/opensearch-controls.html#opensearch-11](https://docs.aws.amazon.com/securityhub/latest/userguide/opensearch-controls.html#opensearch-11)
- [https://docs.aws.amazon.com/opensearch-service/latest/developerguide/managedomains-dedicatedmasternodes.html#dedicatedmasternodes-number](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/managedomains-dedicatedmasternodes.html#dedicatedmasternodes-number)

## 技术信息

- Source Metadata：[sources/aws/opensearch_service_domains_fault_tolerant_master_nodes/metadata.json](../../sources/aws/opensearch_service_domains_fault_tolerant_master_nodes/metadata.json)
- Source Code：[sources/aws/opensearch_service_domains_fault_tolerant_master_nodes/check.py](../../sources/aws/opensearch_service_domains_fault_tolerant_master_nodes/check.py)
- Source Metadata Path：`sources/aws/opensearch_service_domains_fault_tolerant_master_nodes/metadata.json`
- Source Code Path：`sources/aws/opensearch_service_domains_fault_tolerant_master_nodes/check.py`
