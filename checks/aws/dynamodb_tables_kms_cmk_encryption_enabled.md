# DynamoDB table is encrypted at rest with AWS KMS

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `dynamodb_tables_kms_cmk_encryption_enabled` |
| 云平台 | AWS |
| 服务 | dynamodb |
| 严重等级 | medium |
| 类别 | encryption |
| 检查类型 | Software and Configuration Checks/Industry and Regulatory Standards/AWS Foundational Security Best Practices, Software and Configuration Checks/Industry and Regulatory Standards/CIS AWS Foundations Benchmark, Software and Configuration Checks/AWS Security Best Practices |
| 资源类型 | AwsDynamoDbTable |
| 资源组 | database |

## 描述

**DynamoDB tables** use **AWS KMS keys** (`KMS`) for encryption at rest instead of the default service-owned key

## 风险

Relying on the default service-owned key reduces control over **confidentiality**: no custom key policies, limited auditability, and no independent rotation or disablement. This weakens least-privilege enforcement and incident response, and can impede meeting mandates that require customer-controlled keys.

## 推荐措施

Encrypt tables with **KMS keys** in your account-prefer **customer-managed keys** for sensitive data. - Enforce least-privilege key policies and scope grants - Enable rotation and monitor key usage - Separate duties for key admins vs data users - Restrict which principals can use the key for DynamoDB

## 修复步骤


### CLI

```text
aws dynamodb update-table --table-name <example_resource_name> --sse-specification Enabled=true,SSEType=KMS
```

### Native IaC

```yaml
# CloudFormation: Enable KMS encryption on a DynamoDB table
Resources:
  <example_resource_name>:
    Type: AWS::DynamoDB::Table
    Properties:
      AttributeDefinitions:
        - AttributeName: id
          AttributeType: S
      KeySchema:
        - AttributeName: id
          KeyType: HASH
      BillingMode: PAY_PER_REQUEST
      SSESpecification:
        SSEEnabled: true  # Critical: enables KMS-based encryption
        SSEType: KMS      # Critical: switches from DEFAULT to AWS KMS
```

### Terraform

```hcl
resource "aws_dynamodb_table" "<example_resource_name>" {
  name         = "<example_resource_name>"
  billing_mode = "PAY_PER_REQUEST"
  hash_key     = "id"

  attribute {
    name = "id"
    type = "S"
  }

  server_side_encryption {
    enabled = true  # Critical: enables AWS KMS encryption (uses AWS managed key if no key ARN provided)
  }
}
```

### Other

1. Open the AWS Management Console and go to DynamoDB
2. Select your table
3. In Table details, find Encryption at rest and click Edit
4. Select AWS KMS: choose AWS managed key (alias/aws/dynamodb) or a customer managed key
5. Click Save

## 参考资料

- [https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/EncryptionAtRest.html](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/EncryptionAtRest.html)

## 技术信息

- Source Metadata：[sources/aws/dynamodb_tables_kms_cmk_encryption_enabled/metadata.json](../../sources/aws/dynamodb_tables_kms_cmk_encryption_enabled/metadata.json)
- Source Code：[sources/aws/dynamodb_tables_kms_cmk_encryption_enabled/check.py](../../sources/aws/dynamodb_tables_kms_cmk_encryption_enabled/check.py)
- Source Metadata Path：`sources/aws/dynamodb_tables_kms_cmk_encryption_enabled/metadata.json`
- Source Code Path：`sources/aws/dynamodb_tables_kms_cmk_encryption_enabled/check.py`
