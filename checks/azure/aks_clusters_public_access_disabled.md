# Ensure clusters are created with Private Endpoint Enabled and Public Access Disabled

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `aks_clusters_public_access_disabled` |
| クラウドプラットフォーム | Azure |
| サービス | aks |
| 重大度 | high |
| カテゴリ | Uncategorized |
| リソースタイプ | Microsoft.ContainerService/ManagedClusters |
| リソースグループ | container |

## 説明

Disable access to the Kubernetes API from outside the node network if it is not required.

## リスク

In a private cluster, the master node has two endpoints, a private and public endpoint. The private endpoint is the internal IP address of the master, behind an internal load balancer in the master's wirtual network. Nodes communicate with the master using the private endpoint. The public endpoint enables the Kubernetes API to be accessed from outside the master's virtual network. Although Kubernetes API requires an authorized token to perform sensitive actions, a vulnerability could potentially expose the Kubernetes publically with unrestricted access. Additionally, an attacker may be able to identify the current cluster and Kubernetes API version and determine whether it is vulnerable to an attack. Unless required, disabling public endpoint will help prevent such threats, and require the attacker to be on the master's virtual network to perform any attack on the Kubernetes API.

## 推奨事項

To use a private endpoint, create a new private endpoint in your virtual network then create a link between your virtual network and a new private DNS zone

- 推奨リンク：[https://learn.microsoft.com/en-us/azure/aks/access-private-cluster?tabs=azure-cli](https://learn.microsoft.com/en-us/azure/aks/access-private-cluster?tabs=azure-cli)

## 修正手順


### CLI

```text
az aks update -n <cluster_name> -g <resource_group> --disable-public-fqdn
```

## 参考資料

- [https://learn.microsoft.com/en-us/azure/aks/private-clusters?tabs=azure-portal](https://learn.microsoft.com/en-us/azure/aks/private-clusters?tabs=azure-portal)
- [https://learn.microsoft.com/en-us/azure/aks/access-private-cluster?tabs=azure-cli](https://learn.microsoft.com/en-us/azure/aks/access-private-cluster?tabs=azure-cli)

## 技術情報

- Source Metadata：[sources/azure/aks_clusters_public_access_disabled/metadata.json](../../sources/azure/aks_clusters_public_access_disabled/metadata.json)
- Source Code：[sources/azure/aks_clusters_public_access_disabled/check.py](../../sources/azure/aks_clusters_public_access_disabled/check.py)
- Source Metadata Path：`sources/azure/aks_clusters_public_access_disabled/metadata.json`
- Source Code Path：`sources/azure/aks_clusters_public_access_disabled/check.py`
