# Ensure that Microsoft Defender for SQL is set to 'On' for critical SQL Servers

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `sqlserver_microsoft_defender_enabled` |
| 云平台 | Azure |
| 服务 | sqlserver |
| 严重等级 | medium |
| 类别 | Uncategorized |
| 资源类型 | SQLServer |
| 资源组 | database |

## 描述

Ensure that Microsoft Defender for SQL is set to 'On' for critical SQL Servers

## 风险

Microsoft Defender for SQL is a unified package for advanced SQL security capabilities. Microsoft Defender is available for Azure SQL Database, Azure SQL Managed classifying sensitive data, surfacing and mitigating potential database vulnerabilities, and detecting anomalous activities that could indicate a threat to your database. It provides a single go-to location for enabling and managing these capabilities.

## 推荐措施

1. Go to SQL servers For each production SQL server instance: 2. Click Microsoft Defender for Cloud 3. Click Enable Microsoft Defender for SQL

- 推荐链接：[https://learn.microsoft.com/en-us/azure/defender-for-cloud/defender-for-sql-usage](https://learn.microsoft.com/en-us/azure/defender-for-cloud/defender-for-sql-usage)

## 修复步骤


### Other

[https://www.trendmicro.com/cloudoneconformity-staging/knowledge-base/azure/SecurityCenter/defender-azure-sql.html](https://www.trendmicro.com/cloudoneconformity-staging/knowledge-base/azure/SecurityCenter/defender-azure-sql.html)

## 参考资料

- [https://docs.microsoft.com/en-us/azure/azure-sql/database/azure-defender-for-sql?view=azuresql](https://docs.microsoft.com/en-us/azure/azure-sql/database/azure-defender-for-sql?view=azuresql)
- [https://learn.microsoft.com/en-us/azure/defender-for-cloud/defender-for-sql-usage](https://learn.microsoft.com/en-us/azure/defender-for-cloud/defender-for-sql-usage)

## 技术信息

- Source Metadata：[sources/azure/sqlserver_microsoft_defender_enabled/metadata.json](../../sources/azure/sqlserver_microsoft_defender_enabled/metadata.json)
- Source Code：[sources/azure/sqlserver_microsoft_defender_enabled/check.py](../../sources/azure/sqlserver_microsoft_defender_enabled/check.py)
- Source Metadata Path：`sources/azure/sqlserver_microsoft_defender_enabled/metadata.json`
- Source Code Path：`sources/azure/sqlserver_microsoft_defender_enabled/check.py`
