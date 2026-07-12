# Ensure no EC2 instances allow ingress from the internet to TCP port 11211 (Memcached).

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `ec2_instance_port_memcached_exposed_to_internet` |
| クラウドプラットフォーム | AWS |
| サービス | ec2 |
| サブサービス | instance |
| 重大度 | critical |
| カテゴリ | internet-exposed |
| チェックタイプ | Infrastructure Security |
| リソースタイプ | AwsEc2Instance |
| リソースグループ | compute |

## 説明

Ensure no EC2 instances allow ingress from the internet to TCP port 11211 (Memcached).

## リスク

Memcached is an open-source, high-performance, distributed memory object caching system. It is often used to speed up dynamic database-driven websites by caching data and objects in RAM to reduce the number of times an external data source must be read. Memcached is designed to be used in trusted environments and should not be exposed to the internet. If Memcached is exposed to the internet, it can be exploited by attackers to perform distributed denial-of-service (DDoS) attacks, data exfiltration, and other malicious activities.

## 推奨事項

Modify the security group associated with the EC2 instance to remove the rule that allows ingress from the internet to TCP port 11211 (Memcached).

- 推奨リンク：[https://docs.aws.amazon.com/vpc/latest/userguide/VPC_SecurityGroups.html](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_SecurityGroups.html)

## 修正手順

No remediation steps available.

## 参考資料

- [https://docs.aws.amazon.com/vpc/latest/userguide/VPC_SecurityGroups.html](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_SecurityGroups.html)

## 技術情報

- Source Metadata：[sources/aws/ec2_instance_port_memcached_exposed_to_internet/metadata.json](../../sources/aws/ec2_instance_port_memcached_exposed_to_internet/metadata.json)
- Source Code：[sources/aws/ec2_instance_port_memcached_exposed_to_internet/check.py](../../sources/aws/ec2_instance_port_memcached_exposed_to_internet/check.py)
- Source Metadata Path：`sources/aws/ec2_instance_port_memcached_exposed_to_internet/metadata.json`
- Source Code Path：`sources/aws/ec2_instance_port_memcached_exposed_to_internet/check.py`
