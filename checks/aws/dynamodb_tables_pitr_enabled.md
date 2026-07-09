# DynamoDB table has point-in-time recovery (PITR) enabled

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `dynamodb_tables_pitr_enabled` |
| 云平台 | AWS |
| 服务 | dynamodb |
| 严重等级 | medium |
| 类别 | resilience |
| 检查类型 | Software and Configuration Checks/Industry and Regulatory Standards/AWS Foundational Security Best Practices, Effects/Data Destruction |
| 资源类型 | AwsDynamoDbTable |
| 资源组 | database |

## 描述

**DynamoDB tables** have **Point-in-Time Recovery** (`PITR`) enabled

## 风险

Without **PITR**, unintended or malicious writes/deletes cannot be precisely rolled back, leading to permanent data loss and corrupted state. Failures from buggy deployments, compromised credentials, or faulty batch jobs reduce data **integrity** and **availability**, and prolong incident recovery and forensic analysis.

## 推荐措施

Enable **PITR** on critical tables and set a recovery window aligned to your RPO (1-35 days). Enforce **least privilege** on who can modify backup settings. Regularly test restores and monitor backup status. Embed PITR in IaC and change control for consistency, and apply **defense in depth** with on-demand backups for key milestones.

## 修复步骤


### CLI

```text
aws dynamodb update-continuous-backups --table-name <table_name> --point-in-time-recovery-specification PointInTimeRecoveryEnabled=true
```

### Native IaC

```yaml
# CloudFormation: enable PITR on a DynamoDB table
Resources:
  <example_resource_name>:
    Type: AWS::DynamoDB::Table
    Properties:
      PointInTimeRecoverySpecification:
        PointInTimeRecoveryEnabled: true  # Critical: enables Point-in-Time Recovery (PITR)
```

### Terraform

```hcl
# Enable PITR on a DynamoDB table
resource "aws_dynamodb_table" "<example_resource_name>" {
  name         = "<example_resource_name>"
  billing_mode = "PAY_PER_REQUEST"
  hash_key     = "id"

  attribute {
    name = "id"
    type = "S"
  }

  point_in_time_recovery {
    enabled = true  # Critical: enables PITR
  }
}
```

### Other

1. Open the AWS Management Console and go to DynamoDB
2. Select your table and open the Backups tab
3. Click Edit in the Point-in-time recovery section and choose Turn on point-in-time recovery
4. Click Save

## 参考资料

- [https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/PointInTimeRecovery_Howitworks.html](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/PointInTimeRecovery_Howitworks.html)
- [https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/PointInTimeRecovery.Tutorial.html](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/PointInTimeRecovery.Tutorial.html)

## 技术信息

- Source Metadata：[sources/aws/dynamodb_tables_pitr_enabled/metadata.json](../../sources/aws/dynamodb_tables_pitr_enabled/metadata.json)
- Source Code：[sources/aws/dynamodb_tables_pitr_enabled/check.py](../../sources/aws/dynamodb_tables_pitr_enabled/check.py)
- Source Metadata Path：`sources/aws/dynamodb_tables_pitr_enabled/metadata.json`
- Source Code Path：`sources/aws/dynamodb_tables_pitr_enabled/check.py`
