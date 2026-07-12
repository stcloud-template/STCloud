# Ensure SQL server's Transparent Data Encryption (TDE) protector is encrypted

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `sqlserver_tde_encryption_enabled` |
| クラウドプラットフォーム | Azure |
| サービス | sqlserver |
| 重大度 | medium |
| カテゴリ | Uncategorized |
| リソースタイプ | SQLServer |
| リソースグループ | database |

## 説明

Enable Transparent Data Encryption on every SQL server.

## リスク

Azure SQL Database transparent data encryption helps protect against the threat of malicious activity by performing real-time encryption and decryption of the database, associated backups, and transaction log files at rest without requiring changes to the application.

## 推奨事項

1. Go to SQL databases 2. For each DB instance 3. Click on Transparent data encryption 4. Set Data encryption to On

- 推奨リンク：[https://learn.microsoft.com/en-us/azure/azure-sql/database/transparent-data-encryption-byok-overview?view=azuresql](https://learn.microsoft.com/en-us/azure/azure-sql/database/transparent-data-encryption-byok-overview?view=azuresql)

## 修正手順


### CLI

```text
az sql db tde set --resource-group resourceGroup --server dbServerName --database dbName --status Enabled
```

### Other

[https://www.trendmicro.com/cloudoneconformity-staging/knowledge-base/azure/Sql/data-encryption.html#](https://www.trendmicro.com/cloudoneconformity-staging/knowledge-base/azure/Sql/data-encryption.html#)

## 参考資料

- [https://docs.microsoft.com/en-us/sql/relational-databases/security/encryption/transparent-data-encryption-with-azure-sql-database](https://docs.microsoft.com/en-us/sql/relational-databases/security/encryption/transparent-data-encryption-with-azure-sql-database)
- [https://learn.microsoft.com/en-us/azure/azure-sql/database/transparent-data-encryption-byok-overview?view=azuresql](https://learn.microsoft.com/en-us/azure/azure-sql/database/transparent-data-encryption-byok-overview?view=azuresql)

## 技術情報

- Source Metadata：[sources/azure/sqlserver_tde_encryption_enabled/metadata.json](../../sources/azure/sqlserver_tde_encryption_enabled/metadata.json)
- Source Code：[sources/azure/sqlserver_tde_encryption_enabled/check.py](../../sources/azure/sqlserver_tde_encryption_enabled/check.py)
- Source Metadata Path：`sources/azure/sqlserver_tde_encryption_enabled/metadata.json`
- Source Code Path：`sources/azure/sqlserver_tde_encryption_enabled/check.py`
