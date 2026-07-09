# Ensure that Storage Account Access Keys are Periodically Regenerated

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `storage_key_rotation_90_days` |
| 云平台 | Azure |
| 服务 | storage |
| 严重等级 | medium |
| 类别 | encryption |
| 资源类型 | AzureStorageAccount |
| 资源组 | storage |

## 描述

Ensure that Storage Account Access Keys are Periodically Regenerated

## 风险

If the access keys are not regenerated periodically, the likelihood of accidental exposures increases, which can lead to unauthorized access to your storage account resources.

## 推荐措施

Ensure that Azure Storage account access keys are regenerated every 90 days in order to decrease the likelihood of accidental exposures and protect your storage account resources against unauthorized access.

- 推荐链接：[https://learn.microsoft.com/en-us/azure/storage/common/storage-account-create?tabs=azure-portal#regenerate-storage-access-keys](https://learn.microsoft.com/en-us/azure/storage/common/storage-account-create?tabs=azure-portal#regenerate-storage-access-keys)

## 修复步骤


### Other

[https://www.trendmicro.com/cloudoneconformity-staging/knowledge-base/azure/StorageAccounts/regenerate-storage-account-access-keys-periodically.html#](https://www.trendmicro.com/cloudoneconformity-staging/knowledge-base/azure/StorageAccounts/regenerate-storage-account-access-keys-periodically.html#)

## 参考资料

- [https://learn.microsoft.com/en-us/azure/storage/common/storage-account-keys-manage?tabs=azure-portal](https://learn.microsoft.com/en-us/azure/storage/common/storage-account-keys-manage?tabs=azure-portal)
- [https://learn.microsoft.com/en-us/azure/storage/common/storage-account-create?tabs=azure-portal#regenerate-storage-access-keys](https://learn.microsoft.com/en-us/azure/storage/common/storage-account-create?tabs=azure-portal#regenerate-storage-access-keys)

## 技术信息

- Source Metadata：[sources/azure/storage_key_rotation_90_days/metadata.json](../../sources/azure/storage_key_rotation_90_days/metadata.json)
- Source Code：[sources/azure/storage_key_rotation_90_days/check.py](../../sources/azure/storage_key_rotation_90_days/check.py)
- Source Metadata Path：`sources/azure/storage_key_rotation_90_days/metadata.json`
- Source Code Path：`sources/azure/storage_key_rotation_90_days/check.py`
