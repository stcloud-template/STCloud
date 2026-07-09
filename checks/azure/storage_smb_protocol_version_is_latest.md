# Ensure SMB protocol version for file shares is set to the latest version.

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `storage_smb_protocol_version_is_latest` |
| 云平台 | Azure |
| 服务 | storage |
| 严重等级 | medium |
| 类别 | Uncategorized |
| 资源类型 | AzureStorageAccount |
| 资源组 | storage |

## 描述

Ensure that SMB file shares are configured to use only the latest SMB protocol version.

## 风险

Allowing older SMB protocol versions may expose file shares to known vulnerabilities and security risks.

## 推荐措施

Configure your Azure Storage Account file shares to allow only the latest SMB protocol version.

- 推荐链接：[https://www.trendmicro.com/cloudoneconformity/knowledge-base/azure/StorageAccounts/latest-smb-protocol-version.html](https://www.trendmicro.com/cloudoneconformity/knowledge-base/azure/StorageAccounts/latest-smb-protocol-version.html)

## 修复步骤


### CLI

```text
az storage account file-service-properties update --resource-group <resource-group> --account-name <storage-account> --versions <latest-version>
```

## 参考资料

- [https://learn.microsoft.com/en-us/azure/storage/files/files-smb-protocol#smb-security-settings](https://learn.microsoft.com/en-us/azure/storage/files/files-smb-protocol#smb-security-settings)
- [https://www.trendmicro.com/cloudoneconformity/knowledge-base/azure/StorageAccounts/latest-smb-protocol-version.html](https://www.trendmicro.com/cloudoneconformity/knowledge-base/azure/StorageAccounts/latest-smb-protocol-version.html)

## 技术信息

- Source Metadata：[sources/azure/storage_smb_protocol_version_is_latest/metadata.json](../../sources/azure/storage_smb_protocol_version_is_latest/metadata.json)
- Source Code：[sources/azure/storage_smb_protocol_version_is_latest/check.py](../../sources/azure/storage_smb_protocol_version_is_latest/check.py)
- Source Metadata Path：`sources/azure/storage_smb_protocol_version_is_latest/metadata.json`
- Source Code Path：`sources/azure/storage_smb_protocol_version_is_latest/check.py`
