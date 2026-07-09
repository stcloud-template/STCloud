# Ensure that 'Allow trusted Microsoft services to access this storage account' is enabled for storage accounts

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `storage_ensure_azure_services_are_trusted_to_access_is_enabled` |
| 云平台 | Azure |
| 服务 | storage |
| 严重等级 | medium |
| 类别 | Uncategorized |
| 资源类型 | AzureStorageAccount |
| 资源组 | storage |

## 描述

Ensure that 'Allow trusted Microsoft services to access this storage account' is enabled within your Azure Storage account configuration settings to grant access to trusted cloud services.

## 风险

Not allowing to access storage account by Azure services the following services: Azure Backup, Azure Event Grid, Azure Site Recovery, Azure DevTest Labs, Azure Event Hubs, Azure Networking, Azure Monitor and Azure SQL Data Warehouse (when registered in the subscription), are not granted access to your storage account

## 推荐措施

To allow these Azure services to work as intended and be able to access your storage account resources, you have to add an exception so that the trusted Microsoft Azure services can bypass your network rules

## 修复步骤


### CLI

```text
az storage account update --name <StorageAccountName> --resource-group <resourceGroupName> --bypass AzureServices
```

### Terraform

[https://docs.ST Cloud.com/checks/azure/azure-networking-policies/enable-trusted-microsoft-services-for-storage-account-access#terraform](https://docs.ST Cloud.com/checks/azure/azure-networking-policies/enable-trusted-microsoft-services-for-storage-account-access#terraform)

### Other

[https://www.trendmicro.com/cloudoneconformity/knowledge-base/azure/StorageAccounts/enable-trusted-microsoft-services.html](https://www.trendmicro.com/cloudoneconformity/knowledge-base/azure/StorageAccounts/enable-trusted-microsoft-services.html)

## 参考资料

No external references available.

## 技术信息

- Source Metadata：[sources/azure/storage_ensure_azure_services_are_trusted_to_access_is_enabled/metadata.json](../../sources/azure/storage_ensure_azure_services_are_trusted_to_access_is_enabled/metadata.json)
- Source Code：[sources/azure/storage_ensure_azure_services_are_trusted_to_access_is_enabled/check.py](../../sources/azure/storage_ensure_azure_services_are_trusted_to_access_is_enabled/check.py)
- Source Metadata Path：`sources/azure/storage_ensure_azure_services_are_trusted_to_access_is_enabled/metadata.json`
- Source Code Path：`sources/azure/storage_ensure_azure_services_are_trusted_to_access_is_enabled/check.py`
