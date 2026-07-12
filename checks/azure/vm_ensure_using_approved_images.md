# Ensure that Azure VMs are using an approved machine image.

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `vm_ensure_using_approved_images` |
| クラウドプラットフォーム | Azure |
| サービス | vm |
| サブサービス | image |
| 重大度 | medium |
| カテゴリ | Uncategorized |
| リソースタイプ | Microsoft.Compute/images |
| リソースグループ | compute |

## 説明

Ensure that all your Azure virtual machine instances are launched from approved machine images only.

## リスク

An approved machine image is a custom virtual machine (VM) image that contains a pre-configured OS and a well-defined stack of server software approved by Azure, fully configured to run your application. Using approved (golden) machine images to launch new VM instances within your Azure cloud environment brings major benefits such as fast and stable application deployment and scaling, secure application stack upgrades, and versioning.

## 推奨事項

Re-create the required VM instances using the approved (golden) machine image.

- 推奨リンク：[https://docs.microsoft.com/en-us/azure/virtual-machines/windows/create-vm-generalized-managed](https://docs.microsoft.com/en-us/azure/virtual-machines/windows/create-vm-generalized-managed)

## 修正手順


### Other

[https://www.trendmicro.com/cloudoneconformity/knowledge-base/azure/VirtualMachines/approved-machine-image.html](https://www.trendmicro.com/cloudoneconformity/knowledge-base/azure/VirtualMachines/approved-machine-image.html)

## 参考資料

- [https://learn.microsoft.com/en-us/azure/virtual-machines/windows/create-vm-generalized-managed](https://learn.microsoft.com/en-us/azure/virtual-machines/windows/create-vm-generalized-managed)
- [https://docs.microsoft.com/en-us/azure/virtual-machines/windows/create-vm-generalized-managed](https://docs.microsoft.com/en-us/azure/virtual-machines/windows/create-vm-generalized-managed)

## 技術情報

- Source Metadata：[sources/azure/vm_ensure_using_approved_images/metadata.json](../../sources/azure/vm_ensure_using_approved_images/metadata.json)
- Source Code：[sources/azure/vm_ensure_using_approved_images/check.py](../../sources/azure/vm_ensure_using_approved_images/check.py)
- Source Metadata Path：`sources/azure/vm_ensure_using_approved_images/metadata.json`
- Source Code Path：`sources/azure/vm_ensure_using_approved_images/check.py`
