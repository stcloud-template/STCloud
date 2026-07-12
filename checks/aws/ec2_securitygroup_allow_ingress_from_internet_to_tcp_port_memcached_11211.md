# Ensure no security groups allow ingress from 0.0.0.0/0 or ::/0 to Memcached port 11211.

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `ec2_securitygroup_allow_ingress_from_internet_to_tcp_port_memcached_11211` |
| クラウドプラットフォーム | AWS |
| サービス | ec2 |
| サブサービス | securitygroup |
| 重大度 | high |
| カテゴリ | internet-exposed |
| チェックタイプ | Infrastructure Security |
| リソースタイプ | AwsEc2SecurityGroup |
| リソースグループ | network |

## 説明

Ensure no security groups allow ingress from 0.0.0.0/0 or ::/0 to Memcached port 11211.

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

- Source Metadata：[sources/aws/ec2_securitygroup_allow_ingress_from_internet_to_tcp_port_memcached_11211/metadata.json](../../sources/aws/ec2_securitygroup_allow_ingress_from_internet_to_tcp_port_memcached_11211/metadata.json)
- Source Code：[sources/aws/ec2_securitygroup_allow_ingress_from_internet_to_tcp_port_memcached_11211/check.py](../../sources/aws/ec2_securitygroup_allow_ingress_from_internet_to_tcp_port_memcached_11211/check.py)
- Source Metadata Path：`sources/aws/ec2_securitygroup_allow_ingress_from_internet_to_tcp_port_memcached_11211/metadata.json`
- Source Code Path：`sources/aws/ec2_securitygroup_allow_ingress_from_internet_to_tcp_port_memcached_11211/check.py`
