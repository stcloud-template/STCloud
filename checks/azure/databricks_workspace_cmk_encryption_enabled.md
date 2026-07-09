# Ensure Azure Databricks workspaces use customer-managed keys (CMK) for encryption at rest

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `databricks_workspace_cmk_encryption_enabled` |
| 云平台 | Azure |
| 服务 | databricks |
| 子服务 | workspace |
| 严重等级 | high |
| 类别 | Uncategorized |
| 资源类型 | AzureDatabricksWorkspace |
| 资源组 | ai_ml |

## 描述

Checks whether Azure Databricks workspaces are configured to use customer-managed keys (CMK) for encryption at rest, providing greater control over data encryption and compliance.

## 风险

Without CMK, organizations have less control over encryption keys, which may impact regulatory compliance and increase risk of unauthorized data access.

## 推荐措施

Enable customer-managed keys (CMK) for Databricks workspaces using Azure Key Vault to enhance control over data encryption, auditing, and compliance.

- 推荐链接：[https://www.trendmicro.com/cloudoneconformity/knowledge-base/azure/Databricks/enable-encryption-with-cmk.html](https://www.trendmicro.com/cloudoneconformity/knowledge-base/azure/Databricks/enable-encryption-with-cmk.html)

## 修复步骤


### CLI

```text
az databricks workspace update --name <databricks-workspace-name> --resource-group <resource-group-name> --prepare-encryption && databricks workspace update --name <databricks-workspace-name> --resource-group <resource-group-name> --key-source 'Microsoft.KeyVault' --key-name <key-name> --key-vault <key-vault-uri> --key-version <key-version>
```

## 参考资料

- [https://learn.microsoft.com/en-us/azure/databricks/security/keys/customer-managed-keys](https://learn.microsoft.com/en-us/azure/databricks/security/keys/customer-managed-keys)
- [https://www.trendmicro.com/cloudoneconformity/knowledge-base/azure/Databricks/enable-encryption-with-cmk.html](https://www.trendmicro.com/cloudoneconformity/knowledge-base/azure/Databricks/enable-encryption-with-cmk.html)

## 技术信息

- Source Metadata：[sources/azure/databricks_workspace_cmk_encryption_enabled/metadata.json](../../sources/azure/databricks_workspace_cmk_encryption_enabled/metadata.json)
- Source Code：[sources/azure/databricks_workspace_cmk_encryption_enabled/check.py](../../sources/azure/databricks_workspace_cmk_encryption_enabled/check.py)
- Source Metadata Path：`sources/azure/databricks_workspace_cmk_encryption_enabled/metadata.json`
- Source Code Path：`sources/azure/databricks_workspace_cmk_encryption_enabled/check.py`
