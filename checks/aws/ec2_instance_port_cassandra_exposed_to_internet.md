# Ensure no EC2 instances allow ingress from the internet to Cassandra ports (TCP 7000, 7001, 7199, 9042, 9160).

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `ec2_instance_port_cassandra_exposed_to_internet` |
| クラウドプラットフォーム | AWS |
| サービス | ec2 |
| サブサービス | instance |
| 重大度 | critical |
| カテゴリ | internet-exposed |
| チェックタイプ | Infrastructure Security |
| リソースタイプ | AwsEc2Instance |
| リソースグループ | compute |

## 説明

Ensure no EC2 instances allow ingress from the internet to Cassandra ports (TCP 7000, 7001, 7199, 9042, 9160).

## リスク

Cassandra is a distributed database management system designed to handle large amounts of data across many commodity servers, providing high availability with no single point of failure. Exposing Cassandra ports to the internet can lead to unauthorized access to the database, data exfiltration, and data loss.

## 推奨事項

Modify the security group to remove the rule that allows ingress from the internet to TCP ports 7000, 7001, 7199, 9042 or 9160.

- 推奨リンク：[https://docs.aws.amazon.com/vpc/latest/userguide/VPC_SecurityGroups.html](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_SecurityGroups.html)

## 修正手順

No remediation steps available.

## 参考資料

- [https://docs.aws.amazon.com/vpc/latest/userguide/VPC_SecurityGroups.html](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_SecurityGroups.html)

## 技術情報

- Source Metadata：[sources/aws/ec2_instance_port_cassandra_exposed_to_internet/metadata.json](../../sources/aws/ec2_instance_port_cassandra_exposed_to_internet/metadata.json)
- Source Code：[sources/aws/ec2_instance_port_cassandra_exposed_to_internet/check.py](../../sources/aws/ec2_instance_port_cassandra_exposed_to_internet/check.py)
- Source Metadata Path：`sources/aws/ec2_instance_port_cassandra_exposed_to_internet/metadata.json`
- Source Code Path：`sources/aws/ec2_instance_port_cassandra_exposed_to_internet/check.py`
