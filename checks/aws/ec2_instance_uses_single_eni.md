# Amazon EC2 instances should not use multiple ENIs

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `ec2_instance_uses_single_eni` |
| 云平台 | AWS |
| 服务 | ec2 |
| 严重等级 | low |
| 类别 | trust-boundaries |
| 检查类型 | Software and Configuration Checks/AWS Security Best Practices |
| 资源类型 | AwsEc2Instance |
| 资源组 | compute |

## 描述

This control checks whether an EC2 instance uses multiple Elastic Network Interfaces (ENIs) or Elastic Fabric Adapters (EFAs). This control passes if a single network adapter is used. The control includes an optional parameter list to identify the allowed ENIs. This control also fails if an EC2 instance that belongs to an Amazon EKS cluster uses more than one ENI. If your EC2 instances need to have multiple ENIs as part of an Amazon EKS cluster, you can suppress those control findings.

## 风险

Multiple ENIs can cause dual-homed instances, meaning instances that have multiple subnets. This can add network security complexity and introduce unintended network paths and access.

## 推荐措施

To detach a network interface from an EC2 instance, follow the instructions in the Amazon EC2 User Guide.

- 推荐链接：[https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-eni.html#detach_eni](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-eni.html#detach_eni)

## 修复步骤


### Other

[https://docs.aws.amazon.com/securityhub/latest/userguide/ec2-controls.html#ec2-17](https://docs.aws.amazon.com/securityhub/latest/userguide/ec2-controls.html#ec2-17)

## 参考资料

- [https://docs.aws.amazon.com/config/latest/developerguide/ec2-instance-multiple-eni-check.html](https://docs.aws.amazon.com/config/latest/developerguide/ec2-instance-multiple-eni-check.html)
- [https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-eni.html#detach_eni](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-eni.html#detach_eni)

## 技术信息

- Source Metadata：[sources/aws/ec2_instance_uses_single_eni/metadata.json](../../sources/aws/ec2_instance_uses_single_eni/metadata.json)
- Source Code：[sources/aws/ec2_instance_uses_single_eni/check.py](../../sources/aws/ec2_instance_uses_single_eni/check.py)
- Source Metadata Path：`sources/aws/ec2_instance_uses_single_eni/metadata.json`
- Source Code Path：`sources/aws/ec2_instance_uses_single_eni/check.py`
