# DynamoDB table has deletion protection enabled

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `dynamodb_table_deletion_protection_enabled` |
| 云平台 | AWS |
| 服务 | dynamodb |
| 严重等级 | medium |
| 类别 | resilience |
| 检查类型 | Software and Configuration Checks/AWS Security Best Practices, Software and Configuration Checks/Industry and Regulatory Standards/AWS Foundational Security Best Practices, Effects/Data Destruction |
| 资源类型 | AwsDynamoDbTable |
| 资源组 | database |

## 描述

**DynamoDB tables** have **deletion protection** enabled via the `deletion protection` setting, meaning delete operations require this setting to be disabled first

## 风险

Without **deletion protection**, tables can be removed by authorized actions or misconfigured automation, causing irrecoverable data loss and service outage. This impacts **integrity** and **availability**, and increases the blast radius of compromised credentials or mistaken runbooks.

## 推荐措施

Enable **deletion protection** on critical tables. - Enforce **least privilege** to restrict who can modify this setting - Require change control to disable it before planned deletes - Combine with **PITR** and backups for defense in depth - Use automation to make this the default for new tables

## 修复步骤


### CLI

```text
aws dynamodb update-table --table-name <TABLE_NAME> --deletion-protection-enabled
```

### Native IaC

```yaml
Resources:
  <example_resource_name>:
    Type: AWS::DynamoDB::Table
    Properties:
      DeletionProtectionEnabled: true  # CRITICAL: Enables deletion protection to prevent table deletion
```

### Terraform

```hcl
resource "aws_dynamodb_table" "<example_resource_name>" {
  name     = "<example_resource_name>"
  hash_key = "id"

  attribute {
    name = "id"
    type = "S"
  }

  deletion_protection_enabled = true  # CRITICAL: Prevents accidental table deletion
}
```

### Other

1. Open the AWS Management Console and go to DynamoDB
2. Select the table
3. Choose Additional settings
4. Enable Deletion protection
5. Save changes

## 参考资料

- [https://docs.aws.amazon.com/securityhub/latest/userguide/dynamodb-controls.html#dynamodb-6](https://docs.aws.amazon.com/securityhub/latest/userguide/dynamodb-controls.html#dynamodb-6)
- [https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/WorkingWithTables.Basics.html#WorkingWithTables.Basics.DeletionProtection](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/WorkingWithTables.Basics.html#WorkingWithTables.Basics.DeletionProtection)

## 技术信息

- Source Metadata：[sources/aws/dynamodb_table_deletion_protection_enabled/metadata.json](../../sources/aws/dynamodb_table_deletion_protection_enabled/metadata.json)
- Source Code：[sources/aws/dynamodb_table_deletion_protection_enabled/check.py](../../sources/aws/dynamodb_table_deletion_protection_enabled/check.py)
- Source Metadata Path：`sources/aws/dynamodb_table_deletion_protection_enabled/metadata.json`
- Source Code Path：`sources/aws/dynamodb_table_deletion_protection_enabled/check.py`
