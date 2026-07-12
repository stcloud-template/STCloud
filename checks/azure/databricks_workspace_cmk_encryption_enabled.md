# Ensure Azure Databricks workspaces use customer-managed keys (CMK) for encryption at rest

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `databricks_workspace_cmk_encryption_enabled` |
| クラウドプラットフォーム | Azure |
| サービス | databricks |
| サブサービス | workspace |
| 重大度 | high |
| カテゴリ | Uncategorized |
| リソースタイプ | AzureDatabricksWorkspace |
| リソースグループ | ai_ml |

## 説明

Checks whether Azure Databricks workspaces are configured to use customer-managed keys (CMK) for encryption at rest, providing greater control over data encryption and compliance.

## リスク

Without CMK, organizations have less control over encryption keys, which may impact regulatory compliance and increase risk of unauthorized data access.

## 推奨事項

Enable customer-managed keys (CMK) for Databricks workspaces using Azure Key Vault to enhance control over data encryption, auditing, and compliance.

- 推奨リンク：[https://www.trendmicro.com/cloudoneconformity/knowledge-base/azure/Databricks/enable-encryption-with-cmk.html](https://www.trendmicro.com/cloudoneconformity/knowledge-base/azure/Databricks/enable-encryption-with-cmk.html)

## 修正手順


### CLI

```text
az databricks workspace update --name <databricks-workspace-name> --resource-group <resource-group-name> --prepare-encryption && databricks workspace update --name <databricks-workspace-name> --resource-group <resource-group-name> --key-source 'Microsoft.KeyVault' --key-name <key-name> --key-vault <key-vault-uri> --key-version <key-version>
```

## 参考資料

- [https://learn.microsoft.com/en-us/azure/databricks/security/keys/customer-managed-keys](https://learn.microsoft.com/en-us/azure/databricks/security/keys/customer-managed-keys)
- [https://www.trendmicro.com/cloudoneconformity/knowledge-base/azure/Databricks/enable-encryption-with-cmk.html](https://www.trendmicro.com/cloudoneconformity/knowledge-base/azure/Databricks/enable-encryption-with-cmk.html)

## 技術情報

- Source Metadata：[sources/azure/databricks_workspace_cmk_encryption_enabled/metadata.json](../../sources/azure/databricks_workspace_cmk_encryption_enabled/metadata.json)
- Source Code：[sources/azure/databricks_workspace_cmk_encryption_enabled/check.py](../../sources/azure/databricks_workspace_cmk_encryption_enabled/check.py)
- Source Metadata Path：`sources/azure/databricks_workspace_cmk_encryption_enabled/metadata.json`
- Source Code Path：`sources/azure/databricks_workspace_cmk_encryption_enabled/check.py`
