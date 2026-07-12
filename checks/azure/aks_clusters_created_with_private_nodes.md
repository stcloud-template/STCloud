# Ensure clusters are created with Private Nodes

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `aks_clusters_created_with_private_nodes` |
| クラウドプラットフォーム | Azure |
| サービス | aks |
| 重大度 | high |
| カテゴリ | Uncategorized |
| リソースタイプ | Microsoft.ContainerService/ManagedClusters |
| リソースグループ | container |

## 説明

Disable public IP addresses for cluster nodes, so that they only have private IP addresses. Private Nodes are nodes with no public IP addresses.

## リスク

Disabling public IP addresses on cluster nodes restricts access to only internal networks, forcing attackers to obtain local network access before attempting to compromise the underlying Kubernetes hosts.

## 推奨事項

No content available.

- 推奨リンク：[https://learn.microsoft.com/en-us/azure/aks/access-private-cluster](https://learn.microsoft.com/en-us/azure/aks/access-private-cluster)

## 修正手順

No remediation steps available.

## 参考資料

- [https://learn.microsoft.com/en-us/azure/aks/private-clusters](https://learn.microsoft.com/en-us/azure/aks/private-clusters)
- [https://learn.microsoft.com/en-us/azure/aks/access-private-cluster](https://learn.microsoft.com/en-us/azure/aks/access-private-cluster)

## 技術情報

- Source Metadata：[sources/azure/aks_clusters_created_with_private_nodes/metadata.json](../../sources/azure/aks_clusters_created_with_private_nodes/metadata.json)
- Source Code：[sources/azure/aks_clusters_created_with_private_nodes/check.py](../../sources/azure/aks_clusters_created_with_private_nodes/check.py)
- Source Metadata Path：`sources/azure/aks_clusters_created_with_private_nodes/metadata.json`
- Source Code Path：`sources/azure/aks_clusters_created_with_private_nodes/check.py`
