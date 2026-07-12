# Ensure no EC2 instances allow ingress from the internet to Elasticsearch and Kibana ports (TCP 9200, 9300, 5601).

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `ec2_instance_port_elasticsearch_kibana_exposed_to_internet` |
| クラウドプラットフォーム | AWS |
| サービス | ec2 |
| サブサービス | instance |
| 重大度 | critical |
| カテゴリ | internet-exposed |
| チェックタイプ | Infrastructure Security |
| リソースタイプ | AwsEc2Instance |
| リソースグループ | compute |

## 説明

Ensure no EC2 instances allow ingress from the internet to Elasticsearch and Kibana ports (TCP 9200, 9300, 5601).

## リスク

Elasticsearch and Kibana are commonly used for log and data analysis. Allowing ingress from the internet to these ports can expose sensitive data to unauthorized users.

## 推奨事項

Modify the security group to remove the rule that allows ingress from the internet to TCP ports 9200, 9300, 5601.

- 推奨リンク：[https://docs.aws.amazon.com/vpc/latest/userguide/VPC_SecurityGroups.html](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_SecurityGroups.html)

## 修正手順

No remediation steps available.

## 参考資料

- [https://docs.aws.amazon.com/vpc/latest/userguide/VPC_SecurityGroups.html](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_SecurityGroups.html)

## 技術情報

- Source Metadata：[sources/aws/ec2_instance_port_elasticsearch_kibana_exposed_to_internet/metadata.json](../../sources/aws/ec2_instance_port_elasticsearch_kibana_exposed_to_internet/metadata.json)
- Source Code：[sources/aws/ec2_instance_port_elasticsearch_kibana_exposed_to_internet/check.py](../../sources/aws/ec2_instance_port_elasticsearch_kibana_exposed_to_internet/check.py)
- Source Metadata Path：`sources/aws/ec2_instance_port_elasticsearch_kibana_exposed_to_internet/metadata.json`
- Source Code Path：`sources/aws/ec2_instance_port_elasticsearch_kibana_exposed_to_internet/check.py`
