# Ensure no EC2 instances allow ingress from the internet to TCP port 1433 or 1434 (SQL Server).

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `ec2_instance_port_sqlserver_exposed_to_internet` |
| クラウドプラットフォーム | AWS |
| サービス | ec2 |
| サブサービス | instance |
| 重大度 | critical |
| カテゴリ | internet-exposed |
| チェックタイプ | Infrastructure Security |
| リソースタイプ | AwsEc2Instance |
| リソースグループ | compute |

## 説明

Ensure no EC2 instances allow ingress from the internet to TCP port 1433 or 1434 (SQL Server).

## リスク

SQL Server is a database management system that is used to store and retrieve data. If an EC2 instance allows ingress from the internet to TCP port 1433 or 1434, it may be vulnerable to unauthorized access and data exfiltration.

## 推奨事項

Modify the security group to remove the rule that allows ingress from the internet to TCP port 1433 or 1434 (SQL Server).

- 推奨リンク：[https://docs.aws.amazon.com/vpc/latest/userguide/VPC_SecurityGroups.html](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_SecurityGroups.html)

## 修正手順

No remediation steps available.

## 参考資料

- [https://docs.aws.amazon.com/vpc/latest/userguide/VPC_SecurityGroups.html](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_SecurityGroups.html)

## 技術情報

- Source Metadata：[sources/aws/ec2_instance_port_sqlserver_exposed_to_internet/metadata.json](../../sources/aws/ec2_instance_port_sqlserver_exposed_to_internet/metadata.json)
- Source Code：[sources/aws/ec2_instance_port_sqlserver_exposed_to_internet/check.py](../../sources/aws/ec2_instance_port_sqlserver_exposed_to_internet/check.py)
- Source Metadata Path：`sources/aws/ec2_instance_port_sqlserver_exposed_to_internet/metadata.json`
- Source Code Path：`sources/aws/ec2_instance_port_sqlserver_exposed_to_internet/check.py`
