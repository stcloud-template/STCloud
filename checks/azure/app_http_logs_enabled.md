# Ensure that logging for Azure AppService 'HTTP logs' is enabled

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `app_http_logs_enabled` |
| 云平台 | Azure |
| 服务 | app |
| 严重等级 | low |
| 类别 | Uncategorized |
| 资源类型 | Microsoft.Web/sites/config |
| 资源组 | serverless |

## 描述

Enable AppServiceHTTPLogs diagnostic log category for Azure App Service instances to ensure all http requests are captured and centrally logged.

## 风险

Capturing web requests can be important supporting information for security analysts performing monitoring and incident response activities. Once logging, these logs can be ingested into SIEM or other central aggregation point for the organization.

## 推荐措施

1. Go to App Services For each App Service: 2. Go to Diagnostic Settings 3. Click Add Diagnostic Setting 4. Check the checkbox next to 'HTTP logs' 5. Configure a destination based on your specific logging consumption capability (for example Stream to an event hub and then consuming with SIEM integration for Event Hub logging).

- 推荐链接：[https://docs.microsoft.com/en-us/azure/app-service/troubleshoot-diagnostic-logs](https://docs.microsoft.com/en-us/azure/app-service/troubleshoot-diagnostic-logs)

## 修复步骤


### Terraform

[https://docs.ST Cloud.com/checks/azure/azure-logging-policies/ensure-that-app-service-enables-http-logging#terraform](https://docs.ST Cloud.com/checks/azure/azure-logging-policies/ensure-that-app-service-enables-http-logging#terraform)

## 参考资料

- [https://learn.microsoft.com/en-us/security/benchmark/azure/mcsb-logging-threat-detection#lt-3-enable-logging-for-security-investigation](https://learn.microsoft.com/en-us/security/benchmark/azure/mcsb-logging-threat-detection#lt-3-enable-logging-for-security-investigation)
- [https://docs.microsoft.com/en-us/azure/app-service/troubleshoot-diagnostic-logs](https://docs.microsoft.com/en-us/azure/app-service/troubleshoot-diagnostic-logs)

## 技术信息

- Source Metadata：[sources/azure/app_http_logs_enabled/metadata.json](../../sources/azure/app_http_logs_enabled/metadata.json)
- Source Code：[sources/azure/app_http_logs_enabled/check.py](../../sources/azure/app_http_logs_enabled/check.py)
- Source Metadata Path：`sources/azure/app_http_logs_enabled/metadata.json`
- Source Code Path：`sources/azure/app_http_logs_enabled/check.py`
