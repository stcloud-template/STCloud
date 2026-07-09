# Ensure That IAM Users Are Not Assigned the Service Account User or Service Account Token Creator Roles at Project Level

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `iam_no_service_roles_at_project_level` |
| 云平台 | GCP |
| 服务 | iam |
| 严重等级 | medium |
| 类别 | Uncategorized |
| 资源类型 | IAM Policy |
| 资源组 | IAM |

## 描述

It is recommended to assign the `Service Account User (iam.serviceAccountUser)` and `Service Account Token Creator (iam.serviceAccountTokenCreator)` roles to a user for a specific service account rather than assigning the role to a user at project level.

## 风险

The Service Account User (iam.serviceAccountUser) role allows an IAM user to attach a service account to a long-running job service such as an App Engine App or Dataflow Job, whereas the Service Account Token Creator (iam.serviceAccountTokenCreator) role allows a user to directly impersonate the identity of a service account.

## 推荐措施

Ensure that the Service Account User and Service Account Token Creator roles are assigned to a user for a specific GCP service account rather than to a user at the GCP project level, in order to implement the principle of least privilege (POLP). The principle of least privilege (also known as the principle of minimal privilege) is the practice of providing every user the minimal amount of access required to perform its tasks. Google Cloud Platform (GCP) IAM users should not have assigned the Service Account User or Service Account Token Creator roles at the GCP project level. Instead, these roles should be allocated to a user associated with a specific service account, providing that user access to the service account only.

- 推荐链接：[https://cloud.google.com/iam/docs/granting-changing-revoking-access](https://cloud.google.com/iam/docs/granting-changing-revoking-access)

## 修复步骤


### Terraform

[https://docs.ST Cloud.com/checks/gcp/google-cloud-iam-policies/bc_gcp_iam_3#terraform](https://docs.ST Cloud.com/checks/gcp/google-cloud-iam-policies/bc_gcp_iam_3#terraform)

### Other

[https://docs.ST Cloud.com/checks/gcp/google-cloud-iam-policies/bc_gcp_iam_3](https://docs.ST Cloud.com/checks/gcp/google-cloud-iam-policies/bc_gcp_iam_3)

## 参考资料

- [https://www.trendmicro.com/cloudoneconformity/knowledge-base/gcp/CloudIAM/check-for-iam-users-with-service-roles.html](https://www.trendmicro.com/cloudoneconformity/knowledge-base/gcp/CloudIAM/check-for-iam-users-with-service-roles.html)
- [https://cloud.google.com/iam/docs/granting-changing-revoking-access](https://cloud.google.com/iam/docs/granting-changing-revoking-access)

## 技术信息

- Source Metadata：[sources/gcp/iam_no_service_roles_at_project_level/metadata.json](../../sources/gcp/iam_no_service_roles_at_project_level/metadata.json)
- Source Code：[sources/gcp/iam_no_service_roles_at_project_level/check.py](../../sources/gcp/iam_no_service_roles_at_project_level/check.py)
- Source Metadata Path：`sources/gcp/iam_no_service_roles_at_project_level/metadata.json`
- Source Code Path：`sources/gcp/iam_no_service_roles_at_project_level/check.py`
