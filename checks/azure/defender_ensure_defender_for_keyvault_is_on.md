# Ensure That Microsoft Defender for KeyVault Is Set To 'On'

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `defender_ensure_defender_for_keyvault_is_on` |
| 云平台 | Azure |
| 服务 | defender |
| 严重等级 | high |
| 类别 | Uncategorized |
| 资源类型 | AzureDefenderPlan |
| 资源组 | security |

## 描述

Ensure That Microsoft Defender for KeyVault Is Set To 'On'

## 风险

By default, Microsoft Defender for Cloud is disabled for Azure key vaults. Defender for Cloud detects unusual and potentially harmful attempts to access or exploit your Azure Key Vault data. This layer of protection allows you to address threats without being a security expert, and without the need to use and manage third-party security monitoring tools or services.

## 推荐措施

Ensure that Microsoft Defender for Cloud is enabled for Azure key vaults. Key Vault is the Azure cloud service that safeguards encryption keys and secrets like certificates, connection-based strings, and passwords.

## 修复步骤


### Terraform

[https://docs.ST Cloud.com/checks/azure/azure-general-policies/ensure-that-azure-defender-is-set-to-on-for-key-vault#terraform](https://docs.ST Cloud.com/checks/azure/azure-general-policies/ensure-that-azure-defender-is-set-to-on-for-key-vault#terraform)

### Other

[https://www.trendmicro.com/cloudoneconformity/knowledge-base/azure/SecurityCenter/defender-key-vault.html](https://www.trendmicro.com/cloudoneconformity/knowledge-base/azure/SecurityCenter/defender-key-vault.html)

## 参考资料

No external references available.

## 技术信息

- Source Metadata：[sources/azure/defender_ensure_defender_for_keyvault_is_on/metadata.json](../../sources/azure/defender_ensure_defender_for_keyvault_is_on/metadata.json)
- Source Code：[sources/azure/defender_ensure_defender_for_keyvault_is_on/check.py](../../sources/azure/defender_ensure_defender_for_keyvault_is_on/check.py)
- Source Metadata Path：`sources/azure/defender_ensure_defender_for_keyvault_is_on/metadata.json`
- Source Code Path：`sources/azure/defender_ensure_defender_for_keyvault_is_on/check.py`
