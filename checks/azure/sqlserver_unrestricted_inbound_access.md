# Ensure no Azure SQL Databases allow ingress from 0.0.0.0/0 (ANY IP)

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `sqlserver_unrestricted_inbound_access` |
| クラウドプラットフォーム | Azure |
| サービス | sqlserver |
| 重大度 | critical |
| カテゴリ | Uncategorized |
| リソースタイプ | SQLServer |
| リソースグループ | database |

## 説明

Ensure that there are no firewall rules allowing traffic from 0.0.0.0-255.255.255.255

## リスク

Azure SQL servers provide a firewall that, by default, blocks all Internet connections. When the rule (0.0.0.0-255.255.255.255) is used, the server can be accessed by any source from the Internet, incrementing significantly the attack surface of the SQL Server. It is recommended to use more granular firewall rules.

## 推奨事項

Remove firewall rules allowing all sources and, instead, use more granular rules

## 修正手順


### CLI

```text
az sql server firewall-rule delete --resource-group resource_group_name --server sql_server_name --name rule_name
```

### Terraform

[https://docs.ST Cloud.com/checks/azure/azure-networking-policies/bc_azr_networking_4#terraform](https://docs.ST Cloud.com/checks/azure/azure-networking-policies/bc_azr_networking_4#terraform)

### Other

[https://www.trendmicro.com/cloudoneconformity/knowledge-base/azure/Sql/unrestricted-sql-database-access.html](https://www.trendmicro.com/cloudoneconformity/knowledge-base/azure/Sql/unrestricted-sql-database-access.html)

## 参考資料

- [https://docs.microsoft.com/en-us/azure/sql-database/sql-database-vnet-service-endpoint-rule-overview](https://docs.microsoft.com/en-us/azure/sql-database/sql-database-vnet-service-endpoint-rule-overview)

## 技術情報

- Source Metadata：[sources/azure/sqlserver_unrestricted_inbound_access/metadata.json](../../sources/azure/sqlserver_unrestricted_inbound_access/metadata.json)
- Source Code：[sources/azure/sqlserver_unrestricted_inbound_access/check.py](../../sources/azure/sqlserver_unrestricted_inbound_access/check.py)
- Source Metadata Path：`sources/azure/sqlserver_unrestricted_inbound_access/metadata.json`
- Source Code Path：`sources/azure/sqlserver_unrestricted_inbound_access/check.py`
