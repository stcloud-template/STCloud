# Ensure Default Network Access Rule for Storage Accounts is Set to Deny

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `storage_default_network_access_rule_is_denied` |
| 云平台 | Azure |
| 服务 | storage |
| 严重等级 | medium |
| 类别 | Uncategorized |
| 资源类型 | AzureStorageAccount |
| 资源组 | storage |

## 描述

Restricting default network access helps to provide a new layer of security, since storage accounts accept connections from clients on any network. To limit access toselected networks, the default action must be changed.

## 风险

Storage accounts should be configured to deny access to traffic from all networks (including internet traffic). Access can be granted to traffic from specific Azure Virtualnetworks, allowing a secure network boundary for specific applications to be built.Access can also be granted to public internet IP address ranges to enable connectionsfrom specific internet or on-premises clients. When network rules are configured, onlyapplications from allowed networks can access a storage account. When calling from anallowed network, applications continue to require proper authorization (a valid accesskey or SAS token) to access the storage account.

## 推荐措施

1. Go to Storage Accounts 2. For each storage account, Click on the Networking blade 3. Click the Firewalls and virtual networks heading. 4. Ensure that you have elected to allow access from Selected networks 5. Add rules to allow traffic from specific network. 6. Click Save to apply your changes.

## 修复步骤


### CLI

```text
az storage account update --name <StorageAccountName> --resource-group <resourceGroupName> --default-action Deny
```

### Terraform

[https://docs.ST Cloud.com/checks/azure/azure-networking-policies/set-default-network-access-rule-for-storage-accounts-to-deny#terraform](https://docs.ST Cloud.com/checks/azure/azure-networking-policies/set-default-network-access-rule-for-storage-accounts-to-deny#terraform)

### Other

[https://www.trendmicro.com/cloudoneconformity/knowledge-base/azure/StorageAccounts/restrict-default-network-access.html](https://www.trendmicro.com/cloudoneconformity/knowledge-base/azure/StorageAccounts/restrict-default-network-access.html)

## 参考资料

No external references available.

## 技术信息

- Source Metadata：[sources/azure/storage_default_network_access_rule_is_denied/metadata.json](../../sources/azure/storage_default_network_access_rule_is_denied/metadata.json)
- Source Code：[sources/azure/storage_default_network_access_rule_is_denied/check.py](../../sources/azure/storage_default_network_access_rule_is_denied/check.py)
- Source Metadata Path：`sources/azure/storage_default_network_access_rule_is_denied/metadata.json`
- Source Code Path：`sources/azure/storage_default_network_access_rule_is_denied/check.py`
