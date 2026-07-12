# Enforce Separation of Duties for Service-Account Related Roles

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `iam_role_sa_enforce_separation_of_duties` |
| クラウドプラットフォーム | GCP |
| サービス | iam |
| 重大度 | medium |
| カテゴリ | Uncategorized |
| リソースタイプ | IAMRole |
| リソースグループ | IAM |

## 説明

Ensure that separation of duties (also known as segregation of duties - SoD) is enforced for all Google Cloud Platform (GCP) service-account related roles. The security principle of separation of duties has as its primary objective the prevention of fraud and human error. This objective is achieved by disbanding the tasks and associated privileges for a specific business process among multiple users/members. To follow security best practices, your GCP service accounts should not have the Service Account Admin and Service Account User roles assigned at the same time.

## リスク

The principle of separation of duties should be enforced in order to eliminate the need for high-privileged IAM members, as the permissions granted to these members can allow them to perform malicious or unwanted actions.

## 推奨事項

Ensure that separation of duties (also known as segregation of duties - SoD) is enforced for all Google Cloud Platform (GCP) service-account related roles. The security principle of separation of duties has as its primary objective the prevention of fraud and human error. This objective is achieved by disbanding the tasks and associated privileges for a specific business process among multiple users/members. To follow security best practices, your GCP service accounts should not have the Service Account Admin and Service Account User roles assigned at the same time.

- 推奨リンク：[https://cloud.google.com/iam/docs/understanding-roles](https://cloud.google.com/iam/docs/understanding-roles)

## 修正手順


### Terraform

[https://docs.ST Cloud.com/checks/gcp/google-cloud-iam-policies/bc_gcp_iam_10#terraform](https://docs.ST Cloud.com/checks/gcp/google-cloud-iam-policies/bc_gcp_iam_10#terraform)

### Other

[https://www.trendmicro.com/cloudoneconformity/knowledge-base/gcp/CloudIAM/enforce-separation-of-duties-for-service-account-roles.html](https://www.trendmicro.com/cloudoneconformity/knowledge-base/gcp/CloudIAM/enforce-separation-of-duties-for-service-account-roles.html)

## 参考資料

- [https://cloud.google.com/iam/docs/understanding-roles](https://cloud.google.com/iam/docs/understanding-roles)

## 技術情報

- Source Metadata：[sources/gcp/iam_role_sa_enforce_separation_of_duties/metadata.json](../../sources/gcp/iam_role_sa_enforce_separation_of_duties/metadata.json)
- Source Code：[sources/gcp/iam_role_sa_enforce_separation_of_duties/check.py](../../sources/gcp/iam_role_sa_enforce_separation_of_duties/check.py)
- Source Metadata Path：`sources/gcp/iam_role_sa_enforce_separation_of_duties/metadata.json`
- Source Code Path：`sources/gcp/iam_role_sa_enforce_separation_of_duties/check.py`
