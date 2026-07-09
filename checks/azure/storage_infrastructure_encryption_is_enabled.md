# Ensure that 'Enable Infrastructure Encryption' for Each Storage Account in Azure Storage is Set to 'enabled'

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `storage_infrastructure_encryption_is_enabled` |
| 云平台 | Azure |
| 服务 | storage |
| 严重等级 | low |
| 类别 | encryption |
| 资源类型 | AzureRole |
| 资源组 | IAM |

## 描述

Ensure that 'Enable Infrastructure Encryption' for Each Storage Account in Azure Storage is Set to 'enabled'

## 风险

Double encryption of Azure Storage data protects against a scenario where one of the encryption algorithms or keys may be compromised

## 推荐措施

Enabling double encryption at the hardware level on top of the default software encryption for Storage Accounts accessing Azure storage solutions.

## 修复步骤

No remediation steps available.

## 参考资料

No external references available.

## 技术信息

- Source Metadata：[sources/azure/storage_infrastructure_encryption_is_enabled/metadata.json](../../sources/azure/storage_infrastructure_encryption_is_enabled/metadata.json)
- Source Code：[sources/azure/storage_infrastructure_encryption_is_enabled/check.py](../../sources/azure/storage_infrastructure_encryption_is_enabled/check.py)
- Source Metadata Path：`sources/azure/storage_infrastructure_encryption_is_enabled/metadata.json`
- Source Code Path：`sources/azure/storage_infrastructure_encryption_is_enabled/check.py`
