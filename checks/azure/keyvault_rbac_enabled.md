# Enable Role Based Access Control for Azure Key Vault

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `keyvault_rbac_enabled` |
| クラウドプラットフォーム | Azure |
| サービス | keyvault |
| 重大度 | high |
| カテゴリ | Uncategorized |
| リソースタイプ | KeyVault |
| リソースグループ | security |

## 説明

WARNING: Role assignments disappear when a Key Vault has been deleted (soft-delete) and recovered. Afterwards it will be required to recreate all role assignments. This is a limitation of the soft-delete feature across all Azure services.

## リスク

The new RBAC permissions model for Key Vaults enables a much finer grained access control for key vault secrets, keys, certificates, etc., than the vault access policy. This in turn will permit the use of privileged identity management over these roles, thus securing the key vaults with JIT Access management.

## 推奨事項

From Azure Portal Key Vaults can be configured to use Azure role-based access control on creation. For existing Key Vaults: 1. From Azure Home open the Portal Menu in the top left corner 2. Select Key Vaults 3. Select a Key Vault to audit 4. Select Access configuration 5. Set the Permission model radio button to Azure role-based access control, taking note of the warning message 6. Click Save 7. Select Access Control (IAM) 8. Select the Role Assignments tab 9. Reapply permissions as needed to groups or users

- 推奨リンク：[https://docs.microsoft.com/en-gb/azure/role-based-access-control/role-assignments-portal?tabs=current](https://docs.microsoft.com/en-gb/azure/role-based-access-control/role-assignments-portal?tabs=current)

## 修正手順

No remediation steps available.

## 参考資料

- [https://docs.microsoft.com/en-gb/azure/key-vault/general/rbac-migration#vault-access-policy-to-azure-rbac-migration-steps](https://docs.microsoft.com/en-gb/azure/key-vault/general/rbac-migration#vault-access-policy-to-azure-rbac-migration-steps)
- [https://docs.microsoft.com/en-gb/azure/role-based-access-control/role-assignments-portal?tabs=current](https://docs.microsoft.com/en-gb/azure/role-based-access-control/role-assignments-portal?tabs=current)

## 技術情報

- Source Metadata：[sources/azure/keyvault_rbac_enabled/metadata.json](../../sources/azure/keyvault_rbac_enabled/metadata.json)
- Source Code：[sources/azure/keyvault_rbac_enabled/check.py](../../sources/azure/keyvault_rbac_enabled/check.py)
- Source Metadata Path：`sources/azure/keyvault_rbac_enabled/metadata.json`
- Source Code Path：`sources/azure/keyvault_rbac_enabled/check.py`
