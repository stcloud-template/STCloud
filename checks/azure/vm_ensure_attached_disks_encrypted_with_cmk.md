# Ensure that 'OS and Data' disks are encrypted with Customer Managed Key (CMK)

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `vm_ensure_attached_disks_encrypted_with_cmk` |
| クラウドプラットフォーム | Azure |
| サービス | vm |
| 重大度 | high |
| カテゴリ | Uncategorized |
| リソースタイプ | Microsoft.Compute/virtualMachines |
| リソースグループ | compute |

## 説明

Ensure that OS disks (boot volumes) and data disks (non-boot volumes) are encrypted with CMK (Customer Managed Keys). Customer Managed keys can be either ADE or Server Side Encryption (SSE).

## リスク

Encrypting the IaaS VM's OS disk (boot volume) and Data disks (non-boot volume) ensures that the entire content is fully unrecoverable without a key, thus protecting the volume from unwanted reads. PMK (Platform Managed Keys) are enabled by default in Azure-managed disks and allow encryption at rest. CMK is recommended because it gives the customer the option to control which specific keys are used for the encryption and decryption of the disk. The customer can then change keys and increase security by disabling them instead of relying on the PMK key that remains unchanging. There is also the option to increase security further by using automatically rotating keys so that access to disk is ensured to be limited. Organizations should evaluate what their security requirements are, however, for the data stored on the disk. For high-risk data using CMK is a must, as it provides extra steps of security. If the data is low risk, PMK is enabled by default and provides sufficient data security.

## 推奨事項

Note: Disks must be detached from VMs to have encryption changed. 1. Go to Virtual machines 2. For each virtual machine, go to Settings 3. Click on Disks 4. Click the ellipsis (...), then click Detach to detach the disk from the VM 5. Now search for Disks and locate the unattached disk 6. Click the disk then select Encryption 7. Change your encryption type, then select your encryption set 8. Click Save 9. Go back to the VM and re-attach the disk

- 推奨リンク：[https://learn.microsoft.com/en-us/azure/security/fundamentals/data-encryption-best-practices#protect-data-at-rest](https://learn.microsoft.com/en-us/azure/security/fundamentals/data-encryption-best-practices#protect-data-at-rest)

## 修正手順


### Terraform

[https://docs.ST Cloud.com/checks/azure/azure-general-policies/bc_azr_general_1#terraform](https://docs.ST Cloud.com/checks/azure/azure-general-policies/bc_azr_general_1#terraform)

### Other

[https://www.trendmicro.com/cloudoneconformity/knowledge-base/azure/VirtualMachines/sse-boot-disk-cmk.html#](https://www.trendmicro.com/cloudoneconformity/knowledge-base/azure/VirtualMachines/sse-boot-disk-cmk.html#)

## 参考資料

- [https://learn.microsoft.com/en-us/azure/virtual-machines/disk-encryption-overview](https://learn.microsoft.com/en-us/azure/virtual-machines/disk-encryption-overview)
- [https://learn.microsoft.com/en-us/azure/security/fundamentals/data-encryption-best-practices#protect-data-at-rest](https://learn.microsoft.com/en-us/azure/security/fundamentals/data-encryption-best-practices#protect-data-at-rest)

## 技術情報

- Source Metadata：[sources/azure/vm_ensure_attached_disks_encrypted_with_cmk/metadata.json](../../sources/azure/vm_ensure_attached_disks_encrypted_with_cmk/metadata.json)
- Source Code：[sources/azure/vm_ensure_attached_disks_encrypted_with_cmk/check.py](../../sources/azure/vm_ensure_attached_disks_encrypted_with_cmk/check.py)
- Source Metadata Path：`sources/azure/vm_ensure_attached_disks_encrypted_with_cmk/metadata.json`
- Source Code Path：`sources/azure/vm_ensure_attached_disks_encrypted_with_cmk/check.py`
