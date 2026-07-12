# Check for EC2 Instances with Public IP.

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `ec2_instance_public_ip` |
| クラウドプラットフォーム | AWS |
| サービス | ec2 |
| サブサービス | instance |
| 重大度 | medium |
| カテゴリ | internet-exposed |
| チェックタイプ | Infrastructure Security |
| リソースタイプ | AwsEc2Instance |
| リソースグループ | compute |

## 説明

Check for EC2 Instances with Public IP.

## リスク

Exposing an EC2 directly to internet increases the attack surface and therefore the risk of compromise.

## 推奨事項

Use an ALB and apply WAF ACL.

- 推奨リンク：[https://aws.amazon.com/blogs/aws/aws-web-application-firewall-waf-for-application-load-balancers/](https://aws.amazon.com/blogs/aws/aws-web-application-firewall-waf-for-application-load-balancers/)

## 修正手順


### Native IaC

[https://docs.ST Cloud.com/checks/aws/public-policies/public_12#cloudformation](https://docs.ST Cloud.com/checks/aws/public-policies/public_12#cloudformation)

### Terraform

[https://docs.ST Cloud.com/checks/aws/public-policies/public_12#terraform](https://docs.ST Cloud.com/checks/aws/public-policies/public_12#terraform)

### Other

[https://docs.ST Cloud.com/checks/aws/public-policies/public_12#aws-console](https://docs.ST Cloud.com/checks/aws/public-policies/public_12#aws-console)

## 参考資料

- [https://aws.amazon.com/blogs/aws/aws-web-application-firewall-waf-for-application-load-balancers/](https://aws.amazon.com/blogs/aws/aws-web-application-firewall-waf-for-application-load-balancers/)

## 技術情報

- Source Metadata：[sources/aws/ec2_instance_public_ip/metadata.json](../../sources/aws/ec2_instance_public_ip/metadata.json)
- Source Code：[sources/aws/ec2_instance_public_ip/check.py](../../sources/aws/ec2_instance_public_ip/check.py)
- Source Metadata Path：`sources/aws/ec2_instance_public_ip/metadata.json`
- Source Code Path：`sources/aws/ec2_instance_public_ip/check.py`
