# Security Groups created by EC2 Launch Wizard.

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `ec2_securitygroup_from_launch_wizard` |
| 云平台 | AWS |
| 服务 | ec2 |
| 子服务 | securitygroup |
| 严重等级 | medium |
| 类别 | Uncategorized |
| 检查类型 | Infrastructure Security |
| 资源类型 | AwsEc2SecurityGroup |
| 资源组 | network |

## 描述

Security Groups created by EC2 Launch Wizard.

## 风险

Security Groups Created on the AWS Console using the EC2 wizard may allow port 22 from 0.0.0.0/0.

## 推荐措施

Apply Zero Trust approach. Implement a process to scan and remediate security groups created by the EC2 Wizard. Recommended best practices is to use an authorized security group.

- 推荐链接：[https://docs.aws.amazon.com/eks/latest/userguide/sec-group-reqs.html](https://docs.aws.amazon.com/eks/latest/userguide/sec-group-reqs.html)

## 修复步骤


### Other

[https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/EC2/security-group-prefixed-with-launch-wizard.html](https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/EC2/security-group-prefixed-with-launch-wizard.html)

## 参考资料

- [https://docs.aws.amazon.com/eks/latest/userguide/sec-group-reqs.html](https://docs.aws.amazon.com/eks/latest/userguide/sec-group-reqs.html)

## 技术信息

- Source Metadata：[sources/aws/ec2_securitygroup_from_launch_wizard/metadata.json](../../sources/aws/ec2_securitygroup_from_launch_wizard/metadata.json)
- Source Code：[sources/aws/ec2_securitygroup_from_launch_wizard/check.py](../../sources/aws/ec2_securitygroup_from_launch_wizard/check.py)
- Source Metadata Path：`sources/aws/ec2_securitygroup_from_launch_wizard/metadata.json`
- Source Code Path：`sources/aws/ec2_securitygroup_from_launch_wizard/check.py`
