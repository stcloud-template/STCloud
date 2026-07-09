# Amazon OpenSearch Service domain has node-to-node encryption enabled

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `opensearch_service_domains_node_to_node_encryption_enabled` |
| 云平台 | AWS |
| 服务 | opensearch |
| 严重等级 | high |
| 类别 | encryption |
| 检查类型 | Software and Configuration Checks/AWS Security Best Practices, Software and Configuration Checks/Industry and Regulatory Standards/AWS Foundational Security Best Practices, Software and Configuration Checks/Industry and Regulatory Standards/NIST CSF Controls (USA), Software and Configuration Checks/Industry and Regulatory Standards/NIST 800-53 Controls (USA), Software and Configuration Checks/Industry and Regulatory Standards/PCI-DSS |
| 资源类型 | AwsOpenSearchServiceDomain |
| 资源组 | database |

## 描述

**Amazon OpenSearch domains** with **node-to-node encryption** use TLS to protect traffic between cluster nodes. The finding evaluates the domain's `node_to_node_encryption` configuration for intra-cluster communications.

## 风险

Unencrypted intra-cluster traffic enables interception and manipulation by anyone with network foothold. - **Confidentiality**: exposure of documents, credentials, metadata - **Integrity**: tampering with queries and shard replication - **Availability**: spoofing/MITM can disrupt coordination and cause outages

## 推荐措施

Enable **node-to-node encryption** (`node_to_node_encryption: true`) to enforce TLS for inter-node traffic. Apply **defense in depth**: require HTTPS for clients, restrict network exposure, and use least privilege. Validate performance in staging and plan carefully, as the setting is effectively irreversible.

## 修复步骤


### CLI

```text
aws opensearchservice update-domain-config --domain-name <DOMAIN_NAME> --node-to-node-encryption-options Enabled=true
```

### Native IaC

```yaml
# CloudFormation: Enable node-to-node encryption for an OpenSearch domain
Resources:
  OpenSearchDomain:
    Type: AWS::OpenSearchService::Domain
    Properties:
      NodeToNodeEncryptionOptions:
        Enabled: true  # Critical: enables TLS between nodes to pass the check
```

### Terraform

```hcl
# Terraform: Enable node-to-node encryption for an OpenSearch domain
resource "aws_opensearch_domain" "<example_resource_name>" {
  domain_name = "<example_resource_name>"

  node_to_node_encryption {
    enabled = true  # Critical: encrypts intra-cluster traffic to pass the check
  }
}
```

### Other

1. In the AWS Console, go to OpenSearch Service > Domains
2. Select the target domain
3. Click Edit (or Actions > Edit security configuration)
4. Under Encryption, enable Node-to-node encryption
5. Click Save changes

## 参考资料

- [https://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/ntn.html](https://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/ntn.html)
- [https://docs.aws.amazon.com/opensearch-service/latest/developerguide/ntn.html](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/ntn.html)
- [https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/Elasticsearch/node-to-node-encryption.html](https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/Elasticsearch/node-to-node-encryption.html)

## 技术信息

- Source Metadata：[sources/aws/opensearch_service_domains_node_to_node_encryption_enabled/metadata.json](../../sources/aws/opensearch_service_domains_node_to_node_encryption_enabled/metadata.json)
- Source Code：[sources/aws/opensearch_service_domains_node_to_node_encryption_enabled/check.py](../../sources/aws/opensearch_service_domains_node_to_node_encryption_enabled/check.py)
- Source Metadata Path：`sources/aws/opensearch_service_domains_node_to_node_encryption_enabled/metadata.json`
- Source Code Path：`sources/aws/opensearch_service_domains_node_to_node_encryption_enabled/check.py`
