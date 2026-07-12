# Ensure that Microsoft Defender Recommendation for 'Apply system updates' status is 'Completed'

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `defender_ensure_system_updates_are_applied` |
| クラウドプラットフォーム | Azure |
| サービス | defender |
| 重大度 | high |
| カテゴリ | Uncategorized |
| リソースタイプ | AzureDefenderRecommendation |
| リソースグループ | security |

## 説明

Ensure that the latest OS patches for all virtual machines are applied.

## リスク

The Azure Security Center retrieves a list of available security and critical updates from Windows Update or Windows Server Update Services (WSUS), depending on which service is configured on a Windows VM. The security center also checks for the latest updates in Linux systems. If a VM is missing a system update, the security center will recommend system updates be applied.

## 推奨事項

Follow Microsoft Azure documentation to apply security patches from the security center. Alternatively, you can employ your own patch assessment and management tool to periodically assess, report, and install the required security patches for your OS.

- 推奨リンク：[https://learn.microsoft.com/en-us/azure/virtual-machines/updates-maintenance-overview](https://learn.microsoft.com/en-us/azure/virtual-machines/updates-maintenance-overview)

## 修正手順


### Other

[https://www.trendmicro.com/cloudoneconformity/knowledge-base/azure/VirtualMachines/apply-latest-os-patches.html](https://www.trendmicro.com/cloudoneconformity/knowledge-base/azure/VirtualMachines/apply-latest-os-patches.html)

## 参考資料

- [https://docs.microsoft.com/en-us/security/benchmark/azure/security-controls-v3-posture-vulnerability-management#pv-7-rapidly-and-automatically-remediate-software-vulnerabilities](https://docs.microsoft.com/en-us/security/benchmark/azure/security-controls-v3-posture-vulnerability-management#pv-7-rapidly-and-automatically-remediate-software-vulnerabilities)
- [https://learn.microsoft.com/en-us/azure/virtual-machines/updates-maintenance-overview](https://learn.microsoft.com/en-us/azure/virtual-machines/updates-maintenance-overview)

## 技術情報

- Source Metadata：[sources/azure/defender_ensure_system_updates_are_applied/metadata.json](../../sources/azure/defender_ensure_system_updates_are_applied/metadata.json)
- Source Code：[sources/azure/defender_ensure_system_updates_are_applied/check.py](../../sources/azure/defender_ensure_system_updates_are_applied/check.py)
- Source Metadata Path：`sources/azure/defender_ensure_system_updates_are_applied/metadata.json`
- Source Code Path：`sources/azure/defender_ensure_system_updates_are_applied/check.py`
