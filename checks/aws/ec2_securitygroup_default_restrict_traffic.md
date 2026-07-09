# Ensure the default security group of every VPC restricts all traffic.

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `ec2_securitygroup_default_restrict_traffic` |
| 云平台 | AWS |
| 服务 | ec2 |
| 子服务 | securitygroup |
| 严重等级 | high |
| 类别 | Uncategorized |
| 检查类型 | Infrastructure Security |
| 资源类型 | AwsEc2SecurityGroup |
| 资源组 | network |

## 描述

Ensure the default security group of every VPC restricts all traffic.

## 风险

Even having a perimeter firewall, having security groups open allows any user or malware with vpc access to scan for well known and sensitive ports and gain access to instance.

## 推荐措施

Apply Zero Trust approach. Implement a process to scan and remediate unrestricted or overly permissive security groups. Recommended best practices is to narrow the definition for the minimum ports required.

- 推荐链接：[https://docs.aws.amazon.com/eks/latest/userguide/sec-group-reqs.html](https://docs.aws.amazon.com/eks/latest/userguide/sec-group-reqs.html)

## 修复步骤


### Terraform

[https://docs.ST Cloud.com/checks/aws/networking-policies/networking_4#terraform](https://docs.ST Cloud.com/checks/aws/networking-policies/networking_4#terraform)

### Other

[https://docs.ST Cloud.com/checks/aws/networking-policies/networking_4#aws-console](https://docs.ST Cloud.com/checks/aws/networking-policies/networking_4#aws-console)

## 参考资料

- [https://docs.aws.amazon.com/eks/latest/userguide/sec-group-reqs.html](https://docs.aws.amazon.com/eks/latest/userguide/sec-group-reqs.html)

## 技术信息

- Source Metadata：[sources/aws/ec2_securitygroup_default_restrict_traffic/metadata.json](../../sources/aws/ec2_securitygroup_default_restrict_traffic/metadata.json)
- Source Code：[sources/aws/ec2_securitygroup_default_restrict_traffic/check.py](../../sources/aws/ec2_securitygroup_default_restrict_traffic/check.py)
- Source Metadata Path：`sources/aws/ec2_securitygroup_default_restrict_traffic/metadata.json`
- Source Code Path：`sources/aws/ec2_securitygroup_default_restrict_traffic/check.py`
