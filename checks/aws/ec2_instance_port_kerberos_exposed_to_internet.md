# Ensure no EC2 instances allow ingress from the internet to TCP port 88, 464, 749 or 750 (Kerberos).

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `ec2_instance_port_kerberos_exposed_to_internet` |
| 云平台 | AWS |
| 服务 | ec2 |
| 子服务 | instance |
| 严重等级 | critical |
| 类别 | internet-exposed |
| 检查类型 | Infrastructure Security |
| 资源类型 | AwsEc2Instance |
| 资源组 | compute |

## 描述

Ensure no EC2 instances allow ingress from the internet to TCP port 88, 464, 749 or 750 (Kerberos).

## 风险

Kerberos is a network authentication protocol that uses secret-key cryptography to authenticate clients and servers. It is typically used in environments where users need to authenticate to access network resources. If an EC2 instance allows ingress from the internet to TCP port 88 or 464, it may be vulnerable to unauthorized access.

## 推荐措施

Modify the security group to remove the rule that allows ingress from the internet to TCP port 88, 464, 749 or 750 (Kerberos).

- 推荐链接：[https://docs.aws.amazon.com/vpc/latest/userguide/VPC_SecurityGroups.html](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_SecurityGroups.html)

## 修复步骤

No remediation steps available.

## 参考资料

- [https://docs.aws.amazon.com/vpc/latest/userguide/VPC_SecurityGroups.html](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_SecurityGroups.html)

## 技术信息

- Source Metadata：[sources/aws/ec2_instance_port_kerberos_exposed_to_internet/metadata.json](../../sources/aws/ec2_instance_port_kerberos_exposed_to_internet/metadata.json)
- Source Code：[sources/aws/ec2_instance_port_kerberos_exposed_to_internet/check.py](../../sources/aws/ec2_instance_port_kerberos_exposed_to_internet/check.py)
- Source Metadata Path：`sources/aws/ec2_instance_port_kerberos_exposed_to_internet/metadata.json`
- Source Code Path：`sources/aws/ec2_instance_port_kerberos_exposed_to_internet/check.py`
