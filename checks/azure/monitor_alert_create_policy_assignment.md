# Ensure that Activity Log Alert exists for Create Policy Assignment

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `monitor_alert_create_policy_assignment` |
| 云平台 | Azure |
| 服务 | monitor |
| 严重等级 | high |
| 类别 | Uncategorized |
| 资源类型 | Monitor |
| 资源组 | monitoring |

## 描述

Create an activity log alert for the Create Policy Assignment event.

## 风险

Monitoring for create policy assignment events gives insight into changes done in 'Azure policy - assignments' and can reduce the time it takes to detect unsolicited changes.

## 推荐措施

1. Navigate to the Monitor blade. 2. Select Alerts. 3. Select Create. 4. Select Alert rule. 5. Under Filter by subscription, choose a subscription. 6. Under Filter by resource type, select Policy assignment (policyAssignments). 7. Under Filter by location, select All. 8. From the results, select the subscription. 9. Select Done. 10. Select the Condition tab. 11. Under Signal name, click Create policy assignment (Microsoft.Authorization/policyAssignments). 12. Select the Actions tab. 13. To use an existing action group, click elect action groups. To create a new action group, click Create action group. Fill out the appropriate details for the selection. 14. Select the Details tab. 15. Select a Resource group, provide an Alert rule name and an optional Alert rule description. 16. Click Review + create. 17. Click Create.

- 推荐链接：[https://docs.microsoft.com/en-in/azure/azure-monitor/platform/alerts-activity-log](https://docs.microsoft.com/en-in/azure/azure-monitor/platform/alerts-activity-log)

## 修复步骤


### CLI

```text
az monitor activity-log alert create --resource-group '<resource group name>' --condition category=Administrative and operationName=Microsoft.Authorization/policyAssignments/write and level=<verbose | information | warning | error | critical> --scope '/subscriptions/<subscription ID>' --name '<activity log rule name>' -- subscription <subscription ID> --action-group <action group ID> --location global
```

### Other

[https://www.trendmicro.com/cloudoneconformity-staging/knowledge-base/azure/ActivityLog/create-alert-for-create-policy-assignment-events.html#trendmicro](https://www.trendmicro.com/cloudoneconformity-staging/knowledge-base/azure/ActivityLog/create-alert-for-create-policy-assignment-events.html#trendmicro)

## 参考资料

- [https://azure.microsoft.com/en-us/updates/classic-alerting-monitoring-retirement](https://azure.microsoft.com/en-us/updates/classic-alerting-monitoring-retirement)
- [https://docs.microsoft.com/en-in/azure/azure-monitor/platform/alerts-activity-log](https://docs.microsoft.com/en-in/azure/azure-monitor/platform/alerts-activity-log)

## 技术信息

- Source Metadata：[sources/azure/monitor_alert_create_policy_assignment/metadata.json](../../sources/azure/monitor_alert_create_policy_assignment/metadata.json)
- Source Code：[sources/azure/monitor_alert_create_policy_assignment/check.py](../../sources/azure/monitor_alert_create_policy_assignment/check.py)
- Source Metadata Path：`sources/azure/monitor_alert_create_policy_assignment/metadata.json`
- Source Code Path：`sources/azure/monitor_alert_create_policy_assignment/check.py`
