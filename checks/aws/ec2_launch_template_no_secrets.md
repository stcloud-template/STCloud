# Find secrets in EC2 Launch Template

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `ec2_launch_template_no_secrets` |
| 云平台 | AWS |
| 服务 | ec2 |
| 严重等级 | critical |
| 类别 | secrets |
| 资源类型 | AwsEc2LaunchTemplate |
| 资源组 | compute |

## 描述

Find secrets in EC2 Launch Template

## 风险

The use of a hard-coded password increases the possibility of password guessing. If hard-coded passwords are used, it is possible that malicious users gain access through the account in question.

## 推荐措施

Do not include sensitive information in user data within the launch templates, try to use Secrets Manager instead.

- 推荐链接：[https://docs.aws.amazon.com/secretsmanager/latest/userguide/intro.html](https://docs.aws.amazon.com/secretsmanager/latest/userguide/intro.html)

## 修复步骤

No remediation steps available.

## 参考资料

- [https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-launch-templates.html](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-launch-templates.html)
- [https://docs.aws.amazon.com/secretsmanager/latest/userguide/intro.html](https://docs.aws.amazon.com/secretsmanager/latest/userguide/intro.html)

## 技术信息

- Source Metadata：[sources/aws/ec2_launch_template_no_secrets/metadata.json](../../sources/aws/ec2_launch_template_no_secrets/metadata.json)
- Source Code：[sources/aws/ec2_launch_template_no_secrets/check.py](../../sources/aws/ec2_launch_template_no_secrets/check.py)
- Source Metadata Path：`sources/aws/ec2_launch_template_no_secrets/metadata.json`
- Source Code Path：`sources/aws/ec2_launch_template_no_secrets/check.py`
