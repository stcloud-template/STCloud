# Ensure that Auto provisioning of 'Log Analytics agent for Azure VMs' is Set to 'On'

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `defender_auto_provisioning_log_analytics_agent_vms_on` |
| クラウドプラットフォーム | Azure |
| サービス | defender |
| 重大度 | medium |
| カテゴリ | Uncategorized |
| リソースタイプ | AzureDefenderPlan |
| リソースグループ | security |

## 説明

Ensure that Auto provisioning of 'Log Analytics agent for Azure VMs' is Set to 'On'. The Microsoft Monitoring Agent scans for various security-related configurations and events such as system updates, OS vulnerabilities, endpoint protection, and provides alerts.

## リスク

Missing critical security information about your Azure VMs, such as security alerts, security recommendations, and change tracking.

## 推奨事項

Ensure comprehensive visibility into possible security vulnerabilities, including missing updates, misconfigured operating system security settings, and active threats, allowing for timely mitigation and improved overall security posture

- 推奨リンク：[https://learn.microsoft.com/en-us/azure/defender-for-cloud/monitoring-components](https://learn.microsoft.com/en-us/azure/defender-for-cloud/monitoring-components)

## 修正手順


### Other

[https://www.trendmicro.com/cloudoneconformity-staging/knowledge-base/azure/SecurityCenter/automatic-provisioning-of-monitoring-agent.html](https://www.trendmicro.com/cloudoneconformity-staging/knowledge-base/azure/SecurityCenter/automatic-provisioning-of-monitoring-agent.html)

## 参考資料

- [https://docs.microsoft.com/en-us/azure/security-center/security-center-data-security](https://docs.microsoft.com/en-us/azure/security-center/security-center-data-security)
- [https://learn.microsoft.com/en-us/azure/defender-for-cloud/monitoring-components](https://learn.microsoft.com/en-us/azure/defender-for-cloud/monitoring-components)

## 技術情報

- Source Metadata：[sources/azure/defender_auto_provisioning_log_analytics_agent_vms_on/metadata.json](../../sources/azure/defender_auto_provisioning_log_analytics_agent_vms_on/metadata.json)
- Source Code：[sources/azure/defender_auto_provisioning_log_analytics_agent_vms_on/check.py](../../sources/azure/defender_auto_provisioning_log_analytics_agent_vms_on/check.py)
- Source Metadata Path：`sources/azure/defender_auto_provisioning_log_analytics_agent_vms_on/metadata.json`
- Source Code Path：`sources/azure/defender_auto_provisioning_log_analytics_agent_vms_on/check.py`
