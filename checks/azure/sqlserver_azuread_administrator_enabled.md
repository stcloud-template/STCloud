# Ensure that SQL Servers have an Azure Active Directory administrator

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `sqlserver_azuread_administrator_enabled` |
| 云平台 | Azure |
| 服务 | sqlserver |
| 严重等级 | medium |
| 类别 | Uncategorized |
| 资源类型 | SQLServer |
| 资源组 | database |

## 描述

Ensure that there is an Azure Active Directory administrator configured

## 风险

Azure Active Directory provides a centralized way of managing identities. Using local SQL administrator identites makes it more difficult to manage user accounts. In addition, from Azure Active Directory, security policies can be enforced to users in centralized way.

## 推荐措施

Enable an Azure Active Directory administrator

## 修复步骤


### CLI

```text
az sql server ad-admin create --resource-group resource_group_name --server server_name --display-name display_name --object-id user_object_id
```

### Terraform

[https://docs.ST Cloud.com/checks/azure/azure-general-policies/ensure-that-azure-active-directory-admin-is-configured#terraform](https://docs.ST Cloud.com/checks/azure/azure-general-policies/ensure-that-azure-active-directory-admin-is-configured#terraform)

### Other

[https://www.trendmicro.com/cloudoneconformity/knowledge-base/azure/Sql/active-directory-admin.html](https://www.trendmicro.com/cloudoneconformity/knowledge-base/azure/Sql/active-directory-admin.html)

## 参考资料

- [https://docs.microsoft.com/en-us/azure/sql-database/sql-database-aad-authentication](https://docs.microsoft.com/en-us/azure/sql-database/sql-database-aad-authentication)

## 技术信息

- Source Metadata：[sources/azure/sqlserver_azuread_administrator_enabled/metadata.json](../../sources/azure/sqlserver_azuread_administrator_enabled/metadata.json)
- Source Code：[sources/azure/sqlserver_azuread_administrator_enabled/check.py](../../sources/azure/sqlserver_azuread_administrator_enabled/check.py)
- Source Metadata Path：`sources/azure/sqlserver_azuread_administrator_enabled/metadata.json`
- Source Code Path：`sources/azure/sqlserver_azuread_administrator_enabled/check.py`
