# Managed Instance Group has autohealing enabled with a valid health check

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `compute_instance_group_autohealing_enabled` |
| クラウドプラットフォーム | GCP |
| サービス | compute |
| 重大度 | high |
| カテゴリ | resilience |
| リソースタイプ | compute.googleapis.com/InstanceGroupManager |
| リソースグループ | compute |

## 説明

Managed Instance Groups (MIGs) should have **autohealing** enabled with a valid health check configured. Autohealing automatically recreates unhealthy instances based on application-level health checks, ensuring continuous availability.

## リスク

Without autohealing, MIGs cannot detect application-level failures such as crashes, freezes, or memory issues. Instances that are technically running but experiencing problems will remain undetected and unreplaced, leading to: - **Service degradation** from unhealthy instances - **Extended downtime** during application failures - **Manual intervention** required to detect and replace failed instances

## 推奨事項

Enable autohealing on all Managed Instance Groups by configuring a health check that validates application-level health. Set an appropriate initial delay to allow instances time to start before health checks begin.

## 修正手順


### CLI

```text
gcloud compute instance-groups managed update INSTANCE_GROUP_NAME --health-check=HEALTH_CHECK_NAME --initial-delay=300 --zone=ZONE
```

### Terraform

```hcl
resource "google_compute_instance_group_manager" "example" {
  name               = "example-mig"
  base_instance_name = "example"
  zone               = "us-central1-a"
  target_size        = 2

  version {
    instance_template = google_compute_instance_template.example.id
  }

  # Enable autohealing with health check
  auto_healing_policies {
    health_check      = google_compute_health_check.example.id
    initial_delay_sec = 300
  }
}

resource "google_compute_health_check" "example" {
  name               = "example-health-check"
  check_interval_sec = 10
  timeout_sec        = 5

  http_health_check {
    port = 80
  }
}
```

### Other

1. Navigate to Compute Engine > Instance groups
2. Select the Managed Instance Group
3. Click 'Edit'
4. Under 'Autohealing', click 'Add health check'
5. Select or create a health check
6. Set an appropriate initial delay (e.g., 300 seconds)
7. Click 'Save'

## 参考資料

- [https://cloud.google.com/compute/docs/instance-groups/autohealing-instances-in-migs](https://cloud.google.com/compute/docs/instance-groups/autohealing-instances-in-migs)
- [https://www.trendmicro.com/cloudoneconformity/knowledge-base/gcp/ComputeEngine/enable-instance-group-autohealing.html](https://www.trendmicro.com/cloudoneconformity/knowledge-base/gcp/ComputeEngine/enable-instance-group-autohealing.html)

## 技術情報

- Source Metadata：[sources/gcp/compute_instance_group_autohealing_enabled/metadata.json](../../sources/gcp/compute_instance_group_autohealing_enabled/metadata.json)
- Source Code：[sources/gcp/compute_instance_group_autohealing_enabled/check.py](../../sources/gcp/compute_instance_group_autohealing_enabled/check.py)
- Source Metadata Path：`sources/gcp/compute_instance_group_autohealing_enabled/metadata.json`
- Source Code Path：`sources/gcp/compute_instance_group_autohealing_enabled/check.py`
