# VM instance attached disks have auto-delete disabled

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `compute_instance_disk_auto_delete_disabled` |
| クラウドプラットフォーム | GCP |
| サービス | compute |
| 重大度 | medium |
| カテゴリ | resilience |
| リソースタイプ | compute.googleapis.com/Instance |

## 説明

This check verifies whether GCP Compute Engine VM instances have **auto-delete** disabled for their attached persistent disks. When auto-delete is enabled, persistent disks are automatically removed when the associated VM instance is deleted, which can lead to unintended data loss.

## リスク

With auto-delete enabled, persistent disks are automatically deleted when the associated VM instance is terminated. This could result in: - **Permanent data loss** if the instance is accidentally or intentionally deleted - **Recovery challenges** for mission-critical workloads - **Compliance violations** where data retention is required

## 推奨事項

Disable `auto-delete` for all persistent disks attached to **production** and **business-critical** VM instances to prevent **accidental data loss**. Regularly review disk configurations to ensure data retention requirements are met.

## 修正手順


### CLI

```text
gcloud compute instances set-disk-auto-delete INSTANCE_NAME --zone=ZONE --no-auto-delete --disk=DISK_NAME
```

### Terraform

```hcl
resource "google_compute_instance" "example_resource" {
  name         = "example-instance"
  machine_type = "e2-medium"
  zone         = "us-central1-a"

  boot_disk {
    # Disable auto-delete for the boot disk
    auto_delete = false

    initialize_params {
      image = "debian-cloud/debian-11"
    }
  }

  attached_disk {
    source      = google_compute_disk.example_disk.id
    # Disable auto-delete for attached disks
    auto_delete = false
  }

  network_interface {
    network = "default"
  }
}
```

### Other

1. Open the Google Cloud Console
2. Navigate to Compute Engine > VM instances
3. Click the target VM instance name
4. Click Edit
5. In the Boot disk section, select 'Keep disk' from the 'When deleting instance' dropdown
6. For Additional disks, click each disk and select 'Keep disk' under 'Deletion rule'
7. Click Save

## 参考資料

- [https://cloud.google.com/compute/docs/disks/add-persistent-disk](https://cloud.google.com/compute/docs/disks/add-persistent-disk)
- [https://www.trendmicro.com/cloudoneconformity/knowledge-base/gcp/ComputeEngine/disable-auto-delete.html](https://www.trendmicro.com/cloudoneconformity/knowledge-base/gcp/ComputeEngine/disable-auto-delete.html)

## 技術情報

- Source Metadata：[sources/gcp/compute_instance_disk_auto_delete_disabled/metadata.json](../../sources/gcp/compute_instance_disk_auto_delete_disabled/metadata.json)
- Source Code：[sources/gcp/compute_instance_disk_auto_delete_disabled/check.py](../../sources/gcp/compute_instance_disk_auto_delete_disabled/check.py)
- Source Metadata Path：`sources/gcp/compute_instance_disk_auto_delete_disabled/metadata.json`
- Source Code Path：`sources/gcp/compute_instance_disk_auto_delete_disabled/check.py`
