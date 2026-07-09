# Ensure Azure Databricks workspaces are deployed in a customer-managed VNet (VNet Injection)

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `databricks_workspace_vnet_injection_enabled` |
| 云平台 | Azure |
| 服务 | databricks |
| 严重等级 | medium |
| 类别 | Uncategorized |
| 资源类型 | AzureDatabricksWorkspace |
| 资源组 | ai_ml |

## 描述

Checks whether Azure Databricks workspaces are deployed in a customer-managed Virtual Network (VNet Injection) instead of a Databricks-managed VNet.

## 风险

Using a Databricks-managed VNet limits control over network security policies, firewall configurations, and routing, increasing the risk of unauthorized access or data exfiltration.

## 推荐措施

Deploy Databricks workspaces into a customer-managed VNet to ensure better control over network security and compliance.

- 推荐链接：[https://www.trendmicro.com/cloudoneconformity/knowledge-base/azure/Databricks/check-for-vnet-injection.html](https://www.trendmicro.com/cloudoneconformity/knowledge-base/azure/Databricks/check-for-vnet-injection.html)

## 修复步骤


### CLI

```text
az databricks workspace create --name <databricks-workspace-name> --resource-group <resource-group-name> --location <region> --managed-resource-group <managed-rg-name> --enable-no-public-ip true --network-security-group-rule "NoAzureServices" --public-network-access Disabled --custom-virtual-network-id /subscriptions/<subscription-id>/resourceGroups/<resource-group-name>/providers/Microsoft.Network/virtualNetworks/<vnet-name>
```

## 参考资料

- [https://learn.microsoft.com/en-us/azure/databricks/administration-guide/cloud-configurations/azure/vnet-inject](https://learn.microsoft.com/en-us/azure/databricks/administration-guide/cloud-configurations/azure/vnet-inject)
- [https://www.trendmicro.com/cloudoneconformity/knowledge-base/azure/Databricks/check-for-vnet-injection.html](https://www.trendmicro.com/cloudoneconformity/knowledge-base/azure/Databricks/check-for-vnet-injection.html)

## 技术信息

- Source Metadata：[sources/azure/databricks_workspace_vnet_injection_enabled/metadata.json](../../sources/azure/databricks_workspace_vnet_injection_enabled/metadata.json)
- Source Code：[sources/azure/databricks_workspace_vnet_injection_enabled/check.py](../../sources/azure/databricks_workspace_vnet_injection_enabled/check.py)
- Source Metadata Path：`sources/azure/databricks_workspace_vnet_injection_enabled/metadata.json`
- Source Code Path：`sources/azure/databricks_workspace_vnet_injection_enabled/check.py`
