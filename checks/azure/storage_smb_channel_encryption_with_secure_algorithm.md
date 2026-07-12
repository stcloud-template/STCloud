# Ensure SMB channel encryption uses a secure algorithm for SMB file shares

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `storage_smb_channel_encryption_with_secure_algorithm` |
| クラウドプラットフォーム | Azure |
| サービス | storage |
| 重大度 | medium |
| カテゴリ | Uncategorized |
| リソースタイプ | AzureStorageAccount |
| リソースグループ | storage |

## 説明

Implement SMB channel encryption with a secure algorithm for SMB file shares to ensure data confidentiality and integrity in transit.

## リスク

Not using the recommended SMB channel encryption may expose data transmitted over SMB channels to unauthorized interception and tampering.

## 推奨事項

Use the portal, CLI or PowerShell to set the SMB channel encryption to a secure algorithm.

- 推奨リンク：[https://learn.microsoft.com/en-us/azure/storage/files/files-smb-protocol?tabs=azure-portal#smb-security-settings](https://learn.microsoft.com/en-us/azure/storage/files/files-smb-protocol?tabs=azure-portal#smb-security-settings)

## 修正手順


### CLI

```text
az storage account file-service-properties update --resource-group <resource-group> --account-name <storage-account> --channel-encryption AES-256-GCM
```

## 参考資料

- [https://learn.microsoft.com/en-us/azure/well-architected/service-guides/azure-files#recommendations-for-smb-file-shares](https://learn.microsoft.com/en-us/azure/well-architected/service-guides/azure-files#recommendations-for-smb-file-shares)
- [https://learn.microsoft.com/en-us/azure/storage/files/files-smb-protocol?tabs=azure-portal#smb-security-settings](https://learn.microsoft.com/en-us/azure/storage/files/files-smb-protocol?tabs=azure-portal#smb-security-settings)

## 技術情報

- Source Metadata：[sources/azure/storage_smb_channel_encryption_with_secure_algorithm/metadata.json](../../sources/azure/storage_smb_channel_encryption_with_secure_algorithm/metadata.json)
- Source Code：[sources/azure/storage_smb_channel_encryption_with_secure_algorithm/check.py](../../sources/azure/storage_smb_channel_encryption_with_secure_algorithm/check.py)
- Source Metadata Path：`sources/azure/storage_smb_channel_encryption_with_secure_algorithm/metadata.json`
- Source Code Path：`sources/azure/storage_smb_channel_encryption_with_secure_algorithm/check.py`
