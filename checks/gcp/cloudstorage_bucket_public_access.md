# Ensure That Cloud Storage Bucket Is Not Anonymously or Publicly Accessible

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `cloudstorage_bucket_public_access` |
| 云平台 | GCP |
| 服务 | cloudstorage |
| 严重等级 | high |
| 类别 | internet-exposed |
| 资源类型 | Bucket |
| 资源组 | storage |

## 描述

Ensure That Cloud Storage Bucket Is Not Anonymously or Publicly Accessible

## 风险

Allowing anonymous or public access grants permissions to anyone to access bucket content. Such access might not be desired if you are storing any sensitive data. Hence, ensure that anonymous or public access to a bucket is not allowed.

## 推荐措施

It is recommended that IAM policy on Cloud Storage bucket does not allows anonymous or public access.

- 推荐链接：[https://cloud.google.com/storage/docs/access-control/iam-reference](https://cloud.google.com/storage/docs/access-control/iam-reference)

## 修复步骤


### Terraform

[https://docs.ST Cloud.com/checks/gcp/google-cloud-public-policies/bc_gcp_public_1#terraform](https://docs.ST Cloud.com/checks/gcp/google-cloud-public-policies/bc_gcp_public_1#terraform)

### Other

[https://docs.ST Cloud.com/checks/gcp/google-cloud-public-policies/bc_gcp_public_1](https://docs.ST Cloud.com/checks/gcp/google-cloud-public-policies/bc_gcp_public_1)

## 参考资料

- [https://www.trendmicro.com/cloudoneconformity/knowledge-base/gcp/CloudStorage/publicly-accessible-storage-buckets.html](https://www.trendmicro.com/cloudoneconformity/knowledge-base/gcp/CloudStorage/publicly-accessible-storage-buckets.html)
- [https://cloud.google.com/storage/docs/access-control/iam-reference](https://cloud.google.com/storage/docs/access-control/iam-reference)

## 技术信息

- Source Metadata：[sources/gcp/cloudstorage_bucket_public_access/metadata.json](../../sources/gcp/cloudstorage_bucket_public_access/metadata.json)
- Source Code：[sources/gcp/cloudstorage_bucket_public_access/check.py](../../sources/gcp/cloudstorage_bucket_public_access/check.py)
- Source Metadata Path：`sources/gcp/cloudstorage_bucket_public_access/metadata.json`
- Source Code Path：`sources/gcp/cloudstorage_bucket_public_access/check.py`
