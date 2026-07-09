# Ensure the storage account containing the container with activity logs is encrypted with Customer Managed Key

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `monitor_storage_account_with_activity_logs_cmk_encrypted` |
| 云平台 | Azure |
| 服务 | monitor |
| 严重等级 | medium |
| 类别 | Uncategorized |
| 资源类型 | Monitor |
| 资源组 | monitoring |

## 描述

Storage accounts with the activity log exports can be configured to use CustomerManaged Keys (CMK).

## 风险

Configuring the storage account with the activity log export container to use CMKs provides additional confidentiality controls on log data, as a given user must have read permission on the corresponding storage account and must be granted decrypt permission by the CMK.

## 推荐措施

1. Go to Activity log 2. Select Export 3. Select Subscription 4. In section Storage Account, note the name of the Storage account 5. Close the Export Audit Logs blade. Close the Monitor - Activity Log blade. 6. In right column, Click service Storage Accounts to access Storage account blade 7. Click on the storage account name noted in step 4. This will open blade specific to that storage account 8. Under Security + networking, click Encryption. 9. Ensure Customer-managed keys is selected and Key URI is set.

- 推荐链接：[https://learn.microsoft.com/en-us/azure/azure-monitor/essentials/activity-log?tabs=cli#managing-legacy-log-profiles](https://learn.microsoft.com/en-us/azure/azure-monitor/essentials/activity-log?tabs=cli#managing-legacy-log-profiles)

## 修复步骤


### CLI

```text
az storage account update --name <name of the storage account> --resource-group <resource group for a storage account> --encryption-key-source=Microsoft.Keyvault --encryption-key-vault <Key Vault URI> --encryption-key-name <KeyName> --encryption-key-version <Key Version>
```

### Terraform

[https://docs.ST Cloud.com/checks/azure/azure-general-policies/ensure-that-storage-accounts-use-customer-managed-key-for-encryption#terraform](https://docs.ST Cloud.com/checks/azure/azure-general-policies/ensure-that-storage-accounts-use-customer-managed-key-for-encryption#terraform)

### Other

[https://www.trendmicro.com/cloudoneconformity-staging/knowledge-base/azure/Monitor/use-cmk-for-activity-log-storage-container-encryption.html](https://www.trendmicro.com/cloudoneconformity-staging/knowledge-base/azure/Monitor/use-cmk-for-activity-log-storage-container-encryption.html)

## 参考资料

- [https://learn.microsoft.com/en-us/security/benchmark/azure/security-controls-v3-data-protection#dp-5-encrypt-sensitive-data-at-rest](https://learn.microsoft.com/en-us/security/benchmark/azure/security-controls-v3-data-protection#dp-5-encrypt-sensitive-data-at-rest)
- [https://learn.microsoft.com/en-us/azure/azure-monitor/essentials/activity-log?tabs=cli#managing-legacy-log-profiles](https://learn.microsoft.com/en-us/azure/azure-monitor/essentials/activity-log?tabs=cli#managing-legacy-log-profiles)

## 技术信息

- Source Metadata：[sources/azure/monitor_storage_account_with_activity_logs_cmk_encrypted/metadata.json](../../sources/azure/monitor_storage_account_with_activity_logs_cmk_encrypted/metadata.json)
- Source Code：[sources/azure/monitor_storage_account_with_activity_logs_cmk_encrypted/check.py](../../sources/azure/monitor_storage_account_with_activity_logs_cmk_encrypted/check.py)
- Source Metadata Path：`sources/azure/monitor_storage_account_with_activity_logs_cmk_encrypted/metadata.json`
- Source Code Path：`sources/azure/monitor_storage_account_with_activity_logs_cmk_encrypted/check.py`
