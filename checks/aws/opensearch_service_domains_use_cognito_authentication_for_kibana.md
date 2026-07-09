# Amazon OpenSearch Service domain has either Amazon Cognito or SAML authentication enabled for Kibana

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `opensearch_service_domains_use_cognito_authentication_for_kibana` |
| 云平台 | AWS |
| 服务 | opensearch |
| 严重等级 | medium |
| 类别 | identity-access |
| 检查类型 | Software and Configuration Checks/AWS Security Best Practices, Software and Configuration Checks/Industry and Regulatory Standards/AWS Foundational Security Best Practices, TTPs/Initial Access/Unauthorized Access, Effects/Data Exposure |
| 资源类型 | AwsOpenSearchServiceDomain |
| 资源组 | database |

## 描述

**OpenSearch Service domains** use **Amazon Cognito** or **SAML** to authenticate access to Kibana/OpenSearch Dashboards. The evaluation identifies domains where either provider is enabled for Dashboards access.

## 风险

Without **federated authentication**, Dashboards can be reached using weak or shared credentials or broad IP rules, enabling unauthorized queries and admin actions. This threatens: - **Confidentiality**: data exposure - **Integrity**: index changes or deletion - **Availability**: heavy queries degrading the cluster

## 推荐措施

Enable **Cognito** or **SAML** for Dashboards and apply **least privilege** with fine-grained access control. Prefer **SSO with MFA**, avoid shared/basic credentials, and restrict access via **VPC/private endpoints** and network controls. Monitor with audit logs and enforce **separation of duties**.

## 修复步骤


### CLI

```text
aws opensearch update-domain-config --domain-name <DOMAIN_NAME> --cognito-options Enabled=true,UserPoolId=<USER_POOL_ID>,IdentityPoolId=<IDENTITY_POOL_ID>,RoleArn=<ROLE_ARN>
```

### Native IaC

```yaml
# Enable Amazon Cognito authentication for OpenSearch Dashboards
Resources:
  <example_resource_name>:
    Type: AWS::OpenSearchService::Domain
    Properties:
      DomainName: <example_resource_name>
      CognitoOptions:
        Enabled: true  # Critical: Enables Cognito auth for Dashboards to pass the check
        UserPoolId: <USER_POOL_ID>
        IdentityPoolId: <IDENTITY_POOL_ID>
        RoleArn: <ROLE_ARN>
```

### Terraform

```hcl
# Enable Amazon Cognito authentication for OpenSearch Dashboards
resource "aws_opensearch_domain" "<example_resource_name>" {
  domain_name = "<example_resource_name>"

  cognito_options {
    enabled          = true  # Critical: Enables Cognito auth for Dashboards to pass the check
    user_pool_id     = "<USER_POOL_ID>"
    identity_pool_id = "<IDENTITY_POOL_ID>"
    role_arn         = "<ROLE_ARN>"
  }
}
```

### Other

1. In the AWS console, go to **OpenSearch Service** > **Domains** and select your domain
2. Click **Edit**
3. Under **OpenSearch Dashboards authentication**, choose **Amazon Cognito** and enable it
4. Enter the **User pool ID**, **Identity pool ID**, and **IAM role** for Cognito
5. Click **Save changes** and wait for the domain update to complete

## 参考资料

- [https://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/es-ac.html](https://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/es-ac.html)

## 技术信息

- Source Metadata：[sources/aws/opensearch_service_domains_use_cognito_authentication_for_kibana/metadata.json](../../sources/aws/opensearch_service_domains_use_cognito_authentication_for_kibana/metadata.json)
- Source Code：[sources/aws/opensearch_service_domains_use_cognito_authentication_for_kibana/check.py](../../sources/aws/opensearch_service_domains_use_cognito_authentication_for_kibana/check.py)
- Source Metadata Path：`sources/aws/opensearch_service_domains_use_cognito_authentication_for_kibana/metadata.json`
- Source Code Path：`sources/aws/opensearch_service_domains_use_cognito_authentication_for_kibana/check.py`
