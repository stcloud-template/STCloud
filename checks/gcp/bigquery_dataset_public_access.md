# Ensure That BigQuery Datasets Are Not Anonymously or Publicly Accessible.

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `bigquery_dataset_public_access` |
| 云平台 | GCP |
| 服务 | bigquery |
| 严重等级 | high |
| 类别 | Uncategorized |
| 资源类型 | Dataset |
| 资源组 | analytics |

## 描述

Ensure That BigQuery Datasets Are Not Anonymously or Publicly Accessible.

## 风险

Granting permissions to allUsers or allAuthenticatedUsers allows anyone to access the dataset. Such access might not be desirable if sensitive data is being stored in the dataset. Therefore, ensure that anonymous and/or public access to a dataset is not allowed.

## 推荐措施

It is recommended that the IAM policy on BigQuery datasets does not allow anonymous and/or public access.

- 推荐链接：[https://cloud.google.com/bigquery/docs/customer-managed-encryption](https://cloud.google.com/bigquery/docs/customer-managed-encryption)

## 修复步骤


### Terraform

[https://docs.ST Cloud.com/checks/gcp/google-cloud-general-policies/bc_gcp_general_3#terraform](https://docs.ST Cloud.com/checks/gcp/google-cloud-general-policies/bc_gcp_general_3#terraform)

### Other

[https://www.trendmicro.com/cloudoneconformity/knowledge-base/gcp/BigQuery/publicly-accessible-big-query-datasets.html](https://www.trendmicro.com/cloudoneconformity/knowledge-base/gcp/BigQuery/publicly-accessible-big-query-datasets.html)

## 参考资料

- [https://cloud.google.com/bigquery/docs/customer-managed-encryption](https://cloud.google.com/bigquery/docs/customer-managed-encryption)

## 技术信息

- Source Metadata：[sources/gcp/bigquery_dataset_public_access/metadata.json](../../sources/gcp/bigquery_dataset_public_access/metadata.json)
- Source Code：[sources/gcp/bigquery_dataset_public_access/check.py](../../sources/gcp/bigquery_dataset_public_access/check.py)
- Source Metadata Path：`sources/gcp/bigquery_dataset_public_access/metadata.json`
- Source Code Path：`sources/gcp/bigquery_dataset_public_access/check.py`
