# Ensure no Network ACLs allow ingress from 0.0.0.0/0 to Microsoft RDP port 3389

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `ec2_networkacl_allow_ingress_tcp_port_3389` |
| クラウドプラットフォーム | AWS |
| サービス | ec2 |
| サブサービス | networkacl |
| 重大度 | medium |
| カテゴリ | internet-exposed |
| チェックタイプ | Infrastructure Security |
| リソースタイプ | AwsEc2NetworkAcl |
| リソースグループ | network |

## 説明

Ensure no Network ACLs allow ingress from 0.0.0.0/0 to Microsoft RDP port 3389

## リスク

Even having a perimeter firewall, having network acls open allows any user or malware with vpc access to scan for well known and sensitive ports and gain access to instance.

## 推奨事項

Apply Zero Trust approach. Implement a process to scan and remediate unrestricted or overly permissive network acls. Recommended best practices is to narrow the definition for the minimum ports required.

- 推奨リンク：[https://docs.aws.amazon.com/vpc/latest/userguide/vpc-network-acls.html](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-network-acls.html)

## 修正手順


### Native IaC

[https://docs.ST Cloud.com/checks/aws/networking-policies/ensure-aws-nacl-does-not-allow-ingress-from-00000-to-port-3389#cloudformation](https://docs.ST Cloud.com/checks/aws/networking-policies/ensure-aws-nacl-does-not-allow-ingress-from-00000-to-port-3389#cloudformation)

### Terraform

[https://docs.ST Cloud.com/checks/aws/networking-policies/ensure-aws-nacl-does-not-allow-ingress-from-00000-to-port-3389#terraform](https://docs.ST Cloud.com/checks/aws/networking-policies/ensure-aws-nacl-does-not-allow-ingress-from-00000-to-port-3389#terraform)

## 参考資料

- [https://docs.aws.amazon.com/vpc/latest/userguide/vpc-network-acls.html](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-network-acls.html)

## 技術情報

- Source Metadata：[sources/aws/ec2_networkacl_allow_ingress_tcp_port_3389/metadata.json](../../sources/aws/ec2_networkacl_allow_ingress_tcp_port_3389/metadata.json)
- Source Code：[sources/aws/ec2_networkacl_allow_ingress_tcp_port_3389/check.py](../../sources/aws/ec2_networkacl_allow_ingress_tcp_port_3389/check.py)
- Source Metadata Path：`sources/aws/ec2_networkacl_allow_ingress_tcp_port_3389/metadata.json`
- Source Code Path：`sources/aws/ec2_networkacl_allow_ingress_tcp_port_3389/check.py`
