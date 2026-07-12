# Check if RDS instances are protected by a backup plan.

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `rds_instance_protected_by_backup_plan` |
| クラウドプラットフォーム | AWS |
| サービス | rds |
| 重大度 | medium |
| カテゴリ | Uncategorized |
| チェックタイプ | Software and Configuration Checks, AWS Security Best Practices |
| リソースタイプ | AwsRdsDbInstance |
| リソースグループ | database |

## 説明

Check if RDS instances are protected by a backup plan.

## リスク

Without a backup plan, RDS instances are vulnerable to data loss, accidental deletion, or corruption. This could lead to significant operational disruptions or loss of critical data.

## 推奨事項

Create a backup plan for the RDS instance to protect it from data loss, accidental deletion, or corruption.

- 推奨リンク：[https://docs.aws.amazon.com/aws-backup/latest/devguide/assigning-resources.html](https://docs.aws.amazon.com/aws-backup/latest/devguide/assigning-resources.html)

## 修正手順


### CLI

```text
aws backup create-backup-plan --backup-plan , aws backup tag-resource --resource-arn <rds-instance-arn> --tags Key=backup,Value=true
```

### Other

[https://docs.aws.amazon.com/securityhub/latest/userguide/rds-controls.html#rds-26](https://docs.aws.amazon.com/securityhub/latest/userguide/rds-controls.html#rds-26)

## 参考資料

- [https://docs.aws.amazon.com/aws-backup/latest/devguide/assigning-resources.html](https://docs.aws.amazon.com/aws-backup/latest/devguide/assigning-resources.html)

## 技術情報

- Source Metadata：[sources/aws/rds_instance_protected_by_backup_plan/metadata.json](../../sources/aws/rds_instance_protected_by_backup_plan/metadata.json)
- Source Code：[sources/aws/rds_instance_protected_by_backup_plan/check.py](../../sources/aws/rds_instance_protected_by_backup_plan/check.py)
- Source Metadata Path：`sources/aws/rds_instance_protected_by_backup_plan/metadata.json`
- Source Code Path：`sources/aws/rds_instance_protected_by_backup_plan/check.py`
