# Ensure no EC2 instances allow ingress from the internet to TCP port 6379 (Redis).

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `ec2_instance_port_redis_exposed_to_internet` |
| 云平台 | AWS |
| 服务 | ec2 |
| 子服务 | instance |
| 严重等级 | critical |
| 类别 | internet-exposed |
| 检查类型 | Infrastructure Security |
| 资源类型 | AwsEc2Instance |
| 资源组 | compute |

## 描述

Ensure no EC2 instances allow ingress from the internet to TCP port 6379 (Redis).

## 风险

Redis is an open-source, in-memory data structure store, used as a database, cache, and message broker. Redis is often used to store sensitive data, such as session tokens, user credentials, and other sensitive information. Allowing ingress from the internet to TCP port 6379 (Redis) can expose sensitive data to unauthorized users.

## 推荐措施

Modify the security group associated with the EC2 instance to remove the rule that allows ingress from the internet to TCP port 6379 (Redis).

- 推荐链接：[https://docs.aws.amazon.com/vpc/latest/userguide/VPC_SecurityGroups.html](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_SecurityGroups.html)

## 修复步骤

No remediation steps available.

## 参考资料

- [https://docs.aws.amazon.com/vpc/latest/userguide/VPC_SecurityGroups.html](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_SecurityGroups.html)

## 技术信息

- Source Metadata：[sources/aws/ec2_instance_port_redis_exposed_to_internet/metadata.json](../../sources/aws/ec2_instance_port_redis_exposed_to_internet/metadata.json)
- Source Code：[sources/aws/ec2_instance_port_redis_exposed_to_internet/check.py](../../sources/aws/ec2_instance_port_redis_exposed_to_internet/check.py)
- Source Metadata Path：`sources/aws/ec2_instance_port_redis_exposed_to_internet/metadata.json`
- Source Code Path：`sources/aws/ec2_instance_port_redis_exposed_to_internet/check.py`
