# Ensure That There Are No Unused Service Accounts

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `iam_service_account_unused` |
| 云平台 | GCP |
| 服务 | iam |
| 严重等级 | medium |
| 类别 | Uncategorized |
| 资源类型 | ServiceAccount |
| 资源组 | IAM |

## 描述

Ensure That There Are No Unused Service Accounts.

## 风险

A malicious actor could make use of privilege escalation or impersonation to access an unused Service Account that is over-privileged.

## 推荐措施

It is recommended to disable or remove unused Service Accounts.

- 推荐链接：[https://cloud.google.com/iam/docs/service-account-overview#identify-unused](https://cloud.google.com/iam/docs/service-account-overview#identify-unused)

## 修复步骤

No remediation steps available.

## 参考资料

- [https://cloud.google.com/iam/docs/service-account-overview#identify-unused](https://cloud.google.com/iam/docs/service-account-overview#identify-unused)

## 技术信息

- Source Metadata：[sources/gcp/iam_service_account_unused/metadata.json](../../sources/gcp/iam_service_account_unused/metadata.json)
- Source Code：[sources/gcp/iam_service_account_unused/check.py](../../sources/gcp/iam_service_account_unused/check.py)
- Source Metadata Path：`sources/gcp/iam_service_account_unused/metadata.json`
- Source Code Path：`sources/gcp/iam_service_account_unused/check.py`
