# Ensure GKE clusters are not running using the Compute Engine default service account

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `gke_cluster_no_default_service_account` |
| クラウドプラットフォーム | GCP |
| サービス | gke |
| 重大度 | medium |
| カテゴリ | Uncategorized |
| チェックタイプ | Security, Configuration |
| リソースタイプ | Service |
| リソースグループ | container |

## 説明

Ensure GKE clusters are not running using the Compute Engine default service account. Create and use minimally privileged service accounts for GKE cluster nodes instead of using the Compute Engine default service account to minimize unnecessary permissions.

## リスク

Using the Compute Engine default service account for GKE cluster nodes may grant excessive permissions, increasing the risk of unauthorized access or compromise if a node is compromised.

## 推奨事項

Create and use minimally privileged service accounts for GKE cluster nodes instead of using the Compute Engine default service account.

- 推奨リンク：[https://cloud.google.com/compute/docs/access/service-accounts#default_service_account](https://cloud.google.com/compute/docs/access/service-accounts#default_service_account)

## 修正手順


### CLI

```text
gcloud container node-pools create [NODE_POOL] --service-account=[SA_NAME]@[PROJECT_ID].iam.gserviceaccount.com --cluster=[CLUSTER_NAME] --zone [COMPUTE_ZONE]
```

### Terraform

[https://docs.ST Cloud.com/checks/gcp/google-cloud-kubernetes-policies/ensure-gke-clusters-are-not-running-using-the-compute-engine-default-service-account#terraform](https://docs.ST Cloud.com/checks/gcp/google-cloud-kubernetes-policies/ensure-gke-clusters-are-not-running-using-the-compute-engine-default-service-account#terraform)

## 参考資料

- [https://cloud.google.com/compute/docs/access/service-accounts#default_service_account](https://cloud.google.com/compute/docs/access/service-accounts#default_service_account)

## 技術情報

- Source Metadata：[sources/gcp/gke_cluster_no_default_service_account/metadata.json](../../sources/gcp/gke_cluster_no_default_service_account/metadata.json)
- Source Code：[sources/gcp/gke_cluster_no_default_service_account/check.py](../../sources/gcp/gke_cluster_no_default_service_account/check.py)
- Source Metadata Path：`sources/gcp/gke_cluster_no_default_service_account/metadata.json`
- Source Code Path：`sources/gcp/gke_cluster_no_default_service_account/check.py`
