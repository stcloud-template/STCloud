# Amazon EC2 paravirtual virtualization type should not be used.

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `ec2_instance_paravirtual_type` |
| クラウドプラットフォーム | AWS |
| サービス | ec2 |
| 重大度 | medium |
| カテゴリ | Uncategorized |
| リソースタイプ | AwsEc2Instance |
| リソースグループ | compute |

## 説明

Ensure that the virtualization type of an EC2 instance is not paravirtual. The control fails if the virtualizationType of the EC2 instance is set to paravirtual.

## リスク

Using paravirtual instances can limit performance and security benefits offered by hardware virtual machine (HVM) instances, such as improved CPU, network, and storage efficiency.

## 推奨事項

To update an EC2 instance to a new instance type, see Change the instance type in the Amazon EC2 User Guide.

- 推奨リンク：[https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instance-resize.html](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instance-resize.html)

## 修正手順


### Other

[https://docs.aws.amazon.com/securityhub/latest/userguide/ec2-controls.html#ec2-24](https://docs.aws.amazon.com/securityhub/latest/userguide/ec2-controls.html#ec2-24)

## 参考資料

- [https://docs.aws.amazon.com/config/latest/developerguide/ec2-paravirtual-instance-check.html](https://docs.aws.amazon.com/config/latest/developerguide/ec2-paravirtual-instance-check.html)
- [https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instance-resize.html](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instance-resize.html)

## 技術情報

- Source Metadata：[sources/aws/ec2_instance_paravirtual_type/metadata.json](../../sources/aws/ec2_instance_paravirtual_type/metadata.json)
- Source Code：[sources/aws/ec2_instance_paravirtual_type/check.py](../../sources/aws/ec2_instance_paravirtual_type/check.py)
- Source Metadata Path：`sources/aws/ec2_instance_paravirtual_type/metadata.json`
- Source Code Path：`sources/aws/ec2_instance_paravirtual_type/check.py`
