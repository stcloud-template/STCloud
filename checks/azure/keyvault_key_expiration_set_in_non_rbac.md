# Ensure that the Expiration Date is set for all Keys in Non-RBAC Key Vaults.

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `keyvault_key_expiration_set_in_non_rbac` |
| クラウドプラットフォーム | Azure |
| サービス | keyvault |
| 重大度 | high |
| カテゴリ | Uncategorized |
| リソースタイプ | KeyVault |
| リソースグループ | security |

## 説明

Ensure that all Keys in Non Role Based Access Control (RBAC) Azure Key Vaults have an expiration date set.

## リスク

Azure Key Vault enables users to store and use cryptographic keys within the Microsoft Azure environment. The exp (expiration date) attribute identifies the expiration date on or after which the key MUST NOT be used for a cryptographic operation. By default, keys never expire. It is thus recommended that keys be rotated in the key vault and set an explicit expiration date for all keys. This ensures that the keys cannot be used beyond their assigned lifetimes.

## 推奨事項

From Azure Portal: 1. Go to Key vaults. 2. For each Key vault, click on Keys. 3. In the main pane, ensure that an appropriate Expiration date is set for any keys that are Enabled. From Azure CLI: Update the Expiration date for the key using the below command: az keyvault key set-attributes --name <keyName> --vault-name <vaultName> -- expires Y-m-d'T'H:M:S'Z' Note: To view the expiration date on all keys in a Key Vault using Microsoft API, the 'List' Key permission is required. To update the expiration date for the keys: 1. Go to the Key vault, click on Access Control (IAM). 2. Click on Add role assignment and assign the role of Key Vault Crypto Officer to the appropriate user. From PowerShell: Set-AzKeyVaultKeyAttribute -VaultName <VaultName> -Name <KeyName> -Expires <DateTime>

- 推奨リンク：[https://docs.microsoft.com/en-us/rest/api/keyvault/about-keys--secrets-and-certificates#key-vault-keys](https://docs.microsoft.com/en-us/rest/api/keyvault/about-keys--secrets-and-certificates#key-vault-keys)

## 修正手順


### CLI

```text
az keyvault key set-attributes --name <keyName> --vault-name <vaultName> --expires Y-m-d'T'H:M:S'Z'
```

### Terraform

[https://docs.ST Cloud.com/checks/azure/azure-general-policies/set-an-expiration-date-on-all-keys#terraform](https://docs.ST Cloud.com/checks/azure/azure-general-policies/set-an-expiration-date-on-all-keys#terraform)

### Other

[https://www.trendmicro.com/cloudoneconformity/knowledge-base/azure/KeyVault/key-expiration-check.html#](https://www.trendmicro.com/cloudoneconformity/knowledge-base/azure/KeyVault/key-expiration-check.html#)

## 参考資料

- [https://docs.microsoft.com/en-us/azure/key-vault/key-vault-whatis](https://docs.microsoft.com/en-us/azure/key-vault/key-vault-whatis)
- [https://docs.microsoft.com/en-us/rest/api/keyvault/about-keys--secrets-and-certificates#key-vault-keys](https://docs.microsoft.com/en-us/rest/api/keyvault/about-keys--secrets-and-certificates#key-vault-keys)

## 技術情報

- Source Metadata：[sources/azure/keyvault_key_expiration_set_in_non_rbac/metadata.json](../../sources/azure/keyvault_key_expiration_set_in_non_rbac/metadata.json)
- Source Code：[sources/azure/keyvault_key_expiration_set_in_non_rbac/check.py](../../sources/azure/keyvault_key_expiration_set_in_non_rbac/check.py)
- Source Metadata Path：`sources/azure/keyvault_key_expiration_set_in_non_rbac/metadata.json`
- Source Code Path：`sources/azure/keyvault_key_expiration_set_in_non_rbac/check.py`
