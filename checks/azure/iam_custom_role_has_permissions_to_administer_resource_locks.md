# Ensure an IAM custom role has permissions to administer resource locks

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `iam_custom_role_has_permissions_to_administer_resource_locks` |
| 云平台 | Azure |
| 服务 | iam |
| 严重等级 | high |
| 类别 | Uncategorized |
| 资源类型 | AzureRole |
| 资源组 | IAM |

## 描述

Ensure a Custom Role is Assigned Permissions for Administering Resource Locks

## 风险

In Azure, resource locks are a way to prevent accidental deletion or modification of critical resources. These locks can be set at the resource group level or the individual resource level. Resource locks administration is a critical task that should be preformed from a custom role with the appropriate permissions. This ensures that only authorized users can administer resource locks.

## 推荐措施

Resouce locks are needed to prevent accidental deletion or modification of critical Azure resources. The administration of resource locks should be performed from a custom role with the appropriate permissions.

- 推荐链接：[https://www.trendmicro.com/cloudoneconformity-staging/knowledge-base/azure/AccessControl/resource-lock-custom-role.html](https://www.trendmicro.com/cloudoneconformity-staging/knowledge-base/azure/AccessControl/resource-lock-custom-role.html)

## 修复步骤


### Other

[https://www.trendmicro.com/cloudoneconformity-staging/knowledge-base/azure/AccessControl/resource-lock-custom-role.html](https://www.trendmicro.com/cloudoneconformity-staging/knowledge-base/azure/AccessControl/resource-lock-custom-role.html)

## 参考资料

- [https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/lock-resources?tabs=json](https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/lock-resources?tabs=json)
- [https://www.trendmicro.com/cloudoneconformity-staging/knowledge-base/azure/AccessControl/resource-lock-custom-role.html](https://www.trendmicro.com/cloudoneconformity-staging/knowledge-base/azure/AccessControl/resource-lock-custom-role.html)

## 技术信息

- Source Metadata：[sources/azure/iam_custom_role_has_permissions_to_administer_resource_locks/metadata.json](../../sources/azure/iam_custom_role_has_permissions_to_administer_resource_locks/metadata.json)
- Source Code：[sources/azure/iam_custom_role_has_permissions_to_administer_resource_locks/check.py](../../sources/azure/iam_custom_role_has_permissions_to_administer_resource_locks/check.py)
- Source Metadata Path：`sources/azure/iam_custom_role_has_permissions_to_administer_resource_locks/metadata.json`
- Source Code Path：`sources/azure/iam_custom_role_has_permissions_to_administer_resource_locks/check.py`
