# VM instance has a single network interface

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `compute_instance_single_network_interface` |
| 云平台 | GCP |
| 服务 | compute |
| 严重等级 | medium |
| 类别 | trust-boundaries |
| 资源类型 | compute.googleapis.com/Instance |
| 资源组 | compute |

## 描述

VM instances should be configured with only **one network interface** unless multiple interfaces are explicitly required for complex network configurations. Multiple network interfaces expand the attack surface and create additional network pathways that may be exploited.

## 风险

Multiple network interfaces on a VM instance can: - **Expand attack surface** by providing additional entry points for unauthorized access - **Create unintended network paths** that bypass security controls - **Increase management complexity** leading to potential misconfigurations

## 推荐措施

Configure VM instances with only the **minimum network connectivity** required for their intended purpose. Review instances with multiple network interfaces and consolidate to a single interface unless multi-NIC configuration is explicitly required for network appliance or routing purposes.

## 修复步骤


### Terraform

```hcl
resource "google_compute_instance" "example_resource" {
  name         = "example-instance"
  machine_type = "e2-medium"
  zone         = "us-central1-a"

  boot_disk {
    initialize_params {
      image = "debian-cloud/debian-11"
    }
  }

  # Only one network interface
  network_interface {
    network = "default"
  }
}
```

### Other

1. Create a machine image from the non-compliant VM instance
2. Create a new VM instance from the machine image with only one network interface
3. Verify the new instance is functioning correctly
4. Delete the original multi-interface instance

## 参考资料

- [https://www.trendmicro.com/cloudoneconformity/knowledge-base/gcp/ComputeEngine/vms-with-multiple-enis.html](https://www.trendmicro.com/cloudoneconformity/knowledge-base/gcp/ComputeEngine/vms-with-multiple-enis.html)
- [https://cloud.google.com/vpc/docs/multiple-interfaces-concepts](https://cloud.google.com/vpc/docs/multiple-interfaces-concepts)

## 技术信息

- Source Metadata：[sources/gcp/compute_instance_single_network_interface/metadata.json](../../sources/gcp/compute_instance_single_network_interface/metadata.json)
- Source Code：[sources/gcp/compute_instance_single_network_interface/check.py](../../sources/gcp/compute_instance_single_network_interface/check.py)
- Source Metadata Path：`sources/gcp/compute_instance_single_network_interface/metadata.json`
- Source Code Path：`sources/gcp/compute_instance_single_network_interface/check.py`
