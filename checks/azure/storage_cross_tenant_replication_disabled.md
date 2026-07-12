# Ensure cross-tenant replication is disabled

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `storage_cross_tenant_replication_disabled` |
| クラウドプラットフォーム | Azure |
| サービス | storage |
| サブサービス | account |
| 重大度 | high |
| カテゴリ | Uncategorized |
| リソースタイプ | AzureStorageAccount |
| リソースグループ | storage |

## 説明

Ensure that cross-tenant replication is not enabled on Azure Storage Accounts to prevent unintended replication of data across tenant boundaries.

## リスク

If cross-tenant replication is enabled, sensitive data could be inadvertently replicated across tenants, increasing the risk of data leakage, unauthorized access, or non-compliance with data governance and privacy policies.

## 推奨事項

Disable Cross Tenant Replication on storage accounts to ensure that data remains within tenant boundaries unless explicitly shared, reducing the risk of data leakage and unauthorized access.

- 推奨リンク：[https://learn.microsoft.com/en-us/azure/storage/blobs/object-replication-prevent-cross-tenant-policies?tabs=portal](https://learn.microsoft.com/en-us/azure/storage/blobs/object-replication-prevent-cross-tenant-policies?tabs=portal)

## 修正手順


### CLI

```text
az storage account update --name <storage-account-name> --resource-group <resource-group> --default-to-oauth-authentication true --allow-cross-tenant-replication false
```

### Other

[https://www.trendmicro.com/cloudoneconformity-staging/knowledge-base/azure/StorageAccounts/disable-cross-tenant-replication.html](https://www.trendmicro.com/cloudoneconformity-staging/knowledge-base/azure/StorageAccounts/disable-cross-tenant-replication.html)

## 参考資料

- [https://learn.microsoft.com/en-us/azure/storage/blobs/object-replication-prevent-cross-tenant-policies?tabs=portal](https://learn.microsoft.com/en-us/azure/storage/blobs/object-replication-prevent-cross-tenant-policies?tabs=portal)

## 技術情報

- Source Metadata：[sources/azure/storage_cross_tenant_replication_disabled/metadata.json](../../sources/azure/storage_cross_tenant_replication_disabled/metadata.json)
- Source Code：[sources/azure/storage_cross_tenant_replication_disabled/check.py](../../sources/azure/storage_cross_tenant_replication_disabled/check.py)
- Source Metadata Path：`sources/azure/storage_cross_tenant_replication_disabled/metadata.json`
- Source Code Path：`sources/azure/storage_cross_tenant_replication_disabled/check.py`
