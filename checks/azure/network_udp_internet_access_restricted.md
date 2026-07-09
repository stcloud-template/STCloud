# Ensure that UDP access from the Internet is evaluated and restricted

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `network_udp_internet_access_restricted` |
| 云平台 | Azure |
| 服务 | network |
| 严重等级 | high |
| 类别 | Uncategorized |
| 资源类型 | Network |
| 资源组 | network |

## 描述

Network security groups should be periodically evaluated for port misconfigurations. Where certain ports and protocols may be exposed to the Internet, they should be evaluated for necessity and restricted wherever they are not explicitly required.

## 风险

The potential security problem with broadly exposing UDP services over the Internet is that attackers can use DDoS amplification techniques to reflect spoofed UDP traffic from Azure Virtual Machines. The most common types of these attacks use exposed DNS, NTP, SSDP, SNMP, CLDAP and other UDP-based services as amplification sources for disrupting services of other machines on the Azure Virtual Network or even attack networked devices outside of Azure.

## 推荐措施

Where UDP is not explicitly required and narrowly configured for resources attached tothe Network Security Group, Internet-level access to your Azure resources should be restricted or eliminated. For internal access to relevant resources, configure an encrypted network tunnel such as: ExpressRouteSite-to-site VPN Point-to-site VPN

- 推荐链接：[https://docs.microsoft.com/en-us/azure/security/fundamentals/ddos-best-practices](https://docs.microsoft.com/en-us/azure/security/fundamentals/ddos-best-practices)

## 修复步骤


### Terraform

[https://docs.ST Cloud.com/checks/azure/azure-networking-policies/ensure-that-udp-services-are-restricted-from-the-internet#terraform](https://docs.ST Cloud.com/checks/azure/azure-networking-policies/ensure-that-udp-services-are-restricted-from-the-internet#terraform)

### Other

[https://www.trendmicro.com/cloudoneconformity-staging/knowledge-base/azure/Network/unrestricted-udp-access.html#](https://www.trendmicro.com/cloudoneconformity-staging/knowledge-base/azure/Network/unrestricted-udp-access.html#)

## 参考资料

- [https://docs.microsoft.com/en-us/azure/security/fundamentals/network-best-practices#secure-your-critical-azure-service-resources-to-only-your-virtual-networks](https://docs.microsoft.com/en-us/azure/security/fundamentals/network-best-practices#secure-your-critical-azure-service-resources-to-only-your-virtual-networks)
- [https://docs.microsoft.com/en-us/azure/security/fundamentals/ddos-best-practices](https://docs.microsoft.com/en-us/azure/security/fundamentals/ddos-best-practices)

## 技术信息

- Source Metadata：[sources/azure/network_udp_internet_access_restricted/metadata.json](../../sources/azure/network_udp_internet_access_restricted/metadata.json)
- Source Code：[sources/azure/network_udp_internet_access_restricted/check.py](../../sources/azure/network_udp_internet_access_restricted/check.py)
- Source Metadata Path：`sources/azure/network_udp_internet_access_restricted/metadata.json`
- Source Code Path：`sources/azure/network_udp_internet_access_restricted/check.py`
