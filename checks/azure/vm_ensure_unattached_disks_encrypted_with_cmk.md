# Ensure that 'Unattached disks' are encrypted with 'Customer Managed Key' (CMK)

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `vm_ensure_unattached_disks_encrypted_with_cmk` |
| クラウドプラットフォーム | Azure |
| サービス | vm |
| 重大度 | high |
| カテゴリ | Uncategorized |
| リソースタイプ | Microsoft.Compute/virtualMachines |
| リソースグループ | compute |

## 説明

Ensure that unattached disks in a subscription are encrypted with a Customer Managed Key (CMK).

## リスク

Managed disks are encrypted by default with Platform-managed keys. Using Customer-managed keys may provide an additional level of security or meet an organization's regulatory requirements. Encrypting managed disks ensures that its entire content is fully unrecoverable without a key and thus protects the volume from unwarranted reads. Even if the disk is not attached to any of the VMs, there is always a risk where a compromised user account with administrative access to VM service can mount/attach these data disks, which may lead to sensitive information disclosure and tampering.

## 推奨事項

If data stored in the disk is no longer useful, refer to Azure documentation to delete unattached data disks at: https://learn.microsoft.com/en-us/rest/api/compute/disks/delete?view=rest-compute-2023-10-02&tabs=HTTP

- 推奨リンク：[https://learn.microsoft.com/en-us/azure/security/fundamentals/data-encryption-best-practices#protect-data-at-rest](https://learn.microsoft.com/en-us/azure/security/fundamentals/data-encryption-best-practices#protect-data-at-rest)

## 修正手順


### Other

[https://www.trendmicro.com/cloudoneconformity/knowledge-base/azure/VirtualMachines/sse-unattached-disk-cmk.html#](https://www.trendmicro.com/cloudoneconformity/knowledge-base/azure/VirtualMachines/sse-unattached-disk-cmk.html#)

## 参考資料

- [https://docs.microsoft.com/en-us/azure/security/fundamentals/azure-disk-encryption-vms-vmss](https://docs.microsoft.com/en-us/azure/security/fundamentals/azure-disk-encryption-vms-vmss)
- [https://learn.microsoft.com/en-us/azure/security/fundamentals/data-encryption-best-practices#protect-data-at-rest](https://learn.microsoft.com/en-us/azure/security/fundamentals/data-encryption-best-practices#protect-data-at-rest)

## 技術情報

- Source Metadata：[sources/azure/vm_ensure_unattached_disks_encrypted_with_cmk/metadata.json](../../sources/azure/vm_ensure_unattached_disks_encrypted_with_cmk/metadata.json)
- Source Code：[sources/azure/vm_ensure_unattached_disks_encrypted_with_cmk/check.py](../../sources/azure/vm_ensure_unattached_disks_encrypted_with_cmk/check.py)
- Source Metadata Path：`sources/azure/vm_ensure_unattached_disks_encrypted_with_cmk/metadata.json`
- Source Code Path：`sources/azure/vm_ensure_unattached_disks_encrypted_with_cmk/check.py`
