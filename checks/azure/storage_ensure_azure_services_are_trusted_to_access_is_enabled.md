# Ensure that 'Allow trusted Microsoft services to access this storage account' is enabled for storage accounts

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `storage_ensure_azure_services_are_trusted_to_access_is_enabled` |
| クラウドプラットフォーム | Azure |
| サービス | storage |
| 重大度 | medium |
| カテゴリ | Uncategorized |
| リソースタイプ | AzureStorageAccount |
| リソースグループ | storage |

## 説明

Ensure that 'Allow trusted Microsoft services to access this storage account' is enabled within your Azure Storage account configuration settings to grant access to trusted cloud services.

## リスク

Not allowing to access storage account by Azure services the following services: Azure Backup, Azure Event Grid, Azure Site Recovery, Azure DevTest Labs, Azure Event Hubs, Azure Networking, Azure Monitor and Azure SQL Data Warehouse (when registered in the subscription), are not granted access to your storage account

## 推奨事項

To allow these Azure services to work as intended and be able to access your storage account resources, you have to add an exception so that the trusted Microsoft Azure services can bypass your network rules

## 修正手順


### CLI

```text
az storage account update --name <StorageAccountName> --resource-group <resourceGroupName> --bypass AzureServices
```

### Terraform

[https://docs.ST Cloud.com/checks/azure/azure-networking-policies/enable-trusted-microsoft-services-for-storage-account-access#terraform](https://docs.ST Cloud.com/checks/azure/azure-networking-policies/enable-trusted-microsoft-services-for-storage-account-access#terraform)

### Other

[https://www.trendmicro.com/cloudoneconformity/knowledge-base/azure/StorageAccounts/enable-trusted-microsoft-services.html](https://www.trendmicro.com/cloudoneconformity/knowledge-base/azure/StorageAccounts/enable-trusted-microsoft-services.html)

## 参考資料

No external references available.

## 技術情報

- Source Metadata：[sources/azure/storage_ensure_azure_services_are_trusted_to_access_is_enabled/metadata.json](../../sources/azure/storage_ensure_azure_services_are_trusted_to_access_is_enabled/metadata.json)
- Source Code：[sources/azure/storage_ensure_azure_services_are_trusted_to_access_is_enabled/check.py](../../sources/azure/storage_ensure_azure_services_are_trusted_to_access_is_enabled/check.py)
- Source Metadata Path：`sources/azure/storage_ensure_azure_services_are_trusted_to_access_is_enabled/metadata.json`
- Source Code Path：`sources/azure/storage_ensure_azure_services_are_trusted_to_access_is_enabled/check.py`
