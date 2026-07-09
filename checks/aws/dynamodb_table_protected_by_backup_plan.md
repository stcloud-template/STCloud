# DynamoDB table is protected by a backup plan

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `dynamodb_table_protected_by_backup_plan` |
| 云平台 | AWS |
| 服务 | dynamodb |
| 严重等级 | medium |
| 类别 | resilience |
| 检查类型 | Software and Configuration Checks/AWS Security Best Practices, Software and Configuration Checks/Industry and Regulatory Standards/AWS Foundational Security Best Practices |
| 资源类型 | AwsDynamoDbTable |
| 资源组 | database |

## 描述

**DynamoDB tables** are evaluated for inclusion in an **AWS Backup backup plan** through resource assignments, including explicit tables, resource-type wildcards, or all-resources coverage. The result indicates whether a table is governed by scheduled backups and retention defined by the plan.

## 风险

Without a backup plan, table data lacks governed copies, harming **availability** and **integrity**. Accidental deletes, corrupt writes, or malicious actions can become unrecoverable, and RPO/RTO worsen. You also forfeit cross-Region/account copies and immutability features, increasing downtime and data loss.

## 推荐措施

Place all critical tables under an **AWS Backup backup plan** following **defense in depth** and **least privilege**: - Use tag-based assignments for coverage at scale - Define schedules, retention, and cross-Region/account copies - Enable **Vault Lock** for immutability - Regularly test restores and restrict backup deletion

## 修复步骤


### Native IaC

```yaml
# CloudFormation: Add DynamoDB tables to an AWS Backup plan
Resources:
  BackupPlan:
    Type: AWS::Backup::BackupPlan
    Properties:
      BackupPlan:
        BackupPlanName: <example_resource_name>
        BackupPlanRule:
          - RuleName: r
            TargetBackupVault: Default

  BackupSelection:
    Type: AWS::Backup::BackupSelection
    Properties:
      BackupPlanId: !Ref BackupPlan
      BackupSelection:
        SelectionName: <example_resource_name>
        IamRoleArn: <example_role_arn>
        Resources:
          - arn:aws:dynamodb:*:*:table/*  # CRITICAL: adds all DynamoDB tables to the backup plan, making them protected
```

### Terraform

```hcl
# Terraform: Add DynamoDB tables to an AWS Backup plan
resource "aws_backup_plan" "<example_resource_name>" {
  name = "<example_resource_name>"
  rule {
    rule_name         = "r"
    target_vault_name = "Default"
  }
}

data "aws_iam_role" "<example_resource_name>" {
  name = "AWSServiceRoleForBackup"
}

resource "aws_backup_selection" "<example_resource_name>" {
  name         = "<example_resource_name>"
  plan_id      = aws_backup_plan.<example_resource_name>.id
  iam_role_arn = data.aws_iam_role.<example_resource_name>.arn
  resources    = [
    "arn:aws:dynamodb:*:*:table/*" # CRITICAL: adds all DynamoDB tables to the backup plan, making them protected
  ]
}
```

### Other

1. In the AWS Backup console, go to Settings > Configure resources and enable DynamoDB, then Confirm
2. Go to Backup plans > Create backup plan > Build a new plan
3. Enter a plan name, set Rule name to any value, set Backup vault to Default, and Create plan
4. On the plan page, choose Assign resources
5. Enter a Resource assignment name, set IAM role to Default role, select your DynamoDB table, and choose Assign resources

## 参考资料

- [https://docs.aws.amazon.com/aws-backup/latest/devguide/assigning-resources.html](https://docs.aws.amazon.com/aws-backup/latest/devguide/assigning-resources.html)
- [https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/CreateBackupAWS.html](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/CreateBackupAWS.html)
- [https://aws.amazon.com/blogs/database/set-up-scheduled-backups-for-amazon-dynamodb-using-aws-backup/](https://aws.amazon.com/blogs/database/set-up-scheduled-backups-for-amazon-dynamodb-using-aws-backup/)

## 技术信息

- Source Metadata：[sources/aws/dynamodb_table_protected_by_backup_plan/metadata.json](../../sources/aws/dynamodb_table_protected_by_backup_plan/metadata.json)
- Source Code：[sources/aws/dynamodb_table_protected_by_backup_plan/check.py](../../sources/aws/dynamodb_table_protected_by_backup_plan/check.py)
- Source Metadata Path：`sources/aws/dynamodb_table_protected_by_backup_plan/metadata.json`
- Source Code Path：`sources/aws/dynamodb_table_protected_by_backup_plan/check.py`
