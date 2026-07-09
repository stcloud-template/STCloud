# Amazon EC2 launch templates should not assign public IPs to network interfaces.

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `ec2_launch_template_no_public_ip` |
| 云平台 | AWS |
| 服务 | ec2 |
| 严重等级 | high |
| 类别 | Uncategorized |
| 资源类型 | AwsEc2LaunchTemplate |
| 资源组 | compute |

## 描述

This control checks if Amazon EC2 launch templates are configured to assign public IP addresses to network interfaces upon launch. The control fails if an EC2 launch template is configured to assign a public IP address to network interfaces or if there is at least one network interface that has a public IP address.

## 风险

A public IP address is reachable from the internet, making associated resources potentially accessible from the internet. EC2 resources should not be publicly accessible to avoid unintended access to workloads.

## 推荐措施

To update an EC2 launch template, see Change the default network interface settings in the Amazon EC2 Auto Scaling User Guide.

- 推荐链接：[https://docs.aws.amazon.com/autoscaling/ec2/userguide/create-launch-template.html#change-network-interface](https://docs.aws.amazon.com/autoscaling/ec2/userguide/create-launch-template.html#change-network-interface)

## 修复步骤


### Other

[https://docs.aws.amazon.com/securityhub/latest/userguide/ec2-controls.html#ec2-25](https://docs.aws.amazon.com/securityhub/latest/userguide/ec2-controls.html#ec2-25)

## 参考资料

- [https://docs.aws.amazon.com/config/latest/developerguide/ec2-launch-template-public-ip-disabled.html](https://docs.aws.amazon.com/config/latest/developerguide/ec2-launch-template-public-ip-disabled.html)
- [https://docs.aws.amazon.com/autoscaling/ec2/userguide/create-launch-template.html#change-network-interface](https://docs.aws.amazon.com/autoscaling/ec2/userguide/create-launch-template.html#change-network-interface)

## 技术信息

- Source Metadata：[sources/aws/ec2_launch_template_no_public_ip/metadata.json](../../sources/aws/ec2_launch_template_no_public_ip/metadata.json)
- Source Code：[sources/aws/ec2_launch_template_no_public_ip/check.py](../../sources/aws/ec2_launch_template_no_public_ip/check.py)
- Source Metadata Path：`sources/aws/ec2_launch_template_no_public_ip/metadata.json`
- Source Code Path：`sources/aws/ec2_launch_template_no_public_ip/check.py`
