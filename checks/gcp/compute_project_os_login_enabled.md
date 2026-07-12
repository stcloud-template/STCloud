# Ensure Os Login Is Enabled for a Project

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `compute_project_os_login_enabled` |
| クラウドプラットフォーム | GCP |
| サービス | compute |
| 重大度 | low |
| カテゴリ | Uncategorized |
| リソースタイプ | GCPProject |
| リソースグループ | governance |

## 説明

Ensure that the OS Login feature is enabled at the Google Cloud Platform (GCP) project level in order to provide you with centralized and automated SSH key pair management.

## リスク

Enabling OS Login feature ensures that the SSH keys used to connect to VM instances are mapped with Google Cloud IAM users. Revoking access to corresponding IAM users will revoke all the SSH keys associated with these users, therefore it facilitates centralized SSH key pair management, which is extremely useful in handling compromised or stolen SSH key pairs and/or revocation of external/third-party/vendor users.

## 推奨事項

Ensure that the OS Login feature is enabled at the Google Cloud Platform (GCP) project level in order to provide you with centralized and automated SSH key pair management.

- 推奨リンク：[https://cloud.google.com/compute/confidential-vm/docs/creating-cvm-instance:https://cloud.google.com/compute/confidential-vm/docs/about-cvm:https://cloud.google.com/confidential-computing:https://cloud.google.com/blog/products/identity-security/introducing-google-cloud-confidential-computing-with-confidential-vms](https://cloud.google.com/compute/confidential-vm/docs/creating-cvm-instance:https://cloud.google.com/compute/confidential-vm/docs/about-cvm:https://cloud.google.com/confidential-computing:https://cloud.google.com/blog/products/identity-security/introducing-google-cloud-confidential-computing-with-confidential-vms)

## 修正手順


### CLI

```text
gcloud compute project-info add-metadata --metadata enable-oslogin=TRUE
```

### Terraform

[https://docs.ST Cloud.com/checks/gcp/google-cloud-networking-policies/bc_gcp_networking_9#terraform](https://docs.ST Cloud.com/checks/gcp/google-cloud-networking-policies/bc_gcp_networking_9#terraform)

### Other

[https://www.trendmicro.com/cloudoneconformity/knowledge-base/gcp/ComputeEngine/enable-os-login.html](https://www.trendmicro.com/cloudoneconformity/knowledge-base/gcp/ComputeEngine/enable-os-login.html)

## 参考資料

- [https://cloud.google.com/compute/confidential-vm/docs/creating-cvm-instance:https://cloud.google.com/compute/confidential-vm/docs/about-cvm:https://cloud.google.com/confidential-computing:https://cloud.google.com/blog/products/identity-security/introducing-google-cloud-confidential-computing-with-confidential-vms](https://cloud.google.com/compute/confidential-vm/docs/creating-cvm-instance:https://cloud.google.com/compute/confidential-vm/docs/about-cvm:https://cloud.google.com/confidential-computing:https://cloud.google.com/blog/products/identity-security/introducing-google-cloud-confidential-computing-with-confidential-vms)

## 技術情報

- Source Metadata：[sources/gcp/compute_project_os_login_enabled/metadata.json](../../sources/gcp/compute_project_os_login_enabled/metadata.json)
- Source Code：[sources/gcp/compute_project_os_login_enabled/check.py](../../sources/gcp/compute_project_os_login_enabled/check.py)
- Source Metadata Path：`sources/gcp/compute_project_os_login_enabled/metadata.json`
- Source Code Path：`sources/gcp/compute_project_os_login_enabled/check.py`
