# Ensure that the 'Public access level' is set to 'Private (no anonymous access)' for all blob containers in your storage account

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `storage_blob_public_access_level_is_disabled` |
| クラウドプラットフォーム | Azure |
| サービス | storage |
| 重大度 | medium |
| カテゴリ | Uncategorized |
| リソースタイプ | AzureStorageAccount |
| リソースグループ | storage |

## 説明

Ensure that the 'Public access level' configuration setting is set to 'Private (no anonymous access)' for all blob containers in your storage account in order to block anonymous access to these Microsoft Azure resources.

## リスク

A user that accesses blob containers anonymously can use constructors that do not require credentials such as shared access signatures.

## 推奨事項

Set 'Public access level' configuration setting to 'Private (no anonymous access)'

## 修正手順


### Terraform

[https://docs.ST Cloud.com/checks/azure/azure-networking-policies/ensure-that-storage-accounts-disallow-public-access#terraform](https://docs.ST Cloud.com/checks/azure/azure-networking-policies/ensure-that-storage-accounts-disallow-public-access#terraform)

### Other

[https://www.trendmicro.com/cloudoneconformity/knowledge-base/azure/StorageAccounts/disable-blob-anonymous-access-for-storage-accounts.html](https://www.trendmicro.com/cloudoneconformity/knowledge-base/azure/StorageAccounts/disable-blob-anonymous-access-for-storage-accounts.html)

## 参考資料

No external references available.

## 技術情報

- Source Metadata：[sources/azure/storage_blob_public_access_level_is_disabled/metadata.json](../../sources/azure/storage_blob_public_access_level_is_disabled/metadata.json)
- Source Code：[sources/azure/storage_blob_public_access_level_is_disabled/check.py](../../sources/azure/storage_blob_public_access_level_is_disabled/check.py)
- Source Metadata Path：`sources/azure/storage_blob_public_access_level_is_disabled/metadata.json`
- Source Code Path：`sources/azure/storage_blob_public_access_level_is_disabled/check.py`
