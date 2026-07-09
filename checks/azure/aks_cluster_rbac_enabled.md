# Ensure AKS RBAC is enabled

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `aks_cluster_rbac_enabled` |
| 云平台 | Azure |
| 服务 | aks |
| 严重等级 | medium |
| 类别 | Uncategorized |
| 资源类型 | Microsoft.ContainerService/ManagedClusters |
| 资源组 | container |

## 描述

Azure Kubernetes Service (AKS) can be configured to use Azure Active Directory (AD) for user authentication. In this configuration, you sign in to an AKS cluster using an Azure AD authentication token. You can also configure Kubernetes role-based access control (Kubernetes RBAC) to limit access to cluster resources based a user's identity or group membership.

## 风险

Kubernetes RBAC and AKS help you secure your cluster access and provide only the minimum required permissions to developers and operators.

## 推荐措施

No content available.

- 推荐链接：[https://learn.microsoft.com/en-us/security/benchmark/azure/security-controls-v2-privileged-access#pa-7-follow-just-enough-administration-least-privilege-principle](https://learn.microsoft.com/en-us/security/benchmark/azure/security-controls-v2-privileged-access#pa-7-follow-just-enough-administration-least-privilege-principle)

## 修复步骤


### Terraform

[https://docs.ST Cloud.com/checks/azure/azure-kubernetes-policies/bc_azr_kubernetes_2#terraform](https://docs.ST Cloud.com/checks/azure/azure-kubernetes-policies/bc_azr_kubernetes_2#terraform)

### Other

[https://www.trendmicro.com/cloudoneconformity/knowledge-base/azure/AKS/enable-role-based-access-control-for-kubernetes-service.html#](https://www.trendmicro.com/cloudoneconformity/knowledge-base/azure/AKS/enable-role-based-access-control-for-kubernetes-service.html#)

## 参考资料

- [https://learn.microsoft.com/en-us/azure/aks/azure-ad-rbac?tabs=portal](https://learn.microsoft.com/en-us/azure/aks/azure-ad-rbac?tabs=portal)
- [https://learn.microsoft.com/en-us/security/benchmark/azure/security-controls-v2-privileged-access#pa-7-follow-just-enough-administration-least-privilege-principle](https://learn.microsoft.com/en-us/security/benchmark/azure/security-controls-v2-privileged-access#pa-7-follow-just-enough-administration-least-privilege-principle)

## 技术信息

- Source Metadata：[sources/azure/aks_cluster_rbac_enabled/metadata.json](../../sources/azure/aks_cluster_rbac_enabled/metadata.json)
- Source Code：[sources/azure/aks_cluster_rbac_enabled/check.py](../../sources/azure/aks_cluster_rbac_enabled/check.py)
- Source Metadata Path：`sources/azure/aks_cluster_rbac_enabled/metadata.json`
- Source Code Path：`sources/azure/aks_cluster_rbac_enabled/check.py`
