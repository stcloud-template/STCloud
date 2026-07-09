# Cloud Storage services are protected by VPC Service Controls

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `cloudstorage_uses_vpc_service_controls` |
| 云平台 | GCP |
| 服务 | cloudstorage |
| 严重等级 | medium |
| 类别 | internet-exposed |
| 资源类型 | cloudresourcemanager.googleapis.com/Project |
| 资源组 | governance |

## 描述

**GCP Projects** are evaluated to ensure they have **VPC Service Controls** enabled for Cloud Storage. VPC Service Controls establish security boundaries by restricting access to Cloud Storage resources to specific networks and trusted clients, preventing unauthorized data access and exfiltration.

## 风险

Projects without VPC Service Controls protection for Cloud Storage may be vulnerable to unauthorized data access and exfiltration, even with proper IAM policies in place. VPC Service Controls provide an additional layer of network-level security that restricts API access based on the context of the request.

## 推荐措施

Enable VPC Service Controls for all Cloud Storage buckets by adding their projects to a service perimeter with storage.googleapis.com as a restricted service. This prevents data exfiltration and ensures API calls are only allowed from authorized networks.

## 修复步骤


### Other

1) Open Google Cloud Console → Security → VPC Service Controls
2) Create a new service perimeter or select an existing one
3) Add the relevant GCP projects to the perimeter's protected resources
4) Add 'storage.googleapis.com' to the list of restricted services
5) Configure appropriate ingress and egress rules
6) Save the perimeter configuration

## 参考资料

- [https://www.trendmicro.com/cloudoneconformity/knowledge-base/gcp/CloudStorage/use-vpc-service-controls.html](https://www.trendmicro.com/cloudoneconformity/knowledge-base/gcp/CloudStorage/use-vpc-service-controls.html)
- [https://cloud.google.com/vpc-service-controls/docs/create-service-perimeters](https://cloud.google.com/vpc-service-controls/docs/create-service-perimeters)

## 技术信息

- Source Metadata：[sources/gcp/cloudstorage_uses_vpc_service_controls/metadata.json](../../sources/gcp/cloudstorage_uses_vpc_service_controls/metadata.json)
- Source Code：[sources/gcp/cloudstorage_uses_vpc_service_controls/check.py](../../sources/gcp/cloudstorage_uses_vpc_service_controls/check.py)
- Source Metadata Path：`sources/gcp/cloudstorage_uses_vpc_service_controls/metadata.json`
- Source Code Path：`sources/gcp/cloudstorage_uses_vpc_service_controls/check.py`
