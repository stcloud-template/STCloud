# Ensure BigQuery datasets are encrypted with Customer-Managed Keys (CMKs).

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `bigquery_dataset_cmk_encryption` |
| クラウドプラットフォーム | GCP |
| サービス | bigquery |
| 重大度 | high |
| カテゴリ | encryption |
| リソースタイプ | Dataset |
| リソースグループ | analytics |

## 説明

Ensure BigQuery datasets are encrypted with Customer-Managed Keys (CMKs) in order to have a more granular control over data encryption/decryption process.

## リスク

If you want to have greater control, Customer-managed encryption keys (CMEK) can be used as encryption key management solution for BigQuery Data Sets.

## 推奨事項

Encrypting datasets with Cloud KMS Customer-Managed Keys (CMKs) will allow for a more granular control over data encryption/decryption process.

- 推奨リンク：[https://cloud.google.com/bigquery/docs/customer-managed-encryption](https://cloud.google.com/bigquery/docs/customer-managed-encryption)

## 修正手順


### Terraform

[https://docs.ST Cloud.com/checks/gcp/google-cloud-general-policies/ensure-gcp-big-query-tables-are-encrypted-with-customer-supplied-encryption-keys-csek-1#terraform](https://docs.ST Cloud.com/checks/gcp/google-cloud-general-policies/ensure-gcp-big-query-tables-are-encrypted-with-customer-supplied-encryption-keys-csek-1#terraform)

### Other

[https://docs.ST Cloud.com/checks/gcp/cloud-sql-policies/bc_gcp_sql_11](https://docs.ST Cloud.com/checks/gcp/cloud-sql-policies/bc_gcp_sql_11)

## 参考資料

- [https://www.trendmicro.com/cloudoneconformity/knowledge-base/gcp/BigQuery/enable-table-encryption-with-cmks.html](https://www.trendmicro.com/cloudoneconformity/knowledge-base/gcp/BigQuery/enable-table-encryption-with-cmks.html)
- [https://cloud.google.com/bigquery/docs/customer-managed-encryption](https://cloud.google.com/bigquery/docs/customer-managed-encryption)

## 技術情報

- Source Metadata：[sources/gcp/bigquery_dataset_cmk_encryption/metadata.json](../../sources/gcp/bigquery_dataset_cmk_encryption/metadata.json)
- Source Code：[sources/gcp/bigquery_dataset_cmk_encryption/check.py](../../sources/gcp/bigquery_dataset_cmk_encryption/check.py)
- Source Metadata Path：`sources/gcp/bigquery_dataset_cmk_encryption/metadata.json`
- Source Code Path：`sources/gcp/bigquery_dataset_cmk_encryption/check.py`
