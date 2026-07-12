# Neptune DB cluster snapshot is encrypted at rest

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `neptune_cluster_snapshot_encrypted` |
| クラウドプラットフォーム | AWS |
| サービス | neptune |
| 重大度 | medium |
| カテゴリ | encryption |
| チェックタイプ | Software and Configuration Checks/AWS Security Best Practices/Encryption at Rest, Software and Configuration Checks/Industry and Regulatory Standards/AWS Foundational Security Best Practices, Effects/Data Exposure |
| リソースタイプ | AwsRdsDbClusterSnapshot |
| リソースグループ | database |

## 説明

Neptune DB cluster snapshot is encrypted at rest. The evaluation looks at whether each snapshot's encrypted attribute is enabled, confirming that the data is protected while stored.

## リスク

**Unencrypted Neptune snapshots** undermine data confidentiality. If accessed or shared due to compromised credentials or misconfiguration, attackers can restore or download snapshot contents, enabling **data exfiltration**, and exposure of sensitive records. This weakens overall data protection posture.

## 推奨事項

Protect snapshot data by enforcing **encryption at rest** and strong key governance. - Use **customer-managed keys** with controlled lifecycle and rotation - Apply **least privilege** to snapshot access and sharing - Prevent creation of unencrypted snapshots via organizational configuration and policy controls

## 修正手順


### CLI

```text
aws rds copy-db-cluster-snapshot --source-db-cluster-snapshot-identifier <source-snapshot> --target-db-cluster-snapshot-identifier <encrypted-snapshot> --kms-key-id <kms-key-id>
```

### Terraform

```hcl
resource "aws_neptune_cluster" "restored" {
  cluster_identifier  = "restored-cluster"
  snapshot_identifier = "<source-snapshot>"
  storage_encrypted   = true  # Ensure restored cluster from snapshot is encrypted
}
```

### Other

1. Sign in to the AWS Management Console and open Amazon Neptune
2. In the left pane choose **Snapshots**
3. Select the unencrypted snapshot and click **Actions** > **Restore snapshot**
4. In the Restore page enable **Encryption** and select a KMS key
5. Click **Restore DB cluster**
6. After the cluster is restored, create a new snapshot of the restored (encrypted) cluster

## 参考資料

- [https://docs.aws.amazon.com/securityhub/latest/userguide/neptune-controls.html#neptune-6](https://docs.aws.amazon.com/securityhub/latest/userguide/neptune-controls.html#neptune-6)
- [https://docs.aws.amazon.com/neptune/latest/userguide/backup-restore-share-snapshot.html](https://docs.aws.amazon.com/neptune/latest/userguide/backup-restore-share-snapshot.html)

## 技術情報

- Source Metadata：[sources/aws/neptune_cluster_snapshot_encrypted/metadata.json](../../sources/aws/neptune_cluster_snapshot_encrypted/metadata.json)
- Source Code：[sources/aws/neptune_cluster_snapshot_encrypted/check.py](../../sources/aws/neptune_cluster_snapshot_encrypted/check.py)
- Source Metadata Path：`sources/aws/neptune_cluster_snapshot_encrypted/metadata.json`
- Source Code Path：`sources/aws/neptune_cluster_snapshot_encrypted/check.py`
