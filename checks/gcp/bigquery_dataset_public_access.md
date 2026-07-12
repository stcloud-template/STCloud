# Ensure That BigQuery Datasets Are Not Anonymously or Publicly Accessible.

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `bigquery_dataset_public_access` |
| クラウドプラットフォーム | GCP |
| サービス | bigquery |
| 重大度 | high |
| カテゴリ | Uncategorized |
| リソースタイプ | Dataset |
| リソースグループ | analytics |

## 説明

Ensure That BigQuery Datasets Are Not Anonymously or Publicly Accessible.

## リスク

Granting permissions to allUsers or allAuthenticatedUsers allows anyone to access the dataset. Such access might not be desirable if sensitive data is being stored in the dataset. Therefore, ensure that anonymous and/or public access to a dataset is not allowed.

## 推奨事項

It is recommended that the IAM policy on BigQuery datasets does not allow anonymous and/or public access.

- 推奨リンク：[https://cloud.google.com/bigquery/docs/customer-managed-encryption](https://cloud.google.com/bigquery/docs/customer-managed-encryption)

## 修正手順


### Terraform

[https://docs.ST Cloud.com/checks/gcp/google-cloud-general-policies/bc_gcp_general_3#terraform](https://docs.ST Cloud.com/checks/gcp/google-cloud-general-policies/bc_gcp_general_3#terraform)

### Other

[https://www.trendmicro.com/cloudoneconformity/knowledge-base/gcp/BigQuery/publicly-accessible-big-query-datasets.html](https://www.trendmicro.com/cloudoneconformity/knowledge-base/gcp/BigQuery/publicly-accessible-big-query-datasets.html)

## 参考資料

- [https://cloud.google.com/bigquery/docs/customer-managed-encryption](https://cloud.google.com/bigquery/docs/customer-managed-encryption)

## 技術情報

- Source Metadata：[sources/gcp/bigquery_dataset_public_access/metadata.json](../../sources/gcp/bigquery_dataset_public_access/metadata.json)
- Source Code：[sources/gcp/bigquery_dataset_public_access/check.py](../../sources/gcp/bigquery_dataset_public_access/check.py)
- Source Metadata Path：`sources/gcp/bigquery_dataset_public_access/metadata.json`
- Source Code Path：`sources/gcp/bigquery_dataset_public_access/check.py`
