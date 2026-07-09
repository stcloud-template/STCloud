# Ensure there are no EBS Volumes unencrypted.

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `ec2_ebs_volume_encryption` |
| 云平台 | AWS |
| 服务 | ec2 |
| 子服务 | volume |
| 严重等级 | medium |
| 类别 | encryption |
| 检查类型 | Data Protection |
| 资源类型 | AwsEc2Volume |
| 资源组 | storage |

## 描述

Ensure there are no EBS Volumes unencrypted.

## 风险

Data encryption at rest prevents data visibility in the event of its unauthorized access or theft.

## 推荐措施

Encrypt all EBS volumes and Enable Encryption by default You can configure your AWS account to enforce the encryption of the new EBS volumes and snapshot copies that you create. For example, Amazon EBS encrypts the EBS volumes created when you launch an instance and the snapshots that you copy from an unencrypted snapshot.

- 推荐链接：[https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EBSEncryption.html](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EBSEncryption.html)

## 修复步骤

No remediation steps available.

## 参考资料

- [https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EBSEncryption.html](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EBSEncryption.html)

## 技术信息

- Source Metadata：[sources/aws/ec2_ebs_volume_encryption/metadata.json](../../sources/aws/ec2_ebs_volume_encryption/metadata.json)
- Source Code：[sources/aws/ec2_ebs_volume_encryption/check.py](../../sources/aws/ec2_ebs_volume_encryption/check.py)
- Source Metadata Path：`sources/aws/ec2_ebs_volume_encryption/metadata.json`
- Source Code Path：`sources/aws/ec2_ebs_volume_encryption/check.py`
