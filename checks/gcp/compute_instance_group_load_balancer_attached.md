# Managed Instance Group is attached to a load balancer

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `compute_instance_group_load_balancer_attached` |
| クラウドプラットフォーム | GCP |
| サービス | compute |
| 重大度 | low |
| カテゴリ | resilience |
| リソースタイプ | compute.googleapis.com/InstanceGroupManager |
| リソースグループ | compute |

## 説明

Managed Instance Groups (MIGs) should be attached to load balancers via backend services to enable traffic distribution across instances. Load balancers provide health checking, autoscaling integration, and high availability features that are essential for production workloads.

## リスク

Without load balancer attachment, MIGs cannot distribute traffic evenly across instances, which impacts: - **Application availability** - No automatic failover when instances become unhealthy - **Scalability** - Autoscaling benefits are limited without proper traffic distribution - **Performance** - Uneven load distribution can cause hotspots and degraded user experience

## 推奨事項

Attach Managed Instance Groups to load balancers using backend services to enable traffic distribution, health checking, and seamless autoscaling. This ensures high availability and optimal performance for production workloads.

## 修正手順


### CLI

```text
gcloud compute backend-services add-backend BACKEND_SERVICE_NAME --instance-group=INSTANCE_GROUP_NAME --instance-group-zone=ZONE --global
```

### Terraform

```hcl
resource "google_compute_backend_service" "example" {
  name        = "example-backend-service"
  protocol    = "HTTP"
  port_name   = "http"
  timeout_sec = 30

  # Attach MIG as backend
  backend {
    group = google_compute_instance_group_manager.example.instance_group
  }

  health_checks = [google_compute_health_check.example.id]
}
```

### Other

1. Navigate to Network Services > Load balancing
2. Create or edit an HTTP(S) load balancer
3. Configure the backend service
4. Select the target MIG from the instance group dropdown
5. Configure port and balancing mode
6. Complete the load balancer setup

## 参考資料

- [https://cloud.google.com/compute/docs/instance-groups](https://cloud.google.com/compute/docs/instance-groups)
- [https://cloud.google.com/load-balancing/docs/backend-service](https://cloud.google.com/load-balancing/docs/backend-service)
- [https://www.trendmicro.com/cloudoneconformity/knowledge-base/gcp/ComputeEngine/mig-load-balancer-check.html](https://www.trendmicro.com/cloudoneconformity/knowledge-base/gcp/ComputeEngine/mig-load-balancer-check.html)

## 技術情報

- Source Metadata：[sources/gcp/compute_instance_group_load_balancer_attached/metadata.json](../../sources/gcp/compute_instance_group_load_balancer_attached/metadata.json)
- Source Code：[sources/gcp/compute_instance_group_load_balancer_attached/check.py](../../sources/gcp/compute_instance_group_load_balancer_attached/check.py)
- Source Metadata Path：`sources/gcp/compute_instance_group_load_balancer_attached/metadata.json`
- Source Code Path：`sources/gcp/compute_instance_group_load_balancer_attached/check.py`
