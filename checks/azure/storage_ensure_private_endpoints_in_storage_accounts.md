# Ensure Private Endpoints are used to access Storage Accounts

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `storage_ensure_private_endpoints_in_storage_accounts` |
| 云平台 | Azure |
| 服务 | storage |
| 严重等级 | medium |
| 类别 | encryption |
| 资源类型 | AzureStorageAccount |
| 资源组 | storage |

## 描述

Use private endpoints for your Azure Storage accounts to allow clients and services to securely access data located over a network via an encrypted Private Link. To do this, the private endpoint uses an IP address from the VNet for each service. Network traffic between disparate services securely traverses encrypted over the VNet. This VNet can also link addressing space, extending your network and accessing resources on it. Similarly, it can be a tunnel through public networks to connect remote infrastructures together. This creates further security through segmenting network traffic and preventing outside sources from accessing it.

## 风险

Storage accounts that are not configured to use Private Endpoints are accessible over the public internet. This can lead to data exfiltration and other security issues.

## 推荐措施

Use Private Endpoints to access Storage Accounts

- 推荐链接：[https://docs.microsoft.com/en-us/azure/storage/common/storage-private-endpoints](https://docs.microsoft.com/en-us/azure/storage/common/storage-private-endpoints)

## 修复步骤


### Other

[https://www.trendmicro.com/cloudoneconformity-staging/knowledge-base/azure/StorageAccounts/private-endpoints.html#](https://www.trendmicro.com/cloudoneconformity-staging/knowledge-base/azure/StorageAccounts/private-endpoints.html#)

## 参考资料

- [https://learn.microsoft.com/en-us/azure/storage/common/storage-private-endpoints](https://learn.microsoft.com/en-us/azure/storage/common/storage-private-endpoints)
- [https://docs.microsoft.com/en-us/azure/storage/common/storage-private-endpoints](https://docs.microsoft.com/en-us/azure/storage/common/storage-private-endpoints)

## 技术信息

- Source Metadata：[sources/azure/storage_ensure_private_endpoints_in_storage_accounts/metadata.json](../../sources/azure/storage_ensure_private_endpoints_in_storage_accounts/metadata.json)
- Source Code：[sources/azure/storage_ensure_private_endpoints_in_storage_accounts/check.py](../../sources/azure/storage_ensure_private_endpoints_in_storage_accounts/check.py)
- Source Metadata Path：`sources/azure/storage_ensure_private_endpoints_in_storage_accounts/metadata.json`
- Source Code Path：`sources/azure/storage_ensure_private_endpoints_in_storage_accounts/check.py`
