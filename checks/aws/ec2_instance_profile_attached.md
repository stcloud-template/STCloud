# Ensure IAM instance roles are used for AWS resource access from instances

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `ec2_instance_profile_attached` |
| 云平台 | AWS |
| 服务 | ec2 |
| 严重等级 | medium |
| 类别 | Uncategorized |
| 检查类型 | Software and Configuration Checks/Industry and Regulatory Standards/CIS AWS Foundations Benchmark |
| 资源类型 | AwsEc2Instance |
| 资源组 | compute |

## 描述

Ensure IAM instance roles are used for AWS resource access from instances.

## 风险

AWS access from within AWS instances can be done by either encoding AWS keys into AWS API calls or by assigning the instance to a role which has an appropriate permissions policy for the required access. AWS IAM roles reduce the risks associated with sharing and rotating credentials that can be used outside of AWS itself. If credentials are compromised, they can be used from outside of the AWS account.

## 推荐措施

Create an IAM instance role if necessary and attach it to the corresponding EC2 instance..

- 推荐链接：[http://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_switch-role-ec2.html](http://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_switch-role-ec2.html)

## 修复步骤


### Other

[https://github.com/cloudmatos/matos/tree/master/remediations/aws/ec2/attach_iam_roles_ec2_instances](https://github.com/cloudmatos/matos/tree/master/remediations/aws/ec2/attach_iam_roles_ec2_instances)

## 参考资料

- [http://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_switch-role-ec2.html](http://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_switch-role-ec2.html)

## 技术信息

- Source Metadata：[sources/aws/ec2_instance_profile_attached/metadata.json](../../sources/aws/ec2_instance_profile_attached/metadata.json)
- Source Code：[sources/aws/ec2_instance_profile_attached/check.py](../../sources/aws/ec2_instance_profile_attached/check.py)
- Source Metadata Path：`sources/aws/ec2_instance_profile_attached/metadata.json`
- Source Code Path：`sources/aws/ec2_instance_profile_attached/check.py`
