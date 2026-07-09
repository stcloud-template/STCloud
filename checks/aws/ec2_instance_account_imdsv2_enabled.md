# Ensure Instance Metadata Service Version 2 (IMDSv2) is enforced for EC2 instances at the account level to protect against SSRF vulnerabilities.

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `ec2_instance_account_imdsv2_enabled` |
| 云平台 | AWS |
| 服务 | ec2 |
| 严重等级 | high |
| 类别 | internet-exposed, ec2-imdsv1 |
| 检查类型 | Data Protection |
| 资源类型 | AwsAccount |
| 资源组 | governance |

## 描述

Ensure Instance Metadata Service Version 2 (IMDSv2) is enforced for EC2 instances at the account level to protect against SSRF vulnerabilities.

## 风险

EC2 instances that use IMDSv1 are vulnerable to SSRF attacks.

## 推荐措施

Enable Instance Metadata Service Version 2 (IMDSv2) on the EC2 instances. Apply this configuration at the account level for each AWS Region to set the default instance metadata version.

- 推荐链接：[https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/configuring-IMDS-new-instances.html#set-imdsv2-account-defaults](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/configuring-IMDS-new-instances.html#set-imdsv2-account-defaults)

## 修复步骤


### CLI

```text
aws ec2 modify-instance-metadata-defaults --region <region> --http-tokens required --http-put-response-hop-limit 2
```

## 参考资料

- [https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/configuring-IMDS-new-instances.html#set-imdsv2-account-defaults](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/configuring-IMDS-new-instances.html#set-imdsv2-account-defaults)

## 技术信息

- Source Metadata：[sources/aws/ec2_instance_account_imdsv2_enabled/metadata.json](../../sources/aws/ec2_instance_account_imdsv2_enabled/metadata.json)
- Source Code：[sources/aws/ec2_instance_account_imdsv2_enabled/check.py](../../sources/aws/ec2_instance_account_imdsv2_enabled/check.py)
- Source Metadata Path：`sources/aws/ec2_instance_account_imdsv2_enabled/metadata.json`
- Source Code Path：`sources/aws/ec2_instance_account_imdsv2_enabled/check.py`
