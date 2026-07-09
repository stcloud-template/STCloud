# Ensure cross-tenant replication is disabled

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `storage_cross_tenant_replication_disabled` |
| 云平台 | Azure |
| 服务 | storage |
| 子服务 | account |
| 严重等级 | high |
| 类别 | Uncategorized |
| 资源类型 | AzureStorageAccount |
| 资源组 | storage |

## 描述

Ensure that cross-tenant replication is not enabled on Azure Storage Accounts to prevent unintended replication of data across tenant boundaries.

## 风险

If cross-tenant replication is enabled, sensitive data could be inadvertently replicated across tenants, increasing the risk of data leakage, unauthorized access, or non-compliance with data governance and privacy policies.

## 推荐措施

Disable Cross Tenant Replication on storage accounts to ensure that data remains within tenant boundaries unless explicitly shared, reducing the risk of data leakage and unauthorized access.

- 推荐链接：[https://learn.microsoft.com/en-us/azure/storage/blobs/object-replication-prevent-cross-tenant-policies?tabs=portal](https://learn.microsoft.com/en-us/azure/storage/blobs/object-replication-prevent-cross-tenant-policies?tabs=portal)

## 修复步骤


### CLI

```text
az storage account update --name <storage-account-name> --resource-group <resource-group> --default-to-oauth-authentication true --allow-cross-tenant-replication false
```

### Other

[https://www.trendmicro.com/cloudoneconformity-staging/knowledge-base/azure/StorageAccounts/disable-cross-tenant-replication.html](https://www.trendmicro.com/cloudoneconformity-staging/knowledge-base/azure/StorageAccounts/disable-cross-tenant-replication.html)

## 参考资料

- [https://learn.microsoft.com/en-us/azure/storage/blobs/object-replication-prevent-cross-tenant-policies?tabs=portal](https://learn.microsoft.com/en-us/azure/storage/blobs/object-replication-prevent-cross-tenant-policies?tabs=portal)

## 技术信息

- Source Metadata：[sources/azure/storage_cross_tenant_replication_disabled/metadata.json](../../sources/azure/storage_cross_tenant_replication_disabled/metadata.json)
- Source Code：[sources/azure/storage_cross_tenant_replication_disabled/check.py](../../sources/azure/storage_cross_tenant_replication_disabled/check.py)
- Source Metadata Path：`sources/azure/storage_cross_tenant_replication_disabled/metadata.json`
- Source Code Path：`sources/azure/storage_cross_tenant_replication_disabled/check.py`
