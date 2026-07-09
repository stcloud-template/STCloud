# Amazon EBS volumes should be protected by a backup plan.

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `ec2_ebs_volume_protected_by_backup_plan` |
| 云平台 | AWS |
| 服务 | ec2 |
| 严重等级 | low |
| 类别 | redundancy |
| 检查类型 | Software and Configuration Checks, AWS Security Best Practices |
| 资源类型 | AwsEc2Volume |
| 资源组 | storage |

## 描述

Evaluates if an Amazon EBS volume in in-use state is covered by a backup plan. The check fails if an EBS volume isn't covered by a backup plan. If you set the backupVaultLockCheck parameter equal to true, the control passes only if the EBS volume is backed up in an AWS Backup locked vault.

## 风险

Without backup coverage, Amazon EBS volumes are vulnerable to data loss or deletion, reducing the resilience of your systems and making recovery from incidents more difficult.

## 推荐措施

Ensure that all in-use Amazon EBS volumes are included in a backup plan, and consider using AWS Backup Vault Lock for additional protection.

- 推荐链接：[https://docs.aws.amazon.com/aws-backup/latest/devguide/assigning-resources.html](https://docs.aws.amazon.com/aws-backup/latest/devguide/assigning-resources.html)

## 修复步骤


### Other

[https://docs.aws.amazon.com/securityhub/latest/userguide/ec2-controls.html#ec2-28](https://docs.aws.amazon.com/securityhub/latest/userguide/ec2-controls.html#ec2-28)

## 参考资料

- [https://docs.aws.amazon.com/config/latest/developerguide/ebs-resources-protected-by-backup-plan.html](https://docs.aws.amazon.com/config/latest/developerguide/ebs-resources-protected-by-backup-plan.html)
- [https://docs.aws.amazon.com/aws-backup/latest/devguide/assigning-resources.html](https://docs.aws.amazon.com/aws-backup/latest/devguide/assigning-resources.html)

## 技术信息

- Source Metadata：[sources/aws/ec2_ebs_volume_protected_by_backup_plan/metadata.json](../../sources/aws/ec2_ebs_volume_protected_by_backup_plan/metadata.json)
- Source Code：[sources/aws/ec2_ebs_volume_protected_by_backup_plan/check.py](../../sources/aws/ec2_ebs_volume_protected_by_backup_plan/check.py)
- Source Metadata Path：`sources/aws/ec2_ebs_volume_protected_by_backup_plan/metadata.json`
- Source Code Path：`sources/aws/ec2_ebs_volume_protected_by_backup_plan/check.py`
