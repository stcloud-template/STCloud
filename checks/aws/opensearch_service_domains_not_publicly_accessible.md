# Amazon OpenSearch Service domain is not publicly accessible

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `opensearch_service_domains_not_publicly_accessible` |
| クラウドプラットフォーム | AWS |
| サービス | opensearch |
| 重大度 | critical |
| カテゴリ | internet-exposed |
| チェックタイプ | Software and Configuration Checks/AWS Security Best Practices/Network Reachability, Software and Configuration Checks/Industry and Regulatory Standards/AWS Foundational Security Best Practices, Effects/Data Exposure, TTPs/Initial Access |
| リソースタイプ | AwsOpenSearchServiceDomain |
| リソースグループ | database |

## 説明

**Amazon OpenSearch domains** are assessed for **public exposure** via their resource-based access policies. Domains inside a VPC are treated as **privately reachable**; domains with overly permissive policies that allow broad, unauthenticated access are identified as **publicly accessible**.

## リスク

Public exposure lets anyone query, index, or delete data, impacting **confidentiality** (record disclosure), **integrity** (unauthorized writes, index tampering), and **availability** (disruption, deletion). Attackers can harvest sensitive logs/PII, alter analytics, or wipe indices, enabling lateral movement and operational outage.

## 推奨事項

Apply **least privilege** and **defense in depth**: - Place domains in a **VPC** and restrict reachability with security groups - Use narrow resource policies; avoid `Principal:"*"` - Require authenticated access (fine-grained controls); *if unavoidable*, limit public endpoints by IP and roles - Monitor access with logs and alerts

## 修正手順


### CLI

```text
aws opensearch update-domain-config --domain-name <DOMAIN_NAME> --access-policies '{"Version":"2012-10-17","Statement":[{"Effect":"Allow","Principal":{"AWS":"arn:aws:iam::<ACCOUNT_ID>:root"},"Action":"es:*","Resource":"arn:aws:es:<REGION>:<ACCOUNT_ID>:domain/<DOMAIN_NAME>/*"}]}'
```

### Native IaC

```yaml
# CloudFormation: restrict OpenSearch access policy to your account only
Resources:
  <example_resource_name>:
    Type: AWS::OpenSearchService::Domain
    Properties:
      DomainName: <example_resource_name>
      AccessPolicies:  # critical: restricts access to your account only, removing public access
        Version: '2012-10-17'
        Statement:
          - Effect: Allow
            Principal:
              AWS: arn:aws:iam::<ACCOUNT_ID>:root  # critical: only this account can access
            Action: es:*
            Resource: arn:aws:es:<REGION>:<ACCOUNT_ID>:domain/<example_resource_name>/*
```

### Terraform

```hcl
# Restrict OpenSearch access policy to your account only
resource "aws_opensearch_domain" "<example_resource_name>" {
  domain_name = "<example_resource_name>"

  # critical: limits access to the owning account, removing public access
  access_policies = jsonencode({
    Version = "2012-10-17"
    Statement = [{
      Effect    = "Allow"
      Principal = { AWS = "arn:aws:iam::<ACCOUNT_ID>:root" }
      Action    = "es:*"
      Resource  = "arn:aws:es:<REGION>:<ACCOUNT_ID>:domain/<example_resource_name>/*"
    }]
  })
}
```

### Other

1. In the AWS console, open Amazon OpenSearch Service and select your domain
2. Go to Security configuration > Edit
3. Choose Access policy > JSON
4. Replace the policy with the following (use your values) and Save changes:
```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {"AWS": "arn:aws:iam::<ACCOUNT_ID>:root"},
      "Action": "es:*",
      "Resource": "arn:aws:es:<REGION>:<ACCOUNT_ID>:domain/<DOMAIN_NAME>/*"
    }
  ]
}
```
5. Verify the domain endpoint is no longer accessible publicly except by your account's IAM principals

## 参考資料

- [https://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/es-vpc.html](https://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/es-vpc.html)
- [https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/Elasticsearch/domain-exposed.html](https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/Elasticsearch/domain-exposed.html)

## 技術情報

- Source Metadata：[sources/aws/opensearch_service_domains_not_publicly_accessible/metadata.json](../../sources/aws/opensearch_service_domains_not_publicly_accessible/metadata.json)
- Source Code：[sources/aws/opensearch_service_domains_not_publicly_accessible/check.py](../../sources/aws/opensearch_service_domains_not_publicly_accessible/check.py)
- Source Metadata Path：`sources/aws/opensearch_service_domains_not_publicly_accessible/metadata.json`
- Source Code Path：`sources/aws/opensearch_service_domains_not_publicly_accessible/check.py`
