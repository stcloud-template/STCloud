# Ensure the Storage Container Storing the Activity Logs is not Publicly Accessible

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `monitor_storage_account_with_activity_logs_is_private` |
| クラウドプラットフォーム | Azure |
| サービス | monitor |
| 重大度 | high |
| カテゴリ | Uncategorized |
| リソースタイプ | Monitor |
| リソースグループ | monitoring |

## 説明

The storage account container containing the activity log export should not be publicly accessible.

## リスク

Allowing public access to activity log content may aid an adversary in identifying weaknesses in the affected account's use or configuration.

## 推奨事項

1. From Azure Home select the Portal Menu 2. Search for Storage Accounts to access Storage account blade 3. Click on the storage account name 4. Click on Configuration under settings 5. Select Enabled under 'Allow Blob public access'

- 推奨リンク：[https://docs.microsoft.com/en-us/security/benchmark/azure/security-controls-v3-network-security#ns-2-secure-cloud-services-with-network-controls](https://docs.microsoft.com/en-us/security/benchmark/azure/security-controls-v3-network-security#ns-2-secure-cloud-services-with-network-controls)

## 修正手順


### CLI

```text
az storage container set-permission --name insights-activity-logs --account-name <Storage Account Name> --public-access off
```

### Terraform

[https://docs.ST Cloud.com/checks/azure/azure-logging-policies/ensure-the-storage-container-storing-the-activity-logs-is-not-publicly-accessible#terraform](https://docs.ST Cloud.com/checks/azure/azure-logging-policies/ensure-the-storage-container-storing-the-activity-logs-is-not-publicly-accessible#terraform)

### Other

[https://www.trendmicro.com/cloudoneconformity-staging/knowledge-base/azure/Monitor/check-for-publicly-accessible-activity-log-storage-container.html](https://www.trendmicro.com/cloudoneconformity-staging/knowledge-base/azure/Monitor/check-for-publicly-accessible-activity-log-storage-container.html)

## 参考資料

- [https://learn.microsoft.com/en-us/azure/azure-monitor/essentials/diagnostic-settings](https://learn.microsoft.com/en-us/azure/azure-monitor/essentials/diagnostic-settings)
- [https://docs.microsoft.com/en-us/security/benchmark/azure/security-controls-v3-network-security#ns-2-secure-cloud-services-with-network-controls](https://docs.microsoft.com/en-us/security/benchmark/azure/security-controls-v3-network-security#ns-2-secure-cloud-services-with-network-controls)

## 技術情報

- Source Metadata：[sources/azure/monitor_storage_account_with_activity_logs_is_private/metadata.json](../../sources/azure/monitor_storage_account_with_activity_logs_is_private/metadata.json)
- Source Code：[sources/azure/monitor_storage_account_with_activity_logs_is_private/check.py](../../sources/azure/monitor_storage_account_with_activity_logs_is_private/check.py)
- Source Metadata Path：`sources/azure/monitor_storage_account_with_activity_logs_is_private/metadata.json`
- Source Code Path：`sources/azure/monitor_storage_account_with_activity_logs_is_private/check.py`
