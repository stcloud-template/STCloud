# Enable VPC Flow Logs for VPC Subnets

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `compute_subnet_flow_logs_enabled` |
| クラウドプラットフォーム | GCP |
| サービス | compute |
| 重大度 | medium |
| カテゴリ | Uncategorized |
| リソースタイプ | Subnet |
| リソースグループ | network |

## 説明

Ensure that VPC Flow Logs is enabled for every subnet created within your production Virtual Private Cloud (VPC) network. Flow Logs is a logging feature that enables users to capture information about the IP traffic (accepted, rejected, or all traffic) going to and from the network interfaces (ENIs) available within your VPC subnets.

## リスク

By default, the VPC Flow Logs feature is disabled when a new VPC network subnet is created. Once enabled, VPC Flow Logs will start collecting network traffic data to and from your Virtual Private Cloud (VPC) subnets, logging data that can be useful for understanding network usage, network traffic expense optimization, network forensics, and real-time security analysis. To enhance Google Cloud VPC network visibility and security it is strongly recommended to enable Flow Logs for every business-critical or production VPC subnet.

## 推奨事項

Ensure that VPC Flow Logs is enabled for every subnet created within your production Virtual Private Cloud (VPC) network. Flow Logs is a logging feature that enables users to capture information about the IP traffic (accepted, rejected, or all traffic) going to and from the network interfaces (ENIs) available within your VPC subnets.

- 推奨リンク：[https://cloud.google.com/vpc/docs/using-flow-logs#enabling_vpc_flow_logging](https://cloud.google.com/vpc/docs/using-flow-logs#enabling_vpc_flow_logging)

## 修正手順


### CLI

```text
gcloud compute networks subnets update [SUBNET_NAME] --region [REGION] --enable-flow-logs
```

### Terraform

[https://docs.ST Cloud.com/checks/gcp/logging-policies-1/bc_gcp_logging_1#terraform](https://docs.ST Cloud.com/checks/gcp/logging-policies-1/bc_gcp_logging_1#terraform)

### Other

[https://www.trendmicro.com/cloudoneconformity/knowledge-base/gcp/CloudVPC/enable-vpc-flow-logs.html](https://www.trendmicro.com/cloudoneconformity/knowledge-base/gcp/CloudVPC/enable-vpc-flow-logs.html)

## 参考資料

- [https://cloud.google.com/vpc/docs/using-flow-logs#enabling_vpc_flow_logging](https://cloud.google.com/vpc/docs/using-flow-logs#enabling_vpc_flow_logging)

## 技術情報

- Source Metadata：[sources/gcp/compute_subnet_flow_logs_enabled/metadata.json](../../sources/gcp/compute_subnet_flow_logs_enabled/metadata.json)
- Source Code：[sources/gcp/compute_subnet_flow_logs_enabled/check.py](../../sources/gcp/compute_subnet_flow_logs_enabled/check.py)
- Source Metadata Path：`sources/gcp/compute_subnet_flow_logs_enabled/metadata.json`
- Source Code Path：`sources/gcp/compute_subnet_flow_logs_enabled/check.py`
