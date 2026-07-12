# Ensure that an Activity Log Alert exists for Service Health

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `monitor_alert_service_health_exists` |
| クラウドプラットフォーム | Azure |
| サービス | monitor |
| 重大度 | high |
| カテゴリ | Uncategorized |
| リソースタイプ | Monitor |
| リソースグループ | monitoring |

## 説明

Ensure that an Azure activity log alert is configured to trigger when Service Health events occur within your Microsoft Azure cloud account. The alert should activate when new events match the specified conditions in the alert rule configuration.

## リスク

Lack of monitoring for Service Health events may result in missing critical service issues, planned maintenance, security advisories, or other changes that could impact Azure services and regions in use.

## 推奨事項

Create an activity log alert for Service Health events and configure an action group to notify appropriate personnel.

- 推奨リンク：[https://learn.microsoft.com/en-us/azure/service-health/alerts-activity-log-service-notifications-portal](https://learn.microsoft.com/en-us/azure/service-health/alerts-activity-log-service-notifications-portal)

## 修正手順


### CLI

```text
az monitor activity-log alert create --subscription <subscription-id> --resource-group <resource-group> --name <alert-rule> --condition category=ServiceHealth and properties.incidentType=Incident --scope /subscriptions/<subscription-id> --action-group <action-group>
```

### Other

[https://www.trendmicro.com/cloudoneconformity/knowledge-base/azure/ActivityLog/service-health-alert.html](https://www.trendmicro.com/cloudoneconformity/knowledge-base/azure/ActivityLog/service-health-alert.html)

## 参考資料

- [https://learn.microsoft.com/en-us/azure/service-health/overview](https://learn.microsoft.com/en-us/azure/service-health/overview)
- [https://learn.microsoft.com/en-us/azure/service-health/alerts-activity-log-service-notifications-portal](https://learn.microsoft.com/en-us/azure/service-health/alerts-activity-log-service-notifications-portal)

## 技術情報

- Source Metadata：[sources/azure/monitor_alert_service_health_exists/metadata.json](../../sources/azure/monitor_alert_service_health_exists/metadata.json)
- Source Code：[sources/azure/monitor_alert_service_health_exists/check.py](../../sources/azure/monitor_alert_service_health_exists/check.py)
- Source Metadata Path：`sources/azure/monitor_alert_service_health_exists/metadata.json`
- Source Code Path：`sources/azure/monitor_alert_service_health_exists/check.py`
