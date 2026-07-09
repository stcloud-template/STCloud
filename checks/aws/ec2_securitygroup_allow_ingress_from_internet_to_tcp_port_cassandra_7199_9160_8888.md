# Ensure no security groups allow ingress from the internet to Cassandra ports TCP 7199, 9160 and 8888.

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `ec2_securitygroup_allow_ingress_from_internet_to_tcp_port_cassandra_7199_9160_8888` |
| 云平台 | AWS |
| 服务 | ec2 |
| 子服务 | securitygroup |
| 严重等级 | critical |
| 类别 | internet-exposed |
| 检查类型 | Infrastructure Security |
| 资源类型 | AwsEc2SecurityGroup |
| 资源组 | network |

## 描述

Ensure no security groups allow ingress from the internet to Cassandra ports TCP 7199, 9160 and 8888.

## 风险

Exposing Cassandra ports to the internet can allow unauthorized access to database services and may lead to data disclosure, data loss or service compromise.

## 推荐措施

Modify the security group to remove ingress rules that allow traffic from the internet to TCP ports 7199, 9160 or 8888.

- 推荐链接：[https://docs.aws.amazon.com/vpc/latest/userguide/VPC_SecurityGroups.html](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_SecurityGroups.html)

## 修复步骤

No remediation steps available.

## 参考资料

- [https://docs.aws.amazon.com/vpc/latest/userguide/VPC_SecurityGroups.html](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_SecurityGroups.html)

## 技术信息

- Source Metadata：[sources/aws/ec2_securitygroup_allow_ingress_from_internet_to_tcp_port_cassandra_7199_9160_8888/metadata.json](../../sources/aws/ec2_securitygroup_allow_ingress_from_internet_to_tcp_port_cassandra_7199_9160_8888/metadata.json)
- Source Code：[sources/aws/ec2_securitygroup_allow_ingress_from_internet_to_tcp_port_cassandra_7199_9160_8888/check.py](../../sources/aws/ec2_securitygroup_allow_ingress_from_internet_to_tcp_port_cassandra_7199_9160_8888/check.py)
- Source Metadata Path：`sources/aws/ec2_securitygroup_allow_ingress_from_internet_to_tcp_port_cassandra_7199_9160_8888/metadata.json`
- Source Code Path：`sources/aws/ec2_securitygroup_allow_ingress_from_internet_to_tcp_port_cassandra_7199_9160_8888/check.py`
