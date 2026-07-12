# Amazon EC2 launch templates should have IMDSv2 enabled and required.

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `ec2_launch_template_imdsv2_required` |
| クラウドプラットフォーム | AWS |
| サービス | ec2 |
| 重大度 | high |
| カテゴリ | Uncategorized |
| チェックタイプ | Software and Configuration Checks/AWS Security Best Practices |
| リソースタイプ | AwsEc2LaunchTemplate |
| リソースグループ | compute |

## 説明

This control checks if Amazon EC2 launch templates are configured with IMDSv2 enabled and required. The control fails if IMDSv2 is not enabled or required in the launch template versions.

## リスク

Without IMDSv2 required, EC2 instances may be vulnerable to metadata service attacks, allowing unauthorized access to instance metadata, potentially leading to compromise of instance credentials or other sensitive data.

## 推奨事項

To ensure EC2 launch templates have IMDSv2 enabled and required, update the template to configure the Instance Metadata Service Version 2 as required.

- 推奨リンク：[https://docs.aws.amazon.com/autoscaling/ec2/userguide/create-launch-template.html#change-metadata-options](https://docs.aws.amazon.com/autoscaling/ec2/userguide/create-launch-template.html#change-metadata-options)

## 修正手順


### CLI

```text
aws ec2 modify-launch-template --launch-template-id <template-id> --version <version-number> --metadata-options HttpTokens=required
```

### Other

[https://docs.aws.amazon.com/securityhub/latest/userguide/ec2-controls.html#ec2-170](https://docs.aws.amazon.com/securityhub/latest/userguide/ec2-controls.html#ec2-170)

## 参考資料

- [https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/configuring-instance-metadata-service.html](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/configuring-instance-metadata-service.html)
- [https://docs.aws.amazon.com/autoscaling/ec2/userguide/create-launch-template.html#change-metadata-options](https://docs.aws.amazon.com/autoscaling/ec2/userguide/create-launch-template.html#change-metadata-options)

## 技術情報

- Source Metadata：[sources/aws/ec2_launch_template_imdsv2_required/metadata.json](../../sources/aws/ec2_launch_template_imdsv2_required/metadata.json)
- Source Code：[sources/aws/ec2_launch_template_imdsv2_required/check.py](../../sources/aws/ec2_launch_template_imdsv2_required/check.py)
- Source Metadata Path：`sources/aws/ec2_launch_template_imdsv2_required/metadata.json`
- Source Code Path：`sources/aws/ec2_launch_template_imdsv2_required/check.py`
