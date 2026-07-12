# Ensure SMB protocol version for file shares is set to the latest version.

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `storage_smb_protocol_version_is_latest` |
| クラウドプラットフォーム | Azure |
| サービス | storage |
| 重大度 | medium |
| カテゴリ | Uncategorized |
| リソースタイプ | AzureStorageAccount |
| リソースグループ | storage |

## 説明

Ensure that SMB file shares are configured to use only the latest SMB protocol version.

## リスク

Allowing older SMB protocol versions may expose file shares to known vulnerabilities and security risks.

## 推奨事項

Configure your Azure Storage Account file shares to allow only the latest SMB protocol version.

- 推奨リンク：[https://www.trendmicro.com/cloudoneconformity/knowledge-base/azure/StorageAccounts/latest-smb-protocol-version.html](https://www.trendmicro.com/cloudoneconformity/knowledge-base/azure/StorageAccounts/latest-smb-protocol-version.html)

## 修正手順


### CLI

```text
az storage account file-service-properties update --resource-group <resource-group> --account-name <storage-account> --versions <latest-version>
```

## 参考資料

- [https://learn.microsoft.com/en-us/azure/storage/files/files-smb-protocol#smb-security-settings](https://learn.microsoft.com/en-us/azure/storage/files/files-smb-protocol#smb-security-settings)
- [https://www.trendmicro.com/cloudoneconformity/knowledge-base/azure/StorageAccounts/latest-smb-protocol-version.html](https://www.trendmicro.com/cloudoneconformity/knowledge-base/azure/StorageAccounts/latest-smb-protocol-version.html)

## 技術情報

- Source Metadata：[sources/azure/storage_smb_protocol_version_is_latest/metadata.json](../../sources/azure/storage_smb_protocol_version_is_latest/metadata.json)
- Source Code：[sources/azure/storage_smb_protocol_version_is_latest/check.py](../../sources/azure/storage_smb_protocol_version_is_latest/check.py)
- Source Metadata Path：`sources/azure/storage_smb_protocol_version_is_latest/metadata.json`
- Source Code Path：`sources/azure/storage_smb_protocol_version_is_latest/check.py`
