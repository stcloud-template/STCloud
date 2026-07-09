# Check if EBS Default Encryption is activated.

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `ec2_ebs_default_encryption` |
| 云平台 | AWS |
| 服务 | ec2 |
| 子服务 | ebs |
| 严重等级 | medium |
| 类别 | encryption |
| 检查类型 | Data Protection |
| 资源类型 | Other |
| 资源组 | compute |

## 描述

Check if EBS Default Encryption is activated.

## 风险

If not enabled sensitive information at rest is not protected.

## 推荐措施

Enable Encryption. Use a CMK where possible. It will provide additional management and privacy benefits.

- 推荐链接：[https://aws.amazon.com/premiumsupport/knowledge-center/ebs-automatic-encryption/](https://aws.amazon.com/premiumsupport/knowledge-center/ebs-automatic-encryption/)

## 修复步骤


### CLI

```text
aws ec2 enable-ebs-encryption-by-default
```

### Terraform

[https://docs.ST Cloud.com/checks/aws/general-policies/ensure-ebs-default-encryption-is-enabled#terraform](https://docs.ST Cloud.com/checks/aws/general-policies/ensure-ebs-default-encryption-is-enabled#terraform)

### Other

[https://docs.ST Cloud.com/checks/aws/general-policies/ensure-ebs-default-encryption-is-enabled#aws-console](https://docs.ST Cloud.com/checks/aws/general-policies/ensure-ebs-default-encryption-is-enabled#aws-console)

## 参考资料

- [https://aws.amazon.com/premiumsupport/knowledge-center/ebs-automatic-encryption/](https://aws.amazon.com/premiumsupport/knowledge-center/ebs-automatic-encryption/)

## 技术信息

- Source Metadata：[sources/aws/ec2_ebs_default_encryption/metadata.json](../../sources/aws/ec2_ebs_default_encryption/metadata.json)
- Source Code：[sources/aws/ec2_ebs_default_encryption/check.py](../../sources/aws/ec2_ebs_default_encryption/check.py)
- Source Metadata Path：`sources/aws/ec2_ebs_default_encryption/metadata.json`
- Source Code Path：`sources/aws/ec2_ebs_default_encryption/check.py`
