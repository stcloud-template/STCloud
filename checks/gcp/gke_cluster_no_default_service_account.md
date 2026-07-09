# Ensure GKE clusters are not running using the Compute Engine default service account

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `gke_cluster_no_default_service_account` |
| 云平台 | GCP |
| 服务 | gke |
| 严重等级 | medium |
| 类别 | Uncategorized |
| 检查类型 | Security, Configuration |
| 资源类型 | Service |
| 资源组 | container |

## 描述

Ensure GKE clusters are not running using the Compute Engine default service account. Create and use minimally privileged service accounts for GKE cluster nodes instead of using the Compute Engine default service account to minimize unnecessary permissions.

## 风险

Using the Compute Engine default service account for GKE cluster nodes may grant excessive permissions, increasing the risk of unauthorized access or compromise if a node is compromised.

## 推荐措施

Create and use minimally privileged service accounts for GKE cluster nodes instead of using the Compute Engine default service account.

- 推荐链接：[https://cloud.google.com/compute/docs/access/service-accounts#default_service_account](https://cloud.google.com/compute/docs/access/service-accounts#default_service_account)

## 修复步骤


### CLI

```text
gcloud container node-pools create [NODE_POOL] --service-account=[SA_NAME]@[PROJECT_ID].iam.gserviceaccount.com --cluster=[CLUSTER_NAME] --zone [COMPUTE_ZONE]
```

### Terraform

[https://docs.ST Cloud.com/checks/gcp/google-cloud-kubernetes-policies/ensure-gke-clusters-are-not-running-using-the-compute-engine-default-service-account#terraform](https://docs.ST Cloud.com/checks/gcp/google-cloud-kubernetes-policies/ensure-gke-clusters-are-not-running-using-the-compute-engine-default-service-account#terraform)

## 参考资料

- [https://cloud.google.com/compute/docs/access/service-accounts#default_service_account](https://cloud.google.com/compute/docs/access/service-accounts#default_service_account)

## 技术信息

- Source Metadata：[sources/gcp/gke_cluster_no_default_service_account/metadata.json](../../sources/gcp/gke_cluster_no_default_service_account/metadata.json)
- Source Code：[sources/gcp/gke_cluster_no_default_service_account/check.py](../../sources/gcp/gke_cluster_no_default_service_account/check.py)
- Source Metadata Path：`sources/gcp/gke_cluster_no_default_service_account/metadata.json`
- Source Code Path：`sources/gcp/gke_cluster_no_default_service_account/check.py`
