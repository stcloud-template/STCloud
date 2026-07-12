# Check if EC2 instances are managed by Systems Manager.

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `ec2_instance_managed_by_ssm` |
| クラウドプラットフォーム | AWS |
| サービス | ec2 |
| サブサービス | instance |
| 重大度 | medium |
| カテゴリ | Uncategorized |
| チェックタイプ | Infrastructure Security |
| リソースタイプ | AwsEc2Instance |
| リソースグループ | compute |

## 説明

Check if EC2 instances are managed by Systems Manager.

## リスク

AWS Config provides AWS Managed Rules, which are predefined, customizable rules that AWS Config uses to evaluate whether your AWS resource configurations comply with common best practices.

## 推奨事項

Verify and apply Systems Manager Prerequisites.

- 推奨リンク：[https://docs.aws.amazon.com/systems-manager/latest/userguide/managed_instances.html](https://docs.aws.amazon.com/systems-manager/latest/userguide/managed_instances.html)

## 修正手順


### Other

[https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/SSM/ssm-managed-instances.html](https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/SSM/ssm-managed-instances.html)

## 参考資料

- [https://docs.aws.amazon.com/systems-manager/latest/userguide/managed_instances.html](https://docs.aws.amazon.com/systems-manager/latest/userguide/managed_instances.html)

## 技術情報

- Source Metadata：[sources/aws/ec2_instance_managed_by_ssm/metadata.json](../../sources/aws/ec2_instance_managed_by_ssm/metadata.json)
- Source Code：[sources/aws/ec2_instance_managed_by_ssm/check.py](../../sources/aws/ec2_instance_managed_by_ssm/check.py)
- Source Metadata Path：`sources/aws/ec2_instance_managed_by_ssm/metadata.json`
- Source Code Path：`sources/aws/ec2_instance_managed_by_ssm/check.py`
