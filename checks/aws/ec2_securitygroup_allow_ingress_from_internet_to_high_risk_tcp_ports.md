# Ensure no security groups allow ingress from 0.0.0.0/0 or ::/0 to high risk ports.

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `ec2_securitygroup_allow_ingress_from_internet_to_high_risk_tcp_ports` |
| 云平台 | AWS |
| 服务 | ec2 |
| 子服务 | securitygroup |
| 严重等级 | critical |
| 类别 | internet-exposed |
| 检查类型 | Infrastructure Security |
| 资源类型 | AwsEc2SecurityGroup |
| 资源组 | network |

## 描述

Ensure no security groups allow ingress from 0.0.0.0/0 or ::/0 to ports 25(SMTP), 110(POP3), 135(RCP), 143(IMAP), 445(CIFS), 3000(Go, Node.js, and Ruby web developemnt frameworks), 4333(ahsp), 5000(Python web development frameworks), 5500(fcp-addr-srvr1), 8080(proxy), 8088(legacy HTTP port).

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

- Source Metadata：[sources/aws/ec2_securitygroup_allow_ingress_from_internet_to_high_risk_tcp_ports/metadata.json](../../sources/aws/ec2_securitygroup_allow_ingress_from_internet_to_high_risk_tcp_ports/metadata.json)
- Source Code：[sources/aws/ec2_securitygroup_allow_ingress_from_internet_to_high_risk_tcp_ports/check.py](../../sources/aws/ec2_securitygroup_allow_ingress_from_internet_to_high_risk_tcp_ports/check.py)
- Source Metadata Path：`sources/aws/ec2_securitygroup_allow_ingress_from_internet_to_high_risk_tcp_ports/metadata.json`
- Source Code Path：`sources/aws/ec2_securitygroup_allow_ingress_from_internet_to_high_risk_tcp_ports/check.py`
