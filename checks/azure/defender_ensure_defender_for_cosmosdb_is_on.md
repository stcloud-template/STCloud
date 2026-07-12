# Ensure That Microsoft Defender for Cosmos DB Is Set To 'On'

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `defender_ensure_defender_for_cosmosdb_is_on` |
| クラウドプラットフォーム | Azure |
| サービス | defender |
| 重大度 | high |
| カテゴリ | Uncategorized |
| リソースタイプ | AzureDefenderPlan |
| リソースグループ | security |

## 説明

Ensure That Microsoft Defender for Cosmos DB Is Set To 'On'

## リスク

In scanning Cosmos DB requests within a subscription, requests are compared to a heuristic list of potential security threats. These threats could be a result of a security breach within your services, thus scanning for them could prevent a potential security threat from being introduced.

## 推奨事項

By default, Microsoft Defender for Cloud is not enabled for your App Service instances. Enabling the Defender security service for App Service instances allows for advanced security defense using threat detection capabilities provided by Microsoft Security Response Center.

- 推奨リンク：[Enable Microsoft Defender for Cosmos DB](Enable Microsoft Defender for Cosmos DB)

## 修正手順

No remediation steps available.

## 参考資料

- [Enable Microsoft Defender for Cosmos DB](Enable Microsoft Defender for Cosmos DB)

## 技術情報

- Source Metadata：[sources/azure/defender_ensure_defender_for_cosmosdb_is_on/metadata.json](../../sources/azure/defender_ensure_defender_for_cosmosdb_is_on/metadata.json)
- Source Code：[sources/azure/defender_ensure_defender_for_cosmosdb_is_on/check.py](../../sources/azure/defender_ensure_defender_for_cosmosdb_is_on/check.py)
- Source Metadata Path：`sources/azure/defender_ensure_defender_for_cosmosdb_is_on/metadata.json`
- Source Code Path：`sources/azure/defender_ensure_defender_for_cosmosdb_is_on/check.py`
