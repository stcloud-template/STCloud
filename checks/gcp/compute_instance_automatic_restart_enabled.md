# Compute Engine VM instances have Automatic Restart enabled

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `compute_instance_automatic_restart_enabled` |
| クラウドプラットフォーム | GCP |
| サービス | compute |
| 重大度 | medium |
| カテゴリ | resilience |
| リソースタイプ | compute.googleapis.com/Instance |
| リソースグループ | compute |

## 説明

**Google Compute Engine virtual machine instances** are evaluated to ensure that **Automatic Restart** is enabled. This feature allows the Google Cloud Compute Engine service to automatically restart VM instances when they are terminated due to non-user-initiated reasons such as maintenance events, hardware failures, or software failures.

## リスク

VM instances without Automatic Restart enabled will not recover automatically from host maintenance events or unexpected failures, potentially leading to prolonged service downtime and requiring manual intervention to restore services.

## 推奨事項

Enable the Automatic Restart feature for Compute Engine VM instances to enhance system reliability by automatically recovering from crashes or system-initiated terminations. This setting does not interfere with user-initiated shutdowns or stops.

## 修正手順


### CLI

```text
gcloud compute instances update <INSTANCE_NAME> --restart-on-failure --zone=<ZONE>
```

### Terraform

```hcl
# Example: enable Automatic Restart for a Compute Engine VM instance
resource "google_compute_instance" "example" {
  name         = var.instance_name
  machine_type = var.machine_type
  zone         = var.zone

  scheduling {
    automatic_restart   = true
    on_host_maintenance = "MIGRATE"
  }
}
```

### Other

1) Open Google Cloud Console → Compute Engine → VM instances
2) Click on the instance name to view details
3) Click 'Edit' at the top of the page
4) Under 'Availability policies', set 'Automatic restart' to 'On (recommended)'
5) Click 'Save' at the bottom of the page

## 参考資料

- [https://www.trendmicro.com/cloudoneconformity/knowledge-base/gcp/ComputeEngine/enable-automatic-restart.html](https://www.trendmicro.com/cloudoneconformity/knowledge-base/gcp/ComputeEngine/enable-automatic-restart.html)
- [https://cloud.google.com/compute/docs/instances/setting-instance-scheduling-options](https://cloud.google.com/compute/docs/instances/setting-instance-scheduling-options)

## 技術情報

- Source Metadata：[sources/gcp/compute_instance_automatic_restart_enabled/metadata.json](../../sources/gcp/compute_instance_automatic_restart_enabled/metadata.json)
- Source Code：[sources/gcp/compute_instance_automatic_restart_enabled/check.py](../../sources/gcp/compute_instance_automatic_restart_enabled/check.py)
- Source Metadata Path：`sources/gcp/compute_instance_automatic_restart_enabled/metadata.json`
- Source Code Path：`sources/gcp/compute_instance_automatic_restart_enabled/check.py`
