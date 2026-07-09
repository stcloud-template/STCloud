# Check for Empty Virtual Machine Scale Sets

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `vm_scaleset_not_empty` |
| 云平台 | Azure |
| 服务 | vm |
| 子服务 | scaleset |
| 严重等级 | low |
| 类别 | Uncategorized |
| 资源类型 | Microsoft.Compute/virtualMachineScaleSets |
| 资源组 | compute |

## 描述

Identify and remove empty virtual machine scale sets from your Azure cloud account.

## 风险

Empty virtual machine scale sets may incur unnecessary costs and complicate cloud resource management, impacting cost optimization and compliance.

## 推荐措施

Remove empty Azure virtual machine scale sets to optimize costs and simplify management.

- 推荐链接：[https://www.trendmicro.com/cloudoneconformity/knowledge-base/azure/VirtualMachines/empty-vm-scale-sets.html](https://www.trendmicro.com/cloudoneconformity/knowledge-base/azure/VirtualMachines/empty-vm-scale-sets.html)

## 修复步骤


### CLI

```text
az vmss delete --name <scale-set-name> --resource-group <resource-group>
```

### Other

[https://www.trendmicro.com/cloudoneconformity/knowledge-base/azure/VirtualMachines/empty-vm-scale-sets.html](https://www.trendmicro.com/cloudoneconformity/knowledge-base/azure/VirtualMachines/empty-vm-scale-sets.html)

## 参考资料

- [https://learn.microsoft.com/en-us/azure/virtual-machine-scale-sets/overview](https://learn.microsoft.com/en-us/azure/virtual-machine-scale-sets/overview)
- [https://www.trendmicro.com/cloudoneconformity/knowledge-base/azure/VirtualMachines/empty-vm-scale-sets.html](https://www.trendmicro.com/cloudoneconformity/knowledge-base/azure/VirtualMachines/empty-vm-scale-sets.html)

## 技术信息

- Source Metadata：[sources/azure/vm_scaleset_not_empty/metadata.json](../../sources/azure/vm_scaleset_not_empty/metadata.json)
- Source Code：[sources/azure/vm_scaleset_not_empty/check.py](../../sources/azure/vm_scaleset_not_empty/check.py)
- Source Metadata Path：`sources/azure/vm_scaleset_not_empty/metadata.json`
- Source Code Path：`sources/azure/vm_scaleset_not_empty/check.py`
