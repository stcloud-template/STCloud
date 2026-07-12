# Ensure That 'Users Can Register Applications' Is Set to 'No'

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `entra_policy_ensure_default_user_cannot_create_apps` |
| クラウドプラットフォーム | Azure |
| サービス | entra |
| 重大度 | high |
| カテゴリ | Uncategorized |
| リソースタイプ | #microsoft.graph.authorizationPolicy |
| リソースグループ | IAM |

## 説明

Require administrators or appropriately delegated users to register third-party applications.

## リスク

It is recommended to only allow an administrator to register custom-developed applications. This ensures that the application undergoes a formal security review and approval process prior to exposing Azure Active Directory data. Certain users like developers or other high-request users may also be delegated permissions to prevent them from waiting on an administrative user. Your organization should review your policies and decide your needs.

## 推奨事項

1. From Azure Home select the Portal Menu 2. Select Azure Active Directory 3. Select Users 4. Select User settings 5. Ensure that Users can register applications is set to No

- 推奨リンク：[https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/delegate-app-roles#restrict-who-can-create-applications](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/delegate-app-roles#restrict-who-can-create-applications)

## 修正手順


### Other

[https://www.trendmicro.com/cloudoneconformity/knowledge-base/azure/ActiveDirectory/users-can-register-applications.html](https://www.trendmicro.com/cloudoneconformity/knowledge-base/azure/ActiveDirectory/users-can-register-applications.html)

## 参考資料

- [https://learn.microsoft.com/en-us/entra/identity-platform/how-applications-are-added#who-has-permission-to-add-applications-to-my-azure-ad-instance](https://learn.microsoft.com/en-us/entra/identity-platform/how-applications-are-added#who-has-permission-to-add-applications-to-my-azure-ad-instance)
- [https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/delegate-app-roles#restrict-who-can-create-applications](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/delegate-app-roles#restrict-who-can-create-applications)

## 技術情報

- Source Metadata：[sources/azure/entra_policy_ensure_default_user_cannot_create_apps/metadata.json](../../sources/azure/entra_policy_ensure_default_user_cannot_create_apps/metadata.json)
- Source Code：[sources/azure/entra_policy_ensure_default_user_cannot_create_apps/check.py](../../sources/azure/entra_policy_ensure_default_user_cannot_create_apps/check.py)
- Source Metadata Path：`sources/azure/entra_policy_ensure_default_user_cannot_create_apps/metadata.json`
- Source Code Path：`sources/azure/entra_policy_ensure_default_user_cannot_create_apps/check.py`
