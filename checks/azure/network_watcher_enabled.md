# Ensure that Network Watcher is 'Enabled' for all locations in the Azure subscription

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `network_watcher_enabled` |
| クラウドプラットフォーム | Azure |
| サービス | network |
| 重大度 | medium |
| カテゴリ | Uncategorized |
| リソースタイプ | Network |
| リソースグループ | network |

## 説明

Enable Network Watcher for Azure subscriptions.

## リスク

Network diagnostic and visualization tools available with Network Watcher help users understand, diagnose, and gain insights to the network in Azure.

## 推奨事項

Opting out of Network Watcher automatic enablement is a permanent change. Once you opt-out you cannot opt-in without contacting support.

- 推奨リンク：[https://learn.microsoft.com/en-us/security/benchmark/azure/security-controls-v2-logging-threat-detection#lt-3-enable-logging-for-azure-network-activities](https://learn.microsoft.com/en-us/security/benchmark/azure/security-controls-v2-logging-threat-detection#lt-3-enable-logging-for-azure-network-activities)

## 修正手順


### Other

[https://www.trendmicro.com/cloudoneconformity-staging/knowledge-base/azure/Network/enable-network-watcher.html](https://www.trendmicro.com/cloudoneconformity-staging/knowledge-base/azure/Network/enable-network-watcher.html)

## 参考資料

- [https://docs.microsoft.com/en-us/azure/network-watcher/network-watcher-monitoring-overview](https://docs.microsoft.com/en-us/azure/network-watcher/network-watcher-monitoring-overview)
- [https://learn.microsoft.com/en-us/security/benchmark/azure/security-controls-v2-logging-threat-detection#lt-3-enable-logging-for-azure-network-activities](https://learn.microsoft.com/en-us/security/benchmark/azure/security-controls-v2-logging-threat-detection#lt-3-enable-logging-for-azure-network-activities)

## 技術情報

- Source Metadata：[sources/azure/network_watcher_enabled/metadata.json](../../sources/azure/network_watcher_enabled/metadata.json)
- Source Code：[sources/azure/network_watcher_enabled/check.py](../../sources/azure/network_watcher_enabled/check.py)
- Source Metadata Path：`sources/azure/network_watcher_enabled/metadata.json`
- Source Code Path：`sources/azure/network_watcher_enabled/check.py`
