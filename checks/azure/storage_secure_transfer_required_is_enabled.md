# Ensure that all data transferred between clients and your Azure Storage account is encrypted using the HTTPS protocol.

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `storage_secure_transfer_required_is_enabled` |
| 云平台 | Azure |
| 服务 | storage |
| 严重等级 | medium |
| 类别 | encryption |
| 资源类型 | AzureStorageAccount |
| 资源组 | storage |

## 描述

Ensure that all data transferred between clients and your Azure Storage account is encrypted using the HTTPS protocol.

## 风险

Requests to the storage account sent outside of a secure connection can be eavesdropped

## 推荐措施

Enable data encryption in transit.

## 修复步骤


### CLI

```text
az storage account update --name <STORAGE_ACCOUNT_NAME> --https-only true
```

### Terraform

[https://docs.ST Cloud.com/checks/azure/azure-networking-policies/ensure-that-storage-account-enables-secure-transfer](https://docs.ST Cloud.com/checks/azure/azure-networking-policies/ensure-that-storage-account-enables-secure-transfer)

### Other

[https://www.trendmicro.com/cloudoneconformity/knowledge-base/azure/StorageAccounts/secure-transfer-required.html](https://www.trendmicro.com/cloudoneconformity/knowledge-base/azure/StorageAccounts/secure-transfer-required.html)

## 参考资料

No external references available.

## 技术信息

- Source Metadata：[sources/azure/storage_secure_transfer_required_is_enabled/metadata.json](../../sources/azure/storage_secure_transfer_required_is_enabled/metadata.json)
- Source Code：[sources/azure/storage_secure_transfer_required_is_enabled/check.py](../../sources/azure/storage_secure_transfer_required_is_enabled/check.py)
- Source Metadata Path：`sources/azure/storage_secure_transfer_required_is_enabled/metadata.json`
- Source Code Path：`sources/azure/storage_secure_transfer_required_is_enabled/check.py`
