# Ensure that no custom subscription owner roles are created

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `iam_subscription_roles_owner_custom_not_created` |
| クラウドプラットフォーム | Azure |
| サービス | iam |
| 重大度 | high |
| カテゴリ | Uncategorized |
| リソースタイプ | AzureRole |
| リソースグループ | IAM |

## 説明

Ensure that no custom subscription owner roles are created

## リスク

Subscription ownership should not include permission to create custom owner roles. The principle of least privilege should be followed and only necessary privileges should be assigned instead of allowing full administrative access.

## 推奨事項

Custom subscription owner roles should not be created. This is because the principle of least privilege should be followed and only necessary privileges should be assigned instead of allowing full administrative access

- 推奨リンク：[https://www.trendmicro.com/cloudoneconformity-staging/knowledge-base/azure/AccessControl/remove-custom-owner-roles.html](https://www.trendmicro.com/cloudoneconformity-staging/knowledge-base/azure/AccessControl/remove-custom-owner-roles.html)

## 修正手順


### Other

[https://www.trendmicro.com/cloudoneconformity-staging/knowledge-base/azure/AccessControl/remove-custom-owner-roles.html](https://www.trendmicro.com/cloudoneconformity-staging/knowledge-base/azure/AccessControl/remove-custom-owner-roles.html)

## 参考資料

- [https://learn.microsoft.com/en-us/azure/role-based-access-control/custom-roles](https://learn.microsoft.com/en-us/azure/role-based-access-control/custom-roles)
- [https://www.trendmicro.com/cloudoneconformity-staging/knowledge-base/azure/AccessControl/remove-custom-owner-roles.html](https://www.trendmicro.com/cloudoneconformity-staging/knowledge-base/azure/AccessControl/remove-custom-owner-roles.html)

## 技術情報

- Source Metadata：[sources/azure/iam_subscription_roles_owner_custom_not_created/metadata.json](../../sources/azure/iam_subscription_roles_owner_custom_not_created/metadata.json)
- Source Code：[sources/azure/iam_subscription_roles_owner_custom_not_created/check.py](../../sources/azure/iam_subscription_roles_owner_custom_not_created/check.py)
- Source Metadata Path：`sources/azure/iam_subscription_roles_owner_custom_not_created/metadata.json`
- Source Code Path：`sources/azure/iam_subscription_roles_owner_custom_not_created/check.py`
