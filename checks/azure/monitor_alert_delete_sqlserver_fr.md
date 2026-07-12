# Ensure that Activity Log Alert exists for Delete SQL Server Firewall Rule

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `monitor_alert_delete_sqlserver_fr` |
| クラウドプラットフォーム | Azure |
| サービス | monitor |
| 重大度 | high |
| カテゴリ | Uncategorized |
| リソースタイプ | Monitor |
| リソースグループ | monitoring |

## 説明

Create an activity log alert for the 'Delete SQL Server Firewall Rule.'

## リスク

Monitoring for Delete SQL Server Firewall Rule events gives insight into SQL network access changes and may reduce the time it takes to detect suspicious activity.

## 推奨事項

1. Navigate to the Monitor blade. 2. Select Alerts. 3. Select Create. 4. Select Alert rule. 5. Under Filter by subscription, choose a subscription. 6. Under Filter by resource type, select Server Firewall Rule (servers/firewallRules). 7. Under Filter by location, select All. 8. From the results, select the subscription. 9. Select Done. 10. Select the Condition tab. 11. Under Signal name, click Delete server firewall rule (Microsoft.Sql/servers/firewallRules). 12. Select the Actions tab. 13. To use an existing action group, click Select action groups. To create a new action group, click Create action group. Fill out the appropriate details for the selection. 14. Select the Details tab. 15. Select a Resource group, provide an Alert rule name and an optional Alert rule description. 16. Click Review + create. 17. Click Create.

- 推奨リンク：[https://azure.microsoft.com/en-us/updates/classic-alerting-monitoring-retirement](https://azure.microsoft.com/en-us/updates/classic-alerting-monitoring-retirement)

## 修正手順


### CLI

```text
az monitor activity-log alert create --resource-group '<resource group name>' --condition category=Administrative and operationName=Microsoft.Sql/servers/firewallRules/delete and level=<verbose | information | warning | error | critical>--scope '/subscriptions/<subscription ID>' --name '<activity log rule name>' -- subscription <subscription id> --action-group <action group ID> --location global
```

### Other

[https://www.trendmicro.com/cloudoneconformity-staging/knowledge-base/azure/ActivityLog/create-or-update-or-delete-sql-server-firewall-rule-alert.html#trendmicro](https://www.trendmicro.com/cloudoneconformity-staging/knowledge-base/azure/ActivityLog/create-or-update-or-delete-sql-server-firewall-rule-alert.html#trendmicro)

## 参考資料

- [https://docs.microsoft.com/en-in/azure/azure-monitor/platform/alerts-activity-log](https://docs.microsoft.com/en-in/azure/azure-monitor/platform/alerts-activity-log)
- [https://azure.microsoft.com/en-us/updates/classic-alerting-monitoring-retirement](https://azure.microsoft.com/en-us/updates/classic-alerting-monitoring-retirement)

## 技術情報

- Source Metadata：[sources/azure/monitor_alert_delete_sqlserver_fr/metadata.json](../../sources/azure/monitor_alert_delete_sqlserver_fr/metadata.json)
- Source Code：[sources/azure/monitor_alert_delete_sqlserver_fr/check.py](../../sources/azure/monitor_alert_delete_sqlserver_fr/check.py)
- Source Metadata Path：`sources/azure/monitor_alert_delete_sqlserver_fr/metadata.json`
- Source Code Path：`sources/azure/monitor_alert_delete_sqlserver_fr/check.py`
