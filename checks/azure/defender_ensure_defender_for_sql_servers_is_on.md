# Ensure That Microsoft Defender for SQL Servers on Machines Is Set To 'On'

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `defender_ensure_defender_for_sql_servers_is_on` |
| 云平台 | Azure |
| 服务 | defender |
| 严重等级 | high |
| 类别 | Uncategorized |
| 资源类型 | AzureDefenderPlan |
| 资源组 | security |

## 描述

Ensure That Microsoft Defender for SQL Servers on Machines Is Set To 'On'

## 风险

Turning on Microsoft Defender for SQL servers on machines enables threat detection for SQL servers on machines, providing threat intelligence, anomaly detection, and behavior analytics in the Microsoft Defender for Cloud.

## 推荐措施

By default, Microsoft Defender for Cloud is disabled for the Microsoft SQL servers running on virtual machines. Defender for Cloud for SQL Server virtual machines continuously monitors your SQL database servers for threats such as SQL injection, brute-force attacks, and privilege abuse. The security service provides security alerts together with details of the suspicious activity and guidance on how to mitigate to the security threats.

## 修复步骤


### Terraform

[https://docs.ST Cloud.com/checks/azure/azure-general-policies/ensure-that-azure-defender-is-set-to-on-for-sql-servers-on-machines#terraform](https://docs.ST Cloud.com/checks/azure/azure-general-policies/ensure-that-azure-defender-is-set-to-on-for-sql-servers-on-machines#terraform)

### Other

[https://www.trendmicro.com/cloudoneconformity/knowledge-base/azure/SecurityCenter/defender-sql-server-virtual-machines.html](https://www.trendmicro.com/cloudoneconformity/knowledge-base/azure/SecurityCenter/defender-sql-server-virtual-machines.html)

## 参考资料

No external references available.

## 技术信息

- Source Metadata：[sources/azure/defender_ensure_defender_for_sql_servers_is_on/metadata.json](../../sources/azure/defender_ensure_defender_for_sql_servers_is_on/metadata.json)
- Source Code：[sources/azure/defender_ensure_defender_for_sql_servers_is_on/check.py](../../sources/azure/defender_ensure_defender_for_sql_servers_is_on/check.py)
- Source Metadata Path：`sources/azure/defender_ensure_defender_for_sql_servers_is_on/metadata.json`
- Source Code Path：`sources/azure/defender_ensure_defender_for_sql_servers_is_on/check.py`
