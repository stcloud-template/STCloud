# Ensure Function App has Application Insights configured

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `app_function_application_insights_enabled` |
| クラウドプラットフォーム | Azure |
| サービス | app |
| サブサービス | function |
| 重大度 | high |
| カテゴリ | Uncategorized |
| リソースタイプ | Microsoft.Web/sites |
| リソースグループ | serverless |

## 説明

Application Insights is a powerful tool for monitoring the performance and health of Azure Function Apps. It provides valuable insights into exceptions, performance issues, and usage patterns, enabling timely detection and resolution of issues.

## リスク

Without Application Insights, you may miss critical errors, performance degradation, or abnormal behavior in your Function App, potentially impacting availability and user experience.

## 推奨事項

Enable Application Insights for your Azure Function App to monitor its performance and health.

- 推奨リンク：[https://learn.microsoft.com/en-us/azure/azure-monitor/app/monitor-functions](https://learn.microsoft.com/en-us/azure/azure-monitor/app/monitor-functions)

## 修正手順


### Other

[https://www.trendmicro.com/cloudoneconformity/knowledge-base/azure/Functions/function-app-insights-on.html](https://www.trendmicro.com/cloudoneconformity/knowledge-base/azure/Functions/function-app-insights-on.html)

## 参考資料

- [https://learn.microsoft.com/en-us/azure/azure-monitor/app/app-insights-overview](https://learn.microsoft.com/en-us/azure/azure-monitor/app/app-insights-overview)
- [https://learn.microsoft.com/en-us/azure/azure-monitor/app/monitor-functions](https://learn.microsoft.com/en-us/azure/azure-monitor/app/monitor-functions)

## 技術情報

- Source Metadata：[sources/azure/app_function_application_insights_enabled/metadata.json](../../sources/azure/app_function_application_insights_enabled/metadata.json)
- Source Code：[sources/azure/app_function_application_insights_enabled/check.py](../../sources/azure/app_function_application_insights_enabled/check.py)
- Source Metadata Path：`sources/azure/app_function_application_insights_enabled/metadata.json`
- Source Code Path：`sources/azure/app_function_application_insights_enabled/check.py`
