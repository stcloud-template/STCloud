# Ensure Compute Instances Have Confidential Computing Enabled

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `compute_instance_confidential_computing_enabled` |
| クラウドプラットフォーム | GCP |
| サービス | compute |
| 重大度 | medium |
| カテゴリ | Uncategorized |
| リソースタイプ | VMInstance |
| リソースグループ | compute |

## 説明

Ensure that the Confidential Computing security feature is enabled for your Google Cloud virtual machine (VM) instances in order to add protection to your sensitive data in use by keeping it encrypted in memory and using encryption keys that Google doesn't have access to. Confidential Computing is a breakthrough technology which encrypts data while it is being processed. This technology keeps data encrypted in memory, outside the CPU.

## リスク

Confidential Computing keeps your sensitive data encrypted while it is used, indexed, queried, or trained on, and does not allow Google to access the encryption keys (these keys are generated in hardware, per VM instance, and can't be exported). In this way, the Confidential Computing feature can help alleviate concerns about risk related to either dependency on Google Cloud infrastructure or Google insiders' access to your data in the clear.

## 推奨事項

Ensure that the Confidential Computing security feature is enabled for your Google Cloud virtual machine (VM) instances in order to add protection to your sensitive data in use by keeping it encrypted in memory and using encryption keys that Google doesn't have access to. Confidential Computing is a breakthrough technology which encrypts data while it is being processed. This technology keeps data encrypted in memory, outside the CPU.

- 推奨リンク：[https://cloud.google.com/compute/confidential-vm/docs/creating-cvm-instance:https://cloud.google.com/compute/confidential-vm/docs/about-cvm:https://cloud.google.com/confidential-computing:https://cloud.google.com/blog/products/identity-security/introducing-google-cloud-confidential-computing-with-confidential-vms](https://cloud.google.com/compute/confidential-vm/docs/creating-cvm-instance:https://cloud.google.com/compute/confidential-vm/docs/about-cvm:https://cloud.google.com/confidential-computing:https://cloud.google.com/blog/products/identity-security/introducing-google-cloud-confidential-computing-with-confidential-vms)

## 修正手順


### Other

[https://www.trendmicro.com/cloudoneconformity/knowledge-base/gcp/ComputeEngine/confidential-computing.html](https://www.trendmicro.com/cloudoneconformity/knowledge-base/gcp/ComputeEngine/confidential-computing.html)

## 参考資料

- [https://cloud.google.com/compute/confidential-vm/docs/creating-cvm-instance:https://cloud.google.com/compute/confidential-vm/docs/about-cvm:https://cloud.google.com/confidential-computing:https://cloud.google.com/blog/products/identity-security/introducing-google-cloud-confidential-computing-with-confidential-vms](https://cloud.google.com/compute/confidential-vm/docs/creating-cvm-instance:https://cloud.google.com/compute/confidential-vm/docs/about-cvm:https://cloud.google.com/confidential-computing:https://cloud.google.com/blog/products/identity-security/introducing-google-cloud-confidential-computing-with-confidential-vms)

## 技術情報

- Source Metadata：[sources/gcp/compute_instance_confidential_computing_enabled/metadata.json](../../sources/gcp/compute_instance_confidential_computing_enabled/metadata.json)
- Source Code：[sources/gcp/compute_instance_confidential_computing_enabled/check.py](../../sources/gcp/compute_instance_confidential_computing_enabled/check.py)
- Source Metadata Path：`sources/gcp/compute_instance_confidential_computing_enabled/metadata.json`
- Source Code Path：`sources/gcp/compute_instance_confidential_computing_enabled/check.py`
