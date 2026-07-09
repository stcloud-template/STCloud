# Check if EC2 Instance Metadata Service Version 2 (IMDSv2) is Enabled and Required.

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `ec2_instance_imdsv2_enabled` |
| 云平台 | AWS |
| 服务 | ec2 |
| 严重等级 | high |
| 类别 | ec2-imdsv1 |
| 检查类型 | Infrastructure Security |
| 资源类型 | AwsEc2Instance |
| 资源组 | compute |

## 描述

Check if EC2 Instance Metadata Service Version 2 (IMDSv2) is Enabled and Required.

## 风险

Using IMDSv2 will protect from misconfiguration and SSRF vulnerabilities. IMDSv1 will not.

## 推荐措施

If you don't need IMDS you can turn it off. Using aws-cli you can force the instance to use only IMDSv2.

- 推荐链接：[https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/configuring-instance-metadata-service.html#configuring-instance-metadata-options](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/configuring-instance-metadata-service.html#configuring-instance-metadata-options)

## 修复步骤


### CLI

```text
aws ec2 modify-instance-metadata-options --instance-id <instance-id> --http-tokens required --http-endpoint enabled
```

### Native IaC

[https://docs.ST Cloud.com/checks/aws/general-policies/bc_aws_general_31#cloudformation](https://docs.ST Cloud.com/checks/aws/general-policies/bc_aws_general_31#cloudformation)

### Terraform

[https://docs.ST Cloud.com/checks/aws/general-policies/bc_aws_general_31#terraform](https://docs.ST Cloud.com/checks/aws/general-policies/bc_aws_general_31#terraform)

### Other

[https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/EC2/require-imds-v2.html](https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/EC2/require-imds-v2.html)

## 参考资料

- [https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/configuring-instance-metadata-service.html#configuring-instance-metadata-options](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/configuring-instance-metadata-service.html#configuring-instance-metadata-options)

## 技术信息

- Source Metadata：[sources/aws/ec2_instance_imdsv2_enabled/metadata.json](../../sources/aws/ec2_instance_imdsv2_enabled/metadata.json)
- Source Code：[sources/aws/ec2_instance_imdsv2_enabled/check.py](../../sources/aws/ec2_instance_imdsv2_enabled/check.py)
- Source Metadata Path：`sources/aws/ec2_instance_imdsv2_enabled/metadata.json`
- Source Code Path：`sources/aws/ec2_instance_imdsv2_enabled/check.py`
