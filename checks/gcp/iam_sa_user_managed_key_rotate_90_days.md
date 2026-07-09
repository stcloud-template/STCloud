# Ensure User-Managed/External Keys for Service Accounts Are Rotated Every 90 Days

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `iam_sa_user_managed_key_rotate_90_days` |
| 云平台 | GCP |
| 服务 | iam |
| 严重等级 | low |
| 类别 | Uncategorized |
| 资源类型 | ServiceAccountKey |
| 资源组 | IAM |

## 描述

Ensure User-Managed/External Keys for Service Accounts Are Rotated Every 90 Days

## 风险

Service Account keys should be rotated to ensure that data cannot be accessed with an old key that might have been lost, cracked, or stolen.

## 推荐措施

It is recommended that all Service Account keys are regularly rotated.

- 推荐链接：[https://cloud.google.com/iam/docs/creating-managing-service-account-keys](https://cloud.google.com/iam/docs/creating-managing-service-account-keys)

## 修复步骤


### Other

[https://www.trendmicro.com/cloudoneconformity/knowledge-base/gcp/CloudIAM/rotate-service-account-user-managed-keys.html](https://www.trendmicro.com/cloudoneconformity/knowledge-base/gcp/CloudIAM/rotate-service-account-user-managed-keys.html)

## 参考资料

- [https://cloud.google.com/iam/docs/creating-managing-service-account-keys](https://cloud.google.com/iam/docs/creating-managing-service-account-keys)

## 技术信息

- Source Metadata：[sources/gcp/iam_sa_user_managed_key_rotate_90_days/metadata.json](../../sources/gcp/iam_sa_user_managed_key_rotate_90_days/metadata.json)
- Source Code：[sources/gcp/iam_sa_user_managed_key_rotate_90_days/check.py](../../sources/gcp/iam_sa_user_managed_key_rotate_90_days/check.py)
- Source Metadata Path：`sources/gcp/iam_sa_user_managed_key_rotate_90_days/metadata.json`
- Source Code Path：`sources/gcp/iam_sa_user_managed_key_rotate_90_days/check.py`
