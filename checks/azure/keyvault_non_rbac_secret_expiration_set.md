# Ensure that the Expiration Date is set for all Secrets in Non-RBAC Key Vaults

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `keyvault_non_rbac_secret_expiration_set` |
| クラウドプラットフォーム | Azure |
| サービス | keyvault |
| 重大度 | high |
| カテゴリ | Uncategorized |
| リソースタイプ | KeyVault |
| リソースグループ | security |

## 説明

Ensure that all Secrets in Non Role Based Access Control (RBAC) Azure Key Vaults have an expiration date set.

## リスク

The Azure Key Vault enables users to store and keep secrets within the Microsoft Azure environment. Secrets in the Azure Key Vault are octet sequences with a maximum size of 25k bytes each. The exp (expiration date) attribute identifies the expiration date on or after which the secret MUST NOT be used. By default, secrets never expire. It is thus recommended to rotate secrets in the key vault and set an explicit expiration date for all secrets. This ensures that the secrets cannot be used beyond their assigned lifetimes.

## 推奨事項

From Azure Portal: 1. Go to Key vaults. 2. For each Key vault, click on Secrets. 3. In the main pane, ensure that the status of the secret is Enabled. 4. Set an appropriate Expiration date on all secrets. From Azure CLI: Update the Expiration date for the secret using the below command: az keyvault secret set-attributes --name <secretName> --vault-name <vaultName> --expires Y-m-d'T'H:M:S'Z' Note: To view the expiration date on all secrets in a Key Vault using Microsoft API, the List Key permission is required. To update the expiration date for the secrets: 1. Go to Key vault, click on Access policies. 2. Click on Create and add an access policy with the Update permission (in the Secret Permissions - Secret Management Operations section). From PowerShell: For each Key vault with the EnableRbacAuthorization setting set to False or empty, run the following command. Set-AzKeyVaultSecret -VaultName <Vault Name> -Name <Secret Name> -Expires <DateTime>

- 推奨リンク：[https://docs.microsoft.com/en-us/rest/api/keyvault/about-keys--secrets-and-certificates#key-vault-secrets](https://docs.microsoft.com/en-us/rest/api/keyvault/about-keys--secrets-and-certificates#key-vault-secrets)

## 修正手順


### CLI

```text
az keyvault secret set-attributes --name <secretName> --vault-name <vaultName> --expires Y-m-d'T'H:M:S'Z'
```

### Terraform

[https://docs.ST Cloud.com/checks/azure/azure-secrets-policies/set-an-expiration-date-on-all-secrets#terraform](https://docs.ST Cloud.com/checks/azure/azure-secrets-policies/set-an-expiration-date-on-all-secrets#terraform)

## 参考資料

- [https://docs.microsoft.com/en-us/azure/key-vault/key-vault-whatis](https://docs.microsoft.com/en-us/azure/key-vault/key-vault-whatis)
- [https://docs.microsoft.com/en-us/rest/api/keyvault/about-keys--secrets-and-certificates#key-vault-secrets](https://docs.microsoft.com/en-us/rest/api/keyvault/about-keys--secrets-and-certificates#key-vault-secrets)

## 技術情報

- Source Metadata：[sources/azure/keyvault_non_rbac_secret_expiration_set/metadata.json](../../sources/azure/keyvault_non_rbac_secret_expiration_set/metadata.json)
- Source Code：[sources/azure/keyvault_non_rbac_secret_expiration_set/check.py](../../sources/azure/keyvault_non_rbac_secret_expiration_set/check.py)
- Source Metadata Path：`sources/azure/keyvault_non_rbac_secret_expiration_set/metadata.json`
- Source Code Path：`sources/azure/keyvault_non_rbac_secret_expiration_set/check.py`
