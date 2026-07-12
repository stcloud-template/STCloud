# Ensure SQL server's Transparent Data Encryption (TDE) protector is encrypted with Customer-managed key

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `sqlserver_tde_encrypted_with_cmk` |
| クラウドプラットフォーム | Azure |
| サービス | sqlserver |
| 重大度 | medium |
| カテゴリ | Uncategorized |
| リソースタイプ | SQLServer |
| リソースグループ | database |

## 説明

Transparent Data Encryption (TDE) with Customer-managed key support provides increased transparency and control over the TDE Protector, increased security with an HSM-backed external service, and promotion of separation of duties.

## リスク

Customer-managed key support for Transparent Data Encryption (TDE) allows user control of TDE encryption keys and restricts who can access them and when. Azure Key Vault, Azure cloud-based external key management system, is the first key management service where TDE has integrated support for Customer-managed keys. With Customer-managed key support, the database encryption key is protected by an asymmetric key stored in the Key Vault. The asymmetric key is set at the server level and inherited by all databases under that server

## 推奨事項

1. Go to SQL servers For the desired server instance 2. Click On Transparent data encryption 3. Set Transparent data encryption to Customer-managed key 4. Browse through your key vaults to Select an existing key or create a new key in the Azure Key Vault. 5. Check Make selected key the default TDE protector

- 推奨リンク：[https://learn.microsoft.com/en-us/azure/azure-sql/database/transparent-data-encryption-byok-overview?view=azuresql](https://learn.microsoft.com/en-us/azure/azure-sql/database/transparent-data-encryption-byok-overview?view=azuresql)

## 修正手順


### CLI

```text
az sql server tde-key set --resource-group resourceName --server dbServerName --server-key-type {AzureKeyVault} --kid keyIdentifier
```

### Other

[https://www.trendmicro.com/cloudoneconformity-staging/knowledge-base/azure/Sql/use-byok-for-transparent-data-encryption.html#](https://www.trendmicro.com/cloudoneconformity-staging/knowledge-base/azure/Sql/use-byok-for-transparent-data-encryption.html#)

## 参考資料

- [https://docs.microsoft.com/en-us/sql/relational-databases/security/encryption/transparent-data-encryption-byok-azure-sql](https://docs.microsoft.com/en-us/sql/relational-databases/security/encryption/transparent-data-encryption-byok-azure-sql)
- [https://learn.microsoft.com/en-us/azure/azure-sql/database/transparent-data-encryption-byok-overview?view=azuresql](https://learn.microsoft.com/en-us/azure/azure-sql/database/transparent-data-encryption-byok-overview?view=azuresql)

## 技術情報

- Source Metadata：[sources/azure/sqlserver_tde_encrypted_with_cmk/metadata.json](../../sources/azure/sqlserver_tde_encrypted_with_cmk/metadata.json)
- Source Code：[sources/azure/sqlserver_tde_encrypted_with_cmk/check.py](../../sources/azure/sqlserver_tde_encrypted_with_cmk/check.py)
- Source Metadata Path：`sources/azure/sqlserver_tde_encrypted_with_cmk/metadata.json`
- Source Code Path：`sources/azure/sqlserver_tde_encrypted_with_cmk/check.py`
