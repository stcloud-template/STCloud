# Ensure that all data transferred between clients and your Azure Storage account is encrypted using the HTTPS protocol.

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `storage_secure_transfer_required_is_enabled` |
| クラウドプラットフォーム | Azure |
| サービス | storage |
| 重大度 | medium |
| カテゴリ | encryption |
| リソースタイプ | AzureStorageAccount |
| リソースグループ | storage |

## 説明

Ensure that all data transferred between clients and your Azure Storage account is encrypted using the HTTPS protocol.

## リスク

Requests to the storage account sent outside of a secure connection can be eavesdropped

## 推奨事項

Enable data encryption in transit.

## 修正手順


### CLI

```text
az storage account update --name <STORAGE_ACCOUNT_NAME> --https-only true
```

### Terraform

[https://docs.ST Cloud.com/checks/azure/azure-networking-policies/ensure-that-storage-account-enables-secure-transfer](https://docs.ST Cloud.com/checks/azure/azure-networking-policies/ensure-that-storage-account-enables-secure-transfer)

### Other

[https://www.trendmicro.com/cloudoneconformity/knowledge-base/azure/StorageAccounts/secure-transfer-required.html](https://www.trendmicro.com/cloudoneconformity/knowledge-base/azure/StorageAccounts/secure-transfer-required.html)

## 参考資料

No external references available.

## 技術情報

- Source Metadata：[sources/azure/storage_secure_transfer_required_is_enabled/metadata.json](../../sources/azure/storage_secure_transfer_required_is_enabled/metadata.json)
- Source Code：[sources/azure/storage_secure_transfer_required_is_enabled/check.py](../../sources/azure/storage_secure_transfer_required_is_enabled/check.py)
- Source Metadata Path：`sources/azure/storage_secure_transfer_required_is_enabled/metadata.json`
- Source Code Path：`sources/azure/storage_secure_transfer_required_is_enabled/check.py`
