# VM Scale Set Is Associated With Load Balancer

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `vm_scaleset_associated_with_load_balancer` |
| 云平台 | Azure |
| 服务 | vm |
| 子服务 | scaleset |
| 严重等级 | medium |
| 类别 | Uncategorized |
| 资源类型 | Microsoft.Compute/virtualMachineScaleSets |
| 资源组 | compute |

## 描述

Ensure that your Azure virtual machine scale sets are using load balancers for traffic distribution.

## 风险

Without load balancer integration, Azure virtual machine scale sets may experience reduced availability and potential service disruptions during traffic spikes or instance failures, leading to degraded user experience and potential business impact.

## 推荐措施

Attach a load balancer to your Azure virtual machine scale set to ensure high availability and optimal traffic distribution.

- 推荐链接：[https://docs.microsoft.com/en-us/azure/load-balancer/load-balancer-overview](https://docs.microsoft.com/en-us/azure/load-balancer/load-balancer-overview)

## 修复步骤


### Other

[https://www.trendmicro.com/cloudoneconformity/knowledge-base/azure/VirtualMachines/associated-load-balancers.html](https://www.trendmicro.com/cloudoneconformity/knowledge-base/azure/VirtualMachines/associated-load-balancers.html)

## 参考资料

- [https://learn.microsoft.com/en-us/azure/virtual-network/network-overview](https://learn.microsoft.com/en-us/azure/virtual-network/network-overview)
- [https://docs.microsoft.com/en-us/azure/load-balancer/load-balancer-overview](https://docs.microsoft.com/en-us/azure/load-balancer/load-balancer-overview)

## 技术信息

- Source Metadata：[sources/azure/vm_scaleset_associated_with_load_balancer/metadata.json](../../sources/azure/vm_scaleset_associated_with_load_balancer/metadata.json)
- Source Code：[sources/azure/vm_scaleset_associated_with_load_balancer/check.py](../../sources/azure/vm_scaleset_associated_with_load_balancer/check.py)
- Source Metadata Path：`sources/azure/vm_scaleset_associated_with_load_balancer/metadata.json`
- Source Code Path：`sources/azure/vm_scaleset_associated_with_load_balancer/check.py`
