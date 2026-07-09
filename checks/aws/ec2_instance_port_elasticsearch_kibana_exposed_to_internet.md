# Ensure no EC2 instances allow ingress from the internet to Elasticsearch and Kibana ports (TCP 9200, 9300, 5601).

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `ec2_instance_port_elasticsearch_kibana_exposed_to_internet` |
| 云平台 | AWS |
| 服务 | ec2 |
| 子服务 | instance |
| 严重等级 | critical |
| 类别 | internet-exposed |
| 检查类型 | Infrastructure Security |
| 资源类型 | AwsEc2Instance |
| 资源组 | compute |

## 描述

Ensure no EC2 instances allow ingress from the internet to Elasticsearch and Kibana ports (TCP 9200, 9300, 5601).

## 风险

Elasticsearch and Kibana are commonly used for log and data analysis. Allowing ingress from the internet to these ports can expose sensitive data to unauthorized users.

## 推荐措施

Modify the security group to remove the rule that allows ingress from the internet to TCP ports 9200, 9300, 5601.

- 推荐链接：[https://docs.aws.amazon.com/vpc/latest/userguide/VPC_SecurityGroups.html](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_SecurityGroups.html)

## 修复步骤

No remediation steps available.

## 参考资料

- [https://docs.aws.amazon.com/vpc/latest/userguide/VPC_SecurityGroups.html](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_SecurityGroups.html)

## 技术信息

- Source Metadata：[sources/aws/ec2_instance_port_elasticsearch_kibana_exposed_to_internet/metadata.json](../../sources/aws/ec2_instance_port_elasticsearch_kibana_exposed_to_internet/metadata.json)
- Source Code：[sources/aws/ec2_instance_port_elasticsearch_kibana_exposed_to_internet/check.py](../../sources/aws/ec2_instance_port_elasticsearch_kibana_exposed_to_internet/check.py)
- Source Metadata Path：`sources/aws/ec2_instance_port_elasticsearch_kibana_exposed_to_internet/metadata.json`
- Source Code Path：`sources/aws/ec2_instance_port_elasticsearch_kibana_exposed_to_internet/check.py`
