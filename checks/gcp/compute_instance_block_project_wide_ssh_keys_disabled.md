# Ensure “Block Project-Wide SSH Keys” Is Enabled for VM Instances

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `compute_instance_block_project_wide_ssh_keys_disabled` |
| 云平台 | GCP |
| 服务 | compute |
| 严重等级 | medium |
| 类别 | Uncategorized |
| 资源类型 | VMInstance |
| 资源组 | compute |

## 描述

It is recommended to use Instance specific SSH key(s) instead of using common/shared project-wide SSH key(s) to access Instances.

## 风险

Project-wide SSH keys are stored in Compute/Project-meta-data. Project wide SSH keys can be used to login into all the instances within project. Using project-wide SSH keys eases the SSH key management but if compromised, poses the security risk which can impact all the instances within project.

## 推荐措施

It is recommended to use Instance specific SSH keys which can limit the attack surface if the SSH keys are compromised.

- 推荐链接：[https://cloud.google.com/compute/docs/instances/adding-removing-ssh-keys](https://cloud.google.com/compute/docs/instances/adding-removing-ssh-keys)

## 修复步骤


### CLI

```text
gcloud compute instances add-metadata <INSTANCE_NAME> --metadata block-projectssh-keys=TRUE
```

### Terraform

[https://docs.ST Cloud.com/checks/gcp/google-cloud-networking-policies/bc_gcp_networking_8#terraform](https://docs.ST Cloud.com/checks/gcp/google-cloud-networking-policies/bc_gcp_networking_8#terraform)

### Other

[https://www.trendmicro.com/cloudoneconformity/knowledge-base/gcp/ComputeEngine/enable-block-project-wide-ssh-keys.html](https://www.trendmicro.com/cloudoneconformity/knowledge-base/gcp/ComputeEngine/enable-block-project-wide-ssh-keys.html)

## 参考资料

- [https://cloud.google.com/compute/docs/instances/adding-removing-ssh-keys](https://cloud.google.com/compute/docs/instances/adding-removing-ssh-keys)

## 技术信息

- Source Metadata：[sources/gcp/compute_instance_block_project_wide_ssh_keys_disabled/metadata.json](../../sources/gcp/compute_instance_block_project_wide_ssh_keys_disabled/metadata.json)
- Source Code：[sources/gcp/compute_instance_block_project_wide_ssh_keys_disabled/check.py](../../sources/gcp/compute_instance_block_project_wide_ssh_keys_disabled/check.py)
- Source Metadata Path：`sources/gcp/compute_instance_block_project_wide_ssh_keys_disabled/metadata.json`
- Source Code Path：`sources/gcp/compute_instance_block_project_wide_ssh_keys_disabled/check.py`
