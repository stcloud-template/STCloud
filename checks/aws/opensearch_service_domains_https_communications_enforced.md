# OpenSearch domain has HTTPS enforcement enabled

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `opensearch_service_domains_https_communications_enforced` |
| 云平台 | AWS |
| 服务 | opensearch |
| 严重等级 | high |
| 类别 | encryption |
| 检查类型 | Software and Configuration Checks/AWS Security Best Practices, Software and Configuration Checks/Industry and Regulatory Standards/AWS Foundational Security Best Practices, Software and Configuration Checks/Industry and Regulatory Standards/NIST 800-53 Controls (USA), Software and Configuration Checks/Industry and Regulatory Standards/PCI-DSS |
| 资源类型 | AwsOpenSearchServiceDomain |
| 资源组 | database |

## 描述

Amazon OpenSearch Service domains with **HTTPS enforcement** require encrypted connections. This assessment identifies domains missing `Require HTTPS for all traffic`, indicating that unencrypted HTTP is accepted.

## 风险

Allowing HTTP exposes queries, credentials, and results in cleartext, enabling interception and session hijacking. Adversaries can alter requests or responses, compromising **confidentiality** and **integrity**, and harvest auth data for **lateral movement**.

## 推荐措施

Enable `Require HTTPS for all traffic` on every domain to enforce TLS. Prefer strong protocols (TLS 1.2+), and block HTTP via network controls for defense in depth. Apply **least privilege** access policies and use private connectivity to minimize exposure and downgrade risks.

## 修复步骤


### CLI

```text
aws opensearch update-domain-config --domain-name <example_resource_name> --domain-endpoint-options EnforceHTTPS=true
```

### Native IaC

```yaml
# CloudFormation - Enable HTTPS enforcement on an OpenSearch domain
Resources:
  <example_resource_name>:
    Type: AWS::OpenSearchService::Domain
    Properties:
      DomainEndpointOptions:
        EnforceHTTPS: true  # Critical: requires all traffic to use HTTPS, fixing the finding
```

### Terraform

```hcl
# Enable HTTPS enforcement on an OpenSearch domain
resource "aws_opensearch_domain" "<example_resource_name>" {
  domain_name = "<example_resource_name>"

  domain_endpoint_options {
    enforce_https = true  # Critical: requires HTTPS for all requests
  }
}
```

### Other

1. Open the Amazon OpenSearch Service console
2. Go to Domains and select your domain
3. Click Actions > Edit security configuration
4. Check "Require HTTPS for all traffic to the domain"
5. Click Save changes

## 参考资料

- [https://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/es-createupdatedomains.html](https://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/es-createupdatedomains.html)

## 技术信息

- Source Metadata：[sources/aws/opensearch_service_domains_https_communications_enforced/metadata.json](../../sources/aws/opensearch_service_domains_https_communications_enforced/metadata.json)
- Source Code：[sources/aws/opensearch_service_domains_https_communications_enforced/check.py](../../sources/aws/opensearch_service_domains_https_communications_enforced/check.py)
- Source Metadata Path：`sources/aws/opensearch_service_domains_https_communications_enforced/metadata.json`
- Source Code Path：`sources/aws/opensearch_service_domains_https_communications_enforced/check.py`
