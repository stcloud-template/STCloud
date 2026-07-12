# Ensure Application Insights are Configured.

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `appinsights_ensure_is_configured` |
| クラウドプラットフォーム | Azure |
| サービス | appinsights |
| 重大度 | low |
| カテゴリ | Uncategorized |
| リソースタイプ | Microsoft.Insights/components |
| リソースグループ | monitoring |

## 説明

Application Insights within Azure act as an Application Performance Monitoring solution providing valuable data into how well an application performs and additional information when performing incident response. The types of log data collected include application metrics, telemetry data, and application trace logging data providing organizations with detailed information about application activity and application transactions. Both data sets help organizations adopt a proactive and retroactive means to handle security and performance related metrics within their modern applications.

## リスク

Configuring Application Insights provides additional data not found elsewhere within Azure as part of a much larger logging and monitoring program within an organization's Information Security practice. The types and contents of these logs will act as both a potential cost saving measure (application performance) and a means to potentially confirm the source of a potential incident (trace logging). Metrics and Telemetry data provide organizations with a proactive approach to cost savings by monitoring an application's performance, while the trace logging data provides necessary details in a reactive incident response scenario by helping organizations identify the potential source of an incident within their application.

## 推奨事項

1. Navigate to Application Insights 2. Under the Basics tab within the PROJECT DETAILS section, select the Subscription 3. Select the Resource group 4. Within the INSTANCE DETAILS, enter a Name 5. Select a Region 6. Next to Resource Mode, select Workspace-based 7. Within the WORKSPACE DETAILS, select the Subscription for the log analytics workspace 8. Select the appropriate Log Analytics Workspace 9. Click Next:Tags > 10. Enter the appropriate Tags as Name, Value pairs. 11. Click Next:Review+Create 12. Click Create.

## 修正手順


### CLI

```text
az monitor app-insights component create --app <app name> --resource-group <resource group name> --location <location> --kind 'web' --retention-time <INT days to retain logs> --workspace <log analytics workspace ID> -- subscription <subscription ID>
```

### Other

[https://www.tenable.com/audits/items/CIS_Microsoft_Azure_Foundations_v2.0.0_L2.audit:8a7a608d180042689ad9d3f16aa359f1](https://www.tenable.com/audits/items/CIS_Microsoft_Azure_Foundations_v2.0.0_L2.audit:8a7a608d180042689ad9d3f16aa359f1)

## 参考資料

- [https://learn.microsoft.com/en-us/azure/azure-monitor/app/app-insights-overview](https://learn.microsoft.com/en-us/azure/azure-monitor/app/app-insights-overview)

## 技術情報

- Source Metadata：[sources/azure/appinsights_ensure_is_configured/metadata.json](../../sources/azure/appinsights_ensure_is_configured/metadata.json)
- Source Code：[sources/azure/appinsights_ensure_is_configured/check.py](../../sources/azure/appinsights_ensure_is_configured/check.py)
- Source Metadata Path：`sources/azure/appinsights_ensure_is_configured/metadata.json`
- Source Code Path：`sources/azure/appinsights_ensure_is_configured/check.py`
