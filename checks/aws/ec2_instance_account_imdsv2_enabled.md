# Ensure Instance Metadata Service Version 2 (IMDSv2) is enforced for EC2 instances at the account level to protect against SSRF vulnerabilities.

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `ec2_instance_account_imdsv2_enabled` |
| クラウドプラットフォーム | AWS |
| サービス | ec2 |
| 重大度 | high |
| カテゴリ | internet-exposed, ec2-imdsv1 |
| チェックタイプ | Data Protection |
| リソースタイプ | AwsAccount |
| リソースグループ | governance |

## 説明

Ensure Instance Metadata Service Version 2 (IMDSv2) is enforced for EC2 instances at the account level to protect against SSRF vulnerabilities.

## リスク

EC2 instances that use IMDSv1 are vulnerable to SSRF attacks.

## 推奨事項

Enable Instance Metadata Service Version 2 (IMDSv2) on the EC2 instances. Apply this configuration at the account level for each AWS Region to set the default instance metadata version.

- 推奨リンク：[https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/configuring-IMDS-new-instances.html#set-imdsv2-account-defaults](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/configuring-IMDS-new-instances.html#set-imdsv2-account-defaults)

## 修正手順


### CLI

```text
aws ec2 modify-instance-metadata-defaults --region <region> --http-tokens required --http-put-response-hop-limit 2
```

## 参考資料

- [https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/configuring-IMDS-new-instances.html#set-imdsv2-account-defaults](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/configuring-IMDS-new-instances.html#set-imdsv2-account-defaults)

## 技術情報

- Source Metadata：[sources/aws/ec2_instance_account_imdsv2_enabled/metadata.json](../../sources/aws/ec2_instance_account_imdsv2_enabled/metadata.json)
- Source Code：[sources/aws/ec2_instance_account_imdsv2_enabled/check.py](../../sources/aws/ec2_instance_account_imdsv2_enabled/check.py)
- Source Metadata Path：`sources/aws/ec2_instance_account_imdsv2_enabled/metadata.json`
- Source Code Path：`sources/aws/ec2_instance_account_imdsv2_enabled/check.py`
