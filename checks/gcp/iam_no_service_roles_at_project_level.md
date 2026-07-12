# Ensure That IAM Users Are Not Assigned the Service Account User or Service Account Token Creator Roles at Project Level

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `iam_no_service_roles_at_project_level` |
| クラウドプラットフォーム | GCP |
| サービス | iam |
| 重大度 | medium |
| カテゴリ | Uncategorized |
| リソースタイプ | IAM Policy |
| リソースグループ | IAM |

## 説明

It is recommended to assign the `Service Account User (iam.serviceAccountUser)` and `Service Account Token Creator (iam.serviceAccountTokenCreator)` roles to a user for a specific service account rather than assigning the role to a user at project level.

## リスク

The Service Account User (iam.serviceAccountUser) role allows an IAM user to attach a service account to a long-running job service such as an App Engine App or Dataflow Job, whereas the Service Account Token Creator (iam.serviceAccountTokenCreator) role allows a user to directly impersonate the identity of a service account.

## 推奨事項

Ensure that the Service Account User and Service Account Token Creator roles are assigned to a user for a specific GCP service account rather than to a user at the GCP project level, in order to implement the principle of least privilege (POLP). The principle of least privilege (also known as the principle of minimal privilege) is the practice of providing every user the minimal amount of access required to perform its tasks. Google Cloud Platform (GCP) IAM users should not have assigned the Service Account User or Service Account Token Creator roles at the GCP project level. Instead, these roles should be allocated to a user associated with a specific service account, providing that user access to the service account only.

- 推奨リンク：[https://cloud.google.com/iam/docs/granting-changing-revoking-access](https://cloud.google.com/iam/docs/granting-changing-revoking-access)

## 修正手順


### Terraform

[https://docs.ST Cloud.com/checks/gcp/google-cloud-iam-policies/bc_gcp_iam_3#terraform](https://docs.ST Cloud.com/checks/gcp/google-cloud-iam-policies/bc_gcp_iam_3#terraform)

### Other

[https://docs.ST Cloud.com/checks/gcp/google-cloud-iam-policies/bc_gcp_iam_3](https://docs.ST Cloud.com/checks/gcp/google-cloud-iam-policies/bc_gcp_iam_3)

## 参考資料

- [https://www.trendmicro.com/cloudoneconformity/knowledge-base/gcp/CloudIAM/check-for-iam-users-with-service-roles.html](https://www.trendmicro.com/cloudoneconformity/knowledge-base/gcp/CloudIAM/check-for-iam-users-with-service-roles.html)
- [https://cloud.google.com/iam/docs/granting-changing-revoking-access](https://cloud.google.com/iam/docs/granting-changing-revoking-access)

## 技術情報

- Source Metadata：[sources/gcp/iam_no_service_roles_at_project_level/metadata.json](../../sources/gcp/iam_no_service_roles_at_project_level/metadata.json)
- Source Code：[sources/gcp/iam_no_service_roles_at_project_level/check.py](../../sources/gcp/iam_no_service_roles_at_project_level/check.py)
- Source Metadata Path：`sources/gcp/iam_no_service_roles_at_project_level/metadata.json`
- Source Code Path：`sources/gcp/iam_no_service_roles_at_project_level/check.py`
