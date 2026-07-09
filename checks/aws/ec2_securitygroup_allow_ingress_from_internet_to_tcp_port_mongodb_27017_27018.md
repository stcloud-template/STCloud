# Ensure no security groups allow ingress from 0.0.0.0/0 or ::/0 to MongoDB ports 27017 and 27018.

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `ec2_securitygroup_allow_ingress_from_internet_to_tcp_port_mongodb_27017_27018` |
| 云平台 | AWS |
| 服务 | ec2 |
| 子服务 | securitygroup |
| 严重等级 | high |
| 类别 | internet-exposed |
| 检查类型 | Infrastructure Security |
| 资源类型 | AwsEc2SecurityGroup |
| 资源组 | network |

## 描述

Ensure no security groups allow ingress from 0.0.0.0/0 or ::/0 to MongoDB ports 27017 and 27018.

## 风险

If Security groups are not properly configured the attack surface is increased.

## 推荐措施

Use a Zero Trust approach. Narrow ingress traffic as much as possible. Consider north-south as well as east-west traffic.

- 推荐链接：[https://docs.aws.amazon.com/vpc/latest/userguide/VPC_SecurityGroups.html](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_SecurityGroups.html)

## 修复步骤

No remediation steps available.

## 参考资料

- [https://docs.aws.amazon.com/vpc/latest/userguide/VPC_SecurityGroups.html](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_SecurityGroups.html)

## 技术信息

- Source Metadata：[sources/aws/ec2_securitygroup_allow_ingress_from_internet_to_tcp_port_mongodb_27017_27018/metadata.json](../../sources/aws/ec2_securitygroup_allow_ingress_from_internet_to_tcp_port_mongodb_27017_27018/metadata.json)
- Source Code：[sources/aws/ec2_securitygroup_allow_ingress_from_internet_to_tcp_port_mongodb_27017_27018/check.py](../../sources/aws/ec2_securitygroup_allow_ingress_from_internet_to_tcp_port_mongodb_27017_27018/check.py)
- Source Metadata Path：`sources/aws/ec2_securitygroup_allow_ingress_from_internet_to_tcp_port_mongodb_27017_27018/metadata.json`
- Source Code Path：`sources/aws/ec2_securitygroup_allow_ingress_from_internet_to_tcp_port_mongodb_27017_27018/check.py`
