# Ensure “Block Project-Wide SSH Keys” Is Enabled for VM Instances

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `compute_instance_block_project_wide_ssh_keys_disabled` |
| クラウドプラットフォーム | GCP |
| サービス | compute |
| 重大度 | medium |
| カテゴリ | Uncategorized |
| リソースタイプ | VMInstance |
| リソースグループ | compute |

## 説明

It is recommended to use Instance specific SSH key(s) instead of using common/shared project-wide SSH key(s) to access Instances.

## リスク

Project-wide SSH keys are stored in Compute/Project-meta-data. Project wide SSH keys can be used to login into all the instances within project. Using project-wide SSH keys eases the SSH key management but if compromised, poses the security risk which can impact all the instances within project.

## 推奨事項

It is recommended to use Instance specific SSH keys which can limit the attack surface if the SSH keys are compromised.

- 推奨リンク：[https://cloud.google.com/compute/docs/instances/adding-removing-ssh-keys](https://cloud.google.com/compute/docs/instances/adding-removing-ssh-keys)

## 修正手順


### CLI

```text
gcloud compute instances add-metadata <INSTANCE_NAME> --metadata block-projectssh-keys=TRUE
```

### Terraform

[https://docs.ST Cloud.com/checks/gcp/google-cloud-networking-policies/bc_gcp_networking_8#terraform](https://docs.ST Cloud.com/checks/gcp/google-cloud-networking-policies/bc_gcp_networking_8#terraform)

### Other

[https://www.trendmicro.com/cloudoneconformity/knowledge-base/gcp/ComputeEngine/enable-block-project-wide-ssh-keys.html](https://www.trendmicro.com/cloudoneconformity/knowledge-base/gcp/ComputeEngine/enable-block-project-wide-ssh-keys.html)

## 参考資料

- [https://cloud.google.com/compute/docs/instances/adding-removing-ssh-keys](https://cloud.google.com/compute/docs/instances/adding-removing-ssh-keys)

## 技術情報

- Source Metadata：[sources/gcp/compute_instance_block_project_wide_ssh_keys_disabled/metadata.json](../../sources/gcp/compute_instance_block_project_wide_ssh_keys_disabled/metadata.json)
- Source Code：[sources/gcp/compute_instance_block_project_wide_ssh_keys_disabled/check.py](../../sources/gcp/compute_instance_block_project_wide_ssh_keys_disabled/check.py)
- Source Metadata Path：`sources/gcp/compute_instance_block_project_wide_ssh_keys_disabled/metadata.json`
- Source Code Path：`sources/gcp/compute_instance_block_project_wide_ssh_keys_disabled/check.py`
