# Ensure Function App has Application Insights configured

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `app_function_application_insights_enabled` |
| 云平台 | Azure |
| 服务 | app |
| 子服务 | function |
| 严重等级 | high |
| 类别 | Uncategorized |
| 资源类型 | Microsoft.Web/sites |
| 资源组 | serverless |

## 描述

Application Insights is a powerful tool for monitoring the performance and health of Azure Function Apps. It provides valuable insights into exceptions, performance issues, and usage patterns, enabling timely detection and resolution of issues.

## 风险

Without Application Insights, you may miss critical errors, performance degradation, or abnormal behavior in your Function App, potentially impacting availability and user experience.

## 推荐措施

Enable Application Insights for your Azure Function App to monitor its performance and health.

- 推荐链接：[https://learn.microsoft.com/en-us/azure/azure-monitor/app/monitor-functions](https://learn.microsoft.com/en-us/azure/azure-monitor/app/monitor-functions)

## 修复步骤


### Other

[https://www.trendmicro.com/cloudoneconformity/knowledge-base/azure/Functions/function-app-insights-on.html](https://www.trendmicro.com/cloudoneconformity/knowledge-base/azure/Functions/function-app-insights-on.html)

## 参考资料

- [https://learn.microsoft.com/en-us/azure/azure-monitor/app/app-insights-overview](https://learn.microsoft.com/en-us/azure/azure-monitor/app/app-insights-overview)
- [https://learn.microsoft.com/en-us/azure/azure-monitor/app/monitor-functions](https://learn.microsoft.com/en-us/azure/azure-monitor/app/monitor-functions)

## 技术信息

- Source Metadata：[sources/azure/app_function_application_insights_enabled/metadata.json](../../sources/azure/app_function_application_insights_enabled/metadata.json)
- Source Code：[sources/azure/app_function_application_insights_enabled/check.py](../../sources/azure/app_function_application_insights_enabled/check.py)
- Source Metadata Path：`sources/azure/app_function_application_insights_enabled/metadata.json`
- Source Code Path：`sources/azure/app_function_application_insights_enabled/check.py`
