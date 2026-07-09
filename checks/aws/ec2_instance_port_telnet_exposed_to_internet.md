# Ensure no EC2 instances allow ingress from the internet to TCP port 23 (Telnet).

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `ec2_instance_port_telnet_exposed_to_internet` |
| 云平台 | AWS |
| 服务 | ec2 |
| 子服务 | instance |
| 严重等级 | critical |
| 类别 | internet-exposed |
| 检查类型 | Infrastructure Security |
| 资源类型 | AwsEc2Instance |
| 资源组 | compute |

## 描述

Ensure no EC2 instances allow ingress from the internet to TCP port 23 (Telnet).

## 风险

Telnet is an insecure protocol that transmits data in plain text. Exposure of Telnet services to the internet can lead to unauthorized access to the EC2 instance.

## 推荐措施

Modify the security group associated with the EC2 instance to remove the rule that allows ingress from the internet to TCP port 23.

- 推荐链接：[https://docs.aws.amazon.com/vpc/latest/userguide/VPC_SecurityGroups.html](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_SecurityGroups.html)

## 修复步骤

No remediation steps available.

## 参考资料

- [https://docs.aws.amazon.com/vpc/latest/userguide/VPC_SecurityGroups.html](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_SecurityGroups.html)

## 技术信息

- Source Metadata：[sources/aws/ec2_instance_port_telnet_exposed_to_internet/metadata.json](../../sources/aws/ec2_instance_port_telnet_exposed_to_internet/metadata.json)
- Source Code：[sources/aws/ec2_instance_port_telnet_exposed_to_internet/check.py](../../sources/aws/ec2_instance_port_telnet_exposed_to_internet/check.py)
- Source Metadata Path：`sources/aws/ec2_instance_port_telnet_exposed_to_internet/metadata.json`
- Source Code Path：`sources/aws/ec2_instance_port_telnet_exposed_to_internet/check.py`
