# Ensure that 'Restrict non-admin users from creating tenants' is set to 'Yes'

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `entra_policy_ensure_default_user_cannot_create_tenants` |
| クラウドプラットフォーム | Azure |
| サービス | entra |
| 重大度 | high |
| カテゴリ | Uncategorized |
| リソースタイプ | #microsoft.graph.authorizationPolicy |
| リソースグループ | IAM |

## 説明

Require administrators or appropriately delegated users to create new tenants.

## リスク

It is recommended to only allow an administrator to create new tenants. This prevent users from creating new Azure AD or Azure AD B2C tenants and ensures that only authorized users are able to do so.

## 推奨事項

1. From Azure Home select the Portal Menu 2. Select Azure Active Directory 3. Select Users 4. Select User settings 5. Set 'Restrict non-admin users from creating' tenants to 'Yes'

- 推奨リンク：[https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#tenant-creator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#tenant-creator)

## 修正手順

No remediation steps available.

## 参考資料

- [https://learn.microsoft.com/en-us/entra/fundamentals/users-default-permissions](https://learn.microsoft.com/en-us/entra/fundamentals/users-default-permissions)
- [https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#tenant-creator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#tenant-creator)

## 技術情報

- Source Metadata：[sources/azure/entra_policy_ensure_default_user_cannot_create_tenants/metadata.json](../../sources/azure/entra_policy_ensure_default_user_cannot_create_tenants/metadata.json)
- Source Code：[sources/azure/entra_policy_ensure_default_user_cannot_create_tenants/check.py](../../sources/azure/entra_policy_ensure_default_user_cannot_create_tenants/check.py)
- Source Metadata Path：`sources/azure/entra_policy_ensure_default_user_cannot_create_tenants/metadata.json`
- Source Code Path：`sources/azure/entra_policy_ensure_default_user_cannot_create_tenants/check.py`
