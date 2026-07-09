# Check if EBS snapshots are encrypted.

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `ec2_ebs_snapshots_encrypted` |
| 云平台 | AWS |
| 服务 | ec2 |
| 子服务 | snapshot |
| 严重等级 | medium |
| 类别 | encryption |
| 检查类型 | Data Protection |
| 资源类型 | Other |
| 资源组 | compute |

## 描述

Check if EBS snapshots are encrypted.

## 风险

Data encryption at rest prevents data visibility in the event of its unauthorized access or theft.

## 推荐措施

Encrypt all EBS Snapshot and Enable Encryption by default. You can configure your AWS account to enforce the encryption of the new EBS volumes and snapshot copies that you create. For example, Amazon EBS encrypts the EBS volumes created when you launch an instance and the snapshots that you copy from an unencrypted snapshot.

- 推荐链接：[https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EBSEncryption.html#encryption-by-default](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EBSEncryption.html#encryption-by-default)

## 修复步骤


### CLI

```text
aws ec2 --region <REGION> enable-ebs-encryption-by-default
```

### Native IaC

[https://docs.ST Cloud.com/checks/aws/general-policies/general_3-encrypt-ebs-volume#cloudformation](https://docs.ST Cloud.com/checks/aws/general-policies/general_3-encrypt-ebs-volume#cloudformation)

### Terraform

[https://docs.ST Cloud.com/checks/aws/general-policies/general_3-encrypt-ebs-volume#terraform](https://docs.ST Cloud.com/checks/aws/general-policies/general_3-encrypt-ebs-volume#terraform)

### Other

[https://docs.ST Cloud.com/checks/aws/general-policies/general_3-encrypt-ebs-volume#aws-console](https://docs.ST Cloud.com/checks/aws/general-policies/general_3-encrypt-ebs-volume#aws-console)

## 参考资料

- [https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EBSEncryption.html#encryption-by-default](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EBSEncryption.html#encryption-by-default)

## 技术信息

- Source Metadata：[sources/aws/ec2_ebs_snapshots_encrypted/metadata.json](../../sources/aws/ec2_ebs_snapshots_encrypted/metadata.json)
- Source Code：[sources/aws/ec2_ebs_snapshots_encrypted/check.py](../../sources/aws/ec2_ebs_snapshots_encrypted/check.py)
- Source Metadata Path：`sources/aws/ec2_ebs_snapshots_encrypted/metadata.json`
- Source Code Path：`sources/aws/ec2_ebs_snapshots_encrypted/check.py`
