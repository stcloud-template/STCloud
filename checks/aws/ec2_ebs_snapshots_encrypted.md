# Check if EBS snapshots are encrypted.

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `ec2_ebs_snapshots_encrypted` |
| クラウドプラットフォーム | AWS |
| サービス | ec2 |
| サブサービス | snapshot |
| 重大度 | medium |
| カテゴリ | encryption |
| チェックタイプ | Data Protection |
| リソースタイプ | Other |
| リソースグループ | compute |

## 説明

Check if EBS snapshots are encrypted.

## リスク

Data encryption at rest prevents data visibility in the event of its unauthorized access or theft.

## 推奨事項

Encrypt all EBS Snapshot and Enable Encryption by default. You can configure your AWS account to enforce the encryption of the new EBS volumes and snapshot copies that you create. For example, Amazon EBS encrypts the EBS volumes created when you launch an instance and the snapshots that you copy from an unencrypted snapshot.

- 推奨リンク：[https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EBSEncryption.html#encryption-by-default](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EBSEncryption.html#encryption-by-default)

## 修正手順


### CLI

```text
aws ec2 --region <REGION> enable-ebs-encryption-by-default
```

### Native IaC

[https://docs.ST Cloud.com/checks/aws/general-policies/general_3-encrypt-ebs-volume#cloudformation](https://docs.ST Cloud.com/checks/aws/general-policies/general_3-encrypt-ebs-volume#cloudformation)

### Terraform

[https://docs.ST Cloud.com/checks/aws/general-policies/general_3-encrypt-ebs-volume#terraform](https://docs.ST Cloud.com/checks/aws/general-policies/general_3-encrypt-ebs-volume#terraform)

### Other

[https://docs.ST Cloud.com/checks/aws/general-policies/general_3-encrypt-ebs-volume#aws-console](https://docs.ST Cloud.com/checks/aws/general-policies/general_3-encrypt-ebs-volume#aws-console)

## 参考資料

- [https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EBSEncryption.html#encryption-by-default](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EBSEncryption.html#encryption-by-default)

## 技術情報

- Source Metadata：[sources/aws/ec2_ebs_snapshots_encrypted/metadata.json](../../sources/aws/ec2_ebs_snapshots_encrypted/metadata.json)
- Source Code：[sources/aws/ec2_ebs_snapshots_encrypted/check.py](../../sources/aws/ec2_ebs_snapshots_encrypted/check.py)
- Source Metadata Path：`sources/aws/ec2_ebs_snapshots_encrypted/metadata.json`
- Source Code Path：`sources/aws/ec2_ebs_snapshots_encrypted/check.py`
