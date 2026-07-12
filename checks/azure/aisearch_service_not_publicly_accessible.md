# Restrict public network access to the AI Search Service

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `aisearch_service_not_publicly_accessible` |
| クラウドプラットフォーム | Azure |
| サービス | aisearch |
| 重大度 | high |
| カテゴリ | gen-ai |
| リソースタイプ | AzureSearchService |
| リソースグループ | database |

## 説明

Ensure that public network access to the Search Service is restricted.

## リスク

Public accessibility exposes the Search Service to potential attacks, unauthorized usage, and data breaches. Restricting access minimizes the surface area for attacks and ensures that only authorized networks can access the search service.

## 推奨事項

Ensure that the necessary virtual network configurations or IP rules are in place to allow access from required services once public access is restricted. Review the network access settings regularly to maintain a secure environment. To restrict public network access to your Search Service: 1. Navigate to your Search Service y in the Azure Portal. 2. Under 'Settings'->'Networking', configure the 'Public network access' settings to 'Disabled'. 3. Set up virtual network service endpoints or private endpoints as needed for secure access. 4. Review and adjust IP access rules as necessary.

- 推奨リンク：[https://learn.microsoft.com/en-us/azure/search/service-configure-firewall#configure-network-access-in-azure-portal](https://learn.microsoft.com/en-us/azure/search/service-configure-firewall#configure-network-access-in-azure-portal)

## 修正手順


### CLI

```text
az search service update --resource-group <resource_group_name> --name <service_name> --public-access disabled
```

## 参考資料

- [https://learn.microsoft.com/en-us/azure/search/service-configure-firewall#configure-network-access-in-azure-portal](https://learn.microsoft.com/en-us/azure/search/service-configure-firewall#configure-network-access-in-azure-portal)

## 技術情報

- Source Metadata：[sources/azure/aisearch_service_not_publicly_accessible/metadata.json](../../sources/azure/aisearch_service_not_publicly_accessible/metadata.json)
- Source Code：[sources/azure/aisearch_service_not_publicly_accessible/check.py](../../sources/azure/aisearch_service_not_publicly_accessible/check.py)
- Source Metadata Path：`sources/azure/aisearch_service_not_publicly_accessible/metadata.json`
- Source Code Path：`sources/azure/aisearch_service_not_publicly_accessible/check.py`
