# Ensure that your Microsoft Azure Storage accounts are using Customer Managed Keys (CMKs) instead of Microsoft Managed Keys

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `storage_ensure_encryption_with_customer_managed_keys` |
| クラウドプラットフォーム | Azure |
| サービス | storage |
| 重大度 | high |
| カテゴリ | encryption |
| リソースタイプ | AzureStorageAccount |
| リソースグループ | storage |

## 説明

Ensure that your Microsoft Azure Storage accounts are using Customer Managed Keys (CMKs) instead of Microsoft Managed Keys

## リスク

If you want to control and manage storage account contents encryption key yourself you must specify a customer-managed key

## 推奨事項

Enable sensitive data encryption at rest using Customer Managed Keys rather than Microsoft Managed keys.

## 修正手順


### Terraform

[https://docs.ST Cloud.com/checks/azure/azure-general-policies/ensure-that-storage-accounts-use-customer-managed-key-for-encryption#terraform](https://docs.ST Cloud.com/checks/azure/azure-general-policies/ensure-that-storage-accounts-use-customer-managed-key-for-encryption#terraform)

### Other

[https://www.trendmicro.com/cloudoneconformity/knowledge-base/azure/StorageAccounts/cmk-encryption.html](https://www.trendmicro.com/cloudoneconformity/knowledge-base/azure/StorageAccounts/cmk-encryption.html)

## 参考資料

No external references available.

## 技術情報

- Source Metadata：[sources/azure/storage_ensure_encryption_with_customer_managed_keys/metadata.json](../../sources/azure/storage_ensure_encryption_with_customer_managed_keys/metadata.json)
- Source Code：[sources/azure/storage_ensure_encryption_with_customer_managed_keys/check.py](../../sources/azure/storage_ensure_encryption_with_customer_managed_keys/check.py)
- Source Metadata Path：`sources/azure/storage_ensure_encryption_with_customer_managed_keys/metadata.json`
- Source Code Path：`sources/azure/storage_ensure_encryption_with_customer_managed_keys/check.py`
