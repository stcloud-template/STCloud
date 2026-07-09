# Enforce Separation of Duties for Service-Account Related Roles

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `iam_role_sa_enforce_separation_of_duties` |
| 云平台 | GCP |
| 服务 | iam |
| 严重等级 | medium |
| 类别 | Uncategorized |
| 资源类型 | IAMRole |
| 资源组 | IAM |

## 描述

Ensure that separation of duties (also known as segregation of duties - SoD) is enforced for all Google Cloud Platform (GCP) service-account related roles. The security principle of separation of duties has as its primary objective the prevention of fraud and human error. This objective is achieved by disbanding the tasks and associated privileges for a specific business process among multiple users/members. To follow security best practices, your GCP service accounts should not have the Service Account Admin and Service Account User roles assigned at the same time.

## 风险

The principle of separation of duties should be enforced in order to eliminate the need for high-privileged IAM members, as the permissions granted to these members can allow them to perform malicious or unwanted actions.

## 推荐措施

Ensure that separation of duties (also known as segregation of duties - SoD) is enforced for all Google Cloud Platform (GCP) service-account related roles. The security principle of separation of duties has as its primary objective the prevention of fraud and human error. This objective is achieved by disbanding the tasks and associated privileges for a specific business process among multiple users/members. To follow security best practices, your GCP service accounts should not have the Service Account Admin and Service Account User roles assigned at the same time.

- 推荐链接：[https://cloud.google.com/iam/docs/understanding-roles](https://cloud.google.com/iam/docs/understanding-roles)

## 修复步骤


### Terraform

[https://docs.ST Cloud.com/checks/gcp/google-cloud-iam-policies/bc_gcp_iam_10#terraform](https://docs.ST Cloud.com/checks/gcp/google-cloud-iam-policies/bc_gcp_iam_10#terraform)

### Other

[https://www.trendmicro.com/cloudoneconformity/knowledge-base/gcp/CloudIAM/enforce-separation-of-duties-for-service-account-roles.html](https://www.trendmicro.com/cloudoneconformity/knowledge-base/gcp/CloudIAM/enforce-separation-of-duties-for-service-account-roles.html)

## 参考资料

- [https://cloud.google.com/iam/docs/understanding-roles](https://cloud.google.com/iam/docs/understanding-roles)

## 技术信息

- Source Metadata：[sources/gcp/iam_role_sa_enforce_separation_of_duties/metadata.json](../../sources/gcp/iam_role_sa_enforce_separation_of_duties/metadata.json)
- Source Code：[sources/gcp/iam_role_sa_enforce_separation_of_duties/check.py](../../sources/gcp/iam_role_sa_enforce_separation_of_duties/check.py)
- Source Metadata Path：`sources/gcp/iam_role_sa_enforce_separation_of_duties/metadata.json`
- Source Code Path：`sources/gcp/iam_role_sa_enforce_separation_of_duties/check.py`
