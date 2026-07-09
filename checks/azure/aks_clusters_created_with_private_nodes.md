# Ensure clusters are created with Private Nodes

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `aks_clusters_created_with_private_nodes` |
| 云平台 | Azure |
| 服务 | aks |
| 严重等级 | high |
| 类别 | Uncategorized |
| 资源类型 | Microsoft.ContainerService/ManagedClusters |
| 资源组 | container |

## 描述

Disable public IP addresses for cluster nodes, so that they only have private IP addresses. Private Nodes are nodes with no public IP addresses.

## 风险

Disabling public IP addresses on cluster nodes restricts access to only internal networks, forcing attackers to obtain local network access before attempting to compromise the underlying Kubernetes hosts.

## 推荐措施

No content available.

- 推荐链接：[https://learn.microsoft.com/en-us/azure/aks/access-private-cluster](https://learn.microsoft.com/en-us/azure/aks/access-private-cluster)

## 修复步骤

No remediation steps available.

## 参考资料

- [https://learn.microsoft.com/en-us/azure/aks/private-clusters](https://learn.microsoft.com/en-us/azure/aks/private-clusters)
- [https://learn.microsoft.com/en-us/azure/aks/access-private-cluster](https://learn.microsoft.com/en-us/azure/aks/access-private-cluster)

## 技术信息

- Source Metadata：[sources/azure/aks_clusters_created_with_private_nodes/metadata.json](../../sources/azure/aks_clusters_created_with_private_nodes/metadata.json)
- Source Code：[sources/azure/aks_clusters_created_with_private_nodes/check.py](../../sources/azure/aks_clusters_created_with_private_nodes/check.py)
- Source Metadata Path：`sources/azure/aks_clusters_created_with_private_nodes/metadata.json`
- Source Code Path：`sources/azure/aks_clusters_created_with_private_nodes/check.py`
