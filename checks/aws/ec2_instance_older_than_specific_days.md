# Check EC2 Instances older than specific days.

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `ec2_instance_older_than_specific_days` |
| 云平台 | AWS |
| 服务 | ec2 |
| 严重等级 | medium |
| 类别 | Uncategorized |
| 检查类型 | Infrastructure Security |
| 资源类型 | AwsEc2Instance |
| 资源组 | compute |

## 描述

Check EC2 Instances older than specific days.

## 风险

Having old instances within your AWS account could increase the risk of having vulnerable software.

## 推荐措施

Check if software running in the instance is up to date and patched accordingly. Use AWS Systems Manager to patch instances and view patching compliance information.

- 推荐链接：[https://docs.aws.amazon.com/systems-manager/latest/userguide/viewing-patch-compliance-results.html](https://docs.aws.amazon.com/systems-manager/latest/userguide/viewing-patch-compliance-results.html)

## 修复步骤


### Other

[https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/EC2/ec2-instance-too-old.html](https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/EC2/ec2-instance-too-old.html)

## 参考资料

- [https://docs.aws.amazon.com/systems-manager/latest/userguide/viewing-patch-compliance-results.html](https://docs.aws.amazon.com/systems-manager/latest/userguide/viewing-patch-compliance-results.html)

## 技术信息

- Source Metadata：[sources/aws/ec2_instance_older_than_specific_days/metadata.json](../../sources/aws/ec2_instance_older_than_specific_days/metadata.json)
- Source Code：[sources/aws/ec2_instance_older_than_specific_days/check.py](../../sources/aws/ec2_instance_older_than_specific_days/check.py)
- Source Metadata Path：`sources/aws/ec2_instance_older_than_specific_days/metadata.json`
- Source Code Path：`sources/aws/ec2_instance_older_than_specific_days/check.py`
