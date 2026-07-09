# Ensure that Microsoft Defender for Endpoint integration with Microsoft Defender for Cloud is selected

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `defender_ensure_wdatp_is_enabled` |
| 云平台 | Azure |
| 服务 | defender |
| 严重等级 | medium |
| 类别 | Uncategorized |
| 资源类型 | DefenderSettings |
| 资源组 | security |

## 描述

This integration setting enables Microsoft Defender for Endpoint (formerly 'Advanced Threat Protection' or 'ATP' or 'WDATP' - see additional info) to communicate with Microsoft Defender for Cloud.

## 风险

Microsoft Defender for Endpoint integration brings comprehensive Endpoint Detection and Response (EDR) capabilities within Microsoft Defender for Cloud. This integration helps to spot abnormalities, as well as detect and respond to advanced attacks on endpoints monitored by Microsoft Defender for Cloud. MDE works only with Standard Tier subscriptions.

## 推荐措施

No content available.

- 推荐链接：[https://learn.microsoft.com/en-us/microsoft-365/security/defender-endpoint/azure-server-integration?view=o365-worldwide](https://learn.microsoft.com/en-us/microsoft-365/security/defender-endpoint/azure-server-integration?view=o365-worldwide)

## 修复步骤


### Other

[https://www.trendmicro.com/cloudoneconformity/knowledge-base/azure/SecurityCenter/defender-endpoint-integration.html](https://www.trendmicro.com/cloudoneconformity/knowledge-base/azure/SecurityCenter/defender-endpoint-integration.html)

## 参考资料

- [https://learn.microsoft.com/en-in/azure/defender-for-cloud/integration-defender-for-endpoint?tabs=windows](https://learn.microsoft.com/en-in/azure/defender-for-cloud/integration-defender-for-endpoint?tabs=windows)
- [https://learn.microsoft.com/en-us/microsoft-365/security/defender-endpoint/azure-server-integration?view=o365-worldwide](https://learn.microsoft.com/en-us/microsoft-365/security/defender-endpoint/azure-server-integration?view=o365-worldwide)

## 技术信息

- Source Metadata：[sources/azure/defender_ensure_wdatp_is_enabled/metadata.json](../../sources/azure/defender_ensure_wdatp_is_enabled/metadata.json)
- Source Code：[sources/azure/defender_ensure_wdatp_is_enabled/check.py](../../sources/azure/defender_ensure_wdatp_is_enabled/check.py)
- Source Metadata Path：`sources/azure/defender_ensure_wdatp_is_enabled/metadata.json`
- Source Code Path：`sources/azure/defender_ensure_wdatp_is_enabled/check.py`
