# Ensure no Network ACLs allow ingress from 0.0.0.0/0 to SSH port 22

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `ec2_networkacl_allow_ingress_tcp_port_22` |
| 云平台 | AWS |
| 服务 | ec2 |
| 子服务 | networkacl |
| 严重等级 | medium |
| 类别 | internet-exposed |
| 检查类型 | Infrastructure Security |
| 资源类型 | AwsEc2NetworkAcl |
| 资源组 | network |

## 描述

Ensure no Network ACLs allow ingress from 0.0.0.0/0 to SSH port 22

## 风险

Even having a perimeter firewall, having network acls open allows any user or malware with vpc access to scan for well known and sensitive ports and gain access to instance.

## 推荐措施

Apply Zero Trust approach. Implement a process to scan and remediate unrestricted or overly permissive network acls. Recommended best practices is to narrow the definition for the minimum ports required.

- 推荐链接：[https://docs.aws.amazon.com/vpc/latest/userguide/vpc-network-acls.html](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-network-acls.html)

## 修复步骤


### Native IaC

[https://docs.ST Cloud.com/checks/aws/networking-policies/ensure-aws-nacl-does-not-allow-ingress-from-00000-to-port-22#cloudformation](https://docs.ST Cloud.com/checks/aws/networking-policies/ensure-aws-nacl-does-not-allow-ingress-from-00000-to-port-22#cloudformation)

### Terraform

[https://docs.ST Cloud.com/checks/aws/networking-policies/ensure-aws-nacl-does-not-allow-ingress-from-00000-to-port-22#terraform](https://docs.ST Cloud.com/checks/aws/networking-policies/ensure-aws-nacl-does-not-allow-ingress-from-00000-to-port-22#terraform)

## 参考资料

- [https://docs.aws.amazon.com/vpc/latest/userguide/vpc-network-acls.html](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-network-acls.html)

## 技术信息

- Source Metadata：[sources/aws/ec2_networkacl_allow_ingress_tcp_port_22/metadata.json](../../sources/aws/ec2_networkacl_allow_ingress_tcp_port_22/metadata.json)
- Source Code：[sources/aws/ec2_networkacl_allow_ingress_tcp_port_22/check.py](../../sources/aws/ec2_networkacl_allow_ingress_tcp_port_22/check.py)
- Source Metadata Path：`sources/aws/ec2_networkacl_allow_ingress_tcp_port_22/metadata.json`
- Source Code Path：`sources/aws/ec2_networkacl_allow_ingress_tcp_port_22/check.py`
