# Ensure Soft Delete is Enabled for Azure Containers and Blob Storage

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `storage_ensure_soft_delete_is_enabled` |
| クラウドプラットフォーム | Azure |
| サービス | storage |
| 重大度 | medium |
| カテゴリ | encryption |
| リソースタイプ | AzureStorageAccount |
| リソースグループ | storage |

## 説明

The Azure Storage blobs contain data like ePHI or Financial, which can be secret or personal. Data that is erroneously modified or deleted by an application or other storage account user will cause data loss or unavailability.

## リスク

Containers and Blob Storage data can be incorrectly deleted. An attacker/malicious user may do this deliberately in order to cause disruption. Deleting an Azure Storage blob causes immediate data loss. Enabling this configuration for Azure storage ensures that even if blobs/data were deleted from the storage account, Blobs/data objects are recoverable for a particular time which is set in the Retention policies ranging from 7 days to 365 days.

## 推奨事項

From the Azure home page, open the hamburger menu in the top left or click on the arrow pointing right with 'More services' underneath. 2. Select Storage. 3. Select Storage Accounts. 4. For each Storage Account, navigate to Data protection in the left scroll column. 5. Check soft delete for both blobs and containers. Set the retention period to a sufficient length for your organization

- 推奨リンク：[https://docs.microsoft.com/en-us/azure/storage/blobs/storage-blob-soft-delete](https://docs.microsoft.com/en-us/azure/storage/blobs/storage-blob-soft-delete)

## 修正手順


### Other

[https://www.trendmicro.com/cloudoneconformity-staging/knowledge-base/azure/StorageAccounts/enable-soft-delete.html#](https://www.trendmicro.com/cloudoneconformity-staging/knowledge-base/azure/StorageAccounts/enable-soft-delete.html#)

## 参考資料

- [https://learn.microsoft.com/en-us/azure/storage/blobs/soft-delete-blob-enable?tabs=azure-portal](https://learn.microsoft.com/en-us/azure/storage/blobs/soft-delete-blob-enable?tabs=azure-portal)
- [https://docs.microsoft.com/en-us/azure/storage/blobs/storage-blob-soft-delete](https://docs.microsoft.com/en-us/azure/storage/blobs/storage-blob-soft-delete)

## 技術情報

- Source Metadata：[sources/azure/storage_ensure_soft_delete_is_enabled/metadata.json](../../sources/azure/storage_ensure_soft_delete_is_enabled/metadata.json)
- Source Code：[sources/azure/storage_ensure_soft_delete_is_enabled/check.py](../../sources/azure/storage_ensure_soft_delete_is_enabled/check.py)
- Source Metadata Path：`sources/azure/storage_ensure_soft_delete_is_enabled/metadata.json`
- Source Code Path：`sources/azure/storage_ensure_soft_delete_is_enabled/check.py`
