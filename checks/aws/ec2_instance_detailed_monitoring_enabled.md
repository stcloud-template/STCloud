# Check if EC2 instances have detailed monitoring enabled.

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `ec2_instance_detailed_monitoring_enabled` |
| 云平台 | AWS |
| 服务 | ec2 |
| 严重等级 | low |
| 类别 | Uncategorized |
| 检查类型 | Infrastructure Security |
| 资源类型 | AwsEc2Instance |
| 资源组 | compute |

## 描述

Check if EC2 instances have detailed monitoring enabled.

## 风险

Enabling detailed monitoring provides enhanced monitoring and granular insights into EC2 instance metrics. Not having detailed monitoring enabled may limit the ability to troubleshoot performance issues effectively.

## 推荐措施

Enable detailed monitoring for EC2 instances to gain better insights into performance metrics.

- 推荐链接：[https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-cloudwatch-new.html#enable-detailed-monitoring-instance](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-cloudwatch-new.html#enable-detailed-monitoring-instance)

## 修复步骤


### CLI

```text
aws ec2 monitor-instances --instance-ids <EC2_INSTANCE_ID>
```

### Terraform

[https://docs.ST Cloud.com/checks/aws/logging-policies/ensure-that-detailed-monitoring-is-enabled-for-ec2-instances#terraform](https://docs.ST Cloud.com/checks/aws/logging-policies/ensure-that-detailed-monitoring-is-enabled-for-ec2-instances#terraform)

### Other

[https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/EC2/instance-detailed-monitoring.html](https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/EC2/instance-detailed-monitoring.html)

## 参考资料

- [https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-cloudwatch-new.html](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-cloudwatch-new.html)
- [https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-cloudwatch-new.html#enable-detailed-monitoring-instance](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-cloudwatch-new.html#enable-detailed-monitoring-instance)

## 技术信息

- Source Metadata：[sources/aws/ec2_instance_detailed_monitoring_enabled/metadata.json](../../sources/aws/ec2_instance_detailed_monitoring_enabled/metadata.json)
- Source Code：[sources/aws/ec2_instance_detailed_monitoring_enabled/check.py](../../sources/aws/ec2_instance_detailed_monitoring_enabled/check.py)
- Source Metadata Path：`sources/aws/ec2_instance_detailed_monitoring_enabled/metadata.json`
- Source Code Path：`sources/aws/ec2_instance_detailed_monitoring_enabled/check.py`
