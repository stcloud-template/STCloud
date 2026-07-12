# Ensure Default Network Access Rule for Storage Accounts is Set to Deny

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `storage_default_network_access_rule_is_denied` |
| クラウドプラットフォーム | Azure |
| サービス | storage |
| 重大度 | medium |
| カテゴリ | Uncategorized |
| リソースタイプ | AzureStorageAccount |
| リソースグループ | storage |

## 説明

Restricting default network access helps to provide a new layer of security, since storage accounts accept connections from clients on any network. To limit access toselected networks, the default action must be changed.

## リスク

Storage accounts should be configured to deny access to traffic from all networks (including internet traffic). Access can be granted to traffic from specific Azure Virtualnetworks, allowing a secure network boundary for specific applications to be built.Access can also be granted to public internet IP address ranges to enable connectionsfrom specific internet or on-premises clients. When network rules are configured, onlyapplications from allowed networks can access a storage account. When calling from anallowed network, applications continue to require proper authorization (a valid accesskey or SAS token) to access the storage account.

## 推奨事項

1. Go to Storage Accounts 2. For each storage account, Click on the Networking blade 3. Click the Firewalls and virtual networks heading. 4. Ensure that you have elected to allow access from Selected networks 5. Add rules to allow traffic from specific network. 6. Click Save to apply your changes.

## 修正手順


### CLI

```text
az storage account update --name <StorageAccountName> --resource-group <resourceGroupName> --default-action Deny
```

### Terraform

[https://docs.ST Cloud.com/checks/azure/azure-networking-policies/set-default-network-access-rule-for-storage-accounts-to-deny#terraform](https://docs.ST Cloud.com/checks/azure/azure-networking-policies/set-default-network-access-rule-for-storage-accounts-to-deny#terraform)

### Other

[https://www.trendmicro.com/cloudoneconformity/knowledge-base/azure/StorageAccounts/restrict-default-network-access.html](https://www.trendmicro.com/cloudoneconformity/knowledge-base/azure/StorageAccounts/restrict-default-network-access.html)

## 参考資料

No external references available.

## 技術情報

- Source Metadata：[sources/azure/storage_default_network_access_rule_is_denied/metadata.json](../../sources/azure/storage_default_network_access_rule_is_denied/metadata.json)
- Source Code：[sources/azure/storage_default_network_access_rule_is_denied/check.py](../../sources/azure/storage_default_network_access_rule_is_denied/check.py)
- Source Metadata Path：`sources/azure/storage_default_network_access_rule_is_denied/metadata.json`
- Source Code Path：`sources/azure/storage_default_network_access_rule_is_denied/check.py`
