# Security Groups created by EC2 Launch Wizard.

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `ec2_securitygroup_from_launch_wizard` |
| クラウドプラットフォーム | AWS |
| サービス | ec2 |
| サブサービス | securitygroup |
| 重大度 | medium |
| カテゴリ | Uncategorized |
| チェックタイプ | Infrastructure Security |
| リソースタイプ | AwsEc2SecurityGroup |
| リソースグループ | network |

## 説明

Security Groups created by EC2 Launch Wizard.

## リスク

Security Groups Created on the AWS Console using the EC2 wizard may allow port 22 from 0.0.0.0/0.

## 推奨事項

Apply Zero Trust approach. Implement a process to scan and remediate security groups created by the EC2 Wizard. Recommended best practices is to use an authorized security group.

- 推奨リンク：[https://docs.aws.amazon.com/eks/latest/userguide/sec-group-reqs.html](https://docs.aws.amazon.com/eks/latest/userguide/sec-group-reqs.html)

## 修正手順


### Other

[https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/EC2/security-group-prefixed-with-launch-wizard.html](https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/EC2/security-group-prefixed-with-launch-wizard.html)

## 参考資料

- [https://docs.aws.amazon.com/eks/latest/userguide/sec-group-reqs.html](https://docs.aws.amazon.com/eks/latest/userguide/sec-group-reqs.html)

## 技術情報

- Source Metadata：[sources/aws/ec2_securitygroup_from_launch_wizard/metadata.json](../../sources/aws/ec2_securitygroup_from_launch_wizard/metadata.json)
- Source Code：[sources/aws/ec2_securitygroup_from_launch_wizard/check.py](../../sources/aws/ec2_securitygroup_from_launch_wizard/check.py)
- Source Metadata Path：`sources/aws/ec2_securitygroup_from_launch_wizard/metadata.json`
- Source Code Path：`sources/aws/ec2_securitygroup_from_launch_wizard/check.py`
