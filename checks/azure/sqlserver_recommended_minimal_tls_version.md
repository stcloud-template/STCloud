# Ensure SQL server has a recommended minimal TLS version required.

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `sqlserver_recommended_minimal_tls_version` |
| クラウドプラットフォーム | Azure |
| サービス | sqlserver |
| 重大度 | medium |
| カテゴリ | Uncategorized |
| リソースタイプ | SQLServer |
| リソースグループ | database |

## 説明

Ensure that SQL Server instances are configured with the recommended minimal TLS version to maintain secure connections.

## リスク

Using outdated or weak TLS versions can expose SQL Server instances to vulnerabilities, increasing the risk of data breaches and unauthorized access.

## 推奨事項

1. Go to Azure SQL Server 2. Navigate to 'Security' -> 'Networking' 3. Select 'Connectivity' 4. Update the TLS version in the field 'Minimum TLS version' to a recommended minimal version (e.g., TLS 1.2).

- 推奨リンク：[https://learn.microsoft.com/en-us/azure/azure-sql/database/connectivity-settings?view=azuresql&tabs=azure-portal#configure-minimum-tls-version](https://learn.microsoft.com/en-us/azure/azure-sql/database/connectivity-settings?view=azuresql&tabs=azure-portal#configure-minimum-tls-version)

## 修正手順


### CLI

```text
az sql server update -n sql-server-name -g sql-server-group --set minimalTlsVersion=<version>
```

## 参考資料

- [https://learn.microsoft.com/en-us/azure/azure-sql/database/connectivity-settings?view=azuresql&tabs=azure-portal#configure-minimum-tls-version](https://learn.microsoft.com/en-us/azure/azure-sql/database/connectivity-settings?view=azuresql&tabs=azure-portal#configure-minimum-tls-version)

## 技術情報

- Source Metadata：[sources/azure/sqlserver_recommended_minimal_tls_version/metadata.json](../../sources/azure/sqlserver_recommended_minimal_tls_version/metadata.json)
- Source Code：[sources/azure/sqlserver_recommended_minimal_tls_version/check.py](../../sources/azure/sqlserver_recommended_minimal_tls_version/check.py)
- Source Metadata Path：`sources/azure/sqlserver_recommended_minimal_tls_version/metadata.json`
- Source Code Path：`sources/azure/sqlserver_recommended_minimal_tls_version/check.py`
