# Ensure that HTTP(S) access from the Internet is evaluated and restricted

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `network_http_internet_access_restricted` |
| 云平台 | Azure |
| 服务 | network |
| 严重等级 | high |
| 类别 | Uncategorized |
| 资源类型 | Network |
| 资源组 | network |

## 描述

Network security groups should be periodically evaluated for port misconfigurations. Where certain ports and protocols may be exposed to the Internet, they should be evaluated for necessity and restricted wherever they are not explicitly required and narrowly configured.

## 风险

The potential security problem with using HTTP(S) over the Internet is that attackers can use various brute force techniques to gain access to Azure resources. Once the attackers gain access, they can use the resource as a launch point for compromising other resources within the Azure tenant.

## 推荐措施

Where HTTP(S) is not explicitly required and narrowly configured for resources attached to the Network Security Group, Internet-level access to your Azure resources should be restricted or eliminated. For internal access to relevant resources, configure an encrypted network tunnel such as: ExpressRoute Site-to-site VPN Point-to-site VPN

## 修复步骤


### Other

[https://www.trendmicro.com/cloudoneconformity-staging/knowledge-base/azure/Network/unrestricted-http-access.html](https://www.trendmicro.com/cloudoneconformity-staging/knowledge-base/azure/Network/unrestricted-http-access.html)

## 参考资料

- [https://learn.microsoft.com/en-us/security/benchmark/azure/security-controls-v3-network-security#ns-1-establish-network-segmentation-boundaries](https://learn.microsoft.com/en-us/security/benchmark/azure/security-controls-v3-network-security#ns-1-establish-network-segmentation-boundaries)

## 技术信息

- Source Metadata：[sources/azure/network_http_internet_access_restricted/metadata.json](../../sources/azure/network_http_internet_access_restricted/metadata.json)
- Source Code：[sources/azure/network_http_internet_access_restricted/check.py](../../sources/azure/network_http_internet_access_restricted/check.py)
- Source Metadata Path：`sources/azure/network_http_internet_access_restricted/metadata.json`
- Source Code Path：`sources/azure/network_http_internet_access_restricted/check.py`
