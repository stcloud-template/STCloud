# Ensure the Key Vault is Recoverable

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `keyvault_recoverable` |
| 云平台 | Azure |
| 服务 | keyvault |
| 严重等级 | high |
| 类别 | Uncategorized |
| 资源类型 | KeyVault |
| 资源组 | security |

## 描述

The Key Vault contains object keys, secrets, and certificates. Accidental unavailability of a Key Vault can cause immediate data loss or loss of security functions (authentication, validation, verification, non-repudiation, etc.) supported by the Key Vault objects. It is recommended the Key Vault be made recoverable by enabling the 'Do Not Purge' and 'Soft Delete' functions. This is in order to prevent loss of encrypted data, including storage accounts, SQL databases, and/or dependent services provided by Key Vault objects (Keys, Secrets, Certificates) etc. This may happen in the case of accidental deletion by a user or from disruptive activity by a malicious user. WARNING: A current limitation of the soft-delete feature across all Azure services is role assignments disappearing when Key Vault is deleted. All role assignments will need to be recreated after recovery.

## 风险

There could be scenarios where users accidentally run delete/purge commands on Key Vault or an attacker/malicious user deliberately does so in order to cause disruption. Deleting or purging a Key Vault leads to immediate data loss, as keys encrypting data and secrets/certificates allowing access/services will become non-accessible. There are 2 Key Vault properties that play a role in permanent unavailability of a Key Vault: 1. enableSoftDelete: Setting this parameter to 'true' for a Key Vault ensures that even if Key Vault is deleted, Key Vault itself or its objects remain recoverable for the next 90 days. Key Vault/objects can either be recovered or purged (permanent deletion) during those 90 days. If no action is taken, key vault and its objects will subsequently be purged. 2. enablePurgeProtection: enableSoftDelete only ensures that Key Vault is not deleted permanently and will be recoverable for 90 days from date of deletion. However, there are scenarios in which the Key Vault and/or its objects are accidentally purged and hence will not be recoverable. Setting enablePurgeProtection to 'true' ensures that the Key Vault and its objects cannot be purged. Enabling both the parameters on Key Vaults ensures that Key Vaults and their objects cannot be deleted/purged permanently.

## 推荐措施

To enable 'Do Not Purge' and 'Soft Delete' for a Key Vault: From Azure Portal 1. Go to Key Vaults 2. For each Key Vault 3. Click Properties 4. Ensure the status of soft-delete reads Soft delete has been enabled on this key vault. 5. At the bottom of the page, click 'Enable Purge Protection' Note, once enabled you cannot disable it. From Azure CLI az resource update --id /subscriptions/xxxxxx-xxxx-xxxx-xxxx- xxxxxxxxxxxx/resourceGroups/<resourceGroupName>/providers/Microsoft.KeyVault /vaults/<keyVaultName> --set properties.enablePurgeProtection=true properties.enableSoftDelete=true From PowerShell Update-AzKeyVault -VaultName <vaultName -ResourceGroupName <resourceGroupName -EnablePurgeProtection

- 推荐链接：[https://blogs.technet.microsoft.com/kv/2017/05/10/azure-key-vault-recovery-options/](https://blogs.technet.microsoft.com/kv/2017/05/10/azure-key-vault-recovery-options/)

## 修复步骤


### CLI

```text
az resource update --id /subscriptions/xxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx/resourceGroups/<resourceGroupName>/providers/Microsoft.KeyVault/vaults/<keyVaultName> --set properties.enablePurgeProtection=trueproperties.enableSoftDelete=true
```

### Terraform

[https://docs.ST Cloud.com/checks/azure/azure-general-policies/ensure-the-key-vault-is-recoverable#terraform](https://docs.ST Cloud.com/checks/azure/azure-general-policies/ensure-the-key-vault-is-recoverable#terraform)

### Other

[https://www.trendmicro.com/cloudoneconformity/knowledge-base/azure/KeyVault/enable-key-vault-recoverability.html#](https://www.trendmicro.com/cloudoneconformity/knowledge-base/azure/KeyVault/enable-key-vault-recoverability.html#)

## 参考资料

- [https://docs.microsoft.com/en-us/azure/key-vault/key-vault-soft-delete-cli](https://docs.microsoft.com/en-us/azure/key-vault/key-vault-soft-delete-cli)
- [https://blogs.technet.microsoft.com/kv/2017/05/10/azure-key-vault-recovery-options/](https://blogs.technet.microsoft.com/kv/2017/05/10/azure-key-vault-recovery-options/)

## 技术信息

- Source Metadata：[sources/azure/keyvault_recoverable/metadata.json](../../sources/azure/keyvault_recoverable/metadata.json)
- Source Code：[sources/azure/keyvault_recoverable/check.py](../../sources/azure/keyvault_recoverable/check.py)
- Source Metadata Path：`sources/azure/keyvault_recoverable/metadata.json`
- Source Code Path：`sources/azure/keyvault_recoverable/check.py`
