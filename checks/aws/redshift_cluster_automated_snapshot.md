# Redshift cluster has automated snapshots enabled

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `redshift_cluster_automated_snapshot` |
| クラウドプラットフォーム | AWS |
| サービス | redshift |
| 重大度 | high |
| カテゴリ | resilience |
| チェックタイプ | Software and Configuration Checks/AWS Security Best Practices, Software and Configuration Checks/Industry and Regulatory Standards/AWS Foundational Security Best Practices |
| リソースタイプ | AwsRedshiftCluster |
| リソースグループ | analytics |

## 説明

**Amazon Redshift clusters** are evaluated for **automated snapshots** being enabled with a retention period `> 0`, confirming that periodic backups are created and retained.

## リスク

Without **automated snapshots**, clusters lack recent recovery points, degrading **availability** and **integrity**. Accidental deletion, malicious changes, or failed ETL can cause data loss and prolonged recovery, increasing RPO/RTO and limiting effective forensic analysis.

## 推奨事項

Enable **automated snapshots** with retention aligned to RPO/RTO. Enforce **least privilege** on snapshot access and use **encryption**. Regularly test restores and monitor backup health. *For resilience*, replicate snapshots to another Region/account and separate backup administration from data owners.

## 修正手順


### CLI

```text
aws redshift modify-cluster --cluster-identifier <example_resource_id> --automated-snapshot-retention-period 1
```

### Native IaC

```yaml
# CloudFormation: Enable automated snapshots for a Redshift cluster
Resources:
  <example_resource_name>:
    Type: AWS::Redshift::Cluster
    Properties:
      ClusterType: single-node
      NodeType: <NODE_TYPE>
      DBName: <DB_NAME>
      MasterUsername: <MASTER_USERNAME>
      MasterUserPassword: <MASTER_PASSWORD>
      AutomatedSnapshotRetentionPeriod: 1  # Critical: enables automated snapshots by retaining them for 1 day
```

### Terraform

```hcl
# Terraform: Enable automated snapshots for a Redshift cluster
resource "aws_redshift_cluster" "<example_resource_name>" {
  cluster_identifier = "<example_resource_id>"
  cluster_type       = "single-node"
  node_type          = "<NODE_TYPE>"
  database_name      = "<DB_NAME>"
  master_username    = "<MASTER_USERNAME>"
  master_password    = "<MASTER_PASSWORD>"

  automated_snapshot_retention_period = 1  # Critical: enables automated snapshots by retaining them for 1 day
}
```

### Other

1. Open the AWS Console and go to Amazon Redshift
2. Select your cluster and click Modify
3. Under Backup, set Automated snapshot retention period to 1 (or greater)
4. Click Save changes and apply the modification

## 参考資料

- [https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_Redshift.html](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_Redshift.html)

## 技術情報

- Source Metadata：[sources/aws/redshift_cluster_automated_snapshot/metadata.json](../../sources/aws/redshift_cluster_automated_snapshot/metadata.json)
- Source Code：[sources/aws/redshift_cluster_automated_snapshot/check.py](../../sources/aws/redshift_cluster_automated_snapshot/check.py)
- Source Metadata Path：`sources/aws/redshift_cluster_automated_snapshot/metadata.json`
- Source Code Path：`sources/aws/redshift_cluster_automated_snapshot/check.py`
