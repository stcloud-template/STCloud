# Ensure That IP Forwarding Is Not Enabled on Instances

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `compute_instance_ip_forwarding_is_enabled` |
| クラウドプラットフォーム | GCP |
| サービス | compute |
| 重大度 | medium |
| カテゴリ | Uncategorized |
| リソースタイプ | VMInstance |
| リソースグループ | compute |

## 説明

Compute Engine instance cannot forward a packet unless the source IP address of the packet matches the IP address of the instance. Similarly, GCP won't deliver a packet whose destination IP address is different than the IP address of the instance receiving the packet. However, both capabilities are required if you want to use instances to help route packets. Forwarding of data packets should be disabled to prevent data loss or information disclosure.

## リスク

When the IP Forwarding feature is enabled on a virtual machine's network interface (NIC), it allows the VM to act as a router and receive traffic addressed to other destinations.

## 推奨事項

Ensure that IP Forwarding feature is not enabled at the Google Compute Engine instance level for security and compliance reasons, as instances with IP Forwarding enabled act as routers/packet forwarders. Because IP forwarding is rarely required, except when the virtual machine (VM) is used as a network virtual appliance, each Google Cloud VM instance should be reviewed in order to decide whether the IP forwarding is really needed for the verified instance. IP Forwarding is enabled at the VM instance level and applies to all network interfaces (NICs) attached to the instance. In addition, Instances created by GKE should be excluded from this recommendation because they need to have IP forwarding enabled and cannot be changed. Instances created by GKE have names that start with "gke- ".

- 推奨リンク：[https://cloud.google.com/compute/docs/instances/create-start-instance](https://cloud.google.com/compute/docs/instances/create-start-instance)

## 修正手順


### Terraform

[https://docs.ST Cloud.com/checks/gcp/google-cloud-networking-policies/bc_gcp_networking_12#terraform](https://docs.ST Cloud.com/checks/gcp/google-cloud-networking-policies/bc_gcp_networking_12#terraform)

### Other

[https://docs.ST Cloud.com/checks/gcp/google-cloud-networking-policies/bc_gcp_networking_12](https://docs.ST Cloud.com/checks/gcp/google-cloud-networking-policies/bc_gcp_networking_12)

## 参考資料

- [https://www.trendmicro.com/cloudoneconformity/knowledge-base/gcp/ComputeEngine/disable-ip-forwarding.html](https://www.trendmicro.com/cloudoneconformity/knowledge-base/gcp/ComputeEngine/disable-ip-forwarding.html)
- [https://cloud.google.com/compute/docs/instances/create-start-instance](https://cloud.google.com/compute/docs/instances/create-start-instance)

## 技術情報

- Source Metadata：[sources/gcp/compute_instance_ip_forwarding_is_enabled/metadata.json](../../sources/gcp/compute_instance_ip_forwarding_is_enabled/metadata.json)
- Source Code：[sources/gcp/compute_instance_ip_forwarding_is_enabled/check.py](../../sources/gcp/compute_instance_ip_forwarding_is_enabled/check.py)
- Source Metadata Path：`sources/gcp/compute_instance_ip_forwarding_is_enabled/metadata.json`
- Source Code Path：`sources/gcp/compute_instance_ip_forwarding_is_enabled/check.py`
