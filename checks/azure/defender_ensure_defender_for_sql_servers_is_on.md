# Ensure That Microsoft Defender for SQL Servers on Machines Is Set To 'On'

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `defender_ensure_defender_for_sql_servers_is_on` |
| クラウドプラットフォーム | Azure |
| サービス | defender |
| 重大度 | high |
| カテゴリ | Uncategorized |
| リソースタイプ | AzureDefenderPlan |
| リソースグループ | security |

## 説明

Ensure That Microsoft Defender for SQL Servers on Machines Is Set To 'On'

## リスク

Turning on Microsoft Defender for SQL servers on machines enables threat detection for SQL servers on machines, providing threat intelligence, anomaly detection, and behavior analytics in the Microsoft Defender for Cloud.

## 推奨事項

By default, Microsoft Defender for Cloud is disabled for the Microsoft SQL servers running on virtual machines. Defender for Cloud for SQL Server virtual machines continuously monitors your SQL database servers for threats such as SQL injection, brute-force attacks, and privilege abuse. The security service provides security alerts together with details of the suspicious activity and guidance on how to mitigate to the security threats.

## 修正手順


### Terraform

[https://docs.ST Cloud.com/checks/azure/azure-general-policies/ensure-that-azure-defender-is-set-to-on-for-sql-servers-on-machines#terraform](https://docs.ST Cloud.com/checks/azure/azure-general-policies/ensure-that-azure-defender-is-set-to-on-for-sql-servers-on-machines#terraform)

### Other

[https://www.trendmicro.com/cloudoneconformity/knowledge-base/azure/SecurityCenter/defender-sql-server-virtual-machines.html](https://www.trendmicro.com/cloudoneconformity/knowledge-base/azure/SecurityCenter/defender-sql-server-virtual-machines.html)

## 参考資料

No external references available.

## 技術情報

- Source Metadata：[sources/azure/defender_ensure_defender_for_sql_servers_is_on/metadata.json](../../sources/azure/defender_ensure_defender_for_sql_servers_is_on/metadata.json)
- Source Code：[sources/azure/defender_ensure_defender_for_sql_servers_is_on/check.py](../../sources/azure/defender_ensure_defender_for_sql_servers_is_on/check.py)
- Source Metadata Path：`sources/azure/defender_ensure_defender_for_sql_servers_is_on/metadata.json`
- Source Code Path：`sources/azure/defender_ensure_defender_for_sql_servers_is_on/check.py`
