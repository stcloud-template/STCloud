# Ensure that SQL Servers have an Azure Active Directory administrator

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `sqlserver_azuread_administrator_enabled` |
| クラウドプラットフォーム | Azure |
| サービス | sqlserver |
| 重大度 | medium |
| カテゴリ | Uncategorized |
| リソースタイプ | SQLServer |
| リソースグループ | database |

## 説明

Ensure that there is an Azure Active Directory administrator configured

## リスク

Azure Active Directory provides a centralized way of managing identities. Using local SQL administrator identites makes it more difficult to manage user accounts. In addition, from Azure Active Directory, security policies can be enforced to users in centralized way.

## 推奨事項

Enable an Azure Active Directory administrator

## 修正手順


### CLI

```text
az sql server ad-admin create --resource-group resource_group_name --server server_name --display-name display_name --object-id user_object_id
```

### Terraform

[https://docs.ST Cloud.com/checks/azure/azure-general-policies/ensure-that-azure-active-directory-admin-is-configured#terraform](https://docs.ST Cloud.com/checks/azure/azure-general-policies/ensure-that-azure-active-directory-admin-is-configured#terraform)

### Other

[https://www.trendmicro.com/cloudoneconformity/knowledge-base/azure/Sql/active-directory-admin.html](https://www.trendmicro.com/cloudoneconformity/knowledge-base/azure/Sql/active-directory-admin.html)

## 参考資料

- [https://docs.microsoft.com/en-us/azure/sql-database/sql-database-aad-authentication](https://docs.microsoft.com/en-us/azure/sql-database/sql-database-aad-authentication)

## 技術情報

- Source Metadata：[sources/azure/sqlserver_azuread_administrator_enabled/metadata.json](../../sources/azure/sqlserver_azuread_administrator_enabled/metadata.json)
- Source Code：[sources/azure/sqlserver_azuread_administrator_enabled/check.py](../../sources/azure/sqlserver_azuread_administrator_enabled/check.py)
- Source Metadata Path：`sources/azure/sqlserver_azuread_administrator_enabled/metadata.json`
- Source Code Path：`sources/azure/sqlserver_azuread_administrator_enabled/check.py`
