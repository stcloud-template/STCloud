# Ensure that Microsoft Defender for Cloud Apps integration with Microsoft Defender for Cloud is Selected

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `defender_ensure_mcas_is_enabled` |
| 云平台 | Azure |
| 服务 | defender |
| 严重等级 | medium |
| 类别 | Uncategorized |
| 资源类型 | DefenderSettings |
| 资源组 | security |

## 描述

This integration setting enables Microsoft Defender for Cloud Apps (formerly 'Microsoft Cloud App Security' or 'MCAS' - see additional info) to communicate with Microsoft Defender for Cloud.

## 风险

Microsoft Defender for Cloud offers an additional layer of protection by using Azure Resource Manager events, which is considered to be the control plane for Azure. By analyzing the Azure Resource Manager records, Microsoft Defender for Cloud detects unusual or potentially harmful operations in the Azure subscription environment. Several of the preceding analytics are powered by Microsoft Defender for Cloud Apps. To benefit from these analytics, subscription must have a Cloud App Security license. Microsoft Defender for Cloud Apps works only with Standard Tier subscriptions.

## 推荐措施

1. From Azure Home select the Portal Menu. 2. Select Microsoft Defender for Cloud. 3. Select Environment Settings blade. 4. Select the subscription. 5. Check App Service Defender Plan to On. 6. Select Save.

- 推荐链接：[https://docs.microsoft.com/en-us/rest/api/securitycenter/settings/list](https://docs.microsoft.com/en-us/rest/api/securitycenter/settings/list)

## 修复步骤


### Other

[https://www.trendmicro.com/cloudoneconformity/knowledge-base/azure/SecurityCenter/defender-cloud-apps-integration.html#](https://www.trendmicro.com/cloudoneconformity/knowledge-base/azure/SecurityCenter/defender-cloud-apps-integration.html#)

## 参考资料

- [https://learn.microsoft.com/en-in/azure/defender-for-cloud/defender-for-cloud-introduction#secure-cloud-applications](https://learn.microsoft.com/en-in/azure/defender-for-cloud/defender-for-cloud-introduction#secure-cloud-applications)
- [https://docs.microsoft.com/en-us/rest/api/securitycenter/settings/list](https://docs.microsoft.com/en-us/rest/api/securitycenter/settings/list)

## 技术信息

- Source Metadata：[sources/azure/defender_ensure_mcas_is_enabled/metadata.json](../../sources/azure/defender_ensure_mcas_is_enabled/metadata.json)
- Source Code：[sources/azure/defender_ensure_mcas_is_enabled/check.py](../../sources/azure/defender_ensure_mcas_is_enabled/check.py)
- Source Metadata Path：`sources/azure/defender_ensure_mcas_is_enabled/metadata.json`
- Source Code Path：`sources/azure/defender_ensure_mcas_is_enabled/check.py`
