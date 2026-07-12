# Ensure that network flow logs are captured and fed into a central log analytics workspace.

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `network_flow_log_captured_sent` |
| クラウドプラットフォーム | Azure |
| サービス | network |
| 重大度 | high |
| カテゴリ | Uncategorized |
| リソースタイプ | Network |
| リソースグループ | network |

## 説明

Ensure that network flow logs are captured and fed into a central log analytics workspace.

## リスク

Network Flow Logs provide valuable insight into the flow of traffic around your network and feed into both Azure Monitor and Azure Sentinel (if in use), permitting the generation of visual flow diagrams to aid with analyzing for lateral movement, etc.

## 推奨事項

1. Navigate to Network Watcher. 2. Select NSG flow logs. 3. Select + Create. 4. Select the desired Subscription. 5. Select + Select NSG. 6. Select a network security group. 7. Click Confirm selection. 8. Select or create a new Storage Account. 9. Input the retention in days to retain the log. 10. Click Next. 11. Under Configuration, select Version 2. 12. If rich analytics are required, select Enable Traffic Analytics, a processing interval, and a Log Analytics Workspace. 13. Select Next. 14. Optionally add Tags. 15. Select Review + create. 16. Select Create. Warning The remediation policy creates remediation deployment and names them by concatenating the subscription name and the resource group name. The MAXIMUM permitted length of a deployment name is 64 characters. Exceeding this will cause the remediation task to fail.

- 推奨リンク：[https://docs.microsoft.com/en-us/azure/network-watcher/network-watcher-nsg-flow-logging-portal](https://docs.microsoft.com/en-us/azure/network-watcher/network-watcher-nsg-flow-logging-portal)

## 修正手順

No remediation steps available.

## 参考資料

- [https://learn.microsoft.com/en-us/security/benchmark/azure/mcsb-logging-threat-detection#lt-4-enable-network-logging-for-security-investigation](https://learn.microsoft.com/en-us/security/benchmark/azure/mcsb-logging-threat-detection#lt-4-enable-network-logging-for-security-investigation)
- [https://docs.microsoft.com/en-us/azure/network-watcher/network-watcher-nsg-flow-logging-portal](https://docs.microsoft.com/en-us/azure/network-watcher/network-watcher-nsg-flow-logging-portal)

## 技術情報

- Source Metadata：[sources/azure/network_flow_log_captured_sent/metadata.json](../../sources/azure/network_flow_log_captured_sent/metadata.json)
- Source Code：[sources/azure/network_flow_log_captured_sent/check.py](../../sources/azure/network_flow_log_captured_sent/check.py)
- Source Metadata Path：`sources/azure/network_flow_log_captured_sent/metadata.json`
- Source Code Path：`sources/azure/network_flow_log_captured_sent/check.py`
