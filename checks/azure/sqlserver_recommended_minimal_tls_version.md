# Ensure SQL server has a recommended minimal TLS version required.

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `sqlserver_recommended_minimal_tls_version` |
| 云平台 | Azure |
| 服务 | sqlserver |
| 严重等级 | medium |
| 类别 | Uncategorized |
| 资源类型 | SQLServer |
| 资源组 | database |

## 描述

Ensure that SQL Server instances are configured with the recommended minimal TLS version to maintain secure connections.

## 风险

Using outdated or weak TLS versions can expose SQL Server instances to vulnerabilities, increasing the risk of data breaches and unauthorized access.

## 推荐措施

1. Go to Azure SQL Server 2. Navigate to 'Security' -> 'Networking' 3. Select 'Connectivity' 4. Update the TLS version in the field 'Minimum TLS version' to a recommended minimal version (e.g., TLS 1.2).

- 推荐链接：[https://learn.microsoft.com/en-us/azure/azure-sql/database/connectivity-settings?view=azuresql&tabs=azure-portal#configure-minimum-tls-version](https://learn.microsoft.com/en-us/azure/azure-sql/database/connectivity-settings?view=azuresql&tabs=azure-portal#configure-minimum-tls-version)

## 修复步骤


### CLI

```text
az sql server update -n sql-server-name -g sql-server-group --set minimalTlsVersion=<version>
```

## 参考资料

- [https://learn.microsoft.com/en-us/azure/azure-sql/database/connectivity-settings?view=azuresql&tabs=azure-portal#configure-minimum-tls-version](https://learn.microsoft.com/en-us/azure/azure-sql/database/connectivity-settings?view=azuresql&tabs=azure-portal#configure-minimum-tls-version)

## 技术信息

- Source Metadata：[sources/azure/sqlserver_recommended_minimal_tls_version/metadata.json](../../sources/azure/sqlserver_recommended_minimal_tls_version/metadata.json)
- Source Code：[sources/azure/sqlserver_recommended_minimal_tls_version/check.py](../../sources/azure/sqlserver_recommended_minimal_tls_version/check.py)
- Source Metadata Path：`sources/azure/sqlserver_recommended_minimal_tls_version/metadata.json`
- Source Code Path：`sources/azure/sqlserver_recommended_minimal_tls_version/check.py`
