# Ensure That RDP Access Is Restricted From the Internet

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `compute_firewall_rdp_access_from_the_internet_allowed` |
| クラウドプラットフォーム | GCP |
| サービス | compute |
| 重大度 | critical |
| カテゴリ | internet-exposed |
| リソースタイプ | FirewallRule |
| リソースグループ | network |

## 説明

GCP `Firewall Rules` are specific to a `VPC Network`. Each rule either `allows` or `denies` traffic when its conditions are met. Its conditions allow users to specify the type of traffic, such as ports and protocols, and the source or destination of the traffic, including IP addresses, subnets, and instances. Firewall rules are defined at the VPC network level and are specific to the network in which they are defined. The rules themselves cannot be shared among networks. Firewall rules only support IPv4 traffic. When specifying a source for an ingress rule or a destination for an egress rule by address, an `IPv4` address or `IPv4 block in CIDR` notation can be used. Generic `(0.0.0.0/0)` incoming traffic from the Internet to a VPC or VM instance using `RDP` on `Port 3389` can be avoided.

## リスク

Allowing unrestricted Remote Desktop Protocol (RDP) access can increase opportunities for malicious activities such as hacking, Man-In-The-Middle attacks (MITM) and Pass-The-Hash (PTH) attacks.

## 推奨事項

Ensure that Google Cloud Virtual Private Cloud (VPC) firewall rules do not allow unrestricted access (i.e. 0.0.0.0/0) on TCP port 3389 in order to restrict Remote Desktop Protocol (RDP) traffic to trusted IP addresses or IP ranges only and reduce the attack surface. TCP port 3389 is used for secure remote GUI login to Windows VM instances by connecting a RDP client application with an RDP server.

- 推奨リンク：[https://cloud.google.com/vpc/docs/using-firewalls](https://cloud.google.com/vpc/docs/using-firewalls)

## 修正手順


### CLI

```text
gcloud compute firewall-rules delete default-allow-rdp
```

### Terraform

[https://docs.ST Cloud.com/checks/gcp/google-cloud-networking-policies/bc_gcp_networking_2#terraform](https://docs.ST Cloud.com/checks/gcp/google-cloud-networking-policies/bc_gcp_networking_2#terraform)

### Other

[https://www.trendmicro.com/cloudoneconformity/knowledge-base/gcp/CloudVPC/unrestricted-rdp-access.html](https://www.trendmicro.com/cloudoneconformity/knowledge-base/gcp/CloudVPC/unrestricted-rdp-access.html)

## 参考資料

- [https://cloud.google.com/vpc/docs/using-firewalls](https://cloud.google.com/vpc/docs/using-firewalls)

## 技術情報

- Source Metadata：[sources/gcp/compute_firewall_rdp_access_from_the_internet_allowed/metadata.json](../../sources/gcp/compute_firewall_rdp_access_from_the_internet_allowed/metadata.json)
- Source Code：[sources/gcp/compute_firewall_rdp_access_from_the_internet_allowed/check.py](../../sources/gcp/compute_firewall_rdp_access_from_the_internet_allowed/check.py)
- Source Metadata Path：`sources/gcp/compute_firewall_rdp_access_from_the_internet_allowed/metadata.json`
- Source Code Path：`sources/gcp/compute_firewall_rdp_access_from_the_internet_allowed/check.py`
