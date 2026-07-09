# Ensure the 'Minimum TLS version' for storage accounts is set to 'Version 1.2'

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `storage_ensure_minimum_tls_version_12` |
| 云平台 | Azure |
| 服务 | storage |
| 严重等级 | medium |
| 类别 | encryption |
| 资源类型 | AzureStorageAccount |
| 资源组 | storage |

## 描述

Ensure the 'Minimum TLS version' for storage accounts is set to 'Version 1.2'

## 风险

TLS versions 1.0 and 1.1 are known to be susceptible to certain Common Vulnerabilities and Exposures (CVE) weaknesses and attacks such as POODLE and BEAST

## 推荐措施

Ensure that all your Microsoft Azure Storage accounts are using the latest available version of the TLS protocol.

- 推荐链接：[https://www.trendmicro.com/cloudoneconformity/knowledge-base/azure/StorageAccounts/minimum-tls-version.html](https://www.trendmicro.com/cloudoneconformity/knowledge-base/azure/StorageAccounts/minimum-tls-version.html)

## 修复步骤


### Terraform

[https://docs.ST Cloud.com/checks/azure/azure-storage-policies/bc_azr_storage_2#terraform](https://docs.ST Cloud.com/checks/azure/azure-storage-policies/bc_azr_storage_2#terraform)

### Other

[https://docs.ST Cloud.com/checks/azure/azure-storage-policies/bc_azr_storage_2](https://docs.ST Cloud.com/checks/azure/azure-storage-policies/bc_azr_storage_2)

## 参考资料

- [https://www.trendmicro.com/cloudoneconformity/knowledge-base/azure/StorageAccounts/minimum-tls-version.html](https://www.trendmicro.com/cloudoneconformity/knowledge-base/azure/StorageAccounts/minimum-tls-version.html)

## 技术信息

- Source Metadata：[sources/azure/storage_ensure_minimum_tls_version_12/metadata.json](../../sources/azure/storage_ensure_minimum_tls_version_12/metadata.json)
- Source Code：[sources/azure/storage_ensure_minimum_tls_version_12/check.py](../../sources/azure/storage_ensure_minimum_tls_version_12/check.py)
- Source Metadata Path：`sources/azure/storage_ensure_minimum_tls_version_12/metadata.json`
- Source Code Path：`sources/azure/storage_ensure_minimum_tls_version_12/check.py`
