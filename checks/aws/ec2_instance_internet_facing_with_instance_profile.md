# Check for internet facing EC2 instances with Instance Profiles attached.

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `ec2_instance_internet_facing_with_instance_profile` |
| 云平台 | AWS |
| 服务 | ec2 |
| 严重等级 | medium |
| 类别 | internet-exposed |
| 检查类型 | Infrastructure Security |
| 资源类型 | AwsEc2Instance |
| 资源组 | compute |

## 描述

Check for internet facing EC2 instances with Instance Profiles attached.

## 风险

Exposing an EC2 directly to internet increases the attack surface and therefore the risk of compromise.

## 推荐措施

Use an ALB and apply WAF ACL.

- 推荐链接：[https://aws.amazon.com/blogs/aws/aws-web-application-firewall-waf-for-application-load-balancers/](https://aws.amazon.com/blogs/aws/aws-web-application-firewall-waf-for-application-load-balancers/)

## 修复步骤

No remediation steps available.

## 参考资料

- [https://aws.amazon.com/blogs/aws/aws-web-application-firewall-waf-for-application-load-balancers/](https://aws.amazon.com/blogs/aws/aws-web-application-firewall-waf-for-application-load-balancers/)

## 技术信息

- Source Metadata：[sources/aws/ec2_instance_internet_facing_with_instance_profile/metadata.json](../../sources/aws/ec2_instance_internet_facing_with_instance_profile/metadata.json)
- Source Code：[sources/aws/ec2_instance_internet_facing_with_instance_profile/check.py](../../sources/aws/ec2_instance_internet_facing_with_instance_profile/check.py)
- Source Metadata Path：`sources/aws/ec2_instance_internet_facing_with_instance_profile/metadata.json`
- Source Code Path：`sources/aws/ec2_instance_internet_facing_with_instance_profile/check.py`
