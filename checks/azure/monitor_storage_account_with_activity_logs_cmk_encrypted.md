# Ensure the storage account containing the container with activity logs is encrypted with Customer Managed Key

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `monitor_storage_account_with_activity_logs_cmk_encrypted` |
| クラウドプラットフォーム | Azure |
| サービス | monitor |
| 重大度 | medium |
| カテゴリ | Uncategorized |
| リソースタイプ | Monitor |
| リソースグループ | monitoring |

## 説明

Storage accounts with the activity log exports can be configured to use CustomerManaged Keys (CMK).

## リスク

Configuring the storage account with the activity log export container to use CMKs provides additional confidentiality controls on log data, as a given user must have read permission on the corresponding storage account and must be granted decrypt permission by the CMK.

## 推奨事項

1. Go to Activity log 2. Select Export 3. Select Subscription 4. In section Storage Account, note the name of the Storage account 5. Close the Export Audit Logs blade. Close the Monitor - Activity Log blade. 6. In right column, Click service Storage Accounts to access Storage account blade 7. Click on the storage account name noted in step 4. This will open blade specific to that storage account 8. Under Security + networking, click Encryption. 9. Ensure Customer-managed keys is selected and Key URI is set.

- 推奨リンク：[https://learn.microsoft.com/en-us/azure/azure-monitor/essentials/activity-log?tabs=cli#managing-legacy-log-profiles](https://learn.microsoft.com/en-us/azure/azure-monitor/essentials/activity-log?tabs=cli#managing-legacy-log-profiles)

## 修正手順


### CLI

```text
az storage account update --name <name of the storage account> --resource-group <resource group for a storage account> --encryption-key-source=Microsoft.Keyvault --encryption-key-vault <Key Vault URI> --encryption-key-name <KeyName> --encryption-key-version <Key Version>
```

### Terraform

[https://docs.ST Cloud.com/checks/azure/azure-general-policies/ensure-that-storage-accounts-use-customer-managed-key-for-encryption#terraform](https://docs.ST Cloud.com/checks/azure/azure-general-policies/ensure-that-storage-accounts-use-customer-managed-key-for-encryption#terraform)

### Other

[https://www.trendmicro.com/cloudoneconformity-staging/knowledge-base/azure/Monitor/use-cmk-for-activity-log-storage-container-encryption.html](https://www.trendmicro.com/cloudoneconformity-staging/knowledge-base/azure/Monitor/use-cmk-for-activity-log-storage-container-encryption.html)

## 参考資料

- [https://learn.microsoft.com/en-us/security/benchmark/azure/security-controls-v3-data-protection#dp-5-encrypt-sensitive-data-at-rest](https://learn.microsoft.com/en-us/security/benchmark/azure/security-controls-v3-data-protection#dp-5-encrypt-sensitive-data-at-rest)
- [https://learn.microsoft.com/en-us/azure/azure-monitor/essentials/activity-log?tabs=cli#managing-legacy-log-profiles](https://learn.microsoft.com/en-us/azure/azure-monitor/essentials/activity-log?tabs=cli#managing-legacy-log-profiles)

## 技術情報

- Source Metadata：[sources/azure/monitor_storage_account_with_activity_logs_cmk_encrypted/metadata.json](../../sources/azure/monitor_storage_account_with_activity_logs_cmk_encrypted/metadata.json)
- Source Code：[sources/azure/monitor_storage_account_with_activity_logs_cmk_encrypted/check.py](../../sources/azure/monitor_storage_account_with_activity_logs_cmk_encrypted/check.py)
- Source Metadata Path：`sources/azure/monitor_storage_account_with_activity_logs_cmk_encrypted/metadata.json`
- Source Code Path：`sources/azure/monitor_storage_account_with_activity_logs_cmk_encrypted/check.py`
