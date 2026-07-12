# Ensure no Network ACLs allow ingress from 0.0.0.0/0 to any port.

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `ec2_networkacl_allow_ingress_any_port` |
| クラウドプラットフォーム | AWS |
| サービス | ec2 |
| サブサービス | networkacl |
| 重大度 | medium |
| カテゴリ | internet-exposed |
| チェックタイプ | Software and Configuration Checks, Industry and Regulatory Standards, CIS AWS Foundations Benchmark |
| リソースタイプ | AwsEc2NetworkAcl |
| リソースグループ | network |

## 説明

Ensure no Network ACLs allow ingress from 0.0.0.0/0 to any port.

## リスク

Even having a perimeter firewall, having network acls open allows any user or malware with vpc access to scan for well known and sensitive ports and gain access to instance.

## 推奨事項

Apply Zero Trust approach. Implement a process to scan and remediate unrestricted or overly permissive network acls. Recommended best practices is to narrow the definition for the minimum ports required.

- 推奨リンク：[https://docs.aws.amazon.com/vpc/latest/userguide/vpc-network-acls.html](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-network-acls.html)

## 修正手順

No remediation steps available.

## 参考資料

- [https://docs.aws.amazon.com/vpc/latest/userguide/vpc-network-acls.html](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-network-acls.html)

## 技術情報

- Source Metadata：[sources/aws/ec2_networkacl_allow_ingress_any_port/metadata.json](../../sources/aws/ec2_networkacl_allow_ingress_any_port/metadata.json)
- Source Code：[sources/aws/ec2_networkacl_allow_ingress_any_port/check.py](../../sources/aws/ec2_networkacl_allow_ingress_any_port/check.py)
- Source Metadata Path：`sources/aws/ec2_networkacl_allow_ingress_any_port/metadata.json`
- Source Code Path：`sources/aws/ec2_networkacl_allow_ingress_any_port/check.py`
