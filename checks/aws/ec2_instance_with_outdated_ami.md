# Check for EC2 Instances Using Outdated AMIs

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `ec2_instance_with_outdated_ami` |
| 云平台 | AWS |
| 服务 | ec2 |
| 严重等级 | high |
| 类别 | Uncategorized |
| 资源类型 | AwsEc2Instance |
| 资源组 | compute |

## 描述

This check identifies EC2 instances using outdated Amazon Machine Images (AMIs) by auditing instances to gather AMI IDs, comparing them against the latest available versions, verifying suppo and security update status, and checking for deprecation.

## 风险

Using outdated AMIs can expose EC2 instances to security vulnerabilities, lack of support, and missing critical updates, increasing the risk of exploitation.

## 推荐措施

Regularly update your EC2 instances to use the latest AMIs to ensure they receive the latest security patches and updates.

- 推荐链接：[https://repost.aws/knowledge-center/ec2-find-deprecated-ami](https://repost.aws/knowledge-center/ec2-find-deprecated-ami)

## 修复步骤


### CLI

```text
aws ec2 describe-images --image-ids <ami-id>
```

### Other

[https://repost.aws/knowledge-center/ec2-find-deprecated-ami](https://repost.aws/knowledge-center/ec2-find-deprecated-ami)

## 参考资料

- [https://repost.aws/knowledge-center/ec2-find-deprecated-ami](https://repost.aws/knowledge-center/ec2-find-deprecated-ami)

## 技术信息

- Source Metadata：[sources/aws/ec2_instance_with_outdated_ami/metadata.json](../../sources/aws/ec2_instance_with_outdated_ami/metadata.json)
- Source Code：[sources/aws/ec2_instance_with_outdated_ami/check.py](../../sources/aws/ec2_instance_with_outdated_ami/check.py)
- Source Metadata Path：`sources/aws/ec2_instance_with_outdated_ami/metadata.json`
- Source Code Path：`sources/aws/ec2_instance_with_outdated_ami/check.py`
