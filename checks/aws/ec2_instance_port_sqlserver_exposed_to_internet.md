# Ensure no EC2 instances allow ingress from the internet to TCP port 1433 or 1434 (SQL Server).

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `ec2_instance_port_sqlserver_exposed_to_internet` |
| 云平台 | AWS |
| 服务 | ec2 |
| 子服务 | instance |
| 严重等级 | critical |
| 类别 | internet-exposed |
| 检查类型 | Infrastructure Security |
| 资源类型 | AwsEc2Instance |
| 资源组 | compute |

## 描述

Ensure no EC2 instances allow ingress from the internet to TCP port 1433 or 1434 (SQL Server).

## 风险

SQL Server is a database management system that is used to store and retrieve data. If an EC2 instance allows ingress from the internet to TCP port 1433 or 1434, it may be vulnerable to unauthorized access and data exfiltration.

## 推荐措施

Modify the security group to remove the rule that allows ingress from the internet to TCP port 1433 or 1434 (SQL Server).

- 推荐链接：[https://docs.aws.amazon.com/vpc/latest/userguide/VPC_SecurityGroups.html](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_SecurityGroups.html)

## 修复步骤

No remediation steps available.

## 参考资料

- [https://docs.aws.amazon.com/vpc/latest/userguide/VPC_SecurityGroups.html](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_SecurityGroups.html)

## 技术信息

- Source Metadata：[sources/aws/ec2_instance_port_sqlserver_exposed_to_internet/metadata.json](../../sources/aws/ec2_instance_port_sqlserver_exposed_to_internet/metadata.json)
- Source Code：[sources/aws/ec2_instance_port_sqlserver_exposed_to_internet/check.py](../../sources/aws/ec2_instance_port_sqlserver_exposed_to_internet/check.py)
- Source Metadata Path：`sources/aws/ec2_instance_port_sqlserver_exposed_to_internet/metadata.json`
- Source Code Path：`sources/aws/ec2_instance_port_sqlserver_exposed_to_internet/check.py`
