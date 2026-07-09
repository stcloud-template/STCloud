# Ensure that your virtual machine instances are using SKU sizes that are approved by your organization

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `vm_desired_sku_size` |
| 云平台 | Azure |
| 服务 | vm |
| 严重等级 | high |
| 类别 | Uncategorized |
| 资源类型 | Microsoft.Compute/virtualMachines |
| 资源组 | compute |

## 描述

Ensure that your virtual machine instances are using SKU sizes that are approved by your organization. This check requires configuration of the desired VM SKU sizes in the ST Cloud configuration file.

## 风险

Setting limits for the SKU size(s) of the virtual machine instances provisioned in your Microsoft Azure account can help you to manage better your cloud compute power, address internal compliance requirements and prevent unexpected charges on your Azure monthly bill. Without proper SKU size controls, organizations may face cost overruns and compliance violations.

## 推荐措施

1. Define and document your organization's approved VM SKU sizes based on workload requirements, cost constraints, and compliance needs. 2. Implement Azure Policy to enforce VM size restrictions across your subscriptions. 3. Use the 'Allowed virtual machine size SKUs' built-in policy to restrict VM creation to approved sizes. 4. Regularly review and update your approved SKU list based on changing business requirements and cost optimization goals. 5. Monitor VM usage and costs to ensure compliance with your SKU size policies.

- 推荐链接：[https://learn.microsoft.com/en-us/azure/virtual-machines/sizes/resize-vm](https://learn.microsoft.com/en-us/azure/virtual-machines/sizes/resize-vm)

## 修复步骤


### CLI

```text
az policy assignment create --display-name 'Allowed VM SKU Sizes' --policy cccc23c7-8427-4f53-ad12-b6a63eb452b3 -p '{"listOfAllowedSKUs": {"value": ["<desired-sku-1>", "<desired-sku-2>"]}}' --scope /subscriptions/<subscription-id>
```

## 参考资料

- [https://learn.microsoft.com/en-us/azure/virtual-machines/sizes/overview](https://learn.microsoft.com/en-us/azure/virtual-machines/sizes/overview)
- [https://learn.microsoft.com/en-us/azure/virtual-machines/sizes/resize-vm](https://learn.microsoft.com/en-us/azure/virtual-machines/sizes/resize-vm)

## 技术信息

- Source Metadata：[sources/azure/vm_desired_sku_size/metadata.json](../../sources/azure/vm_desired_sku_size/metadata.json)
- Source Code：[sources/azure/vm_desired_sku_size/check.py](../../sources/azure/vm_desired_sku_size/check.py)
- Source Metadata Path：`sources/azure/vm_desired_sku_size/metadata.json`
- Source Code Path：`sources/azure/vm_desired_sku_size/check.py`
