# Check for Empty Virtual Machine Scale Sets

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `vm_scaleset_not_empty` |
| クラウドプラットフォーム | Azure |
| サービス | vm |
| サブサービス | scaleset |
| 重大度 | low |
| カテゴリ | Uncategorized |
| リソースタイプ | Microsoft.Compute/virtualMachineScaleSets |
| リソースグループ | compute |

## 説明

Identify and remove empty virtual machine scale sets from your Azure cloud account.

## リスク

Empty virtual machine scale sets may incur unnecessary costs and complicate cloud resource management, impacting cost optimization and compliance.

## 推奨事項

Remove empty Azure virtual machine scale sets to optimize costs and simplify management.

- 推奨リンク：[https://www.trendmicro.com/cloudoneconformity/knowledge-base/azure/VirtualMachines/empty-vm-scale-sets.html](https://www.trendmicro.com/cloudoneconformity/knowledge-base/azure/VirtualMachines/empty-vm-scale-sets.html)

## 修正手順


### CLI

```text
az vmss delete --name <scale-set-name> --resource-group <resource-group>
```

### Other

[https://www.trendmicro.com/cloudoneconformity/knowledge-base/azure/VirtualMachines/empty-vm-scale-sets.html](https://www.trendmicro.com/cloudoneconformity/knowledge-base/azure/VirtualMachines/empty-vm-scale-sets.html)

## 参考資料

- [https://learn.microsoft.com/en-us/azure/virtual-machine-scale-sets/overview](https://learn.microsoft.com/en-us/azure/virtual-machine-scale-sets/overview)
- [https://www.trendmicro.com/cloudoneconformity/knowledge-base/azure/VirtualMachines/empty-vm-scale-sets.html](https://www.trendmicro.com/cloudoneconformity/knowledge-base/azure/VirtualMachines/empty-vm-scale-sets.html)

## 技術情報

- Source Metadata：[sources/azure/vm_scaleset_not_empty/metadata.json](../../sources/azure/vm_scaleset_not_empty/metadata.json)
- Source Code：[sources/azure/vm_scaleset_not_empty/check.py](../../sources/azure/vm_scaleset_not_empty/check.py)
- Source Metadata Path：`sources/azure/vm_scaleset_not_empty/metadata.json`
- Source Code Path：`sources/azure/vm_scaleset_not_empty/check.py`
