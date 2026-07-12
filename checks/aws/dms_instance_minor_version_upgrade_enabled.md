# DMS replication instance has auto minor version upgrade enabled

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `dms_instance_minor_version_upgrade_enabled` |
| クラウドプラットフォーム | AWS |
| サービス | dms |
| 重大度 | medium |
| カテゴリ | vulnerabilities |
| チェックタイプ | Software and Configuration Checks/Patch Management, Software and Configuration Checks/AWS Security Best Practices, Software and Configuration Checks/Industry and Regulatory Standards/AWS Foundational Security Best Practices |
| リソースタイプ | AwsDmsReplicationInstance |
| リソースグループ | database |

## 説明

**AWS DMS replication instances** are evaluated for the `auto_minor_version_upgrade` setting to confirm **automatic minor engine updates** are enabled during the maintenance window.

## リスク

Without **automatic minor upgrades**, DMS engines can miss security patches and fixes, enabling exploitation of known flaws and instability. - Confidentiality: exposure via unpatched components - Integrity: replication errors or data drift - Availability: outages during migration or CDC

## 推奨事項

Enable `auto_minor_version_upgrade` on all replication instances to maintain **continuous patching**. - Set a maintenance window and validate in non-prod - Monitor release notes and health metrics - Enforce **least privilege** for change control - Keep **backups** for rollback

## 修正手順


### CLI

```text
aws dms modify-replication-instance --region <REGION> --replication-instance-arn arn:aws:dms:<REGION>:<ACCOUNT_ID>:rep:<REPLICATION_ID> --auto-minor-version-upgrade --apply-immediately
```

### Native IaC

```yaml
# CloudFormation: Enable auto minor version upgrade on a DMS replication instance
Resources:
  <example_resource_name>:
    Type: AWS::DMS::ReplicationInstance
    Properties:
      ReplicationInstanceIdentifier: <example_resource_id>
      ReplicationInstanceClass: dms.t3.micro
      AutoMinorVersionUpgrade: true  # CRITICAL: turns on automatic minor version upgrades
```

### Terraform

```hcl
# Terraform: Enable auto minor version upgrade on a DMS replication instance
resource "aws_dms_replication_instance" "<example_resource_name>" {
  replication_instance_id    = "<example_resource_id>"
  replication_instance_class = "dms.t3.micro"
  auto_minor_version_upgrade = true  # CRITICAL: turns on automatic minor version upgrades
}
```

### Other

1. Open the AWS Console and go to Database Migration Service (DMS)
2. Click Replication instances and select your instance
3. Choose Actions > Modify
4. Check Auto minor version upgrade
5. Select Apply immediately
6. Click Modify to save

## 参考資料

- [https://docs.aws.amazon.com/securityhub/latest/userguide/dms-controls.html#dms-6](https://docs.aws.amazon.com/securityhub/latest/userguide/dms-controls.html#dms-6)
- [https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/DMS/auto-minor-version-upgrade.html](https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/DMS/auto-minor-version-upgrade.html)

## 技術情報

- Source Metadata：[sources/aws/dms_instance_minor_version_upgrade_enabled/metadata.json](../../sources/aws/dms_instance_minor_version_upgrade_enabled/metadata.json)
- Source Code：[sources/aws/dms_instance_minor_version_upgrade_enabled/check.py](../../sources/aws/dms_instance_minor_version_upgrade_enabled/check.py)
- Source Metadata Path：`sources/aws/dms_instance_minor_version_upgrade_enabled/metadata.json`
- Source Code Path：`sources/aws/dms_instance_minor_version_upgrade_enabled/check.py`
