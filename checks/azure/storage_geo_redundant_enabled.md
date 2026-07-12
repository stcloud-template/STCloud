# Ensure geo-redundant storage (GRS) is enabled on critical Azure Storage Accounts

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `storage_geo_redundant_enabled` |
| クラウドプラットフォーム | Azure |
| サービス | storage |
| 重大度 | high |
| カテゴリ | Uncategorized |
| リソースタイプ | AzureStorageAccount |
| リソースグループ | storage |

## 説明

Geo-redundant storage (GRS) must be enabled on critical Azure Storage Accounts to ensure data durability and availability in the event of a regional outage. GRS replicates data within the primary region and asynchronously to a secondary region, offering enhanced resilience and supporting disaster recovery strategies.

## リスク

Without GRS, critical data may be lost or become unavailable during a regional outage, compromising data durability and disaster recovery efforts.

## 推奨事項

Enable geo-redundant storage (GRS) for critical Azure Storage Accounts to ensure data durability and availability across regional failures.

- 推奨リンク：[https://learn.microsoft.com/en-us/azure/storage/common/storage-redundancy](https://learn.microsoft.com/en-us/azure/storage/common/storage-redundancy)

## 修正手順


### CLI

```text
az storage account update --name <storage-account-name> --resource-group <resource-group-name> --sku Standard_GRS
```

### Other

[https://www.trendmicro.com/cloudoneconformity/knowledge-base/azure/StorageAccounts/enable-geo-redundant-storage.html](https://www.trendmicro.com/cloudoneconformity/knowledge-base/azure/StorageAccounts/enable-geo-redundant-storage.html)

## 参考資料

- [https://learn.microsoft.com/en-us/azure/storage/common/storage-redundancy](https://learn.microsoft.com/en-us/azure/storage/common/storage-redundancy)

## 技術情報

- Source Metadata：[sources/azure/storage_geo_redundant_enabled/metadata.json](../../sources/azure/storage_geo_redundant_enabled/metadata.json)
- Source Code：[sources/azure/storage_geo_redundant_enabled/check.py](../../sources/azure/storage_geo_redundant_enabled/check.py)
- Source Metadata Path：`sources/azure/storage_geo_redundant_enabled/metadata.json`
- Source Code Path：`sources/azure/storage_geo_redundant_enabled/check.py`
