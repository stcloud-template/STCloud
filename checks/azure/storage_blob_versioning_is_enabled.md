# Ensure Blob Versioning is Enabled on Azure Blob Storage Accounts

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `storage_blob_versioning_is_enabled` |
| クラウドプラットフォーム | Azure |
| サービス | storage |
| 重大度 | medium |
| カテゴリ | Uncategorized |
| リソースタイプ | AzureStorageAccount |
| リソースグループ | storage |

## 説明

Ensure that blob versioning is enabled on Azure Blob Storage accounts to automatically retain previous versions of objects.

## リスク

Without blob versioning, accidental or malicious changes to blobs cannot be easily recovered, leading to potential data loss.

## 推奨事項

Enable blob versioning for all Azure Storage accounts that store critical or sensitive data.

- 推奨リンク：[https://learn.microsoft.com/en-us/azure/storage/blobs/versioning-enable](https://learn.microsoft.com/en-us/azure/storage/blobs/versioning-enable)

## 修正手順


### CLI

```text
az storage account blob-service-properties update --resource-group <resource_group> --account-name <storage-account> --enable-versioning true
```

### Terraform

```text
resource "azurerm_storage_account" "example" {
  name                     = "examplestorageacct"
  resource_group_name      = azurerm_resource_group.example.name
  location                 = azurerm_resource_group.example.location
  account_tier             = "Standard"
  account_replication_type = "LRS"

  blob_properties {
    versioning_enabled = true
  }
}
```

### Other

[https://www.trendmicro.com/cloudoneconformity/knowledge-base/azure/StorageAccounts/enable-versioning-for-blobs.html](https://www.trendmicro.com/cloudoneconformity/knowledge-base/azure/StorageAccounts/enable-versioning-for-blobs.html)

## 参考資料

- [https://learn.microsoft.com/en-us/azure/storage/blobs/versioning-enable](https://learn.microsoft.com/en-us/azure/storage/blobs/versioning-enable)

## 技術情報

- Source Metadata：[sources/azure/storage_blob_versioning_is_enabled/metadata.json](../../sources/azure/storage_blob_versioning_is_enabled/metadata.json)
- Source Code：[sources/azure/storage_blob_versioning_is_enabled/check.py](../../sources/azure/storage_blob_versioning_is_enabled/check.py)
- Source Metadata Path：`sources/azure/storage_blob_versioning_is_enabled/metadata.json`
- Source Code Path：`sources/azure/storage_blob_versioning_is_enabled/check.py`
