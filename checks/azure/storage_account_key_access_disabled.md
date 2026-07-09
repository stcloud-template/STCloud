# Ensure allow storage account key access is disabled

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `storage_account_key_access_disabled` |
| 云平台 | Azure |
| 服务 | storage |
| 子服务 | account |
| 严重等级 | high |
| 类别 | e3 |
| 资源类型 | AzureStorageAccount |
| 资源组 | storage |

## 描述

Ensures that access to Azure Storage Accounts using account keys is disabled, enforcing the use of Microsoft Entra ID (formerly Azure AD) for authentication.

## 风险

Using Shared Key authorization poses a security risk due to the high privileges associated with storage account keys and the difficulty in auditing such access. Disabling Shared Key access helps enforce identity-based authentication via Microsoft Entra ID, enhancing security and traceability.

## 推荐措施

Disable Shared Key authorization on storage accounts to enforce the use of Microsoft Entra ID for secure, auditable access.

- 推荐链接：[https://learn.microsoft.com/en-us/azure/storage/common/shared-key-authorization-prevent](https://learn.microsoft.com/en-us/azure/storage/common/shared-key-authorization-prevent)

## 修复步骤


### CLI

```text
az storage account update --name <storage-account-name> --resource-group <resource-group> --allow-shared-key-access false
```

### Other

[https://www.trendmicro.com/cloudoneconformity-staging/knowledge-base/azure/StorageAccounts/disable-shared-key-authorization.html](https://www.trendmicro.com/cloudoneconformity-staging/knowledge-base/azure/StorageAccounts/disable-shared-key-authorization.html)

## 参考资料

- [https://learn.microsoft.com/en-us/azure/storage/common/shared-key-authorization-prevent](https://learn.microsoft.com/en-us/azure/storage/common/shared-key-authorization-prevent)

## 技术信息

- Source Metadata：[sources/azure/storage_account_key_access_disabled/metadata.json](../../sources/azure/storage_account_key_access_disabled/metadata.json)
- Source Code：[sources/azure/storage_account_key_access_disabled/check.py](../../sources/azure/storage_account_key_access_disabled/check.py)
- Source Metadata Path：`sources/azure/storage_account_key_access_disabled/metadata.json`
- Source Code Path：`sources/azure/storage_account_key_access_disabled/check.py`
