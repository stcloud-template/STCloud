# Ensure that public access to EBS snapshots is disabled

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `ec2_ebs_snapshot_account_block_public_access` |
| 云平台 | AWS |
| 服务 | ec2 |
| 子服务 | snapshot |
| 严重等级 | high |
| 类别 | internet-exposed |
| 检查类型 | Data Protection |
| 资源类型 | AwsAccount |
| 资源组 | governance |

## 描述

EBS snapshots can be shared with other AWS accounts or made public. By default, EBS snapshots are private and only the AWS account that created the snapshot can access it. If an EBS snapshot is shared with another AWS account or made public, the data in the snapshot can be accessed by the other account or by anyone on the internet. Ensure that public access to EBS snapshots is disabled.

## 风险

If public access to EBS snapshots is enabled, the data in the snapshot can be accessed by anyone on the internet.

## 推荐措施

Use the following procedures to configure and monitor block public access for snapshots.

- 推荐链接：[https://docs.aws.amazon.com/ebs/latest/userguide/block-public-access-snapshots-work.html#block-public-access-snapshots-enable](https://docs.aws.amazon.com/ebs/latest/userguide/block-public-access-snapshots-work.html#block-public-access-snapshots-enable)

## 修复步骤


### CLI

```text
aws ec2 enable-snapshot-block-public-access --state block-all-sharing
```

## 参考资料

- [https://docs.aws.amazon.com/ebs/latest/userguide/block-public-access-snapshots-work.html#block-public-access-snapshots-enable](https://docs.aws.amazon.com/ebs/latest/userguide/block-public-access-snapshots-work.html#block-public-access-snapshots-enable)

## 技术信息

- Source Metadata：[sources/aws/ec2_ebs_snapshot_account_block_public_access/metadata.json](../../sources/aws/ec2_ebs_snapshot_account_block_public_access/metadata.json)
- Source Code：[sources/aws/ec2_ebs_snapshot_account_block_public_access/check.py](../../sources/aws/ec2_ebs_snapshot_account_block_public_access/check.py)
- Source Metadata Path：`sources/aws/ec2_ebs_snapshot_account_block_public_access/metadata.json`
- Source Code Path：`sources/aws/ec2_ebs_snapshot_account_block_public_access/check.py`
