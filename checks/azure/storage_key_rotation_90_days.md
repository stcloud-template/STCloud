# Ensure that Storage Account Access Keys are Periodically Regenerated

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `storage_key_rotation_90_days` |
| クラウドプラットフォーム | Azure |
| サービス | storage |
| 重大度 | medium |
| カテゴリ | encryption |
| リソースタイプ | AzureStorageAccount |
| リソースグループ | storage |

## 説明

Ensure that Storage Account Access Keys are Periodically Regenerated

## リスク

If the access keys are not regenerated periodically, the likelihood of accidental exposures increases, which can lead to unauthorized access to your storage account resources.

## 推奨事項

Ensure that Azure Storage account access keys are regenerated every 90 days in order to decrease the likelihood of accidental exposures and protect your storage account resources against unauthorized access.

- 推奨リンク：[https://learn.microsoft.com/en-us/azure/storage/common/storage-account-create?tabs=azure-portal#regenerate-storage-access-keys](https://learn.microsoft.com/en-us/azure/storage/common/storage-account-create?tabs=azure-portal#regenerate-storage-access-keys)

## 修正手順


### Other

[https://www.trendmicro.com/cloudoneconformity-staging/knowledge-base/azure/StorageAccounts/regenerate-storage-account-access-keys-periodically.html#](https://www.trendmicro.com/cloudoneconformity-staging/knowledge-base/azure/StorageAccounts/regenerate-storage-account-access-keys-periodically.html#)

## 参考資料

- [https://learn.microsoft.com/en-us/azure/storage/common/storage-account-keys-manage?tabs=azure-portal](https://learn.microsoft.com/en-us/azure/storage/common/storage-account-keys-manage?tabs=azure-portal)
- [https://learn.microsoft.com/en-us/azure/storage/common/storage-account-create?tabs=azure-portal#regenerate-storage-access-keys](https://learn.microsoft.com/en-us/azure/storage/common/storage-account-create?tabs=azure-portal#regenerate-storage-access-keys)

## 技術情報

- Source Metadata：[sources/azure/storage_key_rotation_90_days/metadata.json](../../sources/azure/storage_key_rotation_90_days/metadata.json)
- Source Code：[sources/azure/storage_key_rotation_90_days/check.py](../../sources/azure/storage_key_rotation_90_days/check.py)
- Source Metadata Path：`sources/azure/storage_key_rotation_90_days/metadata.json`
- Source Code Path：`sources/azure/storage_key_rotation_90_days/check.py`
