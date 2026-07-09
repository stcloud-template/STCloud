# Neptune cluster has automated backups enabled with retention period equal to or greater than the configured minimum

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `neptune_cluster_backup_enabled` |
| 云平台 | AWS |
| 服务 | neptune |
| 严重等级 | medium |
| 类别 | resilience |
| 检查类型 | Software and Configuration Checks/Industry and Regulatory Standards/AWS Foundational Security Best Practices |
| 资源类型 | AwsRdsDbCluster |
| 资源组 | database |

## 描述

Neptune DB cluster automated backup is enabled and retention days are more than the required minimum retention period (default to `7` days).

## 风险

**Insufficient backup retention** reduces the ability to recover from data corruption, accidental deletion, or ransomware, impacting **availability** and **integrity**. - Prevents point-in-time recovery to required dates - Increases downtime, irreversible data loss, and compliance violations

## 推荐措施

Ensure automated backups are enabled and retention aligns with your **RPO/RTO** and regulatory requirements (at least `7` days). - Define backup lifecycle and storage retention policies - Regularly test restore procedures and monitor backup health - Incorporate backups into Disaster Recovery and retention governance

## 修复步骤


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

## 参考资料

- [https://docs.aws.amazon.com/securityhub/latest/userguide/neptune-controls.html#neptune-5](https://docs.aws.amazon.com/securityhub/latest/userguide/neptune-controls.html#neptune-5)
- [https://trendmicro.com/cloudoneconformity/knowledge-base/aws/Neptune/sufficient-backup-retention-period.html](https://trendmicro.com/cloudoneconformity/knowledge-base/aws/Neptune/sufficient-backup-retention-period.html)
- [https://support.icompaas.com/support/solutions/articles/62000233327-check-for-neptune-clusters-backup-retention-period](https://support.icompaas.com/support/solutions/articles/62000233327-check-for-neptune-clusters-backup-retention-period)
- [https://asecure.cloud/a/p_configrule_neptune_cluster_backup_retention_check/](https://asecure.cloud/a/p_configrule_neptune_cluster_backup_retention_check/)

## 技术信息

- Source Metadata：[sources/aws/neptune_cluster_backup_enabled/metadata.json](../../sources/aws/neptune_cluster_backup_enabled/metadata.json)
- Source Code：[sources/aws/neptune_cluster_backup_enabled/check.py](../../sources/aws/neptune_cluster_backup_enabled/check.py)
- Source Metadata Path：`sources/aws/neptune_cluster_backup_enabled/metadata.json`
- Source Code Path：`sources/aws/neptune_cluster_backup_enabled/check.py`
