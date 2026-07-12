# Ensure that 'Users can create security groups in Azure portals, API or PowerShell' is set to 'No'

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `entra_policy_default_users_cannot_create_security_groups` |
| クラウドプラットフォーム | Azure |
| サービス | entra |
| 重大度 | high |
| カテゴリ | Uncategorized |
| リソースタイプ | #microsoft.graph.authorizationPolicy |
| リソースグループ | IAM |

## 説明

Restrict security group creation to administrators only.

## リスク

When creating security groups is enabled, all users in the directory are allowed to create new security groups and add members to those groups. Unless a business requires this day-to-day delegation, security group creation should be restricted to administrators only.

## 推奨事項

1. From Azure Home select the Portal Menu 2. Select Microsoft Entra ID 3. Select Groups 4. Select General under Settings 5. Set Users can create security groups in Azure portals, API or PowerShell to No

## 修正手順


### Other

[https://www.trendmicro.com/cloudoneconformity/knowledge-base/azure/ActiveDirectory/users-can-create-security-groups.html](https://www.trendmicro.com/cloudoneconformity/knowledge-base/azure/ActiveDirectory/users-can-create-security-groups.html)

## 参考資料

- [https://learn.microsoft.com/en-us/entra/identity/users/groups-self-service-management](https://learn.microsoft.com/en-us/entra/identity/users/groups-self-service-management)

## 技術情報

- Source Metadata：[sources/azure/entra_policy_default_users_cannot_create_security_groups/metadata.json](../../sources/azure/entra_policy_default_users_cannot_create_security_groups/metadata.json)
- Source Code：[sources/azure/entra_policy_default_users_cannot_create_security_groups/check.py](../../sources/azure/entra_policy_default_users_cannot_create_security_groups/check.py)
- Source Metadata Path：`sources/azure/entra_policy_default_users_cannot_create_security_groups/metadata.json`
- Source Code Path：`sources/azure/entra_policy_default_users_cannot_create_security_groups/check.py`
