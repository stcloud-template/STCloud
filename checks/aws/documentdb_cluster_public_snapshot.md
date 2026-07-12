# DocumentDB manual cluster snapshot is not shared publicly

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `documentdb_cluster_public_snapshot` |
| クラウドプラットフォーム | AWS |
| サービス | documentdb |
| 重大度 | critical |
| カテゴリ | internet-exposed |
| チェックタイプ | Software and Configuration Checks/AWS Security Best Practices, Software and Configuration Checks/Industry and Regulatory Standards/AWS Foundational Security Best Practices, Effects/Data Exposure, TTPs/Initial Access |
| リソースタイプ | AwsRdsDbClusterSnapshot |
| リソースグループ | database |

## 説明

**Amazon DocumentDB** manual cluster snapshot visibility is evaluated to detect snapshots marked as **public** instead of limited to specified AWS accounts.

## リスク

**Public snapshots** weaken **confidentiality**: any AWS account can restore and read database contents, enabling data exfiltration. They also aid **lateral movement** by revealing embedded secrets/config and reduce accountability when restores occur outside your account.

## 推奨事項

Keep snapshot visibility `Private` and share only with trusted accounts under **least privilege**. Prefer **CMEK encryption** to enforce key-based access and prevent public sharing. Periodically review sharing lists, restrict IAM permissions that alter visibility, and monitor for exposure as **defense in depth**.

## 修正手順


### CLI

```text
aws docdb modify-db-cluster-snapshot-attribute --db-cluster-snapshot-identifier <snapshot_id> --attribute-name restore --values-to-remove all
```

### Other

1. Open the Amazon DocumentDB console and go to Snapshots
2. Select the public manual cluster snapshot
3. Click Actions > Share
4. Set DB snapshot visibility to Private (remove "all" if listed)
5. Click Save

## 参考資料

- [https://docs.aws.amazon.com/documentdb/latest/developerguide/backup_restore-share_cluster_snapshots.html#backup_restore-share_snapshots](https://docs.aws.amazon.com/documentdb/latest/developerguide/backup_restore-share_cluster_snapshots.html#backup_restore-share_snapshots)
- [https://docs.aws.amazon.com/securityhub/latest/userguide/documentdb-controls.html#documentdb-3](https://docs.aws.amazon.com/securityhub/latest/userguide/documentdb-controls.html#documentdb-3)
- [https://docs.aws.amazon.com/config/latest/developerguide/docdb-cluster-snapshot-public-prohibited.html](https://docs.aws.amazon.com/config/latest/developerguide/docdb-cluster-snapshot-public-prohibited.html)

## 技術情報

- Source Metadata：[sources/aws/documentdb_cluster_public_snapshot/metadata.json](../../sources/aws/documentdb_cluster_public_snapshot/metadata.json)
- Source Code：[sources/aws/documentdb_cluster_public_snapshot/check.py](../../sources/aws/documentdb_cluster_public_snapshot/check.py)
- Source Metadata Path：`sources/aws/documentdb_cluster_public_snapshot/metadata.json`
- Source Code Path：`sources/aws/documentdb_cluster_public_snapshot/check.py`
