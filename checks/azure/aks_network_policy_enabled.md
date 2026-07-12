# Ensure Network Policy is Enabled and set as appropriate

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `aks_network_policy_enabled` |
| クラウドプラットフォーム | Azure |
| サービス | aks |
| 重大度 | medium |
| カテゴリ | Uncategorized |
| リソースタイプ | Microsoft.ContainerService/managedClusters |
| リソースグループ | container |

## 説明

When you run modern, microservices-based applications in Kubernetes, you often want to control which components can communicate with each other. The principle of least privilege should be applied to how traffic can flow between pods in an Azure Kubernetes Service (AKS) cluster. Let's say you likely want to block traffic directly to back-end applications. The Network Policy feature in Kubernetes lets you define rules for ingress and egress traffic between pods in a cluster.

## リスク

All pods in an AKS cluster can send and receive traffic without limitations, by default. To improve security, you can define rules that control the flow of traffic. Back-end applications are often only exposed to required front-end services, for example. Or, database components are only accessible to the application tiers that connect to them. Network Policy is a Kubernetes specification that defines access policies for communication between Pods. Using Network Policies, you define an ordered set of rules to send and receive traffic and apply them to a collection of pods that match one or more label selectors. These network policy rules are defined as YAML manifests. Network policies can be included as part of a wider manifest that also creates a deployment or service.

## 推奨事項

No content available.

- 推奨リンク：[https://learn.microsoft.com/en-us/azure/aks/use-network-policies](https://learn.microsoft.com/en-us/azure/aks/use-network-policies)

## 修正手順


### Terraform

[https://docs.ST Cloud.com/checks/azure/azure-kubernetes-policies/bc_azr_kubernetes_4#terraform](https://docs.ST Cloud.com/checks/azure/azure-kubernetes-policies/bc_azr_kubernetes_4#terraform)

## 参考資料

- [https://learn.microsoft.com/en-us/security/benchmark/azure/security-controls-v2-network-security#ns-2-connect-private-networks-together](https://learn.microsoft.com/en-us/security/benchmark/azure/security-controls-v2-network-security#ns-2-connect-private-networks-together)
- [https://learn.microsoft.com/en-us/azure/aks/use-network-policies](https://learn.microsoft.com/en-us/azure/aks/use-network-policies)

## 技術情報

- Source Metadata：[sources/azure/aks_network_policy_enabled/metadata.json](../../sources/azure/aks_network_policy_enabled/metadata.json)
- Source Code：[sources/azure/aks_network_policy_enabled/check.py](../../sources/azure/aks_network_policy_enabled/check.py)
- Source Metadata Path：`sources/azure/aks_network_policy_enabled/metadata.json`
- Source Code Path：`sources/azure/aks_network_policy_enabled/check.py`
