# Ensure there are no Security Groups not being used.

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `ec2_securitygroup_not_used` |
| クラウドプラットフォーム | AWS |
| サービス | ec2 |
| サブサービス | securitygroup |
| 重大度 | low |
| カテゴリ | Uncategorized |
| チェックタイプ | Infrastructure Security |
| リソースタイプ | AwsEc2SecurityGroup |
| リソースグループ | network |

## 説明

Ensure there are no Security Groups not being used.

## リスク

Having clear definition and scope for Security Groups creates a better administration environment.

## 推奨事項

List all the security groups and then use the cli to check if they are attached to an instance.

- 推奨リンク：[https://aws.amazon.com/premiumsupport/knowledge-center/ec2-find-security-group-resources/](https://aws.amazon.com/premiumsupport/knowledge-center/ec2-find-security-group-resources/)

## 修正手順

No remediation steps available.

## 参考資料

- [https://aws.amazon.com/premiumsupport/knowledge-center/ec2-find-security-group-resources/](https://aws.amazon.com/premiumsupport/knowledge-center/ec2-find-security-group-resources/)

## 技術情報

- Source Metadata：[sources/aws/ec2_securitygroup_not_used/metadata.json](../../sources/aws/ec2_securitygroup_not_used/metadata.json)
- Source Code：[sources/aws/ec2_securitygroup_not_used/check.py](../../sources/aws/ec2_securitygroup_not_used/check.py)
- Source Metadata Path：`sources/aws/ec2_securitygroup_not_used/metadata.json`
- Source Code Path：`sources/aws/ec2_securitygroup_not_used/check.py`
