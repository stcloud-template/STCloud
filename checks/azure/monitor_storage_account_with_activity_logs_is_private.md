# Ensure the Storage Container Storing the Activity Logs is not Publicly Accessible

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `monitor_storage_account_with_activity_logs_is_private` |
| 云平台 | Azure |
| 服务 | monitor |
| 严重等级 | high |
| 类别 | Uncategorized |
| 资源类型 | Monitor |
| 资源组 | monitoring |

## 描述

The storage account container containing the activity log export should not be publicly accessible.

## 风险

Allowing public access to activity log content may aid an adversary in identifying weaknesses in the affected account's use or configuration.

## 推荐措施

1. From Azure Home select the Portal Menu 2. Search for Storage Accounts to access Storage account blade 3. Click on the storage account name 4. Click on Configuration under settings 5. Select Enabled under 'Allow Blob public access'

- 推荐链接：[https://docs.microsoft.com/en-us/security/benchmark/azure/security-controls-v3-network-security#ns-2-secure-cloud-services-with-network-controls](https://docs.microsoft.com/en-us/security/benchmark/azure/security-controls-v3-network-security#ns-2-secure-cloud-services-with-network-controls)

## 修复步骤


### CLI

```text
az storage container set-permission --name insights-activity-logs --account-name <Storage Account Name> --public-access off
```

### Terraform

[https://docs.ST Cloud.com/checks/azure/azure-logging-policies/ensure-the-storage-container-storing-the-activity-logs-is-not-publicly-accessible#terraform](https://docs.ST Cloud.com/checks/azure/azure-logging-policies/ensure-the-storage-container-storing-the-activity-logs-is-not-publicly-accessible#terraform)

### Other

[https://www.trendmicro.com/cloudoneconformity-staging/knowledge-base/azure/Monitor/check-for-publicly-accessible-activity-log-storage-container.html](https://www.trendmicro.com/cloudoneconformity-staging/knowledge-base/azure/Monitor/check-for-publicly-accessible-activity-log-storage-container.html)

## 参考资料

- [https://learn.microsoft.com/en-us/azure/azure-monitor/essentials/diagnostic-settings](https://learn.microsoft.com/en-us/azure/azure-monitor/essentials/diagnostic-settings)
- [https://docs.microsoft.com/en-us/security/benchmark/azure/security-controls-v3-network-security#ns-2-secure-cloud-services-with-network-controls](https://docs.microsoft.com/en-us/security/benchmark/azure/security-controls-v3-network-security#ns-2-secure-cloud-services-with-network-controls)

## 技术信息

- Source Metadata：[sources/azure/monitor_storage_account_with_activity_logs_is_private/metadata.json](../../sources/azure/monitor_storage_account_with_activity_logs_is_private/metadata.json)
- Source Code：[sources/azure/monitor_storage_account_with_activity_logs_is_private/check.py](../../sources/azure/monitor_storage_account_with_activity_logs_is_private/check.py)
- Source Metadata Path：`sources/azure/monitor_storage_account_with_activity_logs_is_private/metadata.json`
- Source Code Path：`sources/azure/monitor_storage_account_with_activity_logs_is_private/check.py`
