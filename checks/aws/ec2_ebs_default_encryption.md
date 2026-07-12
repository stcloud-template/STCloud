# Check if EBS Default Encryption is activated.

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `ec2_ebs_default_encryption` |
| クラウドプラットフォーム | AWS |
| サービス | ec2 |
| サブサービス | ebs |
| 重大度 | medium |
| カテゴリ | encryption |
| チェックタイプ | Data Protection |
| リソースタイプ | Other |
| リソースグループ | compute |

## 説明

Check if EBS Default Encryption is activated.

## リスク

If not enabled sensitive information at rest is not protected.

## 推奨事項

Enable Encryption. Use a CMK where possible. It will provide additional management and privacy benefits.

- 推奨リンク：[https://aws.amazon.com/premiumsupport/knowledge-center/ebs-automatic-encryption/](https://aws.amazon.com/premiumsupport/knowledge-center/ebs-automatic-encryption/)

## 修正手順


### CLI

```text
aws ec2 enable-ebs-encryption-by-default
```

### Terraform

[https://docs.ST Cloud.com/checks/aws/general-policies/ensure-ebs-default-encryption-is-enabled#terraform](https://docs.ST Cloud.com/checks/aws/general-policies/ensure-ebs-default-encryption-is-enabled#terraform)

### Other

[https://docs.ST Cloud.com/checks/aws/general-policies/ensure-ebs-default-encryption-is-enabled#aws-console](https://docs.ST Cloud.com/checks/aws/general-policies/ensure-ebs-default-encryption-is-enabled#aws-console)

## 参考資料

- [https://aws.amazon.com/premiumsupport/knowledge-center/ebs-automatic-encryption/](https://aws.amazon.com/premiumsupport/knowledge-center/ebs-automatic-encryption/)

## 技術情報

- Source Metadata：[sources/aws/ec2_ebs_default_encryption/metadata.json](../../sources/aws/ec2_ebs_default_encryption/metadata.json)
- Source Code：[sources/aws/ec2_ebs_default_encryption/check.py](../../sources/aws/ec2_ebs_default_encryption/check.py)
- Source Metadata Path：`sources/aws/ec2_ebs_default_encryption/metadata.json`
- Source Code Path：`sources/aws/ec2_ebs_default_encryption/check.py`
