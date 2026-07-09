# Compute Engine disk image is not publicly shared

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `compute_image_not_publicly_shared` |
| 云平台 | GCP |
| 服务 | compute |
| 严重等级 | medium |
| 类别 | internet-exposed |
| 资源类型 | compute.googleapis.com/Image |
| 资源组 | compute |

## 描述

Custom disk images should not be shared publicly with **allAuthenticatedUsers**. Note: Per Google Cloud API restrictions, **allUsers** cannot be assigned to Compute Engine images. The security concern is **allAuthenticatedUsers**, which grants access to anyone with a Google account. Publicly shared disk images can expose application snapshots and sensitive data to anyone with a Google Cloud account, potentially leading to unauthorized access and data breaches.

## 风险

Publicly shared disk images can expose **sensitive data** and application configurations to unauthorized users. - Any authenticated GCP user can access the image content - Could lead to **data breaches** if images contain secrets or proprietary code - Attackers may use exposed images to understand application architecture

## 推荐措施

Restrict access to custom disk images by removing the **allAuthenticatedUsers** IAM binding. Apply the principle of least privilege by granting access only to specific users, groups, or service accounts that require it.

## 修复步骤


### CLI

```text
gcloud compute images remove-iam-policy-binding IMAGE_NAME --member='allAuthenticatedUsers' --role='ROLE_NAME'
```

### Terraform

```hcl
resource "google_compute_image_iam_binding" "example_resource" {
  project = "your-project-id"
  image   = "your-image-name"
  role    = "roles/compute.imageUser"
  # Remove allAuthenticatedUsers and grant access only to specific members
  members = [
    "user:specific-user@example.com",
  ]
}
```

### Other

1. Go to the GCP Console
2. Navigate to Compute Engine > Images
3. Select the disk image
4. Click on the INFO PANEL to view permissions
5. Remove **allAuthenticatedUsers** bindings
6. Click Save

## 参考资料

- [https://cloud.google.com/compute/docs/images/managing-access-custom-images](https://cloud.google.com/compute/docs/images/managing-access-custom-images)
- [https://www.trendmicro.com/cloudoneconformity/knowledge-base/gcp/ComputeEngine/publicly-shared-disk-images.html](https://www.trendmicro.com/cloudoneconformity/knowledge-base/gcp/ComputeEngine/publicly-shared-disk-images.html)

## 技术信息

- Source Metadata：[sources/gcp/compute_image_not_publicly_shared/metadata.json](../../sources/gcp/compute_image_not_publicly_shared/metadata.json)
- Source Code：[sources/gcp/compute_image_not_publicly_shared/check.py](../../sources/gcp/compute_image_not_publicly_shared/check.py)
- Source Metadata Path：`sources/gcp/compute_image_not_publicly_shared/metadata.json`
- Source Code Path：`sources/gcp/compute_image_not_publicly_shared/check.py`
