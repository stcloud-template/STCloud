# Check for Virtual Machine Instances with Public IP Addresses

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `compute_instance_public_ip` |
| 云平台 | GCP |
| 服务 | compute |
| 严重等级 | high |
| 类别 | internet-exposed |
| 资源类型 | VMInstance |
| 资源组 | compute |

## 描述

Check for Virtual Machine Instances with Public IP Addresses

## 风险

To reduce your attack surface, Compute instances should not have public IP addresses. Instead, instances should be configured behind load balancers, to minimize the instance's exposure to the internet.

## 推荐措施

Ensure that your Google Compute Engine instances are not configured to have external IP addresses in order to minimize their exposure to the Internet.

- 推荐链接：[https://cloud.google.com/compute/docs/instances/connecting-to-instance](https://cloud.google.com/compute/docs/instances/connecting-to-instance)

## 修复步骤


### Terraform

[https://docs.ST Cloud.com/checks/gcp/google-cloud-public-policies/bc_gcp_public_2#terraform](https://docs.ST Cloud.com/checks/gcp/google-cloud-public-policies/bc_gcp_public_2#terraform)

### Other

[https://docs.ST Cloud.com/checks/gcp/google-cloud-public-policies/bc_gcp_public_2](https://docs.ST Cloud.com/checks/gcp/google-cloud-public-policies/bc_gcp_public_2)

## 参考资料

- [https://cloud.google.com/compute/docs/instances/connecting-to-instance](https://cloud.google.com/compute/docs/instances/connecting-to-instance)

## 技术信息

- Source Metadata：[sources/gcp/compute_instance_public_ip/metadata.json](../../sources/gcp/compute_instance_public_ip/metadata.json)
- Source Code：[sources/gcp/compute_instance_public_ip/check.py](../../sources/gcp/compute_instance_public_ip/check.py)
- Source Metadata Path：`sources/gcp/compute_instance_public_ip/metadata.json`
- Source Code Path：`sources/gcp/compute_instance_public_ip/check.py`
