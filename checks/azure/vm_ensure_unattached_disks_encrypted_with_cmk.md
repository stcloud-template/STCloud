# Ensure that 'Unattached disks' are encrypted with 'Customer Managed Key' (CMK)

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `vm_ensure_unattached_disks_encrypted_with_cmk` |
| 云平台 | Azure |
| 服务 | vm |
| 严重等级 | high |
| 类别 | Uncategorized |
| 资源类型 | Microsoft.Compute/virtualMachines |
| 资源组 | compute |

## 描述

Ensure that unattached disks in a subscription are encrypted with a Customer Managed Key (CMK).

## 风险

Managed disks are encrypted by default with Platform-managed keys. Using Customer-managed keys may provide an additional level of security or meet an organization's regulatory requirements. Encrypting managed disks ensures that its entire content is fully unrecoverable without a key and thus protects the volume from unwarranted reads. Even if the disk is not attached to any of the VMs, there is always a risk where a compromised user account with administrative access to VM service can mount/attach these data disks, which may lead to sensitive information disclosure and tampering.

## 推荐措施

If data stored in the disk is no longer useful, refer to Azure documentation to delete unattached data disks at: https://learn.microsoft.com/en-us/rest/api/compute/disks/delete?view=rest-compute-2023-10-02&tabs=HTTP

- 推荐链接：[https://learn.microsoft.com/en-us/azure/security/fundamentals/data-encryption-best-practices#protect-data-at-rest](https://learn.microsoft.com/en-us/azure/security/fundamentals/data-encryption-best-practices#protect-data-at-rest)

## 修复步骤


### Other

[https://www.trendmicro.com/cloudoneconformity/knowledge-base/azure/VirtualMachines/sse-unattached-disk-cmk.html#](https://www.trendmicro.com/cloudoneconformity/knowledge-base/azure/VirtualMachines/sse-unattached-disk-cmk.html#)

## 参考资料

- [https://docs.microsoft.com/en-us/azure/security/fundamentals/azure-disk-encryption-vms-vmss](https://docs.microsoft.com/en-us/azure/security/fundamentals/azure-disk-encryption-vms-vmss)
- [https://learn.microsoft.com/en-us/azure/security/fundamentals/data-encryption-best-practices#protect-data-at-rest](https://learn.microsoft.com/en-us/azure/security/fundamentals/data-encryption-best-practices#protect-data-at-rest)

## 技术信息

- Source Metadata：[sources/azure/vm_ensure_unattached_disks_encrypted_with_cmk/metadata.json](../../sources/azure/vm_ensure_unattached_disks_encrypted_with_cmk/metadata.json)
- Source Code：[sources/azure/vm_ensure_unattached_disks_encrypted_with_cmk/check.py](../../sources/azure/vm_ensure_unattached_disks_encrypted_with_cmk/check.py)
- Source Metadata Path：`sources/azure/vm_ensure_unattached_disks_encrypted_with_cmk/metadata.json`
- Source Code Path：`sources/azure/vm_ensure_unattached_disks_encrypted_with_cmk/check.py`
