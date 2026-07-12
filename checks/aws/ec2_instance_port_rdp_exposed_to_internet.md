# Ensure no EC2 instances allow ingress from the internet to TCP port 3389 (RDP)

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `ec2_instance_port_rdp_exposed_to_internet` |
| クラウドプラットフォーム | AWS |
| サービス | ec2 |
| サブサービス | instance |
| 重大度 | critical |
| カテゴリ | internet-exposed |
| チェックタイプ | Infrastructure Security |
| リソースタイプ | AwsEc2Instance |
| リソースグループ | compute |

## 説明

Ensure no EC2 instances allow ingress from the internet to TCP port 3389 (RDP).

## リスク

RDP is a proprietary protocol developed by Microsoft for connecting to Windows systems. Exposing RDP to the internet can allow attackers to brute force the login credentials and gain unauthorized access to the EC2 instance.

## 推奨事項

Modify the security group associated with the EC2 instance to remove the rule that allows ingress from the internet to TCP port 3389 (RDP).

- 推奨リンク：[https://docs.aws.amazon.com/vpc/latest/userguide/VPC_SecurityGroups.html](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_SecurityGroups.html)

## 修正手順

No remediation steps available.

## 参考資料

- [https://docs.aws.amazon.com/vpc/latest/userguide/VPC_SecurityGroups.html](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_SecurityGroups.html)

## 技術情報

- Source Metadata：[sources/aws/ec2_instance_port_rdp_exposed_to_internet/metadata.json](../../sources/aws/ec2_instance_port_rdp_exposed_to_internet/metadata.json)
- Source Code：[sources/aws/ec2_instance_port_rdp_exposed_to_internet/check.py](../../sources/aws/ec2_instance_port_rdp_exposed_to_internet/check.py)
- Source Metadata Path：`sources/aws/ec2_instance_port_rdp_exposed_to_internet/metadata.json`
- Source Code Path：`sources/aws/ec2_instance_port_rdp_exposed_to_internet/check.py`
