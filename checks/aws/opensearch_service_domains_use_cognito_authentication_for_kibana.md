# Amazon OpenSearch Service domain has either Amazon Cognito or SAML authentication enabled for Kibana

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `opensearch_service_domains_use_cognito_authentication_for_kibana` |
| クラウドプラットフォーム | AWS |
| サービス | opensearch |
| 重大度 | medium |
| カテゴリ | identity-access |
| チェックタイプ | Software and Configuration Checks/AWS Security Best Practices, Software and Configuration Checks/Industry and Regulatory Standards/AWS Foundational Security Best Practices, TTPs/Initial Access/Unauthorized Access, Effects/Data Exposure |
| リソースタイプ | AwsOpenSearchServiceDomain |
| リソースグループ | database |

## 説明

**OpenSearch Service domains** use **Amazon Cognito** or **SAML** to authenticate access to Kibana/OpenSearch Dashboards. The evaluation identifies domains where either provider is enabled for Dashboards access.

## リスク

Without **federated authentication**, Dashboards can be reached using weak or shared credentials or broad IP rules, enabling unauthorized queries and admin actions. This threatens: - **Confidentiality**: data exposure - **Integrity**: index changes or deletion - **Availability**: heavy queries degrading the cluster

## 推奨事項

Enable **Cognito** or **SAML** for Dashboards and apply **least privilege** with fine-grained access control. Prefer **SSO with MFA**, avoid shared/basic credentials, and restrict access via **VPC/private endpoints** and network controls. Monitor with audit logs and enforce **separation of duties**.

## 修正手順


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

## 参考資料

- [https://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/es-ac.html](https://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/es-ac.html)

## 技術情報

- Source Metadata：[sources/aws/opensearch_service_domains_use_cognito_authentication_for_kibana/metadata.json](../../sources/aws/opensearch_service_domains_use_cognito_authentication_for_kibana/metadata.json)
- Source Code：[sources/aws/opensearch_service_domains_use_cognito_authentication_for_kibana/check.py](../../sources/aws/opensearch_service_domains_use_cognito_authentication_for_kibana/check.py)
- Source Metadata Path：`sources/aws/opensearch_service_domains_use_cognito_authentication_for_kibana/metadata.json`
- Source Code Path：`sources/aws/opensearch_service_domains_use_cognito_authentication_for_kibana/check.py`
