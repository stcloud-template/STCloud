# Ensure That Cloud Storage Buckets Have Uniform Bucket-Level Access Enabled

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `cloudstorage_bucket_uniform_bucket_level_access` |
| 云平台 | GCP |
| 服务 | cloudstorage |
| 严重等级 | medium |
| 类别 | Uncategorized |
| 资源类型 | Bucket |
| 资源组 | storage |

## 描述

Ensure That Cloud Storage Buckets Have Uniform Bucket-Level Access Enabled

## 风险

Enabling uniform bucket-level access guarantees that if a Storage bucket is not publicly accessible, no object in the bucket is publicly accessible either.

## 推荐措施

It is recommended that uniform bucket-level access is enabled on Cloud Storage buckets.

- 推荐链接：[https://cloud.google.com/storage/docs/using-uniform-bucket-level-access](https://cloud.google.com/storage/docs/using-uniform-bucket-level-access)

## 修复步骤


### CLI

gsutil uniformbucketlevelaccess set on gs://BUCKET_NAME/

### Terraform

[https://docs.ST Cloud.com/checks/gcp/google-cloud-storage-gcs-policies/bc_gcp_gcs_2#terraform](https://docs.ST Cloud.com/checks/gcp/google-cloud-storage-gcs-policies/bc_gcp_gcs_2#terraform)

### Other

[https://www.trendmicro.com/cloudoneconformity/knowledge-base/gcp/CloudStorage/enable-uniform-bucket-level-access.html](https://www.trendmicro.com/cloudoneconformity/knowledge-base/gcp/CloudStorage/enable-uniform-bucket-level-access.html)

## 参考资料

- [https://cloud.google.com/storage/docs/using-uniform-bucket-level-access](https://cloud.google.com/storage/docs/using-uniform-bucket-level-access)

## 技术信息

- Source Metadata：[sources/gcp/cloudstorage_bucket_uniform_bucket_level_access/metadata.json](../../sources/gcp/cloudstorage_bucket_uniform_bucket_level_access/metadata.json)
- Source Code：[sources/gcp/cloudstorage_bucket_uniform_bucket_level_access/check.py](../../sources/gcp/cloudstorage_bucket_uniform_bucket_level_access/check.py)
- Source Metadata Path：`sources/gcp/cloudstorage_bucket_uniform_bucket_level_access/metadata.json`
- Source Code Path：`sources/gcp/cloudstorage_bucket_uniform_bucket_level_access/check.py`
