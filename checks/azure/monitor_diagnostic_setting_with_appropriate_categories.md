# Ensure Diagnostic Setting captures appropriate categories

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `monitor_diagnostic_setting_with_appropriate_categories` |
| クラウドプラットフォーム | Azure |
| サービス | monitor |
| サブサービス | Configuring Diagnostic Settings |
| 重大度 | medium |
| カテゴリ | Uncategorized |
| リソースタイプ | Monitor |
| リソースグループ | monitoring |

## 説明

Prerequisite: A Diagnostic Setting must exist. If a Diagnostic Setting does not exist, the navigation and options within this recommendation will not be available. Please review the recommendation at the beginning of this subsection titled: 'Ensure that a 'Diagnostic Setting' exists.' The diagnostic setting should be configured to log the appropriate activities from the control/management plane.

## リスク

A diagnostic setting controls how the diagnostic log is exported. Capturing the diagnostic setting categories for appropriate control/management plane activities allows proper alerting.

## 推奨事項

1. Go to Azure Monitor 2. Click Activity log 3. Click on Export Activity Logs 4. Select the Subscription from the drop down menu 5. Click on Add diagnostic setting 6. Enter a name for your new Diagnostic Setting 7. Check the following categories: Administrative, Alert, Policy, and Security 8. Choose the destination details according to your organization's needs.

- 推奨リンク：[https://learn.microsoft.com/en-us/azure/storage/common/manage-storage-analytics-logs?toc=%2Fazure%2Fstorage%2Fblobs%2Ftoc.json&bc=%2Fazure%2Fstorage%2Fblobs%2Fbreadcrumb%2Ftoc.json&tabs=azure-portal](https://learn.microsoft.com/en-us/azure/storage/common/manage-storage-analytics-logs?toc=%2Fazure%2Fstorage%2Fblobs%2Ftoc.json&bc=%2Fazure%2Fstorage%2Fblobs%2Fbreadcrumb%2Ftoc.json&tabs=azure-portal)

## 修正手順


### CLI

```text
az monitor diagnostic-settings subscription create --subscription <subscription id> --name <diagnostic settings name> --location <location> <[- -event-hub <event hub ID> --event-hub-auth-rule <event hub auth rule ID>] [-- storage-account <storage account ID>] [--workspace <log analytics workspace ID>] --logs '[{category:Security,enabled:true},{category:Administrative,enabled:true},{ca tegory:Alert,enabled:true},{category:Policy,enabled:true}]'>
```

### Other

[https://www.trendmicro.com/cloudoneconformity/knowledge-base/azure/Monitor/diagnostic-setting-categories.html](https://www.trendmicro.com/cloudoneconformity/knowledge-base/azure/Monitor/diagnostic-setting-categories.html)

## 参考資料

- [https://learn.microsoft.com/en-us/azure/azure-monitor/essentials/diagnostic-settings](https://learn.microsoft.com/en-us/azure/azure-monitor/essentials/diagnostic-settings)
- [https://learn.microsoft.com/en-us/azure/storage/common/manage-storage-analytics-logs?toc=%2Fazure%2Fstorage%2Fblobs%2Ftoc.json&bc=%2Fazure%2Fstorage%2Fblobs%2Fbreadcrumb%2Ftoc.json&tabs=azure-portal](https://learn.microsoft.com/en-us/azure/storage/common/manage-storage-analytics-logs?toc=%2Fazure%2Fstorage%2Fblobs%2Ftoc.json&bc=%2Fazure%2Fstorage%2Fblobs%2Fbreadcrumb%2Ftoc.json&tabs=azure-portal)

## 技術情報

- Source Metadata：[sources/azure/monitor_diagnostic_setting_with_appropriate_categories/metadata.json](../../sources/azure/monitor_diagnostic_setting_with_appropriate_categories/metadata.json)
- Source Code：[sources/azure/monitor_diagnostic_setting_with_appropriate_categories/check.py](../../sources/azure/monitor_diagnostic_setting_with_appropriate_categories/check.py)
- Source Metadata Path：`sources/azure/monitor_diagnostic_setting_with_appropriate_categories/metadata.json`
- Source Code Path：`sources/azure/monitor_diagnostic_setting_with_appropriate_categories/check.py`
