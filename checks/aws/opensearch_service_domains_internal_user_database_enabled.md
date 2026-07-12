# Amazon OpenSearch Service domain has internal user database disabled

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `opensearch_service_domains_internal_user_database_enabled` |
| クラウドプラットフォーム | AWS |
| サービス | opensearch |
| 重大度 | medium |
| カテゴリ | identity-access |
| チェックタイプ | Software and Configuration Checks/AWS Security Best Practices |
| リソースタイプ | AwsOpenSearchServiceDomain |
| リソースグループ | database |

## 説明

**Amazon OpenSearch Service domains** are evaluated for the **internal user database** setting (`InternalUserDatabaseEnabled`). The finding identifies domains that rely on built-in HTTP basic users instead of external identity providers.

## リスク

An enabled internal user database creates **credential sprawl** and weak **account lifecycle**. Missing centralized MFA, rotation, and revocation raises unauthorized access risk, impacting **confidentiality** and **integrity**. Basic auth on exposed endpoints eases brute force and reduces **auditability**.

## 推奨事項

Prefer **federated authentication** (IAM, SAML, or Amazon Cognito) and disable the **internal user database**. Enforce **least privilege** roles, require **MFA**, centralize credential rotation and offboarding, and log access. Use **VPC access** and restrictive policies; avoid HTTP basic auth to minimize exposure.

## 修正手順


### CLI

```text
aws opensearch update-domain-config --domain-name <example_resource_name> --advanced-security-options '{"InternalUserDatabaseEnabled":false}'
```

### Native IaC

```yaml
# CloudFormation: disable internal user database for the domain
Resources:
  <example_resource_name>:
    Type: AWS::OpenSearchService::Domain
    Properties:
      AdvancedSecurityOptions:
        InternalUserDatabaseEnabled: false  # Critical: disables internal user DB to pass the check
```

### Terraform

```hcl
# Terraform: disable internal user database for the domain
resource "aws_opensearch_domain" "<example_resource_name>" {
  domain_name = "<example_resource_name>"

  advanced_security_options {
    internal_user_database_enabled = false  # Critical: disables internal user DB to pass the check
  }
}
```

### Other

1. In AWS console, go to Amazon OpenSearch Service > Domains
2. Select the domain and choose Edit security configuration
3. Under Fine-grained access control, turn off Internal user database
4. Click Save changes

## 参考資料

- [https://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/fgac.html](https://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/fgac.html)
- [https://docs.aws.amazon.com/opensearch-service/latest/developerguide/fgac.html](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/fgac.html)

## 技術情報

- Source Metadata：[sources/aws/opensearch_service_domains_internal_user_database_enabled/metadata.json](../../sources/aws/opensearch_service_domains_internal_user_database_enabled/metadata.json)
- Source Code：[sources/aws/opensearch_service_domains_internal_user_database_enabled/check.py](../../sources/aws/opensearch_service_domains_internal_user_database_enabled/check.py)
- Source Metadata Path：`sources/aws/opensearch_service_domains_internal_user_database_enabled/metadata.json`
- Source Code Path：`sources/aws/opensearch_service_domains_internal_user_database_enabled/check.py`
