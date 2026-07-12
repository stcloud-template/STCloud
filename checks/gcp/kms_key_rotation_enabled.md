# Ensure KMS keys are rotated within a period of 90 days

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `kms_key_rotation_enabled` |
| クラウドプラットフォーム | GCP |
| サービス | kms |
| 重大度 | low |
| カテゴリ | Uncategorized |
| リソースタイプ | CryptoKey |
| リソースグループ | security |

## 説明

Ensure KMS keys are rotated within a period of 90 days

## リスク

Ensure that all your Cloud Key Management Service (KMS) keys are rotated within a period of 90 days in order to meet security and compliance requirements

## 推奨事項

After a successful key rotation, the older key version is required in order to decrypt the data encrypted by that previous key version.

- 推奨リンク：[https://cloud.google.com/iam/docs/manage-access-service-accounts](https://cloud.google.com/iam/docs/manage-access-service-accounts)

## 修正手順


### CLI

```text
gcloud kms keys update new --keyring=<KEY_RING> --location=<LOCATION> --nextrotation-time=<NEXT_ROTATION_TIME> --rotation-period=<ROTATION_PERIOD>
```

### Terraform

[https://docs.ST Cloud.com/checks/gcp/google-cloud-general-policies/bc_gcp_general_4#terraform](https://docs.ST Cloud.com/checks/gcp/google-cloud-general-policies/bc_gcp_general_4#terraform)

### Other

[https://www.trendmicro.com/cloudoneconformity/knowledge-base/gcp/CloudKMS/rotate-kms-encryption-keys.html](https://www.trendmicro.com/cloudoneconformity/knowledge-base/gcp/CloudKMS/rotate-kms-encryption-keys.html)

## 参考資料

- [https://cloud.google.com/iam/docs/manage-access-service-accounts](https://cloud.google.com/iam/docs/manage-access-service-accounts)

## 技術情報

- Source Metadata：[sources/gcp/kms_key_rotation_enabled/metadata.json](../../sources/gcp/kms_key_rotation_enabled/metadata.json)
- Source Code：[sources/gcp/kms_key_rotation_enabled/check.py](../../sources/gcp/kms_key_rotation_enabled/check.py)
- Source Metadata Path：`sources/gcp/kms_key_rotation_enabled/metadata.json`
- Source Code Path：`sources/gcp/kms_key_rotation_enabled/check.py`
