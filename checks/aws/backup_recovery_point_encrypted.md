# AWS Backup recovery point is encrypted at rest

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `backup_recovery_point_encrypted` |
| 云平台 | AWS |
| 服务 | backup |
| 严重等级 | medium |
| 类别 | encryption |
| 检查类型 | Software and Configuration Checks/AWS Security Best Practices, Software and Configuration Checks/Industry and Regulatory Standards/AWS Foundational Security Best Practices, Effects/Data Exposure |
| 资源类型 | AwsBackupRecoveryPoint |
| 资源组 | storage |

## 描述

**AWS Backup recovery points** are evaluated for **encryption at rest** using the backup vault's KMS configuration. Items lacking vault-level encryption are highlighted, regardless of the source resource's encryption.

## 风险

Unencrypted recovery points can be read or copied if vault access is obtained, enabling offline analysis and data theft (**confidentiality**). Snapshots or restores may be altered (**integrity**), and unsafe restores can disrupt recovery operations (**availability**).

## 推荐措施

Encrypt all recovery points with **KMS**, preferring **customer-managed keys** for rotation and control. Apply **least privilege** to keys and vaults, require encrypted copies across accounts/Regions, and continuously monitor for unencrypted artifacts. Use `aws/backup` or `CMEK` consistently.

## 修复步骤


### Native IaC

```yaml
# CloudFormation: Encrypted AWS Backup Vault
Resources:
  <example_resource_name>:
    Type: AWS::Backup::BackupVault
    Properties:
      BackupVaultName: <example_resource_name>
      EncryptionKeyArn: <kms_key_arn>  # Critical: vault uses this KMS key so recovery points stored here are encrypted at rest
```

### Terraform

```hcl
# Encrypted AWS Backup Vault
resource "aws_backup_vault" "<example_resource_name>" {
  name        = "<example_resource_name>"
  kms_key_arn = "<kms_key_arn>" # Critical: ensures recovery points in this vault are encrypted at rest
}
```

### Other

1. In AWS Backup, go to Backup vaults > Create backup vault
2. Enter a name and select a KMS key (aws/backup or a customer-managed key)
3. Save the vault
4. Go to Backup plans > select your plan > Edit and set the Target backup vault to the encrypted vault > Save
5. To remediate existing unencrypted recovery points: Recovery points > select the item > Copy > choose the encrypted vault > Start copy, then delete the original unencrypted recovery point

## 参考资料

- [https://docs.aws.amazon.com/securityhub/latest/userguide/backup-controls.html#backup-1](https://docs.aws.amazon.com/securityhub/latest/userguide/backup-controls.html#backup-1)
- [https://readmedium.com/how-would-you-desgin-a-solution-for-autmated-backup-and-recovery-of-data-and-services-in-aws-311662f5a43e](https://readmedium.com/how-would-you-desgin-a-solution-for-autmated-backup-and-recovery-of-data-and-services-in-aws-311662f5a43e)
- [https://docs.aws.amazon.com/aws-backup/latest/devguide/encryption.html](https://docs.aws.amazon.com/aws-backup/latest/devguide/encryption.html)
- [https://medium.com/cloud-devops-security-ai-career-talk/how-would-you-desgin-a-solution-for-autmated-backup-and-recovery-of-data-and-services-in-aws-311662f5a43e](https://medium.com/cloud-devops-security-ai-career-talk/how-would-you-desgin-a-solution-for-autmated-backup-and-recovery-of-data-and-services-in-aws-311662f5a43e)
- [https://github.com/turbot/steampipe-mod-aws-compliance/issues/598](https://github.com/turbot/steampipe-mod-aws-compliance/issues/598)

## 技术信息

- Source Metadata：[sources/aws/backup_recovery_point_encrypted/metadata.json](../../sources/aws/backup_recovery_point_encrypted/metadata.json)
- Source Code：[sources/aws/backup_recovery_point_encrypted/check.py](../../sources/aws/backup_recovery_point_encrypted/check.py)
- Source Metadata Path：`sources/aws/backup_recovery_point_encrypted/metadata.json`
- Source Code Path：`sources/aws/backup_recovery_point_encrypted/check.py`
