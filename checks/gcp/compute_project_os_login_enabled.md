# Ensure Os Login Is Enabled for a Project

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `compute_project_os_login_enabled` |
| 云平台 | GCP |
| 服务 | compute |
| 严重等级 | low |
| 类别 | Uncategorized |
| 资源类型 | GCPProject |
| 资源组 | governance |

## 描述

Ensure that the OS Login feature is enabled at the Google Cloud Platform (GCP) project level in order to provide you with centralized and automated SSH key pair management.

## 风险

Enabling OS Login feature ensures that the SSH keys used to connect to VM instances are mapped with Google Cloud IAM users. Revoking access to corresponding IAM users will revoke all the SSH keys associated with these users, therefore it facilitates centralized SSH key pair management, which is extremely useful in handling compromised or stolen SSH key pairs and/or revocation of external/third-party/vendor users.

## 推荐措施

Ensure that the OS Login feature is enabled at the Google Cloud Platform (GCP) project level in order to provide you with centralized and automated SSH key pair management.

- 推荐链接：[https://cloud.google.com/compute/confidential-vm/docs/creating-cvm-instance:https://cloud.google.com/compute/confidential-vm/docs/about-cvm:https://cloud.google.com/confidential-computing:https://cloud.google.com/blog/products/identity-security/introducing-google-cloud-confidential-computing-with-confidential-vms](https://cloud.google.com/compute/confidential-vm/docs/creating-cvm-instance:https://cloud.google.com/compute/confidential-vm/docs/about-cvm:https://cloud.google.com/confidential-computing:https://cloud.google.com/blog/products/identity-security/introducing-google-cloud-confidential-computing-with-confidential-vms)

## 修复步骤


### CLI

```text
gcloud compute project-info add-metadata --metadata enable-oslogin=TRUE
```

### Terraform

[https://docs.ST Cloud.com/checks/gcp/google-cloud-networking-policies/bc_gcp_networking_9#terraform](https://docs.ST Cloud.com/checks/gcp/google-cloud-networking-policies/bc_gcp_networking_9#terraform)

### Other

[https://www.trendmicro.com/cloudoneconformity/knowledge-base/gcp/ComputeEngine/enable-os-login.html](https://www.trendmicro.com/cloudoneconformity/knowledge-base/gcp/ComputeEngine/enable-os-login.html)

## 参考资料

- [https://cloud.google.com/compute/confidential-vm/docs/creating-cvm-instance:https://cloud.google.com/compute/confidential-vm/docs/about-cvm:https://cloud.google.com/confidential-computing:https://cloud.google.com/blog/products/identity-security/introducing-google-cloud-confidential-computing-with-confidential-vms](https://cloud.google.com/compute/confidential-vm/docs/creating-cvm-instance:https://cloud.google.com/compute/confidential-vm/docs/about-cvm:https://cloud.google.com/confidential-computing:https://cloud.google.com/blog/products/identity-security/introducing-google-cloud-confidential-computing-with-confidential-vms)

## 技术信息

- Source Metadata：[sources/gcp/compute_project_os_login_enabled/metadata.json](../../sources/gcp/compute_project_os_login_enabled/metadata.json)
- Source Code：[sources/gcp/compute_project_os_login_enabled/check.py](../../sources/gcp/compute_project_os_login_enabled/check.py)
- Source Metadata Path：`sources/gcp/compute_project_os_login_enabled/metadata.json`
- Source Code Path：`sources/gcp/compute_project_os_login_enabled/check.py`
