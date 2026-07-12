# Amazon OpenSearch Service domain has encryption at rest enabled

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `opensearch_service_domains_encryption_at_rest_enabled` |
| クラウドプラットフォーム | AWS |
| サービス | opensearch |
| 重大度 | critical |
| カテゴリ | encryption |
| チェックタイプ | Software and Configuration Checks/AWS Security Best Practices, Software and Configuration Checks/Industry and Regulatory Standards/AWS Foundational Security Best Practices, Effects/Data Exposure |
| リソースタイプ | AwsOpenSearchServiceDomain |
| リソースグループ | database |

## 説明

**Amazon OpenSearch Service domains** are evaluated for `encryption at rest` using AWS KMS (`AES-256`) across stored data, including indexes, swap files, and automated snapshots.

## リスク

**Unencrypted OpenSearch data** can be read or copied if an attacker gains **disk-level access**, steals **automated snapshots**, or compromises the host. This jeopardizes **confidentiality** and enables tampering with stored indices, affecting **integrity**.

## 推奨事項

Enable `encryption at rest` with AWS KMS, preferably using **customer-managed keys**. - Enforce **least privilege** key policies and restrict grants - Enable automatic key rotation and monitor KMS usage - Encrypt logs and any exported snapshots - Apply **defense in depth** with network and IAM controls

## 修正手順


### CLI

```text
aws opensearch update-domain-config --domain-name <DOMAIN_NAME> --encryption-at-rest-options Enabled=true
```

### Native IaC

```yaml
# CloudFormation: Enable encryption at rest for an OpenSearch domain
Resources:
  <example_resource_name>:
    Type: AWS::OpenSearchService::Domain
    Properties:
      DomainName: <example_resource_name>
      EncryptionAtRestOptions:
        Enabled: true  # Critical: turns on encryption at rest for the domain
```

### Terraform

```hcl
# Terraform: Enable encryption at rest for an OpenSearch domain
resource "aws_opensearch_domain" "<example_resource_name>" {
  domain_name = "<example_resource_name>"

  encrypt_at_rest {
    enabled = true  # Critical: turns on encryption at rest for the domain
  }
}
```

### Other

1. In the AWS Console, go to OpenSearch Service > Domains and select your domain
2. Click Actions > Edit security configuration
3. Under Encryption, check Enable encryption of data at rest
4. Keep the default AWS owned key (or select a KMS key if required)
5. Click Save changes

## 参考資料

- [https://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/encryption-at-rest.html](https://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/encryption-at-rest.html)
- [https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/Elasticsearch/encryption-at-rest.html](https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/Elasticsearch/encryption-at-rest.html)

## 技術情報

- Source Metadata：[sources/aws/opensearch_service_domains_encryption_at_rest_enabled/metadata.json](../../sources/aws/opensearch_service_domains_encryption_at_rest_enabled/metadata.json)
- Source Code：[sources/aws/opensearch_service_domains_encryption_at_rest_enabled/check.py](../../sources/aws/opensearch_service_domains_encryption_at_rest_enabled/check.py)
- Source Metadata Path：`sources/aws/opensearch_service_domains_encryption_at_rest_enabled/metadata.json`
- Source Code Path：`sources/aws/opensearch_service_domains_encryption_at_rest_enabled/check.py`
