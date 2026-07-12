# Ensure that Dataproc Cluster is encrypted using Customer-Managed Encryption Key

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `dataproc_encrypted_with_cmks_disabled` |
| クラウドプラットフォーム | GCP |
| サービス | dataproc |
| 重大度 | high |
| カテゴリ | encryption, gen-ai |
| リソースタイプ | Cluster |
| リソースグループ | container |

## 説明

When you use Dataproc, cluster and job data is stored on Persistent Disks (PDs) associated with the Compute Engine VMs in your cluster and in a Cloud Storage staging bucket. This PD and bucket data is encrypted using a Google-generated data encryption key (DEK) and key encryption key (KEK). The CMEK feature allows you to create, use, and revoke the key encryption key (KEK). Google still controls the data encryption key (DEK).

## リスク

The Dataproc cluster data is encrypted using a Google-generated Data Encryption Key (DEK) and a Key Encryption Key (KEK). If you need to control and manage your cluster data encryption yourself, you can use your own Customer-Managed Keys (CMKs). Cloud KMS Customer-Managed Keys can be implemented as an additional security layer on top of existing data encryption, and are often used in the enterprise world, where compliance and security controls are very strict.

## 推奨事項

Ensure that your Google Cloud Dataproc clusters on Compute Engine are encrypted with Customer-Managed Keys (CMKs) in order to control the cluster data encryption/decryption process. You can create and manage your own Customer-Managed Keys (CMKs) with Cloud Key Management Service (Cloud KMS). Cloud KMS provides secure and efficient encryption key management, controlled key rotation, and revocation mechanisms.

- 推奨リンク：[https://cloud.google.com/dataproc/docs/concepts/configuring-clusters/customer-managed-encryption](https://cloud.google.com/dataproc/docs/concepts/configuring-clusters/customer-managed-encryption)

## 修正手順


### Terraform

[https://docs.ST Cloud.com/checks/gcp/google-cloud-general-policies/ensure-gcp-dataproc-cluster-is-encrypted-with-customer-supplied-encryption-keys-cseks#terraform](https://docs.ST Cloud.com/checks/gcp/google-cloud-general-policies/ensure-gcp-dataproc-cluster-is-encrypted-with-customer-supplied-encryption-keys-cseks#terraform)

### Other

[https://www.trendmicro.com/cloudoneconformity/knowledge-base/gcp/Dataproc/enable-encryption-with-cmks-for-dataproc-clusters.html](https://www.trendmicro.com/cloudoneconformity/knowledge-base/gcp/Dataproc/enable-encryption-with-cmks-for-dataproc-clusters.html)

## 参考資料

- [https://cloud.google.com/dataproc/docs/concepts/configuring-clusters/customer-managed-encryption](https://cloud.google.com/dataproc/docs/concepts/configuring-clusters/customer-managed-encryption)

## 技術情報

- Source Metadata：[sources/gcp/dataproc_encrypted_with_cmks_disabled/metadata.json](../../sources/gcp/dataproc_encrypted_with_cmks_disabled/metadata.json)
- Source Code：[sources/gcp/dataproc_encrypted_with_cmks_disabled/check.py](../../sources/gcp/dataproc_encrypted_with_cmks_disabled/check.py)
- Source Metadata Path：`sources/gcp/dataproc_encrypted_with_cmks_disabled/metadata.json`
- Source Code Path：`sources/gcp/dataproc_encrypted_with_cmks_disabled/check.py`
