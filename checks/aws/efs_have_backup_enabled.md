# EFS file system has backup enabled

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `efs_have_backup_enabled` |
| 云平台 | AWS |
| 服务 | efs |
| 严重等级 | medium |
| 类别 | resilience |
| 检查类型 | Software and Configuration Checks/AWS Security Best Practices, Software and Configuration Checks/Industry and Regulatory Standards/AWS Foundational Security Best Practices, Effects/Data Destruction |
| 资源类型 | AwsEfsFileSystem |
| 资源组 | storage |

## 描述

**Amazon EFS file systems** are assessed for automated backups configured via the `backup policy`. The finding highlights file systems where backups are not enabled or are being disabled.

## 风险

Absence of EFS backups degrades **availability** and **integrity**. Accidental deletion, ransomware, or misconfiguration can wipe or corrupt data with no recovery path. Without point-in-time copies, RPO/RTO suffer and localized incidents can become prolonged outages and irreversible loss.

## 推荐措施

Enable automated EFS backups by setting the file system `backup policy` to `ENABLED` and applying defense-in-depth: - Schedule frequent jobs with tiered retention - Use immutable vaults and cross-Region copies - Restrict delete/restore via **least privilege** and **separation of duties** - Regularly test restores and document DR objectives

## 修复步骤


### CLI

```text
aws efs put-backup-policy --file-system-id <FILE_SYSTEM_ID> --backup-policy Status=ENABLED
```

### Native IaC

```yaml
# CloudFormation: Enable automatic backups for EFS
Resources:
  <example_resource_name>:
    Type: AWS::EFS::FileSystem
    Properties:
      BackupPolicy:
        Status: ENABLED  # Critical: turns on EFS automatic backups via AWS Backup
```

### Terraform

```hcl
# Enable automatic backups for EFS
resource "aws_efs_file_system" "<example_resource_name>" {
  backup_policy {
    status = "ENABLED"  # Critical: turns on EFS automatic backups
  }
}
```

### Other

1. In the AWS Console, go to Amazon EFS > File systems
2. Select the target file system
3. Click Edit (or Update)
4. Set Automatic backups to Enabled
5. Save changes

## 参考资料

- [https://docs.aws.amazon.com/efs/latest/ug/awsbackup.html](https://docs.aws.amazon.com/efs/latest/ug/awsbackup.html)
- [https://docs.aws.amazon.com/efs/latest/ug/automatic-backups.html](https://docs.aws.amazon.com/efs/latest/ug/automatic-backups.html)

## 技术信息

- Source Metadata：[sources/aws/efs_have_backup_enabled/metadata.json](../../sources/aws/efs_have_backup_enabled/metadata.json)
- Source Code：[sources/aws/efs_have_backup_enabled/check.py](../../sources/aws/efs_have_backup_enabled/check.py)
- Source Metadata Path：`sources/aws/efs_have_backup_enabled/metadata.json`
- Source Code Path：`sources/aws/efs_have_backup_enabled/check.py`
