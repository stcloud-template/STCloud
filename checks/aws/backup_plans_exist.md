# At least one AWS Backup plan exists

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `backup_plans_exist` |
| 云平台 | AWS |
| 服务 | backup |
| 严重等级 | low |
| 类别 | resilience |
| 检查类型 | Software and Configuration Checks/AWS Security Best Practices, Software and Configuration Checks/Industry and Regulatory Standards/AWS Foundational Security Best Practices |
| 资源类型 | AwsBackupBackupPlan |
| 资源组 | storage |

## 描述

**AWS Backup** is assessed for the existence of at least one **backup plan** that schedules and retains recovery points for selected resources. The evaluation determines whether any plan is configured; when none is found-even if backup vaults exist-the absence of a plan is noted.

## 风险

Without a backup plan, resources lack scheduled recovery points, undermining RPO/RTO. - Irrecoverable data after deletion or corruption (integrity) - Prolonged outages due to unavailable restores (availability) - Inconsistent backups that hinder investigations and controlled recovery

## 推荐措施

Establish and enforce **backup plans** for critical workloads: - Define schedules, retention, and lifecycle to meet RPO/RTO - Use tagging to include all required resources by policy - Enable cross-Region/account copies and immutability where feasible - Apply least privilege to backup roles - Regularly test restores and review reports

## 修复步骤


### CLI

```text
aws backup create-backup-plan --backup-plan "{\"BackupPlanName\":\"<example_resource_name>\",\"Rules\":[{\"RuleName\":\"<example_resource_name>\",\"TargetBackupVaultName\":\"Default\"}]}"
```

### Native IaC

```yaml
# CloudFormation: create a minimal AWS Backup Plan to pass the check
Resources:
  <example_resource_name>:
    Type: AWS::Backup::BackupPlan
    Properties:
      BackupPlan:
        BackupPlanName: <example_resource_name>  # Critical: ensures at least one Backup Plan exists
        Rules:
          - RuleName: <example_resource_name>     # Critical: minimal required rule
            TargetBackupVault: Default            # Critical: required vault for the rule
```

### Terraform

```hcl
# Terraform: minimal AWS Backup Plan to satisfy the check
resource "aws_backup_plan" "<example_resource_name>" {
  name = "<example_resource_name>"  # Critical: creates the Backup Plan so the check passes

  rule {
    rule_name         = "<example_resource_name>"  # Critical: minimal rule
    target_vault_name = "Default"                  # Critical: required vault
  }
}
```

### Other

1. In the AWS Console, go to AWS Backup
2. Click Backup plans > Create backup plan
3. Choose Build a new plan
4. Enter Plan name: <example_resource_name>
5. Under Backup rule, set Rule name: <example_resource_name> and Target backup vault: Default
6. Click Create plan

## 参考资料

- [https://awscli.amazonaws.com/v2/documentation/api/2.0.33/reference/backup/create-backup-plan.html](https://awscli.amazonaws.com/v2/documentation/api/2.0.33/reference/backup/create-backup-plan.html)
- [https://docs.aws.amazon.com/aws-backup/latest/devguide/about-backup-plans.html](https://docs.aws.amazon.com/aws-backup/latest/devguide/about-backup-plans.html)
- [https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/backup_plan](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/backup_plan)
- [https://medium.com/@christopheradamson253/backup-strategies-using-aws-backup-1b17b94a7957](https://medium.com/@christopheradamson253/backup-strategies-using-aws-backup-1b17b94a7957)

## 技术信息

- Source Metadata：[sources/aws/backup_plans_exist/metadata.json](../../sources/aws/backup_plans_exist/metadata.json)
- Source Code：[sources/aws/backup_plans_exist/check.py](../../sources/aws/backup_plans_exist/check.py)
- Source Metadata Path：`sources/aws/backup_plans_exist/metadata.json`
- Source Code Path：`sources/aws/backup_plans_exist/check.py`
