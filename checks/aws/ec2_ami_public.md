# Ensure there are no EC2 AMIs set as Public.

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `ec2_ami_public` |
| 云平台 | AWS |
| 服务 | ec2 |
| 子服务 | ami |
| 严重等级 | critical |
| 类别 | internet-exposed |
| 检查类型 | Infrastructure Security |
| 资源类型 | Other |
| 资源组 | compute |

## 描述

Ensure there are no EC2 AMIs set as Public.

## 风险

When your AMIs are publicly accessible, they are available in the Community AMIs where everyone with an AWS account can use them to launch EC2 instances. Your AMIs could contain snapshots of your applications (including their data), therefore exposing your snapshots in this manner is not advised.

## 推荐措施

We recommend your EC2 AMIs are not publicly accessible, or generally available in the Community AMIs.

- 推荐链接：[https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/cancel-sharing-an-AMI.html](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/cancel-sharing-an-AMI.html)

## 修复步骤


### CLI

```text
aws ec2 modify-image-attribute --region <REGION> --image-id <EC2_AMI_ID> --launch-permission {"Remove":[{"Group":"all"}]}
```

### Other

[https://docs.ST Cloud.com/checks/aws/public-policies/public_8](https://docs.ST Cloud.com/checks/aws/public-policies/public_8)

## 参考资料

- [https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/cancel-sharing-an-AMI.html](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/cancel-sharing-an-AMI.html)

## 技术信息

- Source Metadata：[sources/aws/ec2_ami_public/metadata.json](../../sources/aws/ec2_ami_public/metadata.json)
- Source Code：[sources/aws/ec2_ami_public/check.py](../../sources/aws/ec2_ami_public/check.py)
- Source Metadata Path：`sources/aws/ec2_ami_public/metadata.json`
- Source Code Path：`sources/aws/ec2_ami_public/check.py`
