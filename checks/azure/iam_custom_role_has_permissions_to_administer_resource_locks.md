# Ensure an IAM custom role has permissions to administer resource locks

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `iam_custom_role_has_permissions_to_administer_resource_locks` |
| クラウドプラットフォーム | Azure |
| サービス | iam |
| 重大度 | high |
| カテゴリ | Uncategorized |
| リソースタイプ | AzureRole |
| リソースグループ | IAM |

## 説明

Ensure a Custom Role is Assigned Permissions for Administering Resource Locks

## リスク

In Azure, resource locks are a way to prevent accidental deletion or modification of critical resources. These locks can be set at the resource group level or the individual resource level. Resource locks administration is a critical task that should be preformed from a custom role with the appropriate permissions. This ensures that only authorized users can administer resource locks.

## 推奨事項

Resouce locks are needed to prevent accidental deletion or modification of critical Azure resources. The administration of resource locks should be performed from a custom role with the appropriate permissions.

- 推奨リンク：[https://www.trendmicro.com/cloudoneconformity-staging/knowledge-base/azure/AccessControl/resource-lock-custom-role.html](https://www.trendmicro.com/cloudoneconformity-staging/knowledge-base/azure/AccessControl/resource-lock-custom-role.html)

## 修正手順


### Other

[https://www.trendmicro.com/cloudoneconformity-staging/knowledge-base/azure/AccessControl/resource-lock-custom-role.html](https://www.trendmicro.com/cloudoneconformity-staging/knowledge-base/azure/AccessControl/resource-lock-custom-role.html)

## 参考資料

- [https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/lock-resources?tabs=json](https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/lock-resources?tabs=json)
- [https://www.trendmicro.com/cloudoneconformity-staging/knowledge-base/azure/AccessControl/resource-lock-custom-role.html](https://www.trendmicro.com/cloudoneconformity-staging/knowledge-base/azure/AccessControl/resource-lock-custom-role.html)

## 技術情報

- Source Metadata：[sources/azure/iam_custom_role_has_permissions_to_administer_resource_locks/metadata.json](../../sources/azure/iam_custom_role_has_permissions_to_administer_resource_locks/metadata.json)
- Source Code：[sources/azure/iam_custom_role_has_permissions_to_administer_resource_locks/check.py](../../sources/azure/iam_custom_role_has_permissions_to_administer_resource_locks/check.py)
- Source Metadata Path：`sources/azure/iam_custom_role_has_permissions_to_administer_resource_locks/metadata.json`
- Source Code Path：`sources/azure/iam_custom_role_has_permissions_to_administer_resource_locks/check.py`
