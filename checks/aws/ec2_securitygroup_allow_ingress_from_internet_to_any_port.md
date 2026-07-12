# Ensure no security groups allow ingress from 0.0.0.0/0 or ::/0 to any port.

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `ec2_securitygroup_allow_ingress_from_internet_to_any_port` |
| クラウドプラットフォーム | AWS |
| サービス | ec2 |
| サブサービス | securitygroup |
| 重大度 | high |
| カテゴリ | internet-exposed |
| チェックタイプ | Infrastructure Security |
| リソースタイプ | AwsEc2SecurityGroup |
| リソースグループ | network |

## 説明

Ensure no security groups allow ingress from 0.0.0.0/0 or ::/0 to any port and not attached to a network interface with not allowed network interface types or instance owners. By default, the allowed network interface types are 'api_gateway_managed' and 'vpc_endpoint', and the allowed instance owners are 'amazon-elb', you can customize these values by setting the 'ec2_allowed_interface_types' and 'ec2_allowed_instance_owners' variables.

## リスク

The security group allows all traffic from the internet to any port. This could allow an attacker to access the instance.

## 推奨事項

Use a Zero Trust approach. Narrow ingress traffic as much as possible. Consider north-south as well as east-west traffic.

- 推奨リンク：[https://docs.aws.amazon.com/vpc/latest/userguide/VPC_SecurityGroups.html](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_SecurityGroups.html)

## 修正手順

No remediation steps available.

## 参考資料

- [https://docs.aws.amazon.com/vpc/latest/userguide/VPC_SecurityGroups.html](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_SecurityGroups.html)

## 技術情報

- Source Metadata：[sources/aws/ec2_securitygroup_allow_ingress_from_internet_to_any_port/metadata.json](../../sources/aws/ec2_securitygroup_allow_ingress_from_internet_to_any_port/metadata.json)
- Source Code：[sources/aws/ec2_securitygroup_allow_ingress_from_internet_to_any_port/check.py](../../sources/aws/ec2_securitygroup_allow_ingress_from_internet_to_any_port/check.py)
- Source Metadata Path：`sources/aws/ec2_securitygroup_allow_ingress_from_internet_to_any_port/metadata.json`
- Source Code Path：`sources/aws/ec2_securitygroup_allow_ingress_from_internet_to_any_port/check.py`
