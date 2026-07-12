# Ensure the default security group of every VPC restricts all traffic.

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `ec2_securitygroup_default_restrict_traffic` |
| クラウドプラットフォーム | AWS |
| サービス | ec2 |
| サブサービス | securitygroup |
| 重大度 | high |
| カテゴリ | Uncategorized |
| チェックタイプ | Infrastructure Security |
| リソースタイプ | AwsEc2SecurityGroup |
| リソースグループ | network |

## 説明

Ensure the default security group of every VPC restricts all traffic.

## リスク

Even having a perimeter firewall, having security groups open allows any user or malware with vpc access to scan for well known and sensitive ports and gain access to instance.

## 推奨事項

Apply Zero Trust approach. Implement a process to scan and remediate unrestricted or overly permissive security groups. Recommended best practices is to narrow the definition for the minimum ports required.

- 推奨リンク：[https://docs.aws.amazon.com/eks/latest/userguide/sec-group-reqs.html](https://docs.aws.amazon.com/eks/latest/userguide/sec-group-reqs.html)

## 修正手順


### Terraform

[https://docs.ST Cloud.com/checks/aws/networking-policies/networking_4#terraform](https://docs.ST Cloud.com/checks/aws/networking-policies/networking_4#terraform)

### Other

[https://docs.ST Cloud.com/checks/aws/networking-policies/networking_4#aws-console](https://docs.ST Cloud.com/checks/aws/networking-policies/networking_4#aws-console)

## 参考資料

- [https://docs.aws.amazon.com/eks/latest/userguide/sec-group-reqs.html](https://docs.aws.amazon.com/eks/latest/userguide/sec-group-reqs.html)

## 技術情報

- Source Metadata：[sources/aws/ec2_securitygroup_default_restrict_traffic/metadata.json](../../sources/aws/ec2_securitygroup_default_restrict_traffic/metadata.json)
- Source Code：[sources/aws/ec2_securitygroup_default_restrict_traffic/check.py](../../sources/aws/ec2_securitygroup_default_restrict_traffic/check.py)
- Source Metadata Path：`sources/aws/ec2_securitygroup_default_restrict_traffic/metadata.json`
- Source Code Path：`sources/aws/ec2_securitygroup_default_restrict_traffic/check.py`
