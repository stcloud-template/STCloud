# Ensure that Auto provisioning of 'Log Analytics agent for Azure VMs' is Set to 'On'

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `defender_auto_provisioning_log_analytics_agent_vms_on` |
| 云平台 | Azure |
| 服务 | defender |
| 严重等级 | medium |
| 类别 | Uncategorized |
| 资源类型 | AzureDefenderPlan |
| 资源组 | security |

## 描述

Ensure that Auto provisioning of 'Log Analytics agent for Azure VMs' is Set to 'On'. The Microsoft Monitoring Agent scans for various security-related configurations and events such as system updates, OS vulnerabilities, endpoint protection, and provides alerts.

## 风险

Missing critical security information about your Azure VMs, such as security alerts, security recommendations, and change tracking.

## 推荐措施

Ensure comprehensive visibility into possible security vulnerabilities, including missing updates, misconfigured operating system security settings, and active threats, allowing for timely mitigation and improved overall security posture

- 推荐链接：[https://learn.microsoft.com/en-us/azure/defender-for-cloud/monitoring-components](https://learn.microsoft.com/en-us/azure/defender-for-cloud/monitoring-components)

## 修复步骤


### Other

[https://www.trendmicro.com/cloudoneconformity-staging/knowledge-base/azure/SecurityCenter/automatic-provisioning-of-monitoring-agent.html](https://www.trendmicro.com/cloudoneconformity-staging/knowledge-base/azure/SecurityCenter/automatic-provisioning-of-monitoring-agent.html)

## 参考资料

- [https://docs.microsoft.com/en-us/azure/security-center/security-center-data-security](https://docs.microsoft.com/en-us/azure/security-center/security-center-data-security)
- [https://learn.microsoft.com/en-us/azure/defender-for-cloud/monitoring-components](https://learn.microsoft.com/en-us/azure/defender-for-cloud/monitoring-components)

## 技术信息

- Source Metadata：[sources/azure/defender_auto_provisioning_log_analytics_agent_vms_on/metadata.json](../../sources/azure/defender_auto_provisioning_log_analytics_agent_vms_on/metadata.json)
- Source Code：[sources/azure/defender_auto_provisioning_log_analytics_agent_vms_on/check.py](../../sources/azure/defender_auto_provisioning_log_analytics_agent_vms_on/check.py)
- Source Metadata Path：`sources/azure/defender_auto_provisioning_log_analytics_agent_vms_on/metadata.json`
- Source Code Path：`sources/azure/defender_auto_provisioning_log_analytics_agent_vms_on/check.py`
