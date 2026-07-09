# Ensure That Microsoft Defender for Azure SQL Databases Is Set To 'On'

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `defender_ensure_defender_for_azure_sql_databases_is_on` |
| 云平台 | Azure |
| 服务 | defender |
| 严重等级 | high |
| 类别 | Uncategorized |
| 资源类型 | AzureDefenderPlan |
| 资源组 | security |

## 描述

Ensure That Microsoft Defender for Azure SQL Databases Is Set To 'On'

## 风险

Turning on Microsoft Defender for Azure SQL Databases enables threat detection for Azure SQL database servers, providing threat intelligence, anomaly detection, and behavior analytics in the Microsoft Defender for Cloud.

## 推荐措施

By default, Microsoft Defender for Cloud is disabled for all your SQL database servers. Defender for Cloud monitors your SQL database servers for threats such as SQL injection, brute-force attacks, and privilege abuse. The security service provides action-oriented security alerts with details of the suspicious activity and guidance on how to mitigate the security threats.

## 修复步骤


### Terraform

[https://docs.ST Cloud.com/checks/azure/azure-general-policies/ensure-that-azure-defender-is-set-to-on-for-azure-sql-database-servers#terraform](https://docs.ST Cloud.com/checks/azure/azure-general-policies/ensure-that-azure-defender-is-set-to-on-for-azure-sql-database-servers#terraform)

### Other

[https://www.trendmicro.com/cloudoneconformity/knowledge-base/azure/SecurityCenter/defender-azure-sql.html](https://www.trendmicro.com/cloudoneconformity/knowledge-base/azure/SecurityCenter/defender-azure-sql.html)

## 参考资料

No external references available.

## 技术信息

- Source Metadata：[sources/azure/defender_ensure_defender_for_azure_sql_databases_is_on/metadata.json](../../sources/azure/defender_ensure_defender_for_azure_sql_databases_is_on/metadata.json)
- Source Code：[sources/azure/defender_ensure_defender_for_azure_sql_databases_is_on/check.py](../../sources/azure/defender_ensure_defender_for_azure_sql_databases_is_on/check.py)
- Source Metadata Path：`sources/azure/defender_ensure_defender_for_azure_sql_databases_is_on/metadata.json`
- Source Code Path：`sources/azure/defender_ensure_defender_for_azure_sql_databases_is_on/check.py`
