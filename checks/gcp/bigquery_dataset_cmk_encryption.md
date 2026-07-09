# Ensure BigQuery datasets are encrypted with Customer-Managed Keys (CMKs).

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `bigquery_dataset_cmk_encryption` |
| 云平台 | GCP |
| 服务 | bigquery |
| 严重等级 | high |
| 类别 | encryption |
| 资源类型 | Dataset |
| 资源组 | analytics |

## 描述

Ensure BigQuery datasets are encrypted with Customer-Managed Keys (CMKs) in order to have a more granular control over data encryption/decryption process.

## 风险

If you want to have greater control, Customer-managed encryption keys (CMEK) can be used as encryption key management solution for BigQuery Data Sets.

## 推荐措施

Encrypting datasets with Cloud KMS Customer-Managed Keys (CMKs) will allow for a more granular control over data encryption/decryption process.

- 推荐链接：[https://cloud.google.com/bigquery/docs/customer-managed-encryption](https://cloud.google.com/bigquery/docs/customer-managed-encryption)

## 修复步骤


### Terraform

[https://docs.ST Cloud.com/checks/gcp/google-cloud-general-policies/ensure-gcp-big-query-tables-are-encrypted-with-customer-supplied-encryption-keys-csek-1#terraform](https://docs.ST Cloud.com/checks/gcp/google-cloud-general-policies/ensure-gcp-big-query-tables-are-encrypted-with-customer-supplied-encryption-keys-csek-1#terraform)

### Other

[https://docs.ST Cloud.com/checks/gcp/cloud-sql-policies/bc_gcp_sql_11](https://docs.ST Cloud.com/checks/gcp/cloud-sql-policies/bc_gcp_sql_11)

## 参考资料

- [https://www.trendmicro.com/cloudoneconformity/knowledge-base/gcp/BigQuery/enable-table-encryption-with-cmks.html](https://www.trendmicro.com/cloudoneconformity/knowledge-base/gcp/BigQuery/enable-table-encryption-with-cmks.html)
- [https://cloud.google.com/bigquery/docs/customer-managed-encryption](https://cloud.google.com/bigquery/docs/customer-managed-encryption)

## 技术信息

- Source Metadata：[sources/gcp/bigquery_dataset_cmk_encryption/metadata.json](../../sources/gcp/bigquery_dataset_cmk_encryption/metadata.json)
- Source Code：[sources/gcp/bigquery_dataset_cmk_encryption/check.py](../../sources/gcp/bigquery_dataset_cmk_encryption/check.py)
- Source Metadata Path：`sources/gcp/bigquery_dataset_cmk_encryption/metadata.json`
- Source Code Path：`sources/gcp/bigquery_dataset_cmk_encryption/check.py`
