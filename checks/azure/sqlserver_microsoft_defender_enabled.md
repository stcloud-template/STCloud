# Ensure that Microsoft Defender for SQL is set to 'On' for critical SQL Servers

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `sqlserver_microsoft_defender_enabled` |
| クラウドプラットフォーム | Azure |
| サービス | sqlserver |
| 重大度 | medium |
| カテゴリ | Uncategorized |
| リソースタイプ | SQLServer |
| リソースグループ | database |

## 説明

Ensure that Microsoft Defender for SQL is set to 'On' for critical SQL Servers

## リスク

Microsoft Defender for SQL is a unified package for advanced SQL security capabilities. Microsoft Defender is available for Azure SQL Database, Azure SQL Managed classifying sensitive data, surfacing and mitigating potential database vulnerabilities, and detecting anomalous activities that could indicate a threat to your database. It provides a single go-to location for enabling and managing these capabilities.

## 推奨事項

1. Go to SQL servers For each production SQL server instance: 2. Click Microsoft Defender for Cloud 3. Click Enable Microsoft Defender for SQL

- 推奨リンク：[https://learn.microsoft.com/en-us/azure/defender-for-cloud/defender-for-sql-usage](https://learn.microsoft.com/en-us/azure/defender-for-cloud/defender-for-sql-usage)

## 修正手順


### Other

[https://www.trendmicro.com/cloudoneconformity-staging/knowledge-base/azure/SecurityCenter/defender-azure-sql.html](https://www.trendmicro.com/cloudoneconformity-staging/knowledge-base/azure/SecurityCenter/defender-azure-sql.html)

## 参考資料

- [https://docs.microsoft.com/en-us/azure/azure-sql/database/azure-defender-for-sql?view=azuresql](https://docs.microsoft.com/en-us/azure/azure-sql/database/azure-defender-for-sql?view=azuresql)
- [https://learn.microsoft.com/en-us/azure/defender-for-cloud/defender-for-sql-usage](https://learn.microsoft.com/en-us/azure/defender-for-cloud/defender-for-sql-usage)

## 技術情報

- Source Metadata：[sources/azure/sqlserver_microsoft_defender_enabled/metadata.json](../../sources/azure/sqlserver_microsoft_defender_enabled/metadata.json)
- Source Code：[sources/azure/sqlserver_microsoft_defender_enabled/check.py](../../sources/azure/sqlserver_microsoft_defender_enabled/check.py)
- Source Metadata Path：`sources/azure/sqlserver_microsoft_defender_enabled/metadata.json`
- Source Code Path：`sources/azure/sqlserver_microsoft_defender_enabled/check.py`
