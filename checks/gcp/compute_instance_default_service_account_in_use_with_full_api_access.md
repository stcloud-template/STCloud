# Ensure That Instances Are Not Configured To Use the Default Service Account With Full Access to All Cloud APIs

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `compute_instance_default_service_account_in_use_with_full_api_access` |
| クラウドプラットフォーム | GCP |
| サービス | compute |
| 重大度 | medium |
| カテゴリ | Uncategorized |
| リソースタイプ | VMInstance |
| リソースグループ | compute |

## 説明

To support principle of least privileges and prevent potential privilege escalation it is recommended that instances are not assigned to default service account `Compute Engine default service account` with Scope `Allow full access to all Cloud APIs`.

## リスク

When an instance is configured with `Compute Engine default service account` with Scope `Allow full access to all Cloud APIs`, based on IAM roles assigned to the user(s) accessing Instance, it may allow user to perform cloud operations/API calls that user is not supposed to perform leading to successful privilege escalation.

## 推奨事項

To enforce the principle of least privileges and prevent potential privilege escalation, ensure that your Google Compute Engine instances are not configured to use the default service account with the Cloud API access scope set to "Allow full access to all Cloud APIs". The principle of least privilege (POLP), also known as the principle of least authority, is the security concept of giving the user/system/service the minimal set of permissions required to successfully perform its tasks.

- 推奨リンク：[https://cloud.google.com/iam/docs/granting-changing-revoking-access](https://cloud.google.com/iam/docs/granting-changing-revoking-access)

## 修正手順


### CLI

```text
gcloud compute instances set-service-account <INSTANCE_NAME> --service-account=<SERVICE_ACCOUNT_EMAIL> --scopes [<SCOPE1>,<SCOPE2>,...]
```

### Terraform

[https://docs.ST Cloud.com/checks/gcp/google-cloud-iam-policies/bc_gcp_iam_2#terraform](https://docs.ST Cloud.com/checks/gcp/google-cloud-iam-policies/bc_gcp_iam_2#terraform)

### Other

[https://www.trendmicro.com/cloudoneconformity/knowledge-base/gcp/ComputeEngine/default-service-accounts-with-full-access-in-use.html](https://www.trendmicro.com/cloudoneconformity/knowledge-base/gcp/ComputeEngine/default-service-accounts-with-full-access-in-use.html)

## 参考資料

- [https://cloud.google.com/iam/docs/granting-changing-revoking-access](https://cloud.google.com/iam/docs/granting-changing-revoking-access)

## 技術情報

- Source Metadata：[sources/gcp/compute_instance_default_service_account_in_use_with_full_api_access/metadata.json](../../sources/gcp/compute_instance_default_service_account_in_use_with_full_api_access/metadata.json)
- Source Code：[sources/gcp/compute_instance_default_service_account_in_use_with_full_api_access/check.py](../../sources/gcp/compute_instance_default_service_account_in_use_with_full_api_access/check.py)
- Source Metadata Path：`sources/gcp/compute_instance_default_service_account_in_use_with_full_api_access/metadata.json`
- Source Code Path：`sources/gcp/compute_instance_default_service_account_in_use_with_full_api_access/check.py`
