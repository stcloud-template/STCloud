# Enable Cloud DNS Logging for VPC Networks

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `compute_network_dns_logging_enabled` |
| クラウドプラットフォーム | GCP |
| サービス | compute |
| 重大度 | medium |
| カテゴリ | Uncategorized |
| リソースタイプ | Network |
| リソースグループ | network |

## 説明

Ensure that Cloud DNS logging is enabled for all your Virtual Private Cloud (VPC) networks using DNS server policies. Cloud DNS logging records queries that the name servers resolve for your Google Cloud VPC networks, as well as queries from external entities directly to a public DNS zone. Recorded queries can come from virtual machine (VM) instances, GKE containers running in the same VPC network, peering zones, or other Google Cloud resources provisioned within your VPC.

## リスク

Cloud DNS logging is disabled by default on each Google Cloud VPC network. By enabling monitoring of Cloud DNS logs, you can increase visibility into the DNS names requested by the clients within your VPC network. Cloud DNS logs can be monitored for anomalous domain names and evaluated against threat intelligence.

## 推奨事項

Cloud DNS logging records the queries from the name servers within your VPC to Stackdriver. Logged queries can come from Compute Engine VMs, GKE containers, or other GCP resources provisioned within the VPC.

- 推奨リンク：[https://cloud.google.com/dns/docs/monitoring](https://cloud.google.com/dns/docs/monitoring)

## 修正手順


### Other

[https://www.trendmicro.com/cloudoneconformity/knowledge-base/gcp/CloudVPC/dns-logging-for-vpcs.html](https://www.trendmicro.com/cloudoneconformity/knowledge-base/gcp/CloudVPC/dns-logging-for-vpcs.html)

## 参考資料

- [https://cloud.google.com/dns/docs/monitoring](https://cloud.google.com/dns/docs/monitoring)

## 技術情報

- Source Metadata：[sources/gcp/compute_network_dns_logging_enabled/metadata.json](../../sources/gcp/compute_network_dns_logging_enabled/metadata.json)
- Source Code：[sources/gcp/compute_network_dns_logging_enabled/check.py](../../sources/gcp/compute_network_dns_logging_enabled/check.py)
- Source Metadata Path：`sources/gcp/compute_network_dns_logging_enabled/metadata.json`
- Source Code Path：`sources/gcp/compute_network_dns_logging_enabled/check.py`
