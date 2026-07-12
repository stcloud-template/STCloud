# Ensure Microsoft Entra authorization is enabled by default for Azure Storage Accounts

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `storage_default_to_entra_authorization_enabled` |
| クラウドプラットフォーム | Azure |
| サービス | storage |
| 重大度 | high |
| カテゴリ | Uncategorized |
| リソースタイプ | AzureStorageAccount |
| リソースグループ | storage |

## 説明

Ensure that the Azure Storage Account setting 'Default to Microsoft Entra authorization in the Azure portal' is enabled to enforce the use of Microsoft Entra ID for accessing blobs, files, queues, and tables.

## リスク

If this setting is not enabled, the Azure portal may authorize access using less secure methods such as Shared Key, increasing the risk of unauthorized data access.

## 推奨事項

Enable Microsoft Entra authorization by default in the Azure portal to enhance security and avoid reliance on Shared Key authentication.

- 推奨リンク：[https://learn.microsoft.com/en-us/azure/storage/blobs/authorize-access-azure-active-directory](https://learn.microsoft.com/en-us/azure/storage/blobs/authorize-access-azure-active-directory)

## 修正手順


### CLI

```text
az storage account update --name <storage-account-name> --resource-group <resource-group-name> --default-to-AzAd-auth true
```

### Other

[https://www.trendmicro.com/cloudoneconformity-staging/knowledge-base/azure/StorageAccounts/enable-microsoft-entra-authorization-by-default.html](https://www.trendmicro.com/cloudoneconformity-staging/knowledge-base/azure/StorageAccounts/enable-microsoft-entra-authorization-by-default.html)

## 参考資料

- [https://learn.microsoft.com/en-us/azure/storage/blobs/authorize-access-azure-active-directory](https://learn.microsoft.com/en-us/azure/storage/blobs/authorize-access-azure-active-directory)

## 技術情報

- Source Metadata：[sources/azure/storage_default_to_entra_authorization_enabled/metadata.json](../../sources/azure/storage_default_to_entra_authorization_enabled/metadata.json)
- Source Code：[sources/azure/storage_default_to_entra_authorization_enabled/check.py](../../sources/azure/storage_default_to_entra_authorization_enabled/check.py)
- Source Metadata Path：`sources/azure/storage_default_to_entra_authorization_enabled/metadata.json`
- Source Code Path：`sources/azure/storage_default_to_entra_authorization_enabled/check.py`
