# Ensure RDS instances have minor version upgrade enabled.

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `rds_instance_minor_version_upgrade_enabled` |
| クラウドプラットフォーム | AWS |
| サービス | rds |
| 重大度 | low |
| カテゴリ | Uncategorized |
| リソースタイプ | AwsRdsDbInstance |
| リソースグループ | database |

## 説明

Ensure RDS instances have minor version upgrade enabled.

## リスク

Auto Minor Version Upgrade is a feature that you can enable to have your database automatically upgraded when a new minor database engine version is available. Minor version upgrades often patch security vulnerabilities and fix bugs and therefore should be applied.

## 推奨事項

Enable auto minor version upgrade for all databases and environments.

- 推奨リンク：[https://aws.amazon.com/blogs/database/best-practices-for-upgrading-amazon-rds-to-major-and-minor-versions-of-postgresql/](https://aws.amazon.com/blogs/database/best-practices-for-upgrading-amazon-rds-to-major-and-minor-versions-of-postgresql/)

## 修正手順


### CLI

```text
aws rds modify-db-instance --db-instance-identifier <db_instance_id> --auto-minor-version-upgrade --apply-immediately
```

### Native IaC

[https://docs.ST Cloud.com/checks/aws/general-policies/ensure-aws-db-instance-gets-all-minor-upgrades-automatically#cloudformation](https://docs.ST Cloud.com/checks/aws/general-policies/ensure-aws-db-instance-gets-all-minor-upgrades-automatically#cloudformation)

### Terraform

[https://docs.ST Cloud.com/checks/aws/general-policies/ensure-aws-db-instance-gets-all-minor-upgrades-automatically#terraform](https://docs.ST Cloud.com/checks/aws/general-policies/ensure-aws-db-instance-gets-all-minor-upgrades-automatically#terraform)

### Other

[https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/RDS/rds-auto-minor-version-upgrade.html](https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/RDS/rds-auto-minor-version-upgrade.html)

## 参考資料

- [https://aws.amazon.com/blogs/database/best-practices-for-upgrading-amazon-rds-to-major-and-minor-versions-of-postgresql/](https://aws.amazon.com/blogs/database/best-practices-for-upgrading-amazon-rds-to-major-and-minor-versions-of-postgresql/)

## 技術情報

- Source Metadata：[sources/aws/rds_instance_minor_version_upgrade_enabled/metadata.json](../../sources/aws/rds_instance_minor_version_upgrade_enabled/metadata.json)
- Source Code：[sources/aws/rds_instance_minor_version_upgrade_enabled/check.py](../../sources/aws/rds_instance_minor_version_upgrade_enabled/check.py)
- Source Metadata Path：`sources/aws/rds_instance_minor_version_upgrade_enabled/metadata.json`
- Source Code Path：`sources/aws/rds_instance_minor_version_upgrade_enabled/check.py`
