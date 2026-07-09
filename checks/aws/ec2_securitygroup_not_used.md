# Ensure there are no Security Groups not being used.

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `ec2_securitygroup_not_used` |
| 云平台 | AWS |
| 服务 | ec2 |
| 子服务 | securitygroup |
| 严重等级 | low |
| 类别 | Uncategorized |
| 检查类型 | Infrastructure Security |
| 资源类型 | AwsEc2SecurityGroup |
| 资源组 | network |

## 描述

Ensure there are no Security Groups not being used.

## 风险

Having clear definition and scope for Security Groups creates a better administration environment.

## 推荐措施

List all the security groups and then use the cli to check if they are attached to an instance.

- 推荐链接：[https://aws.amazon.com/premiumsupport/knowledge-center/ec2-find-security-group-resources/](https://aws.amazon.com/premiumsupport/knowledge-center/ec2-find-security-group-resources/)

## 修复步骤

No remediation steps available.

## 参考资料

- [https://aws.amazon.com/premiumsupport/knowledge-center/ec2-find-security-group-resources/](https://aws.amazon.com/premiumsupport/knowledge-center/ec2-find-security-group-resources/)

## 技术信息

- Source Metadata：[sources/aws/ec2_securitygroup_not_used/metadata.json](../../sources/aws/ec2_securitygroup_not_used/metadata.json)
- Source Code：[sources/aws/ec2_securitygroup_not_used/check.py](../../sources/aws/ec2_securitygroup_not_used/check.py)
- Source Metadata Path：`sources/aws/ec2_securitygroup_not_used/metadata.json`
- Source Code Path：`sources/aws/ec2_securitygroup_not_used/check.py`
