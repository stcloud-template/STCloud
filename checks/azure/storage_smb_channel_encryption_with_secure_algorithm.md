# Ensure SMB channel encryption uses a secure algorithm for SMB file shares

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `storage_smb_channel_encryption_with_secure_algorithm` |
| 云平台 | Azure |
| 服务 | storage |
| 严重等级 | medium |
| 类别 | Uncategorized |
| 资源类型 | AzureStorageAccount |
| 资源组 | storage |

## 描述

Implement SMB channel encryption with a secure algorithm for SMB file shares to ensure data confidentiality and integrity in transit.

## 风险

Not using the recommended SMB channel encryption may expose data transmitted over SMB channels to unauthorized interception and tampering.

## 推荐措施

Use the portal, CLI or PowerShell to set the SMB channel encryption to a secure algorithm.

- 推荐链接：[https://learn.microsoft.com/en-us/azure/storage/files/files-smb-protocol?tabs=azure-portal#smb-security-settings](https://learn.microsoft.com/en-us/azure/storage/files/files-smb-protocol?tabs=azure-portal#smb-security-settings)

## 修复步骤


### CLI

```text
az storage account file-service-properties update --resource-group <resource-group> --account-name <storage-account> --channel-encryption AES-256-GCM
```

## 参考资料

- [https://learn.microsoft.com/en-us/azure/well-architected/service-guides/azure-files#recommendations-for-smb-file-shares](https://learn.microsoft.com/en-us/azure/well-architected/service-guides/azure-files#recommendations-for-smb-file-shares)
- [https://learn.microsoft.com/en-us/azure/storage/files/files-smb-protocol?tabs=azure-portal#smb-security-settings](https://learn.microsoft.com/en-us/azure/storage/files/files-smb-protocol?tabs=azure-portal#smb-security-settings)

## 技术信息

- Source Metadata：[sources/azure/storage_smb_channel_encryption_with_secure_algorithm/metadata.json](../../sources/azure/storage_smb_channel_encryption_with_secure_algorithm/metadata.json)
- Source Code：[sources/azure/storage_smb_channel_encryption_with_secure_algorithm/check.py](../../sources/azure/storage_smb_channel_encryption_with_secure_algorithm/check.py)
- Source Metadata Path：`sources/azure/storage_smb_channel_encryption_with_secure_algorithm/metadata.json`
- Source Code Path：`sources/azure/storage_smb_channel_encryption_with_secure_algorithm/check.py`
