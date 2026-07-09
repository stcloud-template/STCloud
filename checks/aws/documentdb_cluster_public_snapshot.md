# DocumentDB manual cluster snapshot is not shared publicly

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `documentdb_cluster_public_snapshot` |
| 云平台 | AWS |
| 服务 | documentdb |
| 严重等级 | critical |
| 类别 | internet-exposed |
| 检查类型 | Software and Configuration Checks/AWS Security Best Practices, Software and Configuration Checks/Industry and Regulatory Standards/AWS Foundational Security Best Practices, Effects/Data Exposure, TTPs/Initial Access |
| 资源类型 | AwsRdsDbClusterSnapshot |
| 资源组 | database |

## 描述

**Amazon DocumentDB** manual cluster snapshot visibility is evaluated to detect snapshots marked as **public** instead of limited to specified AWS accounts.

## 风险

**Public snapshots** weaken **confidentiality**: any AWS account can restore and read database contents, enabling data exfiltration. They also aid **lateral movement** by revealing embedded secrets/config and reduce accountability when restores occur outside your account.

## 推荐措施

Keep snapshot visibility `Private` and share only with trusted accounts under **least privilege**. Prefer **CMEK encryption** to enforce key-based access and prevent public sharing. Periodically review sharing lists, restrict IAM permissions that alter visibility, and monitor for exposure as **defense in depth**.

## 修复步骤


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

## 参考资料

- [https://docs.aws.amazon.com/documentdb/latest/developerguide/backup_restore-share_cluster_snapshots.html#backup_restore-share_snapshots](https://docs.aws.amazon.com/documentdb/latest/developerguide/backup_restore-share_cluster_snapshots.html#backup_restore-share_snapshots)
- [https://docs.aws.amazon.com/securityhub/latest/userguide/documentdb-controls.html#documentdb-3](https://docs.aws.amazon.com/securityhub/latest/userguide/documentdb-controls.html#documentdb-3)
- [https://docs.aws.amazon.com/config/latest/developerguide/docdb-cluster-snapshot-public-prohibited.html](https://docs.aws.amazon.com/config/latest/developerguide/docdb-cluster-snapshot-public-prohibited.html)

## 技术信息

- Source Metadata：[sources/aws/documentdb_cluster_public_snapshot/metadata.json](../../sources/aws/documentdb_cluster_public_snapshot/metadata.json)
- Source Code：[sources/aws/documentdb_cluster_public_snapshot/check.py](../../sources/aws/documentdb_cluster_public_snapshot/check.py)
- Source Metadata Path：`sources/aws/documentdb_cluster_public_snapshot/metadata.json`
- Source Code Path：`sources/aws/documentdb_cluster_public_snapshot/check.py`
