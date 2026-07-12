# Check if EC2 instances have detailed monitoring enabled.

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `ec2_instance_detailed_monitoring_enabled` |
| クラウドプラットフォーム | AWS |
| サービス | ec2 |
| 重大度 | low |
| カテゴリ | Uncategorized |
| チェックタイプ | Infrastructure Security |
| リソースタイプ | AwsEc2Instance |
| リソースグループ | compute |

## 説明

Check if EC2 instances have detailed monitoring enabled.

## リスク

Enabling detailed monitoring provides enhanced monitoring and granular insights into EC2 instance metrics. Not having detailed monitoring enabled may limit the ability to troubleshoot performance issues effectively.

## 推奨事項

Enable detailed monitoring for EC2 instances to gain better insights into performance metrics.

- 推奨リンク：[https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-cloudwatch-new.html#enable-detailed-monitoring-instance](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-cloudwatch-new.html#enable-detailed-monitoring-instance)

## 修正手順


### CLI

```text
aws ec2 monitor-instances --instance-ids <EC2_INSTANCE_ID>
```

### Terraform

[https://docs.ST Cloud.com/checks/aws/logging-policies/ensure-that-detailed-monitoring-is-enabled-for-ec2-instances#terraform](https://docs.ST Cloud.com/checks/aws/logging-policies/ensure-that-detailed-monitoring-is-enabled-for-ec2-instances#terraform)

### Other

[https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/EC2/instance-detailed-monitoring.html](https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/EC2/instance-detailed-monitoring.html)

## 参考資料

- [https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-cloudwatch-new.html](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-cloudwatch-new.html)
- [https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-cloudwatch-new.html#enable-detailed-monitoring-instance](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-cloudwatch-new.html#enable-detailed-monitoring-instance)

## 技術情報

- Source Metadata：[sources/aws/ec2_instance_detailed_monitoring_enabled/metadata.json](../../sources/aws/ec2_instance_detailed_monitoring_enabled/metadata.json)
- Source Code：[sources/aws/ec2_instance_detailed_monitoring_enabled/check.py](../../sources/aws/ec2_instance_detailed_monitoring_enabled/check.py)
- Source Metadata Path：`sources/aws/ec2_instance_detailed_monitoring_enabled/metadata.json`
- Source Code Path：`sources/aws/ec2_instance_detailed_monitoring_enabled/check.py`
