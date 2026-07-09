# Ensure no Network ACLs allow ingress from 0.0.0.0/0 to any port.

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `ec2_networkacl_allow_ingress_any_port` |
| 云平台 | AWS |
| 服务 | ec2 |
| 子服务 | networkacl |
| 严重等级 | medium |
| 类别 | internet-exposed |
| 检查类型 | Software and Configuration Checks, Industry and Regulatory Standards, CIS AWS Foundations Benchmark |
| 资源类型 | AwsEc2NetworkAcl |
| 资源组 | network |

## 描述

Ensure no Network ACLs allow ingress from 0.0.0.0/0 to any port.

## 风险

Even having a perimeter firewall, having network acls open allows any user or malware with vpc access to scan for well known and sensitive ports and gain access to instance.

## 推荐措施

Apply Zero Trust approach. Implement a process to scan and remediate unrestricted or overly permissive network acls. Recommended best practices is to narrow the definition for the minimum ports required.

- 推荐链接：[https://docs.aws.amazon.com/vpc/latest/userguide/vpc-network-acls.html](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-network-acls.html)

## 修复步骤

No remediation steps available.

## 参考资料

- [https://docs.aws.amazon.com/vpc/latest/userguide/vpc-network-acls.html](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-network-acls.html)

## 技术信息

- Source Metadata：[sources/aws/ec2_networkacl_allow_ingress_any_port/metadata.json](../../sources/aws/ec2_networkacl_allow_ingress_any_port/metadata.json)
- Source Code：[sources/aws/ec2_networkacl_allow_ingress_any_port/check.py](../../sources/aws/ec2_networkacl_allow_ingress_any_port/check.py)
- Source Metadata Path：`sources/aws/ec2_networkacl_allow_ingress_any_port/metadata.json`
- Source Code Path：`sources/aws/ec2_networkacl_allow_ingress_any_port/check.py`
