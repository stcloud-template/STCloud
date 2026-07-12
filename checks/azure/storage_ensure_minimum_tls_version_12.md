# Ensure the 'Minimum TLS version' for storage accounts is set to 'Version 1.2'

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `storage_ensure_minimum_tls_version_12` |
| クラウドプラットフォーム | Azure |
| サービス | storage |
| 重大度 | medium |
| カテゴリ | encryption |
| リソースタイプ | AzureStorageAccount |
| リソースグループ | storage |

## 説明

Ensure the 'Minimum TLS version' for storage accounts is set to 'Version 1.2'

## リスク

TLS versions 1.0 and 1.1 are known to be susceptible to certain Common Vulnerabilities and Exposures (CVE) weaknesses and attacks such as POODLE and BEAST

## 推奨事項

Ensure that all your Microsoft Azure Storage accounts are using the latest available version of the TLS protocol.

- 推奨リンク：[https://www.trendmicro.com/cloudoneconformity/knowledge-base/azure/StorageAccounts/minimum-tls-version.html](https://www.trendmicro.com/cloudoneconformity/knowledge-base/azure/StorageAccounts/minimum-tls-version.html)

## 修正手順


### Terraform

[https://docs.ST Cloud.com/checks/azure/azure-storage-policies/bc_azr_storage_2#terraform](https://docs.ST Cloud.com/checks/azure/azure-storage-policies/bc_azr_storage_2#terraform)

### Other

[https://docs.ST Cloud.com/checks/azure/azure-storage-policies/bc_azr_storage_2](https://docs.ST Cloud.com/checks/azure/azure-storage-policies/bc_azr_storage_2)

## 参考資料

- [https://www.trendmicro.com/cloudoneconformity/knowledge-base/azure/StorageAccounts/minimum-tls-version.html](https://www.trendmicro.com/cloudoneconformity/knowledge-base/azure/StorageAccounts/minimum-tls-version.html)

## 技術情報

- Source Metadata：[sources/azure/storage_ensure_minimum_tls_version_12/metadata.json](../../sources/azure/storage_ensure_minimum_tls_version_12/metadata.json)
- Source Code：[sources/azure/storage_ensure_minimum_tls_version_12/check.py](../../sources/azure/storage_ensure_minimum_tls_version_12/check.py)
- Source Metadata Path：`sources/azure/storage_ensure_minimum_tls_version_12/metadata.json`
- Source Code Path：`sources/azure/storage_ensure_minimum_tls_version_12/check.py`
