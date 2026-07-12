# Ensure Compute Instances Are Launched With Shielded VM Enabled

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `compute_instance_shielded_vm_enabled` |
| クラウドプラットフォーム | GCP |
| サービス | compute |
| 重大度 | medium |
| カテゴリ | Uncategorized |
| リソースタイプ | VMInstance |
| リソースグループ | compute |

## 説明

To defend against advanced threats and ensure that the boot loader and firmware on your VMs are signed and untampered, it is recommended that Compute instances are launched with Shielded VM enabled.

## リスク

Whithout shielded VM enabled is not possible to defend against advanced threats and ensure that the boot loader and firmware on your Google Compute Engine instances are signed and untampered.

## 推奨事項

Ensure that your Google Compute Engine instances are configured to use Shielded VM security feature for protection against rootkits and bootkits.Google Compute Engine service can enable 3 advanced security components for Shielded VM instances: 1. Virtual Trusted Platform Module (vTPM) - this component validates the guest virtual machine (VM) pre-boot and boot integrity, and provides key generation and protection. 2. Integrity Monitoring - lets you monitor and verify the runtime boot integrity of your shielded VM instances using Google Cloud Operations reports (also known as Stackdriver reports). 3. Secure boot helps - this security component protects your VM instances against boot-level and kernel-level malware and rootkits. To defend against advanced threats and ensure that the boot loader and firmware on your Google Compute Engine instances are signed and untampered, it is strongly recommended that your production instances are launched with Shielded VM enabled.

- 推奨リンク：[https://cloud.google.com/compute/docs/instances/modifying-shielded-vm](https://cloud.google.com/compute/docs/instances/modifying-shielded-vm)

## 修正手順


### CLI

```text
gcloud compute instances update <INSTANCE_NAME> --shielded-vtpm --shielded-vmintegrity-monitoring
```

### Terraform

[https://docs.ST Cloud.com/checks/gcp/google-cloud-general-policies/bc_gcp_general_y#terraform](https://docs.ST Cloud.com/checks/gcp/google-cloud-general-policies/bc_gcp_general_y#terraform)

### Other

[https://www.trendmicro.com/cloudoneconformity/knowledge-base/gcp/ComputeEngine/enable-shielded-vm.html](https://www.trendmicro.com/cloudoneconformity/knowledge-base/gcp/ComputeEngine/enable-shielded-vm.html)

## 参考資料

- [https://cloud.google.com/compute/docs/instances/modifying-shielded-vm](https://cloud.google.com/compute/docs/instances/modifying-shielded-vm)

## 技術情報

- Source Metadata：[sources/gcp/compute_instance_shielded_vm_enabled/metadata.json](../../sources/gcp/compute_instance_shielded_vm_enabled/metadata.json)
- Source Code：[sources/gcp/compute_instance_shielded_vm_enabled/check.py](../../sources/gcp/compute_instance_shielded_vm_enabled/check.py)
- Source Metadata Path：`sources/gcp/compute_instance_shielded_vm_enabled/metadata.json`
- Source Code Path：`sources/gcp/compute_instance_shielded_vm_enabled/check.py`
