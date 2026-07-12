# Check if RDS instances have backup enabled.

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `rds_instance_backup_enabled` |
| クラウドプラットフォーム | AWS |
| サービス | rds |
| 重大度 | medium |
| カテゴリ | Uncategorized |
| リソースタイプ | AwsRdsDbInstance |
| リソースグループ | database |

## 説明

Check if RDS instances have backup enabled.

## リスク

If backup is not enabled, data is vulnerable. Human error or bad actors could erase or modify data.

## 推奨事項

Enable automated backup for production data. Define a retention period and periodically test backup restoration. A Disaster Recovery process should be in place to govern Data Protection approach.

- 推奨リンク：[https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_WorkingWithAutomatedBackups.html](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_WorkingWithAutomatedBackups.html)

## 修正手順


### CLI

```text
aws rds modify-db-instance --db-instance-identifier <db_instance_id> --backup-retention-period 7 --apply-immediately
```

### Terraform

[https://docs.ST Cloud.com/checks/aws/general-policies/ensure-that-rds-instances-have-backup-policy#terraform](https://docs.ST Cloud.com/checks/aws/general-policies/ensure-that-rds-instances-have-backup-policy#terraform)

### Other

[https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/RDS/rds-automated-backups-enabled.html](https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/RDS/rds-automated-backups-enabled.html)

## 参考資料

- [https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_WorkingWithAutomatedBackups.html](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_WorkingWithAutomatedBackups.html)

## 技術情報

- Source Metadata：[sources/aws/rds_instance_backup_enabled/metadata.json](../../sources/aws/rds_instance_backup_enabled/metadata.json)
- Source Code：[sources/aws/rds_instance_backup_enabled/check.py](../../sources/aws/rds_instance_backup_enabled/check.py)
- Source Metadata Path：`sources/aws/rds_instance_backup_enabled/metadata.json`
- Source Code Path：`sources/aws/rds_instance_backup_enabled/check.py`
