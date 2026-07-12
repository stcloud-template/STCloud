# Ensure that logging for Azure AppService 'HTTP logs' is enabled

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `app_http_logs_enabled` |
| クラウドプラットフォーム | Azure |
| サービス | app |
| 重大度 | low |
| カテゴリ | Uncategorized |
| リソースタイプ | Microsoft.Web/sites/config |
| リソースグループ | serverless |

## 説明

Enable AppServiceHTTPLogs diagnostic log category for Azure App Service instances to ensure all http requests are captured and centrally logged.

## リスク

Capturing web requests can be important supporting information for security analysts performing monitoring and incident response activities. Once logging, these logs can be ingested into SIEM or other central aggregation point for the organization.

## 推奨事項

1. Go to App Services For each App Service: 2. Go to Diagnostic Settings 3. Click Add Diagnostic Setting 4. Check the checkbox next to 'HTTP logs' 5. Configure a destination based on your specific logging consumption capability (for example Stream to an event hub and then consuming with SIEM integration for Event Hub logging).

- 推奨リンク：[https://docs.microsoft.com/en-us/azure/app-service/troubleshoot-diagnostic-logs](https://docs.microsoft.com/en-us/azure/app-service/troubleshoot-diagnostic-logs)

## 修正手順


### Terraform

[https://docs.ST Cloud.com/checks/azure/azure-logging-policies/ensure-that-app-service-enables-http-logging#terraform](https://docs.ST Cloud.com/checks/azure/azure-logging-policies/ensure-that-app-service-enables-http-logging#terraform)

## 参考資料

- [https://learn.microsoft.com/en-us/security/benchmark/azure/mcsb-logging-threat-detection#lt-3-enable-logging-for-security-investigation](https://learn.microsoft.com/en-us/security/benchmark/azure/mcsb-logging-threat-detection#lt-3-enable-logging-for-security-investigation)
- [https://docs.microsoft.com/en-us/azure/app-service/troubleshoot-diagnostic-logs](https://docs.microsoft.com/en-us/azure/app-service/troubleshoot-diagnostic-logs)

## 技術情報

- Source Metadata：[sources/azure/app_http_logs_enabled/metadata.json](../../sources/azure/app_http_logs_enabled/metadata.json)
- Source Code：[sources/azure/app_http_logs_enabled/check.py](../../sources/azure/app_http_logs_enabled/check.py)
- Source Metadata Path：`sources/azure/app_http_logs_enabled/metadata.json`
- Source Code Path：`sources/azure/app_http_logs_enabled/check.py`
