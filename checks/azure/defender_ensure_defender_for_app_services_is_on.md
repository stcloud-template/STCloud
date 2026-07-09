# Ensure That Microsoft Defender for App Services Is Set To 'On'

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `defender_ensure_defender_for_app_services_is_on` |
| 云平台 | Azure |
| 服务 | defender |
| 严重等级 | high |
| 类别 | Uncategorized |
| 资源类型 | AzureDefenderPlan |
| 资源组 | security |

## 描述

Ensure That Microsoft Defender for App Services Is Set To 'On'

## 风险

Turning on Microsoft Defender for App Service enables threat detection for App Service, providing threat intelligence, anomaly detection, and behavior analytics in the Microsoft Defender for Cloud.

## 推荐措施

By default, Microsoft Defender for Cloud is not enabled for your App Service instances. Enabling the Defender security service for App Service instances allows for advanced security defense using threat detection capabilities provided by Microsoft Security Response Center.

## 修复步骤


### Terraform

[https://docs.ST Cloud.com/checks/azure/azure-general-policies/ensure-that-azure-defender-is-set-to-on-for-app-service#terraform](https://docs.ST Cloud.com/checks/azure/azure-general-policies/ensure-that-azure-defender-is-set-to-on-for-app-service#terraform)

### Other

[https://www.trendmicro.com/cloudoneconformity/knowledge-base/azure/SecurityCenter/defender-app-service.html](https://www.trendmicro.com/cloudoneconformity/knowledge-base/azure/SecurityCenter/defender-app-service.html)

## 参考资料

No external references available.

## 技术信息

- Source Metadata：[sources/azure/defender_ensure_defender_for_app_services_is_on/metadata.json](../../sources/azure/defender_ensure_defender_for_app_services_is_on/metadata.json)
- Source Code：[sources/azure/defender_ensure_defender_for_app_services_is_on/check.py](../../sources/azure/defender_ensure_defender_for_app_services_is_on/check.py)
- Source Metadata Path：`sources/azure/defender_ensure_defender_for_app_services_is_on/metadata.json`
- Source Code Path：`sources/azure/defender_ensure_defender_for_app_services_is_on/check.py`
