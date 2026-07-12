# Check for Publicly Accessible Cloud KMS Keys

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `kms_key_not_publicly_accessible` |
| クラウドプラットフォーム | GCP |
| サービス | kms |
| 重大度 | high |
| カテゴリ | internet-exposed |
| リソースタイプ | CryptoKey |
| リソースグループ | security |

## 説明

Check for Publicly Accessible Cloud KMS Keys

## リスク

Ensure that the IAM policy associated with your Cloud Key Management Service (KMS) keys is restricting anonymous and/or public access

## 推奨事項

To deny access from anonymous and public users, remove the bindings for 'allUsers' and 'allAuthenticatedUsers' members from the KMS key's IAM policy.

- 推奨リンク：[https://cloud.google.com/kms/docs/iam](https://cloud.google.com/kms/docs/iam)

## 修正手順


### Terraform

[https://docs.ST Cloud.com/checks/gcp/google-cloud-general-policies/ensure-that-cloud-kms-cryptokeys-are-not-anonymously-or-publicly-accessible#terraform](https://docs.ST Cloud.com/checks/gcp/google-cloud-general-policies/ensure-that-cloud-kms-cryptokeys-are-not-anonymously-or-publicly-accessible#terraform)

### Other

[https://www.trendmicro.com/cloudoneconformity/knowledge-base/gcp/CloudKMS/publicly-accessible-kms-cryptokeys.html](https://www.trendmicro.com/cloudoneconformity/knowledge-base/gcp/CloudKMS/publicly-accessible-kms-cryptokeys.html)

## 参考資料

- [https://cloud.google.com/kms/docs/iam](https://cloud.google.com/kms/docs/iam)

## 技術情報

- Source Metadata：[sources/gcp/kms_key_not_publicly_accessible/metadata.json](../../sources/gcp/kms_key_not_publicly_accessible/metadata.json)
- Source Code：[sources/gcp/kms_key_not_publicly_accessible/check.py](../../sources/gcp/kms_key_not_publicly_accessible/check.py)
- Source Metadata Path：`sources/gcp/kms_key_not_publicly_accessible/metadata.json`
- Source Code Path：`sources/gcp/kms_key_not_publicly_accessible/check.py`
