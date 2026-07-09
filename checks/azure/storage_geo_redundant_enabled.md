# Ensure geo-redundant storage (GRS) is enabled on critical Azure Storage Accounts

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `storage_geo_redundant_enabled` |
| 云平台 | Azure |
| 服务 | storage |
| 严重等级 | high |
| 类别 | Uncategorized |
| 资源类型 | AzureStorageAccount |
| 资源组 | storage |

## 描述

Geo-redundant storage (GRS) must be enabled on critical Azure Storage Accounts to ensure data durability and availability in the event of a regional outage. GRS replicates data within the primary region and asynchronously to a secondary region, offering enhanced resilience and supporting disaster recovery strategies.

## 风险

Without GRS, critical data may be lost or become unavailable during a regional outage, compromising data durability and disaster recovery efforts.

## 推荐措施

Enable geo-redundant storage (GRS) for critical Azure Storage Accounts to ensure data durability and availability across regional failures.

- 推荐链接：[https://learn.microsoft.com/en-us/azure/storage/common/storage-redundancy](https://learn.microsoft.com/en-us/azure/storage/common/storage-redundancy)

## 修复步骤


### CLI

```text
az storage account update --name <storage-account-name> --resource-group <resource-group-name> --sku Standard_GRS
```

### Other

[https://www.trendmicro.com/cloudoneconformity/knowledge-base/azure/StorageAccounts/enable-geo-redundant-storage.html](https://www.trendmicro.com/cloudoneconformity/knowledge-base/azure/StorageAccounts/enable-geo-redundant-storage.html)

## 参考资料

- [https://learn.microsoft.com/en-us/azure/storage/common/storage-redundancy](https://learn.microsoft.com/en-us/azure/storage/common/storage-redundancy)

## 技术信息

- Source Metadata：[sources/azure/storage_geo_redundant_enabled/metadata.json](../../sources/azure/storage_geo_redundant_enabled/metadata.json)
- Source Code：[sources/azure/storage_geo_redundant_enabled/check.py](../../sources/azure/storage_geo_redundant_enabled/check.py)
- Source Metadata Path：`sources/azure/storage_geo_redundant_enabled/metadata.json`
- Source Code Path：`sources/azure/storage_geo_redundant_enabled/check.py`
