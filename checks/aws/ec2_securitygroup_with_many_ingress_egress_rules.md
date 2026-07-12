# Find security groups with more than 50 ingress or egress rules.

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `ec2_securitygroup_with_many_ingress_egress_rules` |
| クラウドプラットフォーム | AWS |
| サービス | ec2 |
| サブサービス | securitygroup |
| 重大度 | high |
| カテゴリ | Uncategorized |
| チェックタイプ | Infrastructure Security |
| リソースタイプ | AwsEc2SecurityGroup |
| リソースグループ | network |

## 説明

Find security groups with more than 50 ingress or egress rules.

## リスク

If Security groups are not properly configured the attack surface is increased.

## 推奨事項

Use a Zero Trust approach. Narrow ingress traffic as much as possible. Consider north-south as well as east-west traffic.

- 推奨リンク：[https://docs.aws.amazon.com/vpc/latest/userguide/VPC_SecurityGroups.html](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_SecurityGroups.html)

## 修正手順

No remediation steps available.

## 参考資料

- [https://docs.aws.amazon.com/vpc/latest/userguide/VPC_SecurityGroups.html](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_SecurityGroups.html)

## 技術情報

- Source Metadata：[sources/aws/ec2_securitygroup_with_many_ingress_egress_rules/metadata.json](../../sources/aws/ec2_securitygroup_with_many_ingress_egress_rules/metadata.json)
- Source Code：[sources/aws/ec2_securitygroup_with_many_ingress_egress_rules/check.py](../../sources/aws/ec2_securitygroup_with_many_ingress_egress_rules/check.py)
- Source Metadata Path：`sources/aws/ec2_securitygroup_with_many_ingress_egress_rules/metadata.json`
- Source Code Path：`sources/aws/ec2_securitygroup_with_many_ingress_egress_rules/check.py`
