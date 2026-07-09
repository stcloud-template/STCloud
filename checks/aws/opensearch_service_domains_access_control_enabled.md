# Amazon OpenSearch Service domain has fine-grained access control enabled

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `opensearch_service_domains_access_control_enabled` |
| 云平台 | AWS |
| 服务 | opensearch |
| 严重等级 | high |
| 类别 | identity-access |
| 检查类型 | Software and Configuration Checks/AWS Security Best Practices, Software and Configuration Checks/Industry and Regulatory Standards/AWS Foundational Security Best Practices |
| 资源类型 | AwsOpenSearchServiceDomain |
| 资源组 | database |

## 描述

**Amazon OpenSearch Service domains** are evaluated for **fine-grained access control** being enabled in `advanced-security-options`, ensuring role-based authorization at index, document, and field levels for API and Dashboards access.

## 风险

Without **fine-grained access control**, identities may gain overly broad permissions, enabling unauthorized reads or writes across indices and Dashboards. This undermines **confidentiality** and **integrity**, facilitates lateral movement, and increases the blast radius of a compromised account.

## 推荐措施

Enable **fine-grained access control** in `advanced-security-options`. Define granular, role-based permissions (index/document/field) and map them to federated identities. Apply **least privilege**, deny-by-default, and **separation of duties**. Limit public access and regularly review role mappings.

## 修复步骤


### CLI

```text
aws opensearch update-domain-config --domain-name <DOMAIN_NAME> --advanced-security-options '{"Enabled":true,"MasterUserOptions":{"MasterUserARN":"<MASTER_USER_ARN>"}}'
```

### Native IaC

```yaml
# CloudFormation: Enable fine-grained access control (FGAC) on an OpenSearch domain
Resources:
  <example_resource_name>:
    Type: AWS::OpenSearchService::Domain
    Properties:
      DomainName: <example_resource_name>
      AdvancedSecurityOptions:
        Enabled: true  # Critical: Turns on FGAC
        MasterUserOptions:
          MasterUserARN: <MASTER_USER_ARN>  # Critical: Required to enable FGAC using an IAM principal
```

### Terraform

```hcl
# Enable fine-grained access control (FGAC) on an OpenSearch domain
resource "aws_opensearch_domain" "<example_resource_name>" {
  domain_name = "<example_resource_name>"

  advanced_security_options {
    enabled = true  # Critical: Turns on FGAC
    master_user_options {
      master_user_arn = "<MASTER_USER_ARN>"  # Critical: Required to enable FGAC using an IAM principal
    }
  }
}
```

### Other

1. In the AWS Console, go to Amazon OpenSearch Service
2. Select your domain and choose Edit security configuration
3. Enable Fine-grained access control
4. Set the master user (choose IAM ARN and enter <MASTER_USER_ARN> or create an internal master user)
5. Save changes and wait for the update to complete

## 参考资料

- [https://repost.aws/questions/QUvejSG0WDRByFVMcDchn_5w/how-do-resource-based-access-policies-interact-with-fgac-master-users-in-amazon-opensearch-service](https://repost.aws/questions/QUvejSG0WDRByFVMcDchn_5w/how-do-resource-based-access-policies-interact-with-fgac-master-users-in-amazon-opensearch-service)
- [https://docs.aws.amazon.com/securityhub/latest/userguide/opensearch-controls.html#opensearch-7](https://docs.aws.amazon.com/securityhub/latest/userguide/opensearch-controls.html#opensearch-7)
- [https://docs.aws.amazon.com/opensearch-service/latest/developerguide/fgac.html#fgac-enabling](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/fgac.html#fgac-enabling)
- [https://ealtili.medium.com/how-to-use-fine-grained-access-control-in-amazon-opensearch-service-4dc86bffd40d](https://ealtili.medium.com/how-to-use-fine-grained-access-control-in-amazon-opensearch-service-4dc86bffd40d)

## 技术信息

- Source Metadata：[sources/aws/opensearch_service_domains_access_control_enabled/metadata.json](../../sources/aws/opensearch_service_domains_access_control_enabled/metadata.json)
- Source Code：[sources/aws/opensearch_service_domains_access_control_enabled/check.py](../../sources/aws/opensearch_service_domains_access_control_enabled/check.py)
- Source Metadata Path：`sources/aws/opensearch_service_domains_access_control_enabled/metadata.json`
- Source Code Path：`sources/aws/opensearch_service_domains_access_control_enabled/check.py`
