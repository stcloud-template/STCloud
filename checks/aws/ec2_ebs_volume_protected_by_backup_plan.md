# Amazon EBS volumes should be protected by a backup plan.

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `ec2_ebs_volume_protected_by_backup_plan` |
| クラウドプラットフォーム | AWS |
| サービス | ec2 |
| 重大度 | low |
| カテゴリ | redundancy |
| チェックタイプ | Software and Configuration Checks, AWS Security Best Practices |
| リソースタイプ | AwsEc2Volume |
| リソースグループ | storage |

## 説明

Evaluates if an Amazon EBS volume in in-use state is covered by a backup plan. The check fails if an EBS volume isn't covered by a backup plan. If you set the backupVaultLockCheck parameter equal to true, the control passes only if the EBS volume is backed up in an AWS Backup locked vault.

## リスク

Without backup coverage, Amazon EBS volumes are vulnerable to data loss or deletion, reducing the resilience of your systems and making recovery from incidents more difficult.

## 推奨事項

Ensure that all in-use Amazon EBS volumes are included in a backup plan, and consider using AWS Backup Vault Lock for additional protection.

- 推奨リンク：[https://docs.aws.amazon.com/aws-backup/latest/devguide/assigning-resources.html](https://docs.aws.amazon.com/aws-backup/latest/devguide/assigning-resources.html)

## 修正手順


### Other

[https://docs.aws.amazon.com/securityhub/latest/userguide/ec2-controls.html#ec2-28](https://docs.aws.amazon.com/securityhub/latest/userguide/ec2-controls.html#ec2-28)

## 参考資料

- [https://docs.aws.amazon.com/config/latest/developerguide/ebs-resources-protected-by-backup-plan.html](https://docs.aws.amazon.com/config/latest/developerguide/ebs-resources-protected-by-backup-plan.html)
- [https://docs.aws.amazon.com/aws-backup/latest/devguide/assigning-resources.html](https://docs.aws.amazon.com/aws-backup/latest/devguide/assigning-resources.html)

## 技術情報

- Source Metadata：[sources/aws/ec2_ebs_volume_protected_by_backup_plan/metadata.json](../../sources/aws/ec2_ebs_volume_protected_by_backup_plan/metadata.json)
- Source Code：[sources/aws/ec2_ebs_volume_protected_by_backup_plan/check.py](../../sources/aws/ec2_ebs_volume_protected_by_backup_plan/check.py)
- Source Metadata Path：`sources/aws/ec2_ebs_volume_protected_by_backup_plan/metadata.json`
- Source Code Path：`sources/aws/ec2_ebs_volume_protected_by_backup_plan/check.py`
