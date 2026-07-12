# Ensure that Activity Log Alert exists for Delete Security Solution

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `monitor_alert_delete_security_solution` |
| クラウドプラットフォーム | Azure |
| サービス | monitor |
| 重大度 | high |
| カテゴリ | Uncategorized |
| リソースタイプ | Monitor |
| リソースグループ | monitoring |

## 説明

Create an activity log alert for the Delete Security Solution event.

## リスク

Monitoring for Delete Security Solution events gives insight into changes to the active security solutions and may reduce the time it takes to detect suspicious activity.

## 推奨事項

1. Navigate to the Monitor blade. 2. Select Alerts. 3. Select Create. 4. Select Alert rule. 5. Under Filter by subscription, choose a subscription. 6. Under Filter by resource type, select Security Solutions (securitySolutions). 7. Under Filter by location, select All. 8. From the results, select the subscription. 9. Select Done. 10. Select the Condition tab. 11. Under Signal name, click Delete Security Solutions (Microsoft.Security/securitySolutions). 12. Select the Actions tab. 13. To use an existing action group, click Select action groups. To create a new action group, click Create action group. Fill out the appropriate details for the selection. 14. Select the Details tab. 15. Select a Resource group, provide an Alert rule name and an optional Alert rule description. 16. Click Review + create. 17. Click Create.curitySolutions). 7. Under Filter by location, select All. 8. From the results, select the subscription. 9. Select Done. 10. Select the Condition tab. 11. Under Signal name, click Create or Update Security Solutions (Microsoft.Security/securitySolutions). 12. Select the Actions tab. 13. To use an existing action group, click Select action groups. To create a new action group, click Create action group. Fill out the appropriate details for the selection. 14. Select the Details tab. 15. Select a Resource group, provide an Alert rule name and an optional Alert rule description. 16. Click Review + create. 17. Click Create.

- 推奨リンク：[https://azure.microsoft.com/en-us/updates/classic-alerting-monitoring-retirement](https://azure.microsoft.com/en-us/updates/classic-alerting-monitoring-retirement)

## 修正手順


### CLI

```text
az monitor activity-log alert create --resource-group '<resource group name>' --condition category=Administrative and operationName=Microsoft.Security/securitySolutions/delete and level=<verbose | information | warning | error | critical>--scope '/subscriptions/<subscription ID>' --name '<activity log rule name>' -- subscription <subscription id> --action-group <action group ID> --location global
```

### Other

[https://www.trendmicro.com/cloudoneconformity-staging/knowledge-base/azure/ActivityLog/delete-security-solution-alert.html#trendmicro](https://www.trendmicro.com/cloudoneconformity-staging/knowledge-base/azure/ActivityLog/delete-security-solution-alert.html#trendmicro)

## 参考資料

- [https://docs.microsoft.com/en-in/azure/azure-monitor/platform/alerts-activity-log](https://docs.microsoft.com/en-in/azure/azure-monitor/platform/alerts-activity-log)
- [https://azure.microsoft.com/en-us/updates/classic-alerting-monitoring-retirement](https://azure.microsoft.com/en-us/updates/classic-alerting-monitoring-retirement)

## 技術情報

- Source Metadata：[sources/azure/monitor_alert_delete_security_solution/metadata.json](../../sources/azure/monitor_alert_delete_security_solution/metadata.json)
- Source Code：[sources/azure/monitor_alert_delete_security_solution/check.py](../../sources/azure/monitor_alert_delete_security_solution/check.py)
- Source Metadata Path：`sources/azure/monitor_alert_delete_security_solution/metadata.json`
- Source Code Path：`sources/azure/monitor_alert_delete_security_solution/check.py`
