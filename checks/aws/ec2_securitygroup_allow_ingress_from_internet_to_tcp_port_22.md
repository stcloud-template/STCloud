# Ensure no security groups allow ingress from 0.0.0.0/0 or ::/0 to SSH port 22.

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `ec2_securitygroup_allow_ingress_from_internet_to_tcp_port_22` |
| クラウドプラットフォーム | AWS |
| サービス | ec2 |
| サブサービス | securitygroup |
| 重大度 | high |
| カテゴリ | internet-exposed |
| チェックタイプ | Infrastructure Security |
| リソースタイプ | AwsEc2SecurityGroup |
| リソースグループ | network |

## 説明

Ensure no security groups allow ingress from 0.0.0.0/0 or ::/0 to SSH port 22.

## リスク

If Security groups are not properly configured the attack surface is increased.

## 推奨事項

Use a Zero Trust approach. Narrow ingress traffic as much as possible. Consider north-south as well as east-west traffic.

- 推奨リンク：[https://docs.aws.amazon.com/vpc/latest/userguide/VPC_SecurityGroups.html](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_SecurityGroups.html)

## 修正手順


### CLI

```text
aws ec2 revoke-security-group-ingress --group-id <GROUP_ID> --protocol tcp --port 22 --cidr
```

### Native IaC

[https://docs.ST Cloud.com/checks/aws/networking-policies/networking_1-port-security#cloudformation](https://docs.ST Cloud.com/checks/aws/networking-policies/networking_1-port-security#cloudformation)

### Terraform

[https://docs.ST Cloud.com/checks/aws/networking-policies/networking_1-port-security#terraform](https://docs.ST Cloud.com/checks/aws/networking-policies/networking_1-port-security#terraform)

### Other

[https://docs.ST Cloud.com/checks/aws/networking-policies/networking_1-port-security](https://docs.ST Cloud.com/checks/aws/networking-policies/networking_1-port-security)

## 参考資料

- [https://docs.aws.amazon.com/vpc/latest/userguide/VPC_SecurityGroups.html](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_SecurityGroups.html)

## 技術情報

- Source Metadata：[sources/aws/ec2_securitygroup_allow_ingress_from_internet_to_tcp_port_22/metadata.json](../../sources/aws/ec2_securitygroup_allow_ingress_from_internet_to_tcp_port_22/metadata.json)
- Source Code：[sources/aws/ec2_securitygroup_allow_ingress_from_internet_to_tcp_port_22/check.py](../../sources/aws/ec2_securitygroup_allow_ingress_from_internet_to_tcp_port_22/check.py)
- Source Metadata Path：`sources/aws/ec2_securitygroup_allow_ingress_from_internet_to_tcp_port_22/metadata.json`
- Source Code Path：`sources/aws/ec2_securitygroup_allow_ingress_from_internet_to_tcp_port_22/check.py`
