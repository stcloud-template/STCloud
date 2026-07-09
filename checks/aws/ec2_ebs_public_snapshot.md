# Ensure there are no EBS Snapshots set as Public.

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `ec2_ebs_public_snapshot` |
| 云平台 | AWS |
| 服务 | ec2 |
| 子服务 | snapshot |
| 严重等级 | critical |
| 类别 | internet-exposed |
| 检查类型 | Data Protection |
| 资源类型 | Other |
| 资源组 | compute |

## 描述

Ensure there are no EBS Snapshots set as Public.

## 风险

When you share a snapshot, you are giving others access to all of the data on the snapshot. Share snapshots only with people with whom you want to share all of your snapshot data.

## 推荐措施

Ensure the snapshot should be shared.

- 推荐链接：[https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ebs-modifying-snapshot-permissions.html](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ebs-modifying-snapshot-permissions.html)

## 修复步骤


### CLI

```text
aws ec2 modify-snapshot-attribute --region <REGION> --snapshot-id <EC2_SNAPSHOT_ID> --attribute createVolumePermission --operation remove --user-ids all
```

### Other

[https://docs.ST Cloud.com/checks/aws/public-policies/public_7](https://docs.ST Cloud.com/checks/aws/public-policies/public_7)

## 参考资料

- [https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ebs-modifying-snapshot-permissions.html](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ebs-modifying-snapshot-permissions.html)

## 技术信息

- Source Metadata：[sources/aws/ec2_ebs_public_snapshot/metadata.json](../../sources/aws/ec2_ebs_public_snapshot/metadata.json)
- Source Code：[sources/aws/ec2_ebs_public_snapshot/check.py](../../sources/aws/ec2_ebs_public_snapshot/check.py)
- Source Metadata Path：`sources/aws/ec2_ebs_public_snapshot/metadata.json`
- Source Code Path：`sources/aws/ec2_ebs_public_snapshot/check.py`
