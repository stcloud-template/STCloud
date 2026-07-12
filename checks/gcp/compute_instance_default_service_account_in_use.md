# Ensure That Instances Are Not Configured To Use the Default Service Account

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `compute_instance_default_service_account_in_use` |
| クラウドプラットフォーム | GCP |
| サービス | compute |
| 重大度 | medium |
| カテゴリ | Uncategorized |
| リソースタイプ | VMInstance |
| リソースグループ | compute |

## 説明

It is recommended to configure your instance to not use the default Compute Engine service account because it has the Editor role on the project.

## リスク

The default Compute Engine service account has the Editor role on the project, which allows read and write access to most Google Cloud Services. This can lead to a privilege escalations if your VM is compromised allowing an attacker gaining access to all of your project

## 推奨事項

To defend against privilege escalations if your VM is compromised and prevent an attacker from gaining access to all of your project, it is recommended to not use the default Compute Engine service account. Instead, you should create a new service account and assigning only the permissions needed by your instance. The default Compute Engine service account is named `[PROJECT_NUMBER]-compute@developer.gserviceaccount.com`.

- 推奨リンク：[https://cloud.google.com/iam/docs/granting-changing-revoking-access](https://cloud.google.com/iam/docs/granting-changing-revoking-access)

## 修正手順


### CLI

```text
gcloud compute instances set-service-account <INSTANCE_NAME> --service-account=<SERVICE_ACCOUNT_EMAIL>
```

### Terraform

[https://docs.ST Cloud.com/checks/gcp/google-cloud-iam-policies/bc_gcp_iam_1#terraform](https://docs.ST Cloud.com/checks/gcp/google-cloud-iam-policies/bc_gcp_iam_1#terraform)

### Other

[https://docs.ST Cloud.com/checks/gcp/google-cloud-iam-policies/bc_gcp_iam_1](https://docs.ST Cloud.com/checks/gcp/google-cloud-iam-policies/bc_gcp_iam_1)

## 参考資料

- [https://www.trendmicro.com/cloudoneconformity/knowledge-base/gcp/ComputeEngine/default-service-accounts-in-use.html](https://www.trendmicro.com/cloudoneconformity/knowledge-base/gcp/ComputeEngine/default-service-accounts-in-use.html)
- [https://cloud.google.com/iam/docs/granting-changing-revoking-access](https://cloud.google.com/iam/docs/granting-changing-revoking-access)

## 技術情報

- Source Metadata：[sources/gcp/compute_instance_default_service_account_in_use/metadata.json](../../sources/gcp/compute_instance_default_service_account_in_use/metadata.json)
- Source Code：[sources/gcp/compute_instance_default_service_account_in_use/check.py](../../sources/gcp/compute_instance_default_service_account_in_use/check.py)
- Source Metadata Path：`sources/gcp/compute_instance_default_service_account_in_use/metadata.json`
- Source Code Path：`sources/gcp/compute_instance_default_service_account_in_use/check.py`
