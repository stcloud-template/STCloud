# Ensure that a 'Diagnostic Setting' exists for Subscription Activity Logs

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `monitor_diagnostic_settings_exists` |
| 云平台 | Azure |
| 服务 | monitor |
| 严重等级 | medium |
| 类别 | Uncategorized |
| 资源类型 | Monitor |
| 资源组 | monitoring |

## 描述

Enable Diagnostic settings for exporting activity logs. Diagnostic settings are available for each individual resource within a subscription. Settings should be configured for all appropriate resources for your environment.

## 风险

A diagnostic setting controls how a diagnostic log is exported. By default, logs are retained only for 90 days. Diagnostic settings should be defined so that logs can be exported and stored for a longer duration in order to analyze security activities within an Azure subscription.

## 推荐措施

To enable Diagnostic Settings on a Subscription: 1. Go to Monitor 2. Click on Activity Log 3. Click on Export Activity Logs 4. Click + Add diagnostic setting 5. Enter a Diagnostic setting name 6. Select Categories for the diagnostic settings 7. Select the appropriate Destination details (this may be Log Analytics, Storage Account, Event Hub, or Partner solution) 8. Click Save To enable Diagnostic Settings on a specific resource: 1. Go to Monitor 2. Click Diagnostic settings 3. Click on the resource that has a diagnostics status of disabled 4. Select Add Diagnostic Setting 5. Enter a Diagnostic setting name 6. Select the appropriate log, metric, and destination. (this may be Log Analytics, Storage Account, Event Hub, or Partner solution) 7. Click save Repeat these step for all resources as needed.

- 推荐链接：[https://docs.microsoft.com/en-us/azure/monitoring-and-diagnostics/monitoring-overview-activity-logs#export-the-activity-log-with-a-log-profile](https://docs.microsoft.com/en-us/azure/monitoring-and-diagnostics/monitoring-overview-activity-logs#export-the-activity-log-with-a-log-profile)

## 修复步骤


### CLI

```text
az monitor diagnostic-settings subscription create --subscription <subscription id> --name <diagnostic settings name> --location <location> <[- -event-hub <event hub ID> --event-hub-auth-rule <event hub auth rule ID>] [-- storage-account <storage account ID>] [--workspace <log analytics workspace ID>] --logs '<JSON encoded categories>' (e.g. [{category:Security,enabled:true},{category:Administrative,enabled:true},{cat egory:Alert,enabled:true},{category:Policy,enabled:true}])
```

### Other

[https://www.trendmicro.com/cloudoneconformity-staging/knowledge-base/azure/Monitor/subscription-activity-log-diagnostic-settings.html#trendmicro](https://www.trendmicro.com/cloudoneconformity-staging/knowledge-base/azure/Monitor/subscription-activity-log-diagnostic-settings.html#trendmicro)

## 参考资料

- [https://learn.microsoft.com/en-us/cli/azure/monitor/diagnostic-settings?view=azure-cli-latest](https://learn.microsoft.com/en-us/cli/azure/monitor/diagnostic-settings?view=azure-cli-latest)
- [https://docs.microsoft.com/en-us/azure/monitoring-and-diagnostics/monitoring-overview-activity-logs#export-the-activity-log-with-a-log-profile](https://docs.microsoft.com/en-us/azure/monitoring-and-diagnostics/monitoring-overview-activity-logs#export-the-activity-log-with-a-log-profile)

## 技术信息

- Source Metadata：[sources/azure/monitor_diagnostic_settings_exists/metadata.json](../../sources/azure/monitor_diagnostic_settings_exists/metadata.json)
- Source Code：[sources/azure/monitor_diagnostic_settings_exists/check.py](../../sources/azure/monitor_diagnostic_settings_exists/check.py)
- Source Metadata Path：`sources/azure/monitor_diagnostic_settings_exists/metadata.json`
- Source Code Path：`sources/azure/monitor_diagnostic_settings_exists/check.py`
