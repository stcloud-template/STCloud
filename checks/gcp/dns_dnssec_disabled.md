# Ensure That DNSSEC Is Enabled for Cloud DNS

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `dns_dnssec_disabled` |
| 云平台 | GCP |
| 服务 | dns |
| 严重等级 | medium |
| 类别 | Uncategorized |
| 资源类型 | DNS_Zone |
| 资源组 | network |

## 描述

Cloud Domain Name System (DNS) is a fast, reliable and cost-effective domain name system that powers millions of domains on the internet. Domain Name System Security Extensions (DNSSEC) in Cloud DNS enables domain owners to take easy steps to protect their domains against DNS hijacking and man-in-the-middle and other attacks.

## 风险

Attackers can hijack the process of domain/IP lookup and redirect users to malicious web content through DNS hijacking and Man-In-The-Middle (MITM) attacks.

## 推荐措施

Ensure that DNSSEC security feature is enabled for all your Google Cloud DNS managed zones in order to protect your domains against spoofing and cache poisoning attacks. By default, DNSSEC is not enabled for Google Cloud public DNS managed zones. DNSSEC security feature helps mitigate the risk of such attacks by encrypting signing DNS records. As a result, it prevents attackers from issuing fake DNS responses that may misdirect web clients to fake, fraudulent or scam websites.

- 推荐链接：[https://cloud.google.com/dns/docs/dnssec-config](https://cloud.google.com/dns/docs/dnssec-config)

## 修复步骤


### CLI

```text
gcloud dns managed-zones update <DNS_ZONE> --dnssec-state on
```

### Terraform

[https://docs.ST Cloud.com/checks/gcp/google-cloud-networking-policies/bc_gcp_networking_5#terraform](https://docs.ST Cloud.com/checks/gcp/google-cloud-networking-policies/bc_gcp_networking_5#terraform)

### Other

[https://www.trendmicro.com/cloudoneconformity/knowledge-base/gcp/CloudDNS/enable-dns-sec.html](https://www.trendmicro.com/cloudoneconformity/knowledge-base/gcp/CloudDNS/enable-dns-sec.html)

## 参考资料

- [https://cloud.google.com/dns/docs/dnssec-config](https://cloud.google.com/dns/docs/dnssec-config)

## 技术信息

- Source Metadata：[sources/gcp/dns_dnssec_disabled/metadata.json](../../sources/gcp/dns_dnssec_disabled/metadata.json)
- Source Code：[sources/gcp/dns_dnssec_disabled/check.py](../../sources/gcp/dns_dnssec_disabled/check.py)
- Source Metadata Path：`sources/gcp/dns_dnssec_disabled/metadata.json`
- Source Code Path：`sources/gcp/dns_dnssec_disabled/check.py`
