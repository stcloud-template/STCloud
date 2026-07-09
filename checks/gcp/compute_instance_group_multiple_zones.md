# Ensure Managed Instance Groups span multiple zones for high availability

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `compute_instance_group_multiple_zones` |
| 云平台 | GCP |
| 服务 | compute |
| 严重等级 | low |
| 类别 | resilience |
| 资源类型 | compute.googleapis.com/InstanceGroupManager |
| 资源组 | compute |

## 描述

Managed Instance Groups (MIGs) should be configured for multi-zone deployments to ensure high availability and fault tolerance. A multi-zone MIG distributes instances across multiple zones within a region, protecting applications from zonal failures.

## 风险

Running a MIG in a single zone creates a single point of failure. If that zone experiences an outage, all instances in the group become unavailable, resulting in application downtime during zonal failures, no automatic failover to healthy zones, and reduced resilience against infrastructure issues.

## 推荐措施

Use regional managed instance groups instead of zonal MIGs to distribute instances across multiple zones. This provides automatic failover and load distribution, ensuring high availability for production workloads.

## 修复步骤


### CLI

```text
gcloud compute instance-groups managed create INSTANCE_GROUP_NAME --region=REGION --template=INSTANCE_TEMPLATE --size=TARGET_SIZE --zones=ZONE1,ZONE2,ZONE3
```

### Terraform

```hcl
# Create a regional MIG that spans multiple zones
resource "google_compute_region_instance_group_manager" "example" {
  name               = "example-mig"
  region             = "us-central1"
  base_instance_name = "example"
  target_size        = 3

  version {
    instance_template = google_compute_instance_template.example.id
  }

  # Distribute instances across multiple zones
  distribution_policy_zones = ["us-central1-a", "us-central1-b", "us-central1-c"]
}
```

### Other

1. Navigate to Compute Engine > Instance groups
2. Click 'Create instance group'
3. Select 'New managed instance group (stateless)'
4. For 'Location', select 'Multiple zones'
5. Choose the target region and zones
6. Configure the instance template and target size
7. Click 'Create'

## 参考资料

- [https://cloud.google.com/compute/docs/instance-groups/regional-migs](https://cloud.google.com/compute/docs/instance-groups/regional-migs)
- [https://cloud.google.com/compute/docs/instance-groups/distributing-instances-with-regional-instance-groups](https://cloud.google.com/compute/docs/instance-groups/distributing-instances-with-regional-instance-groups)

## 技术信息

- Source Metadata：[sources/gcp/compute_instance_group_multiple_zones/metadata.json](../../sources/gcp/compute_instance_group_multiple_zones/metadata.json)
- Source Code：[sources/gcp/compute_instance_group_multiple_zones/check.py](../../sources/gcp/compute_instance_group_multiple_zones/check.py)
- Source Metadata Path：`sources/gcp/compute_instance_group_multiple_zones/metadata.json`
- Source Code Path：`sources/gcp/compute_instance_group_multiple_zones/check.py`
