# Ensure admin user is disabled for Azure Container Registry

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `containerregistry_admin_user_disabled` |
| クラウドプラットフォーム | Azure |
| サービス | containerregistry |
| 重大度 | high |
| カテゴリ | Uncategorized |
| リソースタイプ | ContainerRegistry |
| リソースグループ | container |

## 説明

Ensure that the admin user is disabled and Role-Based Access Control (RBAC) is used instead since it could grant unrestricted access to the registry

## リスク

If the admin user is enabled, it may lead to unauthorized access to the container registry and its resources, which could compromise the confidentiality, integrity, and availability of the images stored within.

## 推奨事項

Disable the admin user on Azure Container Registry through the Azure Portal: 1. Navigate to your Container Registry. 2. In the settings, select 'Access keys'. 3. Ensure the 'Admin user' checkbox is not ticked. For all actions relying on registry access, switch to using Role-Based Access Control.

- 推奨リンク：[https://learn.microsoft.com/en-us/azure/container-registry/container-registry-authentication?tabs=azure-cli#admin-account](https://learn.microsoft.com/en-us/azure/container-registry/container-registry-authentication?tabs=azure-cli#admin-account)

## 修正手順


### CLI

```text
az acr update --name <RegistryName> --resource-group <ResourceGroupName> --admin-enabled false
```

## 参考資料

- [https://learn.microsoft.com/en-us/azure/container-registry/container-registry-authentication?tabs=azure-cli#admin-account](https://learn.microsoft.com/en-us/azure/container-registry/container-registry-authentication?tabs=azure-cli#admin-account)

## 技術情報

- Source Metadata：[sources/azure/containerregistry_admin_user_disabled/metadata.json](../../sources/azure/containerregistry_admin_user_disabled/metadata.json)
- Source Code：[sources/azure/containerregistry_admin_user_disabled/check.py](../../sources/azure/containerregistry_admin_user_disabled/check.py)
- Source Metadata Path：`sources/azure/containerregistry_admin_user_disabled/metadata.json`
- Source Code Path：`sources/azure/containerregistry_admin_user_disabled/check.py`
