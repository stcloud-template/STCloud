# Check for internet facing EC2 instances with Instance Profiles attached.

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `ec2_instance_internet_facing_with_instance_profile` |
| クラウドプラットフォーム | AWS |
| サービス | ec2 |
| 重大度 | medium |
| カテゴリ | internet-exposed |
| チェックタイプ | Infrastructure Security |
| リソースタイプ | AwsEc2Instance |
| リソースグループ | compute |

## 説明

Check for internet facing EC2 instances with Instance Profiles attached.

## リスク

Exposing an EC2 directly to internet increases the attack surface and therefore the risk of compromise.

## 推奨事項

Use an ALB and apply WAF ACL.

- 推奨リンク：[https://aws.amazon.com/blogs/aws/aws-web-application-firewall-waf-for-application-load-balancers/](https://aws.amazon.com/blogs/aws/aws-web-application-firewall-waf-for-application-load-balancers/)

## 修正手順

No remediation steps available.

## 参考資料

- [https://aws.amazon.com/blogs/aws/aws-web-application-firewall-waf-for-application-load-balancers/](https://aws.amazon.com/blogs/aws/aws-web-application-firewall-waf-for-application-load-balancers/)

## 技術情報

- Source Metadata：[sources/aws/ec2_instance_internet_facing_with_instance_profile/metadata.json](../../sources/aws/ec2_instance_internet_facing_with_instance_profile/metadata.json)
- Source Code：[sources/aws/ec2_instance_internet_facing_with_instance_profile/check.py](../../sources/aws/ec2_instance_internet_facing_with_instance_profile/check.py)
- Source Metadata Path：`sources/aws/ec2_instance_internet_facing_with_instance_profile/metadata.json`
- Source Code Path：`sources/aws/ec2_instance_internet_facing_with_instance_profile/check.py`
