# Check if EC2 instances are managed by Systems Manager.

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `ec2_instance_managed_by_ssm` |
| 云平台 | AWS |
| 服务 | ec2 |
| 子服务 | instance |
| 严重等级 | medium |
| 类别 | Uncategorized |
| 检查类型 | Infrastructure Security |
| 资源类型 | AwsEc2Instance |
| 资源组 | compute |

## 描述

Check if EC2 instances are managed by Systems Manager.

## 风险

AWS Config provides AWS Managed Rules, which are predefined, customizable rules that AWS Config uses to evaluate whether your AWS resource configurations comply with common best practices.

## 推荐措施

Verify and apply Systems Manager Prerequisites.

- 推荐链接：[https://docs.aws.amazon.com/systems-manager/latest/userguide/managed_instances.html](https://docs.aws.amazon.com/systems-manager/latest/userguide/managed_instances.html)

## 修复步骤


### Other

[https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/SSM/ssm-managed-instances.html](https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/SSM/ssm-managed-instances.html)

## 参考资料

- [https://docs.aws.amazon.com/systems-manager/latest/userguide/managed_instances.html](https://docs.aws.amazon.com/systems-manager/latest/userguide/managed_instances.html)

## 技术信息

- Source Metadata：[sources/aws/ec2_instance_managed_by_ssm/metadata.json](../../sources/aws/ec2_instance_managed_by_ssm/metadata.json)
- Source Code：[sources/aws/ec2_instance_managed_by_ssm/check.py](../../sources/aws/ec2_instance_managed_by_ssm/check.py)
- Source Metadata Path：`sources/aws/ec2_instance_managed_by_ssm/metadata.json`
- Source Code Path：`sources/aws/ec2_instance_managed_by_ssm/check.py`
