# Ensure allow storage account key access is disabled

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `storage_account_key_access_disabled` |
| クラウドプラットフォーム | Azure |
| サービス | storage |
| サブサービス | account |
| 重大度 | high |
| カテゴリ | e3 |
| リソースタイプ | AzureStorageAccount |
| リソースグループ | storage |

## 説明

Ensures that access to Azure Storage Accounts using account keys is disabled, enforcing the use of Microsoft Entra ID (formerly Azure AD) for authentication.

## リスク

Using Shared Key authorization poses a security risk due to the high privileges associated with storage account keys and the difficulty in auditing such access. Disabling Shared Key access helps enforce identity-based authentication via Microsoft Entra ID, enhancing security and traceability.

## 推奨事項

Disable Shared Key authorization on storage accounts to enforce the use of Microsoft Entra ID for secure, auditable access.

- 推奨リンク：[https://learn.microsoft.com/en-us/azure/storage/common/shared-key-authorization-prevent](https://learn.microsoft.com/en-us/azure/storage/common/shared-key-authorization-prevent)

## 修正手順


### CLI

```text
az storage account update --name <storage-account-name> --resource-group <resource-group> --allow-shared-key-access false
```

### Other

[https://www.trendmicro.com/cloudoneconformity-staging/knowledge-base/azure/StorageAccounts/disable-shared-key-authorization.html](https://www.trendmicro.com/cloudoneconformity-staging/knowledge-base/azure/StorageAccounts/disable-shared-key-authorization.html)

## 参考資料

- [https://learn.microsoft.com/en-us/azure/storage/common/shared-key-authorization-prevent](https://learn.microsoft.com/en-us/azure/storage/common/shared-key-authorization-prevent)

## 技術情報

- Source Metadata：[sources/azure/storage_account_key_access_disabled/metadata.json](../../sources/azure/storage_account_key_access_disabled/metadata.json)
- Source Code：[sources/azure/storage_account_key_access_disabled/check.py](../../sources/azure/storage_account_key_access_disabled/check.py)
- Source Metadata Path：`sources/azure/storage_account_key_access_disabled/metadata.json`
- Source Code Path：`sources/azure/storage_account_key_access_disabled/check.py`
