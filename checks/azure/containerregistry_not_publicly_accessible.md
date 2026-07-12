# Restrict public network access to the Container Registry

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `containerregistry_not_publicly_accessible` |
| クラウドプラットフォーム | Azure |
| サービス | containerregistry |
| 重大度 | high |
| カテゴリ | Uncategorized |
| リソースタイプ | ContainerRegistry |
| リソースグループ | container |

## 説明

Ensure that public network access to the Azure Container Registry is restricted.

## リスク

Public accessibility exposes the Container Registry to potential attacks, unauthorized usage, and data breaches. Restricting access minimizes the surface area for attacks and ensures that only authorized networks can access the registry.

## 推奨事項

Ensure that the necessary virtual network configurations or IP rules are in place to allow access from required services once public access is restricted. Review the network access settings regularly to maintain a secure environment. To restrict public network access to your Azure Container Registry: 1. Navigate to your Container Registry in the Azure Portal. 2. Under 'Settings'->'Networking', configure the 'Public network access' settings to 'Disabled'. 3. Set up virtual network service endpoints or private endpoints as needed for secure access. 4. Review and adjust IP access rules as necessary.

- 推奨リンク：[https://learn.microsoft.com/en-us/azure/container-registry/container-registry-access-selected-networks](https://learn.microsoft.com/en-us/azure/container-registry/container-registry-access-selected-networks)

## 修正手順


### CLI

```text
az acr update --name <registry-name> --default-action Deny
```

## 参考資料

- [https://learn.microsoft.com/en-us/azure/container-registry/container-registry-access-selected-networks](https://learn.microsoft.com/en-us/azure/container-registry/container-registry-access-selected-networks)

## 技術情報

- Source Metadata：[sources/azure/containerregistry_not_publicly_accessible/metadata.json](../../sources/azure/containerregistry_not_publicly_accessible/metadata.json)
- Source Code：[sources/azure/containerregistry_not_publicly_accessible/check.py](../../sources/azure/containerregistry_not_publicly_accessible/check.py)
- Source Metadata Path：`sources/azure/containerregistry_not_publicly_accessible/metadata.json`
- Source Code Path：`sources/azure/containerregistry_not_publicly_accessible/check.py`
