# Ensure Soft Delete is Enabled for Azure Containers and Blob Storage

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `storage_ensure_soft_delete_is_enabled` |
| 云平台 | Azure |
| 服务 | storage |
| 严重等级 | medium |
| 类别 | encryption |
| 资源类型 | AzureStorageAccount |
| 资源组 | storage |

## 描述

The Azure Storage blobs contain data like ePHI or Financial, which can be secret or personal. Data that is erroneously modified or deleted by an application or other storage account user will cause data loss or unavailability.

## 风险

Containers and Blob Storage data can be incorrectly deleted. An attacker/malicious user may do this deliberately in order to cause disruption. Deleting an Azure Storage blob causes immediate data loss. Enabling this configuration for Azure storage ensures that even if blobs/data were deleted from the storage account, Blobs/data objects are recoverable for a particular time which is set in the Retention policies ranging from 7 days to 365 days.

## 推荐措施

From the Azure home page, open the hamburger menu in the top left or click on the arrow pointing right with 'More services' underneath. 2. Select Storage. 3. Select Storage Accounts. 4. For each Storage Account, navigate to Data protection in the left scroll column. 5. Check soft delete for both blobs and containers. Set the retention period to a sufficient length for your organization

- 推荐链接：[https://docs.microsoft.com/en-us/azure/storage/blobs/storage-blob-soft-delete](https://docs.microsoft.com/en-us/azure/storage/blobs/storage-blob-soft-delete)

## 修复步骤


### Other

[https://www.trendmicro.com/cloudoneconformity-staging/knowledge-base/azure/StorageAccounts/enable-soft-delete.html#](https://www.trendmicro.com/cloudoneconformity-staging/knowledge-base/azure/StorageAccounts/enable-soft-delete.html#)

## 参考资料

- [https://learn.microsoft.com/en-us/azure/storage/blobs/soft-delete-blob-enable?tabs=azure-portal](https://learn.microsoft.com/en-us/azure/storage/blobs/soft-delete-blob-enable?tabs=azure-portal)
- [https://docs.microsoft.com/en-us/azure/storage/blobs/storage-blob-soft-delete](https://docs.microsoft.com/en-us/azure/storage/blobs/storage-blob-soft-delete)

## 技术信息

- Source Metadata：[sources/azure/storage_ensure_soft_delete_is_enabled/metadata.json](../../sources/azure/storage_ensure_soft_delete_is_enabled/metadata.json)
- Source Code：[sources/azure/storage_ensure_soft_delete_is_enabled/check.py](../../sources/azure/storage_ensure_soft_delete_is_enabled/check.py)
- Source Metadata Path：`sources/azure/storage_ensure_soft_delete_is_enabled/metadata.json`
- Source Code Path：`sources/azure/storage_ensure_soft_delete_is_enabled/check.py`
