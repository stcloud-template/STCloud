# Ensure That SSH Access Is Restricted From the Internet

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `compute_firewall_ssh_access_from_the_internet_allowed` |
| 云平台 | GCP |
| 服务 | compute |
| 严重等级 | critical |
| 类别 | internet-exposed |
| 资源类型 | FirewallRule |
| 资源组 | network |

## 描述

GCP `Firewall Rules` are specific to a `VPC Network`. Each rule either `allows` or `denies` traffic when its conditions are met. Its conditions allow the user to specify the type of traffic, such as ports and protocols, and the source or destination of the traffic, including IP addresses, subnets, and instances. Firewall rules are defined at the VPC network level and are specific to the network in which they are defined. The rules themselves cannot be shared among networks. Firewall rules only support IPv4 traffic. When specifying a source for an ingress rule or a destination for an egress rule by address, only an `IPv4` address or `IPv4 block in CIDR` notation can be used. Generic `(0.0.0.0/0)` incoming traffic from the internet to VPC or VM instance using `SSH` on `Port 22` can be avoided.

## 风险

Exposing Secure Shell (SSH) port 22 to the Internet can increase opportunities for malicious activities such as hacking, Man-In-The-Middle attacks (MITM) and brute-force attacks.

## 推荐措施

Check your Google Cloud Virtual Private Cloud (VPC) firewall rules for inbound rules that allow unrestricted access (i.e. 0.0.0.0/0) on TCP port 22 and restrict the access to trusted IP addresses or IP ranges only in order to implement the principle of least privilege and reduce the attack surface. TCP port 22 is used for secure remote login by connecting an SSH client application with an SSH server. It is strongly recommended to configure your Google Cloud VPC firewall rules to limit inbound traffic on TCP port 22 to known IP addresses only.

- 推荐链接：[https://cloud.google.com/vpc/docs/using-firewalls](https://cloud.google.com/vpc/docs/using-firewalls)

## 修复步骤


### CLI

```text
gcloud compute firewall-rules delete default-allow-ssh
```

### Terraform

[https://docs.ST Cloud.com/checks/gcp/google-cloud-networking-policies/bc_gcp_networking_1#terraform](https://docs.ST Cloud.com/checks/gcp/google-cloud-networking-policies/bc_gcp_networking_1#terraform)

### Other

[https://www.trendmicro.com/cloudoneconformity/knowledge-base/gcp/CloudVPC/unrestricted-ssh-access.html](https://www.trendmicro.com/cloudoneconformity/knowledge-base/gcp/CloudVPC/unrestricted-ssh-access.html)

## 参考资料

- [https://cloud.google.com/vpc/docs/using-firewalls](https://cloud.google.com/vpc/docs/using-firewalls)

## 技术信息

- Source Metadata：[sources/gcp/compute_firewall_ssh_access_from_the_internet_allowed/metadata.json](../../sources/gcp/compute_firewall_ssh_access_from_the_internet_allowed/metadata.json)
- Source Code：[sources/gcp/compute_firewall_ssh_access_from_the_internet_allowed/check.py](../../sources/gcp/compute_firewall_ssh_access_from_the_internet_allowed/check.py)
- Source Metadata Path：`sources/gcp/compute_firewall_ssh_access_from_the_internet_allowed/metadata.json`
- Source Code Path：`sources/gcp/compute_firewall_ssh_access_from_the_internet_allowed/check.py`
