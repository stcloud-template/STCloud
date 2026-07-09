# Ensure that Microsoft Defender Recommendation for 'Apply system updates' status is 'Completed'

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `defender_ensure_system_updates_are_applied` |
| 云平台 | Azure |
| 服务 | defender |
| 严重等级 | high |
| 类别 | Uncategorized |
| 资源类型 | AzureDefenderRecommendation |
| 资源组 | security |

## 描述

Ensure that the latest OS patches for all virtual machines are applied.

## 风险

The Azure Security Center retrieves a list of available security and critical updates from Windows Update or Windows Server Update Services (WSUS), depending on which service is configured on a Windows VM. The security center also checks for the latest updates in Linux systems. If a VM is missing a system update, the security center will recommend system updates be applied.

## 推荐措施

Follow Microsoft Azure documentation to apply security patches from the security center. Alternatively, you can employ your own patch assessment and management tool to periodically assess, report, and install the required security patches for your OS.

- 推荐链接：[https://learn.microsoft.com/en-us/azure/virtual-machines/updates-maintenance-overview](https://learn.microsoft.com/en-us/azure/virtual-machines/updates-maintenance-overview)

## 修复步骤


### Other

[https://www.trendmicro.com/cloudoneconformity/knowledge-base/azure/VirtualMachines/apply-latest-os-patches.html](https://www.trendmicro.com/cloudoneconformity/knowledge-base/azure/VirtualMachines/apply-latest-os-patches.html)

## 参考资料

- [https://docs.microsoft.com/en-us/security/benchmark/azure/security-controls-v3-posture-vulnerability-management#pv-7-rapidly-and-automatically-remediate-software-vulnerabilities](https://docs.microsoft.com/en-us/security/benchmark/azure/security-controls-v3-posture-vulnerability-management#pv-7-rapidly-and-automatically-remediate-software-vulnerabilities)
- [https://learn.microsoft.com/en-us/azure/virtual-machines/updates-maintenance-overview](https://learn.microsoft.com/en-us/azure/virtual-machines/updates-maintenance-overview)

## 技术信息

- Source Metadata：[sources/azure/defender_ensure_system_updates_are_applied/metadata.json](../../sources/azure/defender_ensure_system_updates_are_applied/metadata.json)
- Source Code：[sources/azure/defender_ensure_system_updates_are_applied/check.py](../../sources/azure/defender_ensure_system_updates_are_applied/check.py)
- Source Metadata Path：`sources/azure/defender_ensure_system_updates_are_applied/metadata.json`
- Source Code Path：`sources/azure/defender_ensure_system_updates_are_applied/check.py`
