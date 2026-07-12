# Check if EC2 Instance Metadata Service Version 2 (IMDSv2) is Enabled and Required.

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `ec2_instance_imdsv2_enabled` |
| クラウドプラットフォーム | AWS |
| サービス | ec2 |
| 重大度 | high |
| カテゴリ | ec2-imdsv1 |
| チェックタイプ | Infrastructure Security |
| リソースタイプ | AwsEc2Instance |
| リソースグループ | compute |

## 説明

Check if EC2 Instance Metadata Service Version 2 (IMDSv2) is Enabled and Required.

## リスク

Using IMDSv2 will protect from misconfiguration and SSRF vulnerabilities. IMDSv1 will not.

## 推奨事項

If you don't need IMDS you can turn it off. Using aws-cli you can force the instance to use only IMDSv2.

- 推奨リンク：[https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/configuring-instance-metadata-service.html#configuring-instance-metadata-options](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/configuring-instance-metadata-service.html#configuring-instance-metadata-options)

## 修正手順


### CLI

```text
aws ec2 modify-instance-metadata-options --instance-id <instance-id> --http-tokens required --http-endpoint enabled
```

### Native IaC

[https://docs.ST Cloud.com/checks/aws/general-policies/bc_aws_general_31#cloudformation](https://docs.ST Cloud.com/checks/aws/general-policies/bc_aws_general_31#cloudformation)

### Terraform

[https://docs.ST Cloud.com/checks/aws/general-policies/bc_aws_general_31#terraform](https://docs.ST Cloud.com/checks/aws/general-policies/bc_aws_general_31#terraform)

### Other

[https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/EC2/require-imds-v2.html](https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/EC2/require-imds-v2.html)

## 参考資料

- [https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/configuring-instance-metadata-service.html#configuring-instance-metadata-options](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/configuring-instance-metadata-service.html#configuring-instance-metadata-options)

## 技術情報

- Source Metadata：[sources/aws/ec2_instance_imdsv2_enabled/metadata.json](../../sources/aws/ec2_instance_imdsv2_enabled/metadata.json)
- Source Code：[sources/aws/ec2_instance_imdsv2_enabled/check.py](../../sources/aws/ec2_instance_imdsv2_enabled/check.py)
- Source Metadata Path：`sources/aws/ec2_instance_imdsv2_enabled/metadata.json`
- Source Code Path：`sources/aws/ec2_instance_imdsv2_enabled/check.py`
