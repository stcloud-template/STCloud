# Amazon EC2 launch templates should have IMDSv2 enabled and required.

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `ec2_launch_template_imdsv2_required` |
| 云平台 | AWS |
| 服务 | ec2 |
| 严重等级 | high |
| 类别 | Uncategorized |
| 检查类型 | Software and Configuration Checks/AWS Security Best Practices |
| 资源类型 | AwsEc2LaunchTemplate |
| 资源组 | compute |

## 描述

This control checks if Amazon EC2 launch templates are configured with IMDSv2 enabled and required. The control fails if IMDSv2 is not enabled or required in the launch template versions.

## 风险

Without IMDSv2 required, EC2 instances may be vulnerable to metadata service attacks, allowing unauthorized access to instance metadata, potentially leading to compromise of instance credentials or other sensitive data.

## 推荐措施

To ensure EC2 launch templates have IMDSv2 enabled and required, update the template to configure the Instance Metadata Service Version 2 as required.

- 推荐链接：[https://docs.aws.amazon.com/autoscaling/ec2/userguide/create-launch-template.html#change-metadata-options](https://docs.aws.amazon.com/autoscaling/ec2/userguide/create-launch-template.html#change-metadata-options)

## 修复步骤


### CLI

```text
aws ec2 modify-launch-template --launch-template-id <template-id> --version <version-number> --metadata-options HttpTokens=required
```

### Other

[https://docs.aws.amazon.com/securityhub/latest/userguide/ec2-controls.html#ec2-170](https://docs.aws.amazon.com/securityhub/latest/userguide/ec2-controls.html#ec2-170)

## 参考资料

- [https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/configuring-instance-metadata-service.html](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/configuring-instance-metadata-service.html)
- [https://docs.aws.amazon.com/autoscaling/ec2/userguide/create-launch-template.html#change-metadata-options](https://docs.aws.amazon.com/autoscaling/ec2/userguide/create-launch-template.html#change-metadata-options)

## 技术信息

- Source Metadata：[sources/aws/ec2_launch_template_imdsv2_required/metadata.json](../../sources/aws/ec2_launch_template_imdsv2_required/metadata.json)
- Source Code：[sources/aws/ec2_launch_template_imdsv2_required/check.py](../../sources/aws/ec2_launch_template_imdsv2_required/check.py)
- Source Metadata Path：`sources/aws/ec2_launch_template_imdsv2_required/metadata.json`
- Source Code Path：`sources/aws/ec2_launch_template_imdsv2_required/check.py`
