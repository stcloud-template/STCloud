# DocumentDB cluster has automated backups enabled with retention period of at least 7 days

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `documentdb_cluster_backup_enabled` |
| 云平台 | AWS |
| 服务 | documentdb |
| 严重等级 | medium |
| 类别 | resilience |
| 检查类型 | Software and Configuration Checks/AWS Security Best Practices, Industry and Regulatory Standards/AWS Foundational Security Best Practices, Effects/Data Destruction |
| 资源类型 | AwsRdsDbCluster |
| 资源组 | database |

## 描述

**Amazon DocumentDB clusters** are evaluated for **automated backups** and an adequate **backup retention period**. Clusters should have `backup_retention_period` set to at least the configured minimum (default `7` days). Values of `0` indicate backups are disabled; values below the threshold are considered insufficient.

## 风险

Without adequate backups, clusters can't be reliably restored. Accidental deletes, logical corruption, or ransomware may cause irreversible data loss once a short retention window expires, leading to prolonged outages, missed RPO/RTO, and limited ability to roll back malicious or erroneous changes.

## 推荐措施

Enable **automated backups** and set retention to meet RPO/RTO (typically `7-35` days). - Regularly test point-in-time restores - Apply **least privilege** to backup/snapshot management - Protect backup artifacts and define stable backup windows - Include restores in a tested **disaster recovery** plan

## 修复步骤


### CLI

```text
aws docdb modify-db-cluster --db-cluster-identifier <DB_CLUSTER_ID> --backup-retention-period 7 --apply-immediately
```

### Native IaC

```yaml
# CloudFormation: Set DocumentDB backup retention to at least 7 days
Resources:
  <example_resource_name>:
    Type: AWS::DocDB::DBCluster
    Properties:
      BackupRetentionPeriod: 7  # CRITICAL: enables automated backups and sets retention to >=7 days
```

### Terraform

```hcl
# Terraform: Ensure DocumentDB backup retention is at least 7 days
resource "aws_docdb_cluster" "<example_resource_name>" {
  cluster_identifier      = "<example_resource_id>"
  backup_retention_period = 7  # CRITICAL: enables automated backups and sets retention to >=7 days
}
```

### Other

1. Open the Amazon DocumentDB console
2. Go to Clusters and select <example_resource_id>
3. Click Modify
4. Set Backup retention period to 7 (or higher)
5. Check Apply immediately
6. Click Continue and then Modify cluster

## 参考资料

- [https://docs.amazonaws.cn/en_us/documentdb/latest/developerguide/what-is.html](https://docs.amazonaws.cn/en_us/documentdb/latest/developerguide/what-is.html)
- [https://www.trendmicro.com/cloudoneconformity-staging/knowledge-base/aws/DocumentDB/sufficient-backup-retention-period.html#](https://www.trendmicro.com/cloudoneconformity-staging/knowledge-base/aws/DocumentDB/sufficient-backup-retention-period.html#)
- [https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/aws-enabledocdbclusterbackupretentionperiod.html](https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/aws-enabledocdbclusterbackupretentionperiod.html)

## 技术信息

- Source Metadata：[sources/aws/documentdb_cluster_backup_enabled/metadata.json](../../sources/aws/documentdb_cluster_backup_enabled/metadata.json)
- Source Code：[sources/aws/documentdb_cluster_backup_enabled/check.py](../../sources/aws/documentdb_cluster_backup_enabled/check.py)
- Source Metadata Path：`sources/aws/documentdb_cluster_backup_enabled/metadata.json`
- Source Code Path：`sources/aws/documentdb_cluster_backup_enabled/check.py`
