# Ensure that your Microsoft Azure Storage accounts are using Customer Managed Keys (CMKs) instead of Microsoft Managed Keys

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `storage_ensure_encryption_with_customer_managed_keys` |
| 云平台 | Azure |
| 服务 | storage |
| 严重等级 | high |
| 类别 | encryption |
| 资源类型 | AzureStorageAccount |
| 资源组 | storage |

## 描述

Ensure that your Microsoft Azure Storage accounts are using Customer Managed Keys (CMKs) instead of Microsoft Managed Keys

## 风险

If you want to control and manage storage account contents encryption key yourself you must specify a customer-managed key

## 推荐措施

Enable sensitive data encryption at rest using Customer Managed Keys rather than Microsoft Managed keys.

## 修复步骤


### Terraform

[https://docs.ST Cloud.com/checks/azure/azure-general-policies/ensure-that-storage-accounts-use-customer-managed-key-for-encryption#terraform](https://docs.ST Cloud.com/checks/azure/azure-general-policies/ensure-that-storage-accounts-use-customer-managed-key-for-encryption#terraform)

### Other

[https://www.trendmicro.com/cloudoneconformity/knowledge-base/azure/StorageAccounts/cmk-encryption.html](https://www.trendmicro.com/cloudoneconformity/knowledge-base/azure/StorageAccounts/cmk-encryption.html)

## 参考资料

No external references available.

## 技术信息

- Source Metadata：[sources/azure/storage_ensure_encryption_with_customer_managed_keys/metadata.json](../../sources/azure/storage_ensure_encryption_with_customer_managed_keys/metadata.json)
- Source Code：[sources/azure/storage_ensure_encryption_with_customer_managed_keys/check.py](../../sources/azure/storage_ensure_encryption_with_customer_managed_keys/check.py)
- Source Metadata Path：`sources/azure/storage_ensure_encryption_with_customer_managed_keys/metadata.json`
- Source Code Path：`sources/azure/storage_ensure_encryption_with_customer_managed_keys/check.py`
