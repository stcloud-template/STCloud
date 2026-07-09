# Amazon EC2 paravirtual virtualization type should not be used.

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `ec2_instance_paravirtual_type` |
| 云平台 | AWS |
| 服务 | ec2 |
| 严重等级 | medium |
| 类别 | Uncategorized |
| 资源类型 | AwsEc2Instance |
| 资源组 | compute |

## 描述

Ensure that the virtualization type of an EC2 instance is not paravirtual. The control fails if the virtualizationType of the EC2 instance is set to paravirtual.

## 风险

Using paravirtual instances can limit performance and security benefits offered by hardware virtual machine (HVM) instances, such as improved CPU, network, and storage efficiency.

## 推荐措施

To update an EC2 instance to a new instance type, see Change the instance type in the Amazon EC2 User Guide.

- 推荐链接：[https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instance-resize.html](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instance-resize.html)

## 修复步骤


### Other

[https://docs.aws.amazon.com/securityhub/latest/userguide/ec2-controls.html#ec2-24](https://docs.aws.amazon.com/securityhub/latest/userguide/ec2-controls.html#ec2-24)

## 参考资料

- [https://docs.aws.amazon.com/config/latest/developerguide/ec2-paravirtual-instance-check.html](https://docs.aws.amazon.com/config/latest/developerguide/ec2-paravirtual-instance-check.html)
- [https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instance-resize.html](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instance-resize.html)

## 技术信息

- Source Metadata：[sources/aws/ec2_instance_paravirtual_type/metadata.json](../../sources/aws/ec2_instance_paravirtual_type/metadata.json)
- Source Code：[sources/aws/ec2_instance_paravirtual_type/check.py](../../sources/aws/ec2_instance_paravirtual_type/check.py)
- Source Metadata Path：`sources/aws/ec2_instance_paravirtual_type/metadata.json`
- Source Code Path：`sources/aws/ec2_instance_paravirtual_type/check.py`
