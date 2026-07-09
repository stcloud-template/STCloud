# Ensure no Azure SQL Databases allow ingress from 0.0.0.0/0 (ANY IP)

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `sqlserver_unrestricted_inbound_access` |
| 云平台 | Azure |
| 服务 | sqlserver |
| 严重等级 | critical |
| 类别 | Uncategorized |
| 资源类型 | SQLServer |
| 资源组 | database |

## 描述

Ensure that there are no firewall rules allowing traffic from 0.0.0.0-255.255.255.255

## 风险

Azure SQL servers provide a firewall that, by default, blocks all Internet connections. When the rule (0.0.0.0-255.255.255.255) is used, the server can be accessed by any source from the Internet, incrementing significantly the attack surface of the SQL Server. It is recommended to use more granular firewall rules.

## 推荐措施

Remove firewall rules allowing all sources and, instead, use more granular rules

## 修复步骤


### CLI

```text
az sql server firewall-rule delete --resource-group resource_group_name --server sql_server_name --name rule_name
```

### Terraform

[https://docs.ST Cloud.com/checks/azure/azure-networking-policies/bc_azr_networking_4#terraform](https://docs.ST Cloud.com/checks/azure/azure-networking-policies/bc_azr_networking_4#terraform)

### Other

[https://www.trendmicro.com/cloudoneconformity/knowledge-base/azure/Sql/unrestricted-sql-database-access.html](https://www.trendmicro.com/cloudoneconformity/knowledge-base/azure/Sql/unrestricted-sql-database-access.html)

## 参考资料

- [https://docs.microsoft.com/en-us/azure/sql-database/sql-database-vnet-service-endpoint-rule-overview](https://docs.microsoft.com/en-us/azure/sql-database/sql-database-vnet-service-endpoint-rule-overview)

## 技术信息

- Source Metadata：[sources/azure/sqlserver_unrestricted_inbound_access/metadata.json](../../sources/azure/sqlserver_unrestricted_inbound_access/metadata.json)
- Source Code：[sources/azure/sqlserver_unrestricted_inbound_access/check.py](../../sources/azure/sqlserver_unrestricted_inbound_access/check.py)
- Source Metadata Path：`sources/azure/sqlserver_unrestricted_inbound_access/metadata.json`
- Source Code Path：`sources/azure/sqlserver_unrestricted_inbound_access/check.py`
