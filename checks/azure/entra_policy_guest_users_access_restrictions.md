# Ensure That 'Guest users access restrictions' is set to 'Guest user access is restricted to properties and memberships of their own directory objects'

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `entra_policy_guest_users_access_restrictions` |
| クラウドプラットフォーム | Azure |
| サービス | entra |
| 重大度 | medium |
| カテゴリ | Uncategorized |
| リソースタイプ | #microsoft.graph.authorizationPolicy |
| リソースグループ | IAM |

## 説明

Limit guest user permissions.

## リスク

Limiting guest access ensures that guest accounts do not have permission for certain directory tasks, such as enumerating users, groups or other directory resources, and cannot be assigned to administrative roles in your directory. Guest access has three levels of restriction. 1. Guest users have the same access as members (most inclusive), 2. Guest users have limited access to properties and memberships of directory objects (default value), 3. Guest user access is restricted to properties and memberships of their own directory objects (most restrictive). The recommended option is the 3rd, most restrictive: 'Guest user access is restricted to their own directory object'.

## 推奨事項

1. From Azure Home select the Portal Menu 2. Select Microsoft Entra ID 3. Then External Identities 4. Select External collaboration settings 5. Under Guest user access, change Guest user access restrictions to be Guest user access is restricted to properties and memberships of their own directory objects

- 推奨リンク：[https://learn.microsoft.com/en-us/entra/fundamentals/users-default-permissions#member-and-guest-users](https://learn.microsoft.com/en-us/entra/fundamentals/users-default-permissions#member-and-guest-users)

## 修正手順

No remediation steps available.

## 参考資料

- [https://learn.microsoft.com/en-us/entra/identity/users/users-restrict-guest-permissions](https://learn.microsoft.com/en-us/entra/identity/users/users-restrict-guest-permissions)
- [https://learn.microsoft.com/en-us/entra/fundamentals/users-default-permissions#member-and-guest-users](https://learn.microsoft.com/en-us/entra/fundamentals/users-default-permissions#member-and-guest-users)

## 技術情報

- Source Metadata：[sources/azure/entra_policy_guest_users_access_restrictions/metadata.json](../../sources/azure/entra_policy_guest_users_access_restrictions/metadata.json)
- Source Code：[sources/azure/entra_policy_guest_users_access_restrictions/check.py](../../sources/azure/entra_policy_guest_users_access_restrictions/check.py)
- Source Metadata Path：`sources/azure/entra_policy_guest_users_access_restrictions/metadata.json`
- Source Code Path：`sources/azure/entra_policy_guest_users_access_restrictions/check.py`
