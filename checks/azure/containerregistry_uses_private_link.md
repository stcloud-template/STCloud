# Ensure to use a private link for accessing the Azure Container Registry

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `containerregistry_uses_private_link` |
| クラウドプラットフォーム | Azure |
| サービス | containerregistry |
| 重大度 | medium |
| カテゴリ | Uncategorized |
| リソースタイプ | ContainerRegistry |
| リソースグループ | container |

## 説明

Ensure that a private link is used for accessing the Azure Container Registry to enhance security and restrict access to the registry over the public internet.

## リスク

Without using a private link, the Azure Container Registry may be exposed to the public internet, increasing the risk of unauthorized access and potential data breaches.

## 推奨事項

Create a private link for Azure Container Registry through the Azure Portal: 1. Navigate to your Container Registry. 2. In the settings, select 'Networking'. 3. Select 'Private access'. 4. Configure a private endpoint for the registry.

- 推奨リンク：[https://learn.microsoft.com/en-us/azure/container-registry/container-registry-private-link](https://learn.microsoft.com/en-us/azure/container-registry/container-registry-private-link)

## 修正手順


### CLI

```text
az network private-endpoint create  --connection-name <ConnectionName> --resource-group <ResourceGroupName> --name <Name> --private-connection-resource-id <RegistryId> --vnet-name <VnetName> --subnet <SubnetName> --group-ids registry
```

## 参考資料

- [https://learn.microsoft.com/en-us/azure/private-link/private-link-overview](https://learn.microsoft.com/en-us/azure/private-link/private-link-overview)
- [https://learn.microsoft.com/en-us/azure/container-registry/container-registry-private-link](https://learn.microsoft.com/en-us/azure/container-registry/container-registry-private-link)

## 技術情報

- Source Metadata：[sources/azure/containerregistry_uses_private_link/metadata.json](../../sources/azure/containerregistry_uses_private_link/metadata.json)
- Source Code：[sources/azure/containerregistry_uses_private_link/check.py](../../sources/azure/containerregistry_uses_private_link/check.py)
- Source Metadata Path：`sources/azure/containerregistry_uses_private_link/metadata.json`
- Source Code Path：`sources/azure/containerregistry_uses_private_link/check.py`
