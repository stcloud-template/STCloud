# Ensure That Microsoft Defender for Storage Is Set To 'On'

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `defender_ensure_defender_for_storage_is_on` |
| 云平台 | Azure |
| 服务 | defender |
| 严重等级 | high |
| 类别 | Uncategorized |
| 资源类型 | AzureDefenderPlan |
| 资源组 | security |

## 描述

Ensure That Microsoft Defender for Storage Is Set To 'On'

## 风险

Ensure that Microsoft Defender for Cloud is enabled for your Microsoft Azure storage accounts. Defender for storage accounts is an Azure-native layer of security intelligence that detects unusual and potentially harmful attempts to access or exploit your Azure cloud storage accounts.

## 推荐措施

By default, Microsoft Defender for Cloud is disabled for your storage accounts. Enabling the Defender security service for Azure storage accounts allows for advanced security defense using threat detection capabilities provided by the Microsoft Security Response Center (MSRC). MSRC investigates all reports of security vulnerabilities affecting Microsoft products and services, including Azure cloud services.

## 修复步骤


### Terraform

[https://docs.ST Cloud.com/checks/azure/azure-general-policies/ensure-that-azure-defender-is-set-to-on-for-storage#terraform](https://docs.ST Cloud.com/checks/azure/azure-general-policies/ensure-that-azure-defender-is-set-to-on-for-storage#terraform)

### Other

[https://www.trendmicro.com/cloudoneconformity/knowledge-base/azure/SecurityCenter/defender-storage.html](https://www.trendmicro.com/cloudoneconformity/knowledge-base/azure/SecurityCenter/defender-storage.html)

## 参考资料

No external references available.

## 技术信息

- Source Metadata：[sources/azure/defender_ensure_defender_for_storage_is_on/metadata.json](../../sources/azure/defender_ensure_defender_for_storage_is_on/metadata.json)
- Source Code：[sources/azure/defender_ensure_defender_for_storage_is_on/check.py](../../sources/azure/defender_ensure_defender_for_storage_is_on/check.py)
- Source Metadata Path：`sources/azure/defender_ensure_defender_for_storage_is_on/metadata.json`
- Source Code Path：`sources/azure/defender_ensure_defender_for_storage_is_on/check.py`
