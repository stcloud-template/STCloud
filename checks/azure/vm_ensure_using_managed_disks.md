# Ensure Virtual Machines are utilizing Managed Disks

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `vm_ensure_using_managed_disks` |
| 云平台 | Azure |
| 服务 | vm |
| 严重等级 | medium |
| 类别 | Uncategorized |
| 资源类型 | Microsoft.Compute/virtualMachines |
| 资源组 | compute |

## 描述

Migrate blob-based VHDs to Managed Disks on Virtual Machines to exploit the default features of this configuration. The features include: 1. Default Disk Encryption 2. Resilience, as Microsoft will managed the disk storage and move around if underlying hardware goes faulty 3. Reduction of costs over storage accounts

## 风险

Managed disks are by default encrypted on the underlying hardware, so no additional encryption is required for basic protection. It is available if additional encryption is required. Managed disks are by design more resilient that storage accounts. For ARM-deployed Virtual Machines, Azure Adviser will at some point recommend moving VHDs to managed disks both from a security and cost management perspective.

## 推荐措施

1. Using the search feature, go to Virtual Machines 2. Select the virtual machine you would like to convert 3. Select Disks in the menu for the VM 4. At the top select Migrate to managed disks 5. You may follow the prompts to convert the disk and finish by selecting Migrate to start the process

- 推荐链接：[https://docs.microsoft.com/en-us/security/benchmark/azure/security-controls-v3-data-protection#dp-4-enable-data-at-rest-encryption-by-default](https://docs.microsoft.com/en-us/security/benchmark/azure/security-controls-v3-data-protection#dp-4-enable-data-at-rest-encryption-by-default)

## 修复步骤


### Terraform

[https://docs.ST Cloud.com/checks/azure/azure-general-policies/ensure-virtual-machines-are-utilizing-managed-disks#terraform](https://docs.ST Cloud.com/checks/azure/azure-general-policies/ensure-virtual-machines-are-utilizing-managed-disks#terraform)

### Other

[https://www.trendmicro.com/cloudoneconformity/knowledge-base/azure/VirtualMachines/managed-disks-in-use.html](https://www.trendmicro.com/cloudoneconformity/knowledge-base/azure/VirtualMachines/managed-disks-in-use.html)

## 参考资料

- [https://learn.microsoft.com/en-us/azure/virtual-machines/unmanaged-disks-deprecation](https://learn.microsoft.com/en-us/azure/virtual-machines/unmanaged-disks-deprecation)
- [https://docs.microsoft.com/en-us/security/benchmark/azure/security-controls-v3-data-protection#dp-4-enable-data-at-rest-encryption-by-default](https://docs.microsoft.com/en-us/security/benchmark/azure/security-controls-v3-data-protection#dp-4-enable-data-at-rest-encryption-by-default)

## 技术信息

- Source Metadata：[sources/azure/vm_ensure_using_managed_disks/metadata.json](../../sources/azure/vm_ensure_using_managed_disks/metadata.json)
- Source Code：[sources/azure/vm_ensure_using_managed_disks/check.py](../../sources/azure/vm_ensure_using_managed_disks/check.py)
- Source Metadata Path：`sources/azure/vm_ensure_using_managed_disks/metadata.json`
- Source Code Path：`sources/azure/vm_ensure_using_managed_disks/check.py`
