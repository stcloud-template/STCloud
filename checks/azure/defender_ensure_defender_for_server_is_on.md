# Ensure That Microsoft Defender for Servers Is Set to 'On'

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `defender_ensure_defender_for_server_is_on` |
| 云平台 | Azure |
| 服务 | defender |
| 严重等级 | high |
| 类别 | Uncategorized |
| 资源类型 | AzureDefenderPlan |
| 资源组 | security |

## 描述

Ensure That Microsoft Defender for Servers Is Set to 'On'

## 风险

Turning on Microsoft Defender for Servers enables threat detection for Servers, providing threat intelligence, anomaly detection, and behavior analytics in the Microsoft Defender for Cloud.

## 推荐措施

Enabling Microsoft Defender for Cloud standard pricing tier allows for better security assessment with threat detection provided by the Microsoft Security Response Center (MSRC), advanced security policies, adaptive application control, network threat detection, and regulatory compliance management.

## 修复步骤


### Terraform

[https://docs.ST Cloud.com/checks/azure/azure-general-policies/ensure-that-azure-defender-is-set-to-on-for-servers#terraform](https://docs.ST Cloud.com/checks/azure/azure-general-policies/ensure-that-azure-defender-is-set-to-on-for-servers#terraform)

### Other

[https://www.trendmicro.com/cloudoneconformity/knowledge-base/azure/SecurityCenter/microsoft-defender-vm-server.html](https://www.trendmicro.com/cloudoneconformity/knowledge-base/azure/SecurityCenter/microsoft-defender-vm-server.html)

## 参考资料

No external references available.

## 技术信息

- Source Metadata：[sources/azure/defender_ensure_defender_for_server_is_on/metadata.json](../../sources/azure/defender_ensure_defender_for_server_is_on/metadata.json)
- Source Code：[sources/azure/defender_ensure_defender_for_server_is_on/check.py](../../sources/azure/defender_ensure_defender_for_server_is_on/check.py)
- Source Metadata Path：`sources/azure/defender_ensure_defender_for_server_is_on/metadata.json`
- Source Code Path：`sources/azure/defender_ensure_defender_for_server_is_on/check.py`
