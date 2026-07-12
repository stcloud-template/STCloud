# NeptuneDB cluster snapshot is not publicly shared

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `neptune_cluster_public_snapshot` |
| クラウドプラットフォーム | AWS |
| サービス | neptune |
| 重大度 | critical |
| カテゴリ | internet-exposed |
| チェックタイプ | Software and Configuration Checks/AWS Security Best Practices/Network Reachability, Effects/Data Exposure, TTPs/Initial Access/Unauthorized Access |
| リソースタイプ | AwsRdsDbClusterSnapshot |
| リソースグループ | database |

## 説明

Neptune DB manual cluster snapshot is evaluated to determine if its restore attributes allow access to all AWS accounts *(public)*. A failed status in the report means the snapshot is publicly shared and can be copied or restored by any AWS account; **PASS** means it is not shared publicly.

## リスク

**Public snapshots** compromise confidentiality of stored data and metadata. Attackers or third parties can: - Copy or restore snapshots to external accounts. - Access sensitive data contained in the snapshot.

## 推奨事項

Avoid public sharing and apply **least privilege** when granting snapshot access: share only with specific AWS accounts or roles. Use **encryption**, enforce automated policies and regular audits, and apply **separation of duties** and tagging to control and track snapshot access.

## 修正手順


### CLI

```text
aws neptune modify-db-cluster-snapshot-attribute --db-cluster-snapshot-identifier <snapshot_id> --attribute-name restore --values-to-remove all
```

### Other

1. Sign in to the AWS Management Console and open the Amazon RDS console
2. In the left navigation, choose Snapshots > DB cluster snapshots
3. Select the snapshot, choose Actions > Manage snapshot permissions
4. In the permissions dialog remove the Public/all-accounts permission and click Save

## 参考資料

- [https://docs.aws.amazon.com/securityhub/latest/userguide/neptune-controls.html#neptune-3](https://docs.aws.amazon.com/securityhub/latest/userguide/neptune-controls.html#neptune-3)
- [https://docs.aws.amazon.com/config/latest/developerguide/neptune-cluster-snapshot-public-prohibited.html](https://docs.aws.amazon.com/config/latest/developerguide/neptune-cluster-snapshot-public-prohibited.html)

## 技術情報

- Source Metadata：[sources/aws/neptune_cluster_public_snapshot/metadata.json](../../sources/aws/neptune_cluster_public_snapshot/metadata.json)
- Source Code：[sources/aws/neptune_cluster_public_snapshot/check.py](../../sources/aws/neptune_cluster_public_snapshot/check.py)
- Source Metadata Path：`sources/aws/neptune_cluster_public_snapshot/metadata.json`
- Source Code Path：`sources/aws/neptune_cluster_public_snapshot/check.py`
