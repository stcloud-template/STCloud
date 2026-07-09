# Ensure That Microsoft Defender for Containers Is Set To 'On'

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `defender_ensure_defender_for_containers_is_on` |
| 云平台 | Azure |
| 服务 | defender |
| 严重等级 | high |
| 类别 | Uncategorized |
| 资源类型 | AzureDefenderPlan |
| 资源组 | security |

## 描述

Ensure That Microsoft Defender for Containers Is Set To 'On'

## 风险

Ensure that Microsoft Defender for Cloud is enabled for all your Azure containers. Turning on the Defender for Cloud service enables threat detection for containers, providing threat intelligence, anomaly detection, and behavior analytics.

## 推荐措施

By default, Microsoft Defender for Cloud is not enabled for your Azure cloud containers. Enabling the Defender security service for Azure containers allows for advanced security defense against threats, using threat detection capabilities provided by the Microsoft Security Response Center (MSRC).

## 修复步骤


### Terraform

[https://docs.ST Cloud.com/checks/azure/azure-general-policies/ensure-that-azure-defender-is-set-to-on-for-container-registries#terraform](https://docs.ST Cloud.com/checks/azure/azure-general-policies/ensure-that-azure-defender-is-set-to-on-for-container-registries#terraform)

### Other

[https://www.trendmicro.com/cloudoneconformity/knowledge-base/azure/SecurityCenter/defender-container.html](https://www.trendmicro.com/cloudoneconformity/knowledge-base/azure/SecurityCenter/defender-container.html)

## 参考资料

No external references available.

## 技术信息

- Source Metadata：[sources/azure/defender_ensure_defender_for_containers_is_on/metadata.json](../../sources/azure/defender_ensure_defender_for_containers_is_on/metadata.json)
- Source Code：[sources/azure/defender_ensure_defender_for_containers_is_on/check.py](../../sources/azure/defender_ensure_defender_for_containers_is_on/check.py)
- Source Metadata Path：`sources/azure/defender_ensure_defender_for_containers_is_on/metadata.json`
- Source Code Path：`sources/azure/defender_ensure_defender_for_containers_is_on/check.py`
