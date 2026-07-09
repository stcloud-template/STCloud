# VM instance is not configured as preemptible or Spot VM

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `compute_instance_preemptible_vm_disabled` |
| 云平台 | GCP |
| 服务 | compute |
| 严重等级 | medium |
| 类别 | resilience |
| 资源类型 | compute.googleapis.com/Instance |
| 资源组 | compute |

## 描述

This check verifies that VM instances are not configured as **preemptible** or **Spot VMs**. Both preemptible and Spot VMs can be terminated by Google at any time when resources are needed elsewhere, making them unsuitable for production and business-critical workloads. Spot VMs are the newer version of preemptible VMs and are Google's recommended approach for interruptible workloads.

## 风险

Preemptible and Spot VMs may be **terminated at any time** by Google Cloud, causing: - **Service disruptions** for production workloads - **Data loss** if workloads are not fault-tolerant - **Availability issues** for business-critical applications They are designed for batch jobs and fault-tolerant workloads only.

## 推荐措施

Use standard provisioning model for production and business-critical VM instances. Preemptible and Spot VMs should only be used for fault-tolerant, batch processing, or non-critical workloads that can handle interruptions.

## 修复步骤


### Terraform

```hcl
resource "google_compute_instance" "example_resource" {
  name         = "example-instance"
  machine_type = "e2-medium"
  zone         = "us-central1-a"

  scheduling {
    # Use standard provisioning model for production workloads (not Spot)
    provisioning_model = "STANDARD"
    # Also ensure preemptible is false (legacy field)
    preemptible = false
  }
}
```

### Other

1. Go to Compute Engine console
2. Select the preemptible or Spot VM instance
3. Create a machine image from the instance
4. Create a new instance from the machine image
5. During creation, set **VM provisioning model** to **Standard** (not Spot)
6. Delete the original preemptible or Spot VM instance

## 参考资料

- [https://cloud.google.com/compute/docs/instances/preemptible](https://cloud.google.com/compute/docs/instances/preemptible)
- [https://cloud.google.com/compute/docs/instances/spot](https://cloud.google.com/compute/docs/instances/spot)
- [https://www.trendmicro.com/cloudoneconformity/knowledge-base/gcp/ComputeEngine/disable-preemptibility.html](https://www.trendmicro.com/cloudoneconformity/knowledge-base/gcp/ComputeEngine/disable-preemptibility.html)

## 技术信息

- Source Metadata：[sources/gcp/compute_instance_preemptible_vm_disabled/metadata.json](../../sources/gcp/compute_instance_preemptible_vm_disabled/metadata.json)
- Source Code：[sources/gcp/compute_instance_preemptible_vm_disabled/check.py](../../sources/gcp/compute_instance_preemptible_vm_disabled/check.py)
- Source Metadata Path：`sources/gcp/compute_instance_preemptible_vm_disabled/metadata.json`
- Source Code Path：`sources/gcp/compute_instance_preemptible_vm_disabled/check.py`
