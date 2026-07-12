# Amazon EC2 launch templates should not assign public IPs to network interfaces.

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `ec2_launch_template_no_public_ip` |
| クラウドプラットフォーム | AWS |
| サービス | ec2 |
| 重大度 | high |
| カテゴリ | Uncategorized |
| リソースタイプ | AwsEc2LaunchTemplate |
| リソースグループ | compute |

## 説明

This control checks if Amazon EC2 launch templates are configured to assign public IP addresses to network interfaces upon launch. The control fails if an EC2 launch template is configured to assign a public IP address to network interfaces or if there is at least one network interface that has a public IP address.

## リスク

A public IP address is reachable from the internet, making associated resources potentially accessible from the internet. EC2 resources should not be publicly accessible to avoid unintended access to workloads.

## 推奨事項

To update an EC2 launch template, see Change the default network interface settings in the Amazon EC2 Auto Scaling User Guide.

- 推奨リンク：[https://docs.aws.amazon.com/autoscaling/ec2/userguide/create-launch-template.html#change-network-interface](https://docs.aws.amazon.com/autoscaling/ec2/userguide/create-launch-template.html#change-network-interface)

## 修正手順


### Other

[https://docs.aws.amazon.com/securityhub/latest/userguide/ec2-controls.html#ec2-25](https://docs.aws.amazon.com/securityhub/latest/userguide/ec2-controls.html#ec2-25)

## 参考資料

- [https://docs.aws.amazon.com/config/latest/developerguide/ec2-launch-template-public-ip-disabled.html](https://docs.aws.amazon.com/config/latest/developerguide/ec2-launch-template-public-ip-disabled.html)
- [https://docs.aws.amazon.com/autoscaling/ec2/userguide/create-launch-template.html#change-network-interface](https://docs.aws.amazon.com/autoscaling/ec2/userguide/create-launch-template.html#change-network-interface)

## 技術情報

- Source Metadata：[sources/aws/ec2_launch_template_no_public_ip/metadata.json](../../sources/aws/ec2_launch_template_no_public_ip/metadata.json)
- Source Code：[sources/aws/ec2_launch_template_no_public_ip/check.py](../../sources/aws/ec2_launch_template_no_public_ip/check.py)
- Source Metadata Path：`sources/aws/ec2_launch_template_no_public_ip/metadata.json`
- Source Code Path：`sources/aws/ec2_launch_template_no_public_ip/check.py`
