# VM Scale Set Is Associated With Load Balancer

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `vm_scaleset_associated_with_load_balancer` |
| クラウドプラットフォーム | Azure |
| サービス | vm |
| サブサービス | scaleset |
| 重大度 | medium |
| カテゴリ | Uncategorized |
| リソースタイプ | Microsoft.Compute/virtualMachineScaleSets |
| リソースグループ | compute |

## 説明

Ensure that your Azure virtual machine scale sets are using load balancers for traffic distribution.

## リスク

Without load balancer integration, Azure virtual machine scale sets may experience reduced availability and potential service disruptions during traffic spikes or instance failures, leading to degraded user experience and potential business impact.

## 推奨事項

Attach a load balancer to your Azure virtual machine scale set to ensure high availability and optimal traffic distribution.

- 推奨リンク：[https://docs.microsoft.com/en-us/azure/load-balancer/load-balancer-overview](https://docs.microsoft.com/en-us/azure/load-balancer/load-balancer-overview)

## 修正手順


### Other

[https://www.trendmicro.com/cloudoneconformity/knowledge-base/azure/VirtualMachines/associated-load-balancers.html](https://www.trendmicro.com/cloudoneconformity/knowledge-base/azure/VirtualMachines/associated-load-balancers.html)

## 参考資料

- [https://learn.microsoft.com/en-us/azure/virtual-network/network-overview](https://learn.microsoft.com/en-us/azure/virtual-network/network-overview)
- [https://docs.microsoft.com/en-us/azure/load-balancer/load-balancer-overview](https://docs.microsoft.com/en-us/azure/load-balancer/load-balancer-overview)

## 技術情報

- Source Metadata：[sources/azure/vm_scaleset_associated_with_load_balancer/metadata.json](../../sources/azure/vm_scaleset_associated_with_load_balancer/metadata.json)
- Source Code：[sources/azure/vm_scaleset_associated_with_load_balancer/check.py](../../sources/azure/vm_scaleset_associated_with_load_balancer/check.py)
- Source Metadata Path：`sources/azure/vm_scaleset_associated_with_load_balancer/metadata.json`
- Source Code Path：`sources/azure/vm_scaleset_associated_with_load_balancer/check.py`
