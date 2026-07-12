# Ensure there are no EBS Volumes unencrypted.

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `ec2_ebs_volume_encryption` |
| クラウドプラットフォーム | AWS |
| サービス | ec2 |
| サブサービス | volume |
| 重大度 | medium |
| カテゴリ | encryption |
| チェックタイプ | Data Protection |
| リソースタイプ | AwsEc2Volume |
| リソースグループ | storage |

## 説明

Ensure there are no EBS Volumes unencrypted.

## リスク

Data encryption at rest prevents data visibility in the event of its unauthorized access or theft.

## 推奨事項

Encrypt all EBS volumes and Enable Encryption by default You can configure your AWS account to enforce the encryption of the new EBS volumes and snapshot copies that you create. For example, Amazon EBS encrypts the EBS volumes created when you launch an instance and the snapshots that you copy from an unencrypted snapshot.

- 推奨リンク：[https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EBSEncryption.html](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EBSEncryption.html)

## 修正手順

No remediation steps available.

## 参考資料

- [https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EBSEncryption.html](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EBSEncryption.html)

## 技術情報

- Source Metadata：[sources/aws/ec2_ebs_volume_encryption/metadata.json](../../sources/aws/ec2_ebs_volume_encryption/metadata.json)
- Source Code：[sources/aws/ec2_ebs_volume_encryption/check.py](../../sources/aws/ec2_ebs_volume_encryption/check.py)
- Source Metadata Path：`sources/aws/ec2_ebs_volume_encryption/metadata.json`
- Source Code Path：`sources/aws/ec2_ebs_volume_encryption/check.py`
