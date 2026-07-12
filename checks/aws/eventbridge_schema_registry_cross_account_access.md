# AWS EventBridge schema registry does not allow cross-account access

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `eventbridge_schema_registry_cross_account_access` |
| クラウドプラットフォーム | AWS |
| サービス | eventbridge |
| 重大度 | high |
| カテゴリ | trust-boundaries, identity-access |
| チェックタイプ | Software and Configuration Checks/AWS Security Best Practices, Software and Configuration Checks/Industry and Regulatory Standards/AWS Foundational Security Best Practices, TTPs/Initial Access/Unauthorized Access, Effects/Data Exposure |
| リソースタイプ | AwsEventSchemasRegistry |
| リソースグループ | messaging |

## 説明

**EventBridge schema registry** resource policies are assessed for **cross-account access**. It identifies statements that grant external or public principals (e.g., `Principal: *` or other accounts) permissions to interact with the registry and its schemas.

## リスク

Unknown cross-account access exposes schema definitions, enabling reconnaissance and leaking data models (**confidentiality**). Excessive permissions may let outsiders alter or delete schemas, corrupt code bindings, and disrupt integrations (**integrity** and **availability**).

## 推奨事項

Apply **least privilege** to registry resource policies: - Avoid public principals like `Principal: *` - Allow only trusted account ARNs or org IDs - Grant minimal actions, prefer read-only - Use **separation of duties** and log changes *If cross-account is needed*, scope tightly and review often.

## 修正手順


### CLI

```text
aws schemas put-resource-policy --registry-name <example_resource_name> --policy '{"Version":"2012-10-17","Statement":[{"Effect":"Allow","Principal":{"AWS":"arn:aws:iam::<example_account_id>:root"},"Action":"schemas:*","Resource":"*"}]}'
```

### Native IaC

```yaml
# CloudFormation: Restrict EventBridge Schema Registry policy to same account only
Resources:
  <example_resource_name>RegistryPolicy:
    Type: AWS::EventSchemas::RegistryPolicy
    Properties:
      RegistryName: <example_resource_name>
      # Critical: Principal limited to this AWS account to prevent cross-account access
      Policy: !Sub |
        {
          "Version": "2012-10-17",
          "Statement": [
            {
              "Effect": "Allow",
              "Principal": { "AWS": "arn:${AWS::Partition}:iam::${AWS::AccountId}:root" },
              "Action": "schemas:*",
              "Resource": "*"
            }
          ]
        }
```

### Terraform

```hcl
# Restrict EventBridge Schema Registry policy to same account only
resource "aws_schemas_registry_policy" "<example_resource_name>" {
  registry_name = "<example_resource_name>"

  # Critical: Principal limited to same account to remove cross-account access
  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [{
      Effect    = "Allow"
      Principal = { AWS = "arn:aws:iam::<example_account_id>:root" }
      Action    = "schemas:*"
      Resource  = "*"
    }]
  })
}
```

### Other

1. Open the Amazon EventBridge console
2. Go to Schemas > Registries and select <example_resource_name>
3. Open the Permissions tab and click Edit
4. Remove any statement with Principal set to "*" or an AWS account different from yours
5. Add a single Allow statement with Principal = arn:aws:iam::<your_account_id>:root
6. Save changes

## 参考資料

- [https://aws.amazon.com/about-aws/whats-new/2021/09/cross-account-discovery-amazon-eventbridge-schema/](https://aws.amazon.com/about-aws/whats-new/2021/09/cross-account-discovery-amazon-eventbridge-schema/)
- [https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-schema.html](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-schema.html)

## 技術情報

- Source Metadata：[sources/aws/eventbridge_schema_registry_cross_account_access/metadata.json](../../sources/aws/eventbridge_schema_registry_cross_account_access/metadata.json)
- Source Code：[sources/aws/eventbridge_schema_registry_cross_account_access/check.py](../../sources/aws/eventbridge_schema_registry_cross_account_access/check.py)
- Source Metadata Path：`sources/aws/eventbridge_schema_registry_cross_account_access/metadata.json`
- Source Code Path：`sources/aws/eventbridge_schema_registry_cross_account_access/check.py`
