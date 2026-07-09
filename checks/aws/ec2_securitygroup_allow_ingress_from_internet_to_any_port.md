# Ensure no security groups allow ingress from 0.0.0.0/0 or ::/0 to any port.

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `ec2_securitygroup_allow_ingress_from_internet_to_any_port` |
| 云平台 | AWS |
| 服务 | ec2 |
| 子服务 | securitygroup |
| 严重等级 | high |
| 类别 | internet-exposed |
| 检查类型 | Infrastructure Security |
| 资源类型 | AwsEc2SecurityGroup |
| 资源组 | network |

## 描述

Ensure no security groups allow ingress from 0.0.0.0/0 or ::/0 to any port and not attached to a network interface with not allowed network interface types or instance owners. By default, the allowed network interface types are 'api_gateway_managed' and 'vpc_endpoint', and the allowed instance owners are 'amazon-elb', you can customize these values by setting the 'ec2_allowed_interface_types' and 'ec2_allowed_instance_owners' variables.

## 风险

The security group allows all traffic from the internet to any port. This could allow an attacker to access the instance.

## 推荐措施

Use a Zero Trust approach. Narrow ingress traffic as much as possible. Consider north-south as well as east-west traffic.

- 推荐链接：[https://docs.aws.amazon.com/vpc/latest/userguide/VPC_SecurityGroups.html](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_SecurityGroups.html)

## 修复步骤

No remediation steps available.

## 参考资料

- [https://docs.aws.amazon.com/vpc/latest/userguide/VPC_SecurityGroups.html](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_SecurityGroups.html)

## 技术信息

- Source Metadata：[sources/aws/ec2_securitygroup_allow_ingress_from_internet_to_any_port/metadata.json](../../sources/aws/ec2_securitygroup_allow_ingress_from_internet_to_any_port/metadata.json)
- Source Code：[sources/aws/ec2_securitygroup_allow_ingress_from_internet_to_any_port/check.py](../../sources/aws/ec2_securitygroup_allow_ingress_from_internet_to_any_port/check.py)
- Source Metadata Path：`sources/aws/ec2_securitygroup_allow_ingress_from_internet_to_any_port/metadata.json`
- Source Code Path：`sources/aws/ec2_securitygroup_allow_ingress_from_internet_to_any_port/check.py`
