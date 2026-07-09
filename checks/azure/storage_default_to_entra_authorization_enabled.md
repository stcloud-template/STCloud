# Ensure Microsoft Entra authorization is enabled by default for Azure Storage Accounts

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `storage_default_to_entra_authorization_enabled` |
| 云平台 | Azure |
| 服务 | storage |
| 严重等级 | high |
| 类别 | Uncategorized |
| 资源类型 | AzureStorageAccount |
| 资源组 | storage |

## 描述

Ensure that the Azure Storage Account setting 'Default to Microsoft Entra authorization in the Azure portal' is enabled to enforce the use of Microsoft Entra ID for accessing blobs, files, queues, and tables.

## 风险

If this setting is not enabled, the Azure portal may authorize access using less secure methods such as Shared Key, increasing the risk of unauthorized data access.

## 推荐措施

Enable Microsoft Entra authorization by default in the Azure portal to enhance security and avoid reliance on Shared Key authentication.

- 推荐链接：[https://learn.microsoft.com/en-us/azure/storage/blobs/authorize-access-azure-active-directory](https://learn.microsoft.com/en-us/azure/storage/blobs/authorize-access-azure-active-directory)

## 修复步骤


### CLI

```text
az storage account update --name <storage-account-name> --resource-group <resource-group-name> --default-to-AzAd-auth true
```

### Other

[https://www.trendmicro.com/cloudoneconformity-staging/knowledge-base/azure/StorageAccounts/enable-microsoft-entra-authorization-by-default.html](https://www.trendmicro.com/cloudoneconformity-staging/knowledge-base/azure/StorageAccounts/enable-microsoft-entra-authorization-by-default.html)

## 参考资料

- [https://learn.microsoft.com/en-us/azure/storage/blobs/authorize-access-azure-active-directory](https://learn.microsoft.com/en-us/azure/storage/blobs/authorize-access-azure-active-directory)

## 技术信息

- Source Metadata：[sources/azure/storage_default_to_entra_authorization_enabled/metadata.json](../../sources/azure/storage_default_to_entra_authorization_enabled/metadata.json)
- Source Code：[sources/azure/storage_default_to_entra_authorization_enabled/check.py](../../sources/azure/storage_default_to_entra_authorization_enabled/check.py)
- Source Metadata Path：`sources/azure/storage_default_to_entra_authorization_enabled/metadata.json`
- Source Code Path：`sources/azure/storage_default_to_entra_authorization_enabled/check.py`
