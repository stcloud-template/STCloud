# Check if EBS snapshots exists.

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `ec2_ebs_volume_snapshots_exists` |
| クラウドプラットフォーム | AWS |
| サービス | ec2 |
| サブサービス | volume |
| 重大度 | medium |
| カテゴリ | forensics-ready |
| チェックタイプ | Data Protection |
| リソースタイプ | AwsEc2Volume |
| リソースグループ | storage |

## 説明

Check if EBS snapshots exists.

## リスク

Ensure that your EBS volumes (available or in-use) have recent snapshots (taken weekly) available for point-in-time recovery for a better, more reliable data backup strategy.

## 推奨事項

Creating point-in-time EBS snapshots periodically will allow you to handle efficiently your data recovery process in the event of a failure, to save your data before shutting down an EC2 instance, to back up data for geographical expansion and to maintain your disaster recovery stack up to date.

- 推奨リンク：[https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EBSSnapshots.html](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EBSSnapshots.html)

## 修正手順


### CLI

```text
aws ec2 --region <REGION> create-snapshot --volume-id <VOLUME-ID>
```

### Other

[https://www.trendmicro.com/cloudoneconformity-staging/knowledge-base/aws/EBS/ebs-volumes-recent-snapshots.html](https://www.trendmicro.com/cloudoneconformity-staging/knowledge-base/aws/EBS/ebs-volumes-recent-snapshots.html)

## 参考資料

- [https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EBSSnapshots.html](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EBSSnapshots.html)

## 技術情報

- Source Metadata：[sources/aws/ec2_ebs_volume_snapshots_exists/metadata.json](../../sources/aws/ec2_ebs_volume_snapshots_exists/metadata.json)
- Source Code：[sources/aws/ec2_ebs_volume_snapshots_exists/check.py](../../sources/aws/ec2_ebs_volume_snapshots_exists/check.py)
- Source Metadata Path：`sources/aws/ec2_ebs_volume_snapshots_exists/metadata.json`
- Source Code Path：`sources/aws/ec2_ebs_volume_snapshots_exists/check.py`
