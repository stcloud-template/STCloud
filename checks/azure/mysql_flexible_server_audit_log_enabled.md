# Ensure server parameter 'audit_log_enabled' is set to 'ON' for MySQL Database Server

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `mysql_flexible_server_audit_log_enabled` |
| クラウドプラットフォーム | Azure |
| サービス | mysql |
| 重大度 | medium |
| カテゴリ | Uncategorized |
| リソースタイプ | Microsoft.DBforMySQL/flexibleServers |
| リソースグループ | database |

## 説明

Enable audit_log_enabled on MySQL Servers.

## リスク

Enabling audit_log_enabled helps MySQL Database to log items such as connection attempts to the server, DDL/DML access, and more. Log data can be used to identify, troubleshoot, and repair configuration errors and suboptimal performance.

## 推奨事項

1. Login to Azure Portal using https://portal.azure.com. 2. Select Azure Database for MySQL Servers. 3. Select a database. 4. Under Settings, select Server parameters. 5. Update audit_log_enabled parameter to ON 6. Under Monitoring, select Diagnostic settings. 7. Select + Add diagnostic setting. 8. Provide a diagnostic setting name. 9. Under Categories, select MySQL Audit Logs. 10. Specify destination details. 11. Click Save.

- 推奨リンク：[https://docs.microsoft.com/en-us/security/benchmark/azure/security-controls-v3-logging-threat-detection#lt-3-enable-logging-for-security-investigation](https://docs.microsoft.com/en-us/security/benchmark/azure/security-controls-v3-logging-threat-detection#lt-3-enable-logging-for-security-investigation)

## 修正手順


### Other

[https://www.tenable.com/audits/items/CIS_Microsoft_Azure_Foundations_v1.5.0_L2.audit:c073639a1ce546b535ba73afbf6542aa](https://www.tenable.com/audits/items/CIS_Microsoft_Azure_Foundations_v1.5.0_L2.audit:c073639a1ce546b535ba73afbf6542aa)

## 参考資料

- [https://docs.microsoft.com/en-us/azure/mysql/single-server/how-to-configure-audit-logs-portal](https://docs.microsoft.com/en-us/azure/mysql/single-server/how-to-configure-audit-logs-portal)
- [https://docs.microsoft.com/en-us/security/benchmark/azure/security-controls-v3-logging-threat-detection#lt-3-enable-logging-for-security-investigation](https://docs.microsoft.com/en-us/security/benchmark/azure/security-controls-v3-logging-threat-detection#lt-3-enable-logging-for-security-investigation)

## 技術情報

- Source Metadata：[sources/azure/mysql_flexible_server_audit_log_enabled/metadata.json](../../sources/azure/mysql_flexible_server_audit_log_enabled/metadata.json)
- Source Code：[sources/azure/mysql_flexible_server_audit_log_enabled/check.py](../../sources/azure/mysql_flexible_server_audit_log_enabled/check.py)
- Source Metadata Path：`sources/azure/mysql_flexible_server_audit_log_enabled/metadata.json`
- Source Code Path：`sources/azure/mysql_flexible_server_audit_log_enabled/check.py`
