# NeptuneDB cluster snapshot is not publicly shared

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `neptune_cluster_public_snapshot` |
| 云平台 | AWS |
| 服务 | neptune |
| 严重等级 | critical |
| 类别 | internet-exposed |
| 检查类型 | Software and Configuration Checks/AWS Security Best Practices/Network Reachability, Effects/Data Exposure, TTPs/Initial Access/Unauthorized Access |
| 资源类型 | AwsRdsDbClusterSnapshot |
| 资源组 | database |

## 描述

Neptune DB manual cluster snapshot is evaluated to determine if its restore attributes allow access to all AWS accounts *(public)*. A failed status in the report means the snapshot is publicly shared and can be copied or restored by any AWS account; **PASS** means it is not shared publicly.

## 风险

**Public snapshots** compromise confidentiality of stored data and metadata. Attackers or third parties can: - Copy or restore snapshots to external accounts. - Access sensitive data contained in the snapshot.

## 推荐措施

Avoid public sharing and apply **least privilege** when granting snapshot access: share only with specific AWS accounts or roles. Use **encryption**, enforce automated policies and regular audits, and apply **separation of duties** and tagging to control and track snapshot access.

## 修复步骤


### CLI

```text
aws neptune modify-db-cluster-snapshot-attribute --db-cluster-snapshot-identifier <snapshot_id> --attribute-name restore --values-to-remove all
```

### Other

1. Sign in to the AWS Management Console and open the Amazon RDS console
2. In the left navigation, choose Snapshots > DB cluster snapshots
3. Select the snapshot, choose Actions > Manage snapshot permissions
4. In the permissions dialog remove the Public/all-accounts permission and click Save

## 参考资料

- [https://docs.aws.amazon.com/securityhub/latest/userguide/neptune-controls.html#neptune-3](https://docs.aws.amazon.com/securityhub/latest/userguide/neptune-controls.html#neptune-3)
- [https://docs.aws.amazon.com/config/latest/developerguide/neptune-cluster-snapshot-public-prohibited.html](https://docs.aws.amazon.com/config/latest/developerguide/neptune-cluster-snapshot-public-prohibited.html)

## 技术信息

- Source Metadata：[sources/aws/neptune_cluster_public_snapshot/metadata.json](../../sources/aws/neptune_cluster_public_snapshot/metadata.json)
- Source Code：[sources/aws/neptune_cluster_public_snapshot/check.py](../../sources/aws/neptune_cluster_public_snapshot/check.py)
- Source Metadata Path：`sources/aws/neptune_cluster_public_snapshot/metadata.json`
- Source Code Path：`sources/aws/neptune_cluster_public_snapshot/check.py`
