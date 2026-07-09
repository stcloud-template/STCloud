# Ensure that the 'Public access level' is set to 'Private (no anonymous access)' for all blob containers in your storage account

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `storage_blob_public_access_level_is_disabled` |
| 云平台 | Azure |
| 服务 | storage |
| 严重等级 | medium |
| 类别 | Uncategorized |
| 资源类型 | AzureStorageAccount |
| 资源组 | storage |

## 描述

Ensure that the 'Public access level' configuration setting is set to 'Private (no anonymous access)' for all blob containers in your storage account in order to block anonymous access to these Microsoft Azure resources.

## 风险

A user that accesses blob containers anonymously can use constructors that do not require credentials such as shared access signatures.

## 推荐措施

Set 'Public access level' configuration setting to 'Private (no anonymous access)'

## 修复步骤


### Terraform

[https://docs.ST Cloud.com/checks/azure/azure-networking-policies/ensure-that-storage-accounts-disallow-public-access#terraform](https://docs.ST Cloud.com/checks/azure/azure-networking-policies/ensure-that-storage-accounts-disallow-public-access#terraform)

### Other

[https://www.trendmicro.com/cloudoneconformity/knowledge-base/azure/StorageAccounts/disable-blob-anonymous-access-for-storage-accounts.html](https://www.trendmicro.com/cloudoneconformity/knowledge-base/azure/StorageAccounts/disable-blob-anonymous-access-for-storage-accounts.html)

## 参考资料

No external references available.

## 技术信息

- Source Metadata：[sources/azure/storage_blob_public_access_level_is_disabled/metadata.json](../../sources/azure/storage_blob_public_access_level_is_disabled/metadata.json)
- Source Code：[sources/azure/storage_blob_public_access_level_is_disabled/check.py](../../sources/azure/storage_blob_public_access_level_is_disabled/check.py)
- Source Metadata Path：`sources/azure/storage_blob_public_access_level_is_disabled/metadata.json`
- Source Code Path：`sources/azure/storage_blob_public_access_level_is_disabled/check.py`
