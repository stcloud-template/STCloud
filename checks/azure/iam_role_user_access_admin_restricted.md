# Ensure 'User Access Administrator' role is restricted

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `iam_role_user_access_admin_restricted` |
| クラウドプラットフォーム | Azure |
| サービス | iam |
| 重大度 | high |
| カテゴリ | Uncategorized |
| リソースタイプ | AzureIAMRoleassignment |
| リソースグループ | IAM |

## 説明

Checks for active assignments of the highly privileged 'User Access Administrator' role in Azure subscriptions.

## リスク

Persistent assignment of this role can lead to privilege escalation and unauthorized access, increasing the risk of security breaches.

## 推奨事項

Remove 'User Access Administrator' role assignments immediately after use to minimize security risks.

- 推奨リンク：[https://learn.microsoft.com/en-us/azure/role-based-access-control/elevate-access-global-admin?tabs=azure-portal%2Centra-audit-logs](https://learn.microsoft.com/en-us/azure/role-based-access-control/elevate-access-global-admin?tabs=azure-portal%2Centra-audit-logs)

## 修正手順


### CLI

```text
az role assignment delete --role 'User Access Administrator' --scope '/subscriptions/<subscription_id>'
```

## 参考資料

- [https://learn.microsoft.com/en-us/azure/role-based-access-control/built-in-roles/privileged#user-access-administrator](https://learn.microsoft.com/en-us/azure/role-based-access-control/built-in-roles/privileged#user-access-administrator)
- [https://learn.microsoft.com/en-us/azure/role-based-access-control/elevate-access-global-admin?tabs=azure-portal%2Centra-audit-logs](https://learn.microsoft.com/en-us/azure/role-based-access-control/elevate-access-global-admin?tabs=azure-portal%2Centra-audit-logs)

## 技術情報

- Source Metadata：[sources/azure/iam_role_user_access_admin_restricted/metadata.json](../../sources/azure/iam_role_user_access_admin_restricted/metadata.json)
- Source Code：[sources/azure/iam_role_user_access_admin_restricted/check.py](../../sources/azure/iam_role_user_access_admin_restricted/check.py)
- Source Metadata Path：`sources/azure/iam_role_user_access_admin_restricted/metadata.json`
- Source Code Path：`sources/azure/iam_role_user_access_admin_restricted/check.py`
