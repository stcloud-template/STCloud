# Check EC2 Instances older than specific days.

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `ec2_instance_older_than_specific_days` |
| クラウドプラットフォーム | AWS |
| サービス | ec2 |
| 重大度 | medium |
| カテゴリ | Uncategorized |
| チェックタイプ | Infrastructure Security |
| リソースタイプ | AwsEc2Instance |
| リソースグループ | compute |

## 説明

Check EC2 Instances older than specific days.

## リスク

Having old instances within your AWS account could increase the risk of having vulnerable software.

## 推奨事項

Check if software running in the instance is up to date and patched accordingly. Use AWS Systems Manager to patch instances and view patching compliance information.

- 推奨リンク：[https://docs.aws.amazon.com/systems-manager/latest/userguide/viewing-patch-compliance-results.html](https://docs.aws.amazon.com/systems-manager/latest/userguide/viewing-patch-compliance-results.html)

## 修正手順


### Other

[https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/EC2/ec2-instance-too-old.html](https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/EC2/ec2-instance-too-old.html)

## 参考資料

- [https://docs.aws.amazon.com/systems-manager/latest/userguide/viewing-patch-compliance-results.html](https://docs.aws.amazon.com/systems-manager/latest/userguide/viewing-patch-compliance-results.html)

## 技術情報

- Source Metadata：[sources/aws/ec2_instance_older_than_specific_days/metadata.json](../../sources/aws/ec2_instance_older_than_specific_days/metadata.json)
- Source Code：[sources/aws/ec2_instance_older_than_specific_days/check.py](../../sources/aws/ec2_instance_older_than_specific_days/check.py)
- Source Metadata Path：`sources/aws/ec2_instance_older_than_specific_days/metadata.json`
- Source Code Path：`sources/aws/ec2_instance_older_than_specific_days/check.py`
