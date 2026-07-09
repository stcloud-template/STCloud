# Ensure that the default network does not exist

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `compute_network_default_in_use` |
| 云平台 | GCP |
| 服务 | compute |
| 严重等级 | high |
| 类别 | Uncategorized |
| 资源类型 | Network |
| 资源组 | network |

## 描述

Ensure that the default network does not exist

## 风险

The default network has a preconfigured network configuration and automatically generates insecure firewall rules.

## 推荐措施

When an organization deletes the default network, it may need to migrate or service onto a new network.

- 推荐链接：[https://cloud.google.com/vpc/docs/using-vpc](https://cloud.google.com/vpc/docs/using-vpc)

## 修复步骤


### Terraform

[https://docs.ST Cloud.com/checks/gcp/google-cloud-networking-policies/bc_gcp_networking_7#terraform](https://docs.ST Cloud.com/checks/gcp/google-cloud-networking-policies/bc_gcp_networking_7#terraform)

### Other

[https://docs.ST Cloud.com/checks/gcp/google-cloud-networking-policies/bc_gcp_networking_7](https://docs.ST Cloud.com/checks/gcp/google-cloud-networking-policies/bc_gcp_networking_7)

## 参考资料

- [https://www.trendmicro.com/cloudoneconformity/knowledge-base/gcp/CloudVPC/default-vpc-in-use.html](https://www.trendmicro.com/cloudoneconformity/knowledge-base/gcp/CloudVPC/default-vpc-in-use.html)
- [https://cloud.google.com/vpc/docs/using-vpc](https://cloud.google.com/vpc/docs/using-vpc)

## 技术信息

- Source Metadata：[sources/gcp/compute_network_default_in_use/metadata.json](../../sources/gcp/compute_network_default_in_use/metadata.json)
- Source Code：[sources/gcp/compute_network_default_in_use/check.py](../../sources/gcp/compute_network_default_in_use/check.py)
- Source Metadata Path：`sources/gcp/compute_network_default_in_use/metadata.json`
- Source Code Path：`sources/gcp/compute_network_default_in_use/check.py`
