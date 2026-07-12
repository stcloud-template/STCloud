# Ensure AKS RBAC is enabled

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `aks_cluster_rbac_enabled` |
| クラウドプラットフォーム | Azure |
| サービス | aks |
| 重大度 | medium |
| カテゴリ | Uncategorized |
| リソースタイプ | Microsoft.ContainerService/ManagedClusters |
| リソースグループ | container |

## 説明

Azure Kubernetes Service (AKS) can be configured to use Azure Active Directory (AD) for user authentication. In this configuration, you sign in to an AKS cluster using an Azure AD authentication token. You can also configure Kubernetes role-based access control (Kubernetes RBAC) to limit access to cluster resources based a user's identity or group membership.

## リスク

Kubernetes RBAC and AKS help you secure your cluster access and provide only the minimum required permissions to developers and operators.

## 推奨事項

No content available.

- 推奨リンク：[https://learn.microsoft.com/en-us/security/benchmark/azure/security-controls-v2-privileged-access#pa-7-follow-just-enough-administration-least-privilege-principle](https://learn.microsoft.com/en-us/security/benchmark/azure/security-controls-v2-privileged-access#pa-7-follow-just-enough-administration-least-privilege-principle)

## 修正手順


### Terraform

[https://docs.ST Cloud.com/checks/azure/azure-kubernetes-policies/bc_azr_kubernetes_2#terraform](https://docs.ST Cloud.com/checks/azure/azure-kubernetes-policies/bc_azr_kubernetes_2#terraform)

### Other

[https://www.trendmicro.com/cloudoneconformity/knowledge-base/azure/AKS/enable-role-based-access-control-for-kubernetes-service.html#](https://www.trendmicro.com/cloudoneconformity/knowledge-base/azure/AKS/enable-role-based-access-control-for-kubernetes-service.html#)

## 参考資料

- [https://learn.microsoft.com/en-us/azure/aks/azure-ad-rbac?tabs=portal](https://learn.microsoft.com/en-us/azure/aks/azure-ad-rbac?tabs=portal)
- [https://learn.microsoft.com/en-us/security/benchmark/azure/security-controls-v2-privileged-access#pa-7-follow-just-enough-administration-least-privilege-principle](https://learn.microsoft.com/en-us/security/benchmark/azure/security-controls-v2-privileged-access#pa-7-follow-just-enough-administration-least-privilege-principle)

## 技術情報

- Source Metadata：[sources/azure/aks_cluster_rbac_enabled/metadata.json](../../sources/azure/aks_cluster_rbac_enabled/metadata.json)
- Source Code：[sources/azure/aks_cluster_rbac_enabled/check.py](../../sources/azure/aks_cluster_rbac_enabled/check.py)
- Source Metadata Path：`sources/azure/aks_cluster_rbac_enabled/metadata.json`
- Source Code Path：`sources/azure/aks_cluster_rbac_enabled/check.py`
