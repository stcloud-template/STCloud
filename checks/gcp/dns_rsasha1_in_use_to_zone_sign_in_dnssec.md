# Ensure That RSASHA1 Is Not Used for the Zone-Signing Key in Cloud DNS DNSSEC

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `dns_rsasha1_in_use_to_zone_sign_in_dnssec` |
| 云平台 | GCP |
| 服务 | dns |
| 严重等级 | medium |
| 类别 | Uncategorized |
| 资源类型 | DNS_Zone |
| 资源组 | network |

## 描述

NOTE: Currently, the SHA1 algorithm has been removed from general use by Google, and, if being used, needs to be whitelisted on a project basis by Google and will also, therefore, require a Google Cloud support contract. DNSSEC algorithm numbers in this registry may be used in CERT RRs. Zone signing (DNSSEC) and transaction security mechanisms (SIG(0) and TSIG) make use of particular subsets of these algorithms. The algorithm used for key signing should be a recommended one and it should be strong.

## 风险

SHA1 is considered weak and vulnerable to collision attacks.

## 推荐措施

Ensure that Domain Name System Security Extensions (DNSSEC) feature is not using the deprecated RSASHA1 algorithm for the Zone-Signing Key (ZSK) associated with your public DNS managed zone. The algorithm used for DNSSEC signing should be a strong one, such as RSASHA256, as this algorithm is secure and widely deployed, and therefore it is a good candidate for both DNSSEC validation and signing.

- 推荐链接：[https://cloud.google.com/dns/docs/dnssec-config](https://cloud.google.com/dns/docs/dnssec-config)

## 修复步骤


### Terraform

[https://docs.ST Cloud.com/checks/gcp/google-cloud-networking-policies/bc_gcp_networking_6#terraform](https://docs.ST Cloud.com/checks/gcp/google-cloud-networking-policies/bc_gcp_networking_6#terraform)

### Other

[https://www.trendmicro.com/cloudoneconformity/knowledge-base/gcp/CloudDNS/dns-sec-zone-signing-algorithm-in-use.html](https://www.trendmicro.com/cloudoneconformity/knowledge-base/gcp/CloudDNS/dns-sec-zone-signing-algorithm-in-use.html)

## 参考资料

- [https://cloud.google.com/dns/docs/dnssec-config](https://cloud.google.com/dns/docs/dnssec-config)

## 技术信息

- Source Metadata：[sources/gcp/dns_rsasha1_in_use_to_zone_sign_in_dnssec/metadata.json](../../sources/gcp/dns_rsasha1_in_use_to_zone_sign_in_dnssec/metadata.json)
- Source Code：[sources/gcp/dns_rsasha1_in_use_to_zone_sign_in_dnssec/check.py](../../sources/gcp/dns_rsasha1_in_use_to_zone_sign_in_dnssec/check.py)
- Source Metadata Path：`sources/gcp/dns_rsasha1_in_use_to_zone_sign_in_dnssec/metadata.json`
- Source Code Path：`sources/gcp/dns_rsasha1_in_use_to_zone_sign_in_dnssec/check.py`
