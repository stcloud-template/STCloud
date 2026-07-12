# Ensure that public access to EBS snapshots is disabled

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `ec2_ebs_snapshot_account_block_public_access` |
| クラウドプラットフォーム | AWS |
| サービス | ec2 |
| サブサービス | snapshot |
| 重大度 | high |
| カテゴリ | internet-exposed |
| チェックタイプ | Data Protection |
| リソースタイプ | AwsAccount |
| リソースグループ | governance |

## 説明

EBS snapshots can be shared with other AWS accounts or made public. By default, EBS snapshots are private and only the AWS account that created the snapshot can access it. If an EBS snapshot is shared with another AWS account or made public, the data in the snapshot can be accessed by the other account or by anyone on the internet. Ensure that public access to EBS snapshots is disabled.

## リスク

If public access to EBS snapshots is enabled, the data in the snapshot can be accessed by anyone on the internet.

## 推奨事項

Use the following procedures to configure and monitor block public access for snapshots.

- 推奨リンク：[https://docs.aws.amazon.com/ebs/latest/userguide/block-public-access-snapshots-work.html#block-public-access-snapshots-enable](https://docs.aws.amazon.com/ebs/latest/userguide/block-public-access-snapshots-work.html#block-public-access-snapshots-enable)

## 修正手順


### CLI

```text
aws ec2 enable-snapshot-block-public-access --state block-all-sharing
```

## 参考資料

- [https://docs.aws.amazon.com/ebs/latest/userguide/block-public-access-snapshots-work.html#block-public-access-snapshots-enable](https://docs.aws.amazon.com/ebs/latest/userguide/block-public-access-snapshots-work.html#block-public-access-snapshots-enable)

## 技術情報

- Source Metadata：[sources/aws/ec2_ebs_snapshot_account_block_public_access/metadata.json](../../sources/aws/ec2_ebs_snapshot_account_block_public_access/metadata.json)
- Source Code：[sources/aws/ec2_ebs_snapshot_account_block_public_access/check.py](../../sources/aws/ec2_ebs_snapshot_account_block_public_access/check.py)
- Source Metadata Path：`sources/aws/ec2_ebs_snapshot_account_block_public_access/metadata.json`
- Source Code Path：`sources/aws/ec2_ebs_snapshot_account_block_public_access/check.py`
