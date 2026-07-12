# Ensure there are no EBS Snapshots set as Public.

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `ec2_ebs_public_snapshot` |
| クラウドプラットフォーム | AWS |
| サービス | ec2 |
| サブサービス | snapshot |
| 重大度 | critical |
| カテゴリ | internet-exposed |
| チェックタイプ | Data Protection |
| リソースタイプ | Other |
| リソースグループ | compute |

## 説明

Ensure there are no EBS Snapshots set as Public.

## リスク

When you share a snapshot, you are giving others access to all of the data on the snapshot. Share snapshots only with people with whom you want to share all of your snapshot data.

## 推奨事項

Ensure the snapshot should be shared.

- 推奨リンク：[https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ebs-modifying-snapshot-permissions.html](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ebs-modifying-snapshot-permissions.html)

## 修正手順


### CLI

```text
aws ec2 modify-snapshot-attribute --region <REGION> --snapshot-id <EC2_SNAPSHOT_ID> --attribute createVolumePermission --operation remove --user-ids all
```

### Other

[https://docs.ST Cloud.com/checks/aws/public-policies/public_7](https://docs.ST Cloud.com/checks/aws/public-policies/public_7)

## 参考資料

- [https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ebs-modifying-snapshot-permissions.html](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ebs-modifying-snapshot-permissions.html)

## 技術情報

- Source Metadata：[sources/aws/ec2_ebs_public_snapshot/metadata.json](../../sources/aws/ec2_ebs_public_snapshot/metadata.json)
- Source Code：[sources/aws/ec2_ebs_public_snapshot/check.py](../../sources/aws/ec2_ebs_public_snapshot/check.py)
- Source Metadata Path：`sources/aws/ec2_ebs_public_snapshot/metadata.json`
- Source Code Path：`sources/aws/ec2_ebs_public_snapshot/check.py`
