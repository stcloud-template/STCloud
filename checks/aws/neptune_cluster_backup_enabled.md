# Neptune cluster has automated backups enabled with retention period equal to or greater than the configured minimum

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `neptune_cluster_backup_enabled` |
| クラウドプラットフォーム | AWS |
| サービス | neptune |
| 重大度 | medium |
| カテゴリ | resilience |
| チェックタイプ | Software and Configuration Checks/Industry and Regulatory Standards/AWS Foundational Security Best Practices |
| リソースタイプ | AwsRdsDbCluster |
| リソースグループ | database |

## 説明

Neptune DB cluster automated backup is enabled and retention days are more than the required minimum retention period (default to `7` days).

## リスク

**Insufficient backup retention** reduces the ability to recover from data corruption, accidental deletion, or ransomware, impacting **availability** and **integrity**. - Prevents point-in-time recovery to required dates - Increases downtime, irreversible data loss, and compliance violations

## 推奨事項

Ensure automated backups are enabled and retention aligns with your **RPO/RTO** and regulatory requirements (at least `7` days). - Define backup lifecycle and storage retention policies - Regularly test restore procedures and monitor backup health - Incorporate backups into Disaster Recovery and retention governance

## 修正手順


### CLI

```text
aws neptune modify-db-cluster --db-cluster-identifier <DB_CLUSTER_ID> --backup-retention-period 7 --apply-immediately
```

### Native IaC

```yaml
Parameters:
  DBClusterId:
    Type: String
Resources:
  NeptuneCluster:
    Type: AWS::Neptune::DBCluster
    Properties:
      DBClusterIdentifier: !Ref DBClusterId
      BackupRetentionPeriod: 7  # Enable automated backups with 7-day retention minimum
```

### Terraform

```hcl
resource "aws_neptune_cluster" "example_resource" {
  cluster_identifier      = var.cluster_id
  backup_retention_period = 7  # Enable automated backups with 7-day retention minimum
}
```

### Other

1. Sign in to the AWS Management Console
2. Services → Amazon Neptune → Databases
3. Select the DB cluster and click Modify
4. In Backup retention period set the value to 7 (or higher)
5. Choose Apply immediately and click Modify cluster

## 参考資料

- [https://docs.aws.amazon.com/securityhub/latest/userguide/neptune-controls.html#neptune-5](https://docs.aws.amazon.com/securityhub/latest/userguide/neptune-controls.html#neptune-5)
- [https://trendmicro.com/cloudoneconformity/knowledge-base/aws/Neptune/sufficient-backup-retention-period.html](https://trendmicro.com/cloudoneconformity/knowledge-base/aws/Neptune/sufficient-backup-retention-period.html)
- [https://support.icompaas.com/support/solutions/articles/62000233327-check-for-neptune-clusters-backup-retention-period](https://support.icompaas.com/support/solutions/articles/62000233327-check-for-neptune-clusters-backup-retention-period)
- [https://asecure.cloud/a/p_configrule_neptune_cluster_backup_retention_check/](https://asecure.cloud/a/p_configrule_neptune_cluster_backup_retention_check/)

## 技術情報

- Source Metadata：[sources/aws/neptune_cluster_backup_enabled/metadata.json](../../sources/aws/neptune_cluster_backup_enabled/metadata.json)
- Source Code：[sources/aws/neptune_cluster_backup_enabled/check.py](../../sources/aws/neptune_cluster_backup_enabled/check.py)
- Source Metadata Path：`sources/aws/neptune_cluster_backup_enabled/metadata.json`
- Source Code Path：`sources/aws/neptune_cluster_backup_enabled/check.py`
