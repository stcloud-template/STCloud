# Ensure That There Are Only GCP-Managed Service Account Keys for Each Service Account

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `iam_sa_no_user_managed_keys` |
| 云平台 | GCP |
| 服务 | iam |
| 严重等级 | medium |
| 类别 | Uncategorized |
| 资源类型 | ServiceAccountKey |
| 资源组 | IAM |

## 描述

Ensure That There Are Only GCP-Managed Service Account Keys for Each Service Account

## 风险

Anyone who has access to the keys will be able to access resources through the service account. GCP-managed keys are used by Cloud Platform services such as App Engine and Compute Engine. These keys cannot be downloaded. Google will keep the keys and automatically rotate them on an approximately weekly basis. User-managed keys are created, downloadable, and managed by users.

## 推荐措施

It is recommended to prevent user-managed service account keys.

- 推荐链接：[https://cloud.google.com/iam/docs/creating-managing-service-account-keys](https://cloud.google.com/iam/docs/creating-managing-service-account-keys)

## 修复步骤


### Other

[https://www.trendmicro.com/cloudoneconformity/knowledge-base/gcp/CloudIAM/delete-user-managed-service-account-keys.html](https://www.trendmicro.com/cloudoneconformity/knowledge-base/gcp/CloudIAM/delete-user-managed-service-account-keys.html)

## 参考资料

- [https://cloud.google.com/iam/docs/creating-managing-service-account-keys](https://cloud.google.com/iam/docs/creating-managing-service-account-keys)

## 技术信息

- Source Metadata：[sources/gcp/iam_sa_no_user_managed_keys/metadata.json](../../sources/gcp/iam_sa_no_user_managed_keys/metadata.json)
- Source Code：[sources/gcp/iam_sa_no_user_managed_keys/check.py](../../sources/gcp/iam_sa_no_user_managed_keys/check.py)
- Source Metadata Path：`sources/gcp/iam_sa_no_user_managed_keys/metadata.json`
- Source Code Path：`sources/gcp/iam_sa_no_user_managed_keys/check.py`
