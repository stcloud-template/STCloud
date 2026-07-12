# Ensure Service Account does not have admin privileges

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `iam_sa_no_administrative_privileges` |
| クラウドプラットフォーム | GCP |
| サービス | iam |
| 重大度 | high |
| カテゴリ | Uncategorized |
| リソースタイプ | ServiceAccount |
| リソースグループ | IAM |

## 説明

Ensure Service Account does not have admin privileges

## リスク

Enrolling ServiceAccount with Admin rights gives full access to an assigned application or a VM. A ServiceAccount Access holder can perform critical actions, such as delete and update change settings, without user intervention.

## 推奨事項

Ensure that your Google Cloud user-managed service accounts are not using privileged (administrator) roles, in order to implement the principle of least privilege and prevent any accidental or intentional modifications that may lead to data leaks and/or data loss.

- 推奨リンク：[https://cloud.google.com/iam/docs/manage-access-service-accounts](https://cloud.google.com/iam/docs/manage-access-service-accounts)

## 修正手順


### Terraform

[https://docs.ST Cloud.com/checks/gcp/google-cloud-iam-policies/bc_gcp_iam_4#terraform](https://docs.ST Cloud.com/checks/gcp/google-cloud-iam-policies/bc_gcp_iam_4#terraform)

### Other

[https://docs.ST Cloud.com/checks/gcp/google-cloud-iam-policies/bc_gcp_iam_4](https://docs.ST Cloud.com/checks/gcp/google-cloud-iam-policies/bc_gcp_iam_4)

## 参考資料

- [https://www.trendmicro.com/cloudoneconformity/knowledge-base/gcp/CloudIAM/restrict-admin-access-for-service-accounts.html](https://www.trendmicro.com/cloudoneconformity/knowledge-base/gcp/CloudIAM/restrict-admin-access-for-service-accounts.html)
- [https://cloud.google.com/iam/docs/manage-access-service-accounts](https://cloud.google.com/iam/docs/manage-access-service-accounts)

## 技術情報

- Source Metadata：[sources/gcp/iam_sa_no_administrative_privileges/metadata.json](../../sources/gcp/iam_sa_no_administrative_privileges/metadata.json)
- Source Code：[sources/gcp/iam_sa_no_administrative_privileges/check.py](../../sources/gcp/iam_sa_no_administrative_privileges/check.py)
- Source Metadata Path：`sources/gcp/iam_sa_no_administrative_privileges/metadata.json`
- Source Code Path：`sources/gcp/iam_sa_no_administrative_privileges/check.py`
