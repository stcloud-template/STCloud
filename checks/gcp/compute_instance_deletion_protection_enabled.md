# VM instance has deletion protection enabled

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `compute_instance_deletion_protection_enabled` |
| クラウドプラットフォーム | GCP |
| サービス | compute |
| 重大度 | medium |
| カテゴリ | resilience |
| リソースタイプ | compute.googleapis.com/Instance |
| リソースグループ | compute |

## 説明

This check verifies whether GCP Compute Engine VM instances have **deletion protection** enabled to prevent accidental termination of production or critical workloads.

## リスク

Without deletion protection enabled, VM instances are vulnerable to **accidental deletion** by users with sufficient permissions. This could result in: - **Service disruption** and downtime for critical applications - **Data loss** if persistent disks are also deleted - **Recovery delays** while recreating instances and restoring configurations

## 推奨事項

Enable deletion protection on all production and business-critical VM instances to prevent accidental termination. Regularly review instances to ensure critical workloads are protected.

## 修正手順


### CLI

```text
gcloud compute instances update INSTANCE_NAME --deletion-protection --zone=ZONE
```

### Terraform

```hcl
resource "google_compute_instance" "example_resource" {
  name         = "example-instance"
  machine_type = "e2-medium"
  zone         = "us-central1-a"

  # Enable deletion protection
  deletion_protection = true

  boot_disk {
    initialize_params {
      image = "debian-cloud/debian-11"
    }
  }

  network_interface {
    network = "default"
  }
}
```

### Other

1. Open the Google Cloud Console
2. Navigate to Compute Engine > VM instances
3. Select the target VM instance
4. Click Edit
5. Under Deletion protection, check the box to enable
6. Click Save

## 参考資料

- [https://cloud.google.com/compute/docs/instances/preventing-accidental-vm-deletion](https://cloud.google.com/compute/docs/instances/preventing-accidental-vm-deletion)
- [https://www.trendmicro.com/cloudoneconformity/knowledge-base/gcp/ComputeEngine/enable-deletion-protection.html](https://www.trendmicro.com/cloudoneconformity/knowledge-base/gcp/ComputeEngine/enable-deletion-protection.html)

## 技術情報

- Source Metadata：[sources/gcp/compute_instance_deletion_protection_enabled/metadata.json](../../sources/gcp/compute_instance_deletion_protection_enabled/metadata.json)
- Source Code：[sources/gcp/compute_instance_deletion_protection_enabled/check.py](../../sources/gcp/compute_instance_deletion_protection_enabled/check.py)
- Source Metadata Path：`sources/gcp/compute_instance_deletion_protection_enabled/metadata.json`
- Source Code Path：`sources/gcp/compute_instance_deletion_protection_enabled/check.py`
