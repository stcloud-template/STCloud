# Ensure Access Approval is Enabled in your account

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `iam_account_access_approval_enabled` |
| 云平台 | GCP |
| 服务 | iam |
| 严重等级 | high |
| 类别 | Uncategorized |
| 资源类型 | Account |
| 资源组 | governance |

## 描述

Ensure that Access Approval is enabled within your Google Cloud Platform (GCP) account in order to allow you to require your explicit approval whenever Google personnel need to access your GCP projects. Once the Access Approval feature is enabled, you can delegate users within your organization who can approve the access requests by giving them a security role in Identity and Access Management (IAM). These requests show the requester name/ID in an email or Pub/Sub message that you can choose to approve. This creates a new control and logging layer that reveals who in your organization approved/denied access requests to your projects.

## 风险

Controlling access to your Google Cloud data is crucial when working with business-critical and sensitive data. With Access Approval, you can be certain that your cloud information is accessed by approved Google personnel only. The Access Approval feature ensures that a cryptographically-signed approval is available for Google Cloud support and engineering teams when they need to access your cloud data (certain exceptions apply). By default, Access Approval and its dependency of Access Transparency are not enabled.

## 推荐措施

Ensure that Access Approval is enabled within your Google Cloud Platform (GCP) account in order to allow you to require your explicit approval whenever Google personnel need to access your GCP projects. Once the Access Approval feature is enabled, you can delegate users within your organization who can approve the access requests by giving them a security role in Identity and Access Management (IAM). These requests show the requester name/ID in an email or Pub/Sub message that you can choose to approve. This creates a new control and logging layer that reveals who in your organization approved/denied access requests to your projects.

- 推荐链接：[https://cloud.google.com/cloud-provider-access-management/access-approval/docs](https://cloud.google.com/cloud-provider-access-management/access-approval/docs)

## 修复步骤


### Other

[https://www.trendmicro.com/cloudoneconformity/knowledge-base/gcp/CloudIAM/enable-access-approval.html](https://www.trendmicro.com/cloudoneconformity/knowledge-base/gcp/CloudIAM/enable-access-approval.html)

## 参考资料

- [https://cloud.google.com/cloud-provider-access-management/access-approval/docs](https://cloud.google.com/cloud-provider-access-management/access-approval/docs)

## 技术信息

- Source Metadata：[sources/gcp/iam_account_access_approval_enabled/metadata.json](../../sources/gcp/iam_account_access_approval_enabled/metadata.json)
- Source Code：[sources/gcp/iam_account_access_approval_enabled/check.py](../../sources/gcp/iam_account_access_approval_enabled/check.py)
- Source Metadata Path：`sources/gcp/iam_account_access_approval_enabled/metadata.json`
- Source Code Path：`sources/gcp/iam_account_access_approval_enabled/check.py`
