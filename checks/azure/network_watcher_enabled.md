# Ensure that Network Watcher is 'Enabled' for all locations in the Azure subscription

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `network_watcher_enabled` |
| 云平台 | Azure |
| 服务 | network |
| 严重等级 | medium |
| 类别 | Uncategorized |
| 资源类型 | Network |
| 资源组 | network |

## 描述

Enable Network Watcher for Azure subscriptions.

## 风险

Network diagnostic and visualization tools available with Network Watcher help users understand, diagnose, and gain insights to the network in Azure.

## 推荐措施

Opting out of Network Watcher automatic enablement is a permanent change. Once you opt-out you cannot opt-in without contacting support.

- 推荐链接：[https://learn.microsoft.com/en-us/security/benchmark/azure/security-controls-v2-logging-threat-detection#lt-3-enable-logging-for-azure-network-activities](https://learn.microsoft.com/en-us/security/benchmark/azure/security-controls-v2-logging-threat-detection#lt-3-enable-logging-for-azure-network-activities)

## 修复步骤


### Other

[https://www.trendmicro.com/cloudoneconformity-staging/knowledge-base/azure/Network/enable-network-watcher.html](https://www.trendmicro.com/cloudoneconformity-staging/knowledge-base/azure/Network/enable-network-watcher.html)

## 参考资料

- [https://docs.microsoft.com/en-us/azure/network-watcher/network-watcher-monitoring-overview](https://docs.microsoft.com/en-us/azure/network-watcher/network-watcher-monitoring-overview)
- [https://learn.microsoft.com/en-us/security/benchmark/azure/security-controls-v2-logging-threat-detection#lt-3-enable-logging-for-azure-network-activities](https://learn.microsoft.com/en-us/security/benchmark/azure/security-controls-v2-logging-threat-detection#lt-3-enable-logging-for-azure-network-activities)

## 技术信息

- Source Metadata：[sources/azure/network_watcher_enabled/metadata.json](../../sources/azure/network_watcher_enabled/metadata.json)
- Source Code：[sources/azure/network_watcher_enabled/check.py](../../sources/azure/network_watcher_enabled/check.py)
- Source Metadata Path：`sources/azure/network_watcher_enabled/metadata.json`
- Source Code Path：`sources/azure/network_watcher_enabled/check.py`
