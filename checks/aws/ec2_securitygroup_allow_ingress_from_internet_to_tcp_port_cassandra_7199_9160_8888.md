# Ensure no security groups allow ingress from the internet to Cassandra ports TCP 7199, 9160 and 8888.

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `ec2_securitygroup_allow_ingress_from_internet_to_tcp_port_cassandra_7199_9160_8888` |
| クラウドプラットフォーム | AWS |
| サービス | ec2 |
| サブサービス | securitygroup |
| 重大度 | critical |
| カテゴリ | internet-exposed |
| チェックタイプ | Infrastructure Security |
| リソースタイプ | AwsEc2SecurityGroup |
| リソースグループ | network |

## 説明

Ensure no security groups allow ingress from the internet to Cassandra ports TCP 7199, 9160 and 8888.

## リスク

Exposing Cassandra ports to the internet can allow unauthorized access to database services and may lead to data disclosure, data loss or service compromise.

## 推奨事項

Modify the security group to remove ingress rules that allow traffic from the internet to TCP ports 7199, 9160 or 8888.

- 推奨リンク：[https://docs.aws.amazon.com/vpc/latest/userguide/VPC_SecurityGroups.html](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_SecurityGroups.html)

## 修正手順

No remediation steps available.

## 参考資料

- [https://docs.aws.amazon.com/vpc/latest/userguide/VPC_SecurityGroups.html](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_SecurityGroups.html)

## 技術情報

- Source Metadata：[sources/aws/ec2_securitygroup_allow_ingress_from_internet_to_tcp_port_cassandra_7199_9160_8888/metadata.json](../../sources/aws/ec2_securitygroup_allow_ingress_from_internet_to_tcp_port_cassandra_7199_9160_8888/metadata.json)
- Source Code：[sources/aws/ec2_securitygroup_allow_ingress_from_internet_to_tcp_port_cassandra_7199_9160_8888/check.py](../../sources/aws/ec2_securitygroup_allow_ingress_from_internet_to_tcp_port_cassandra_7199_9160_8888/check.py)
- Source Metadata Path：`sources/aws/ec2_securitygroup_allow_ingress_from_internet_to_tcp_port_cassandra_7199_9160_8888/metadata.json`
- Source Code Path：`sources/aws/ec2_securitygroup_allow_ingress_from_internet_to_tcp_port_cassandra_7199_9160_8888/check.py`
