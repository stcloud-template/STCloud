# Ensure soft delete for Azure File Shares is enabled

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `storage_ensure_file_shares_soft_delete_is_enabled` |
| 云平台 | Azure |
| 服务 | storage |
| 严重等级 | medium |
| 类别 | Uncategorized |
| 资源类型 | AzureStorageAccount |
| 资源组 | storage |

## 描述

Ensure that soft delete is enabled for Azure File Shares to protect against accidental or malicious deletion of important data. This feature allows deleted file shares to be retained for a specified period, during which they can be recovered before permanent deletion occurs.

## 风险

Without soft delete enabled, accidental or malicious deletions of file shares result in permanent data loss, making recovery impossible unless a separate backup mechanism is in place.

## 推荐措施

Enable soft delete for file shares on your Azure Storage Account to allow recovery of deleted shares within a configured retention period.

- 推荐链接：[https://learn.microsoft.com/en-us/azure/storage/files/storage-files-prevent-file-share-deletion?tabs=azure-portal](https://learn.microsoft.com/en-us/azure/storage/files/storage-files-prevent-file-share-deletion?tabs=azure-portal)

## 修复步骤


### CLI

```text
az storage account file-service-properties update --account-name <storage-account-name> --enable-delete-retention true --delete-retention-days <number-of-days>
```

### Other

[https://www.trendmicro.com/cloudoneconformity-staging/knowledge-base/azure/StorageAccounts/enable-soft-delete-for-file-shares.html](https://www.trendmicro.com/cloudoneconformity-staging/knowledge-base/azure/StorageAccounts/enable-soft-delete-for-file-shares.html)

## 参考资料

- [https://learn.microsoft.com/en-us/azure/storage/files/storage-files-prevent-file-share-deletion?tabs=azure-portal](https://learn.microsoft.com/en-us/azure/storage/files/storage-files-prevent-file-share-deletion?tabs=azure-portal)

## 技术信息

- Source Metadata：[sources/azure/storage_ensure_file_shares_soft_delete_is_enabled/metadata.json](../../sources/azure/storage_ensure_file_shares_soft_delete_is_enabled/metadata.json)
- Source Code：[sources/azure/storage_ensure_file_shares_soft_delete_is_enabled/check.py](../../sources/azure/storage_ensure_file_shares_soft_delete_is_enabled/check.py)
- Source Metadata Path：`sources/azure/storage_ensure_file_shares_soft_delete_is_enabled/metadata.json`
- Source Code Path：`sources/azure/storage_ensure_file_shares_soft_delete_is_enabled/check.py`
