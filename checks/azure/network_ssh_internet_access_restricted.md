# Ensure that SSH access from the Internet is evaluated and restricted

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `network_ssh_internet_access_restricted` |
| 云平台 | Azure |
| 服务 | network |
| 严重等级 | high |
| 类别 | Uncategorized |
| 资源类型 | Network |
| 资源组 | network |

## 描述

Network security groups should be periodically evaluated for port misconfigurations. Where certain ports and protocols may be exposed to the Internet, they should be evaluated for necessity and restricted wherever they are not explicitly required.

## 风险

The potential security problem with using SSH over the Internet is that attackers can use various brute force techniques to gain access to Azure Virtual Machines. Once the attackers gain access, they can use a virtual machine as a launch point for compromising other machines on the Azure Virtual Network or even attack networked devices outside of Azure.

## 推荐措施

Where SSH is not explicitly required and narrowly configured for resources attached to the Network Security Group, Internet-level access to your Azure resources should be restricted or eliminated. For internal access to relevant resources, configure an encrypted network tunnel such as: ExpressRoute Site-to-site VPN Point-to-site VPN

- 推荐链接：[https://docs.microsoft.com/en-us/security/benchmark/azure/security-controls-v3-network-security#ns-1-establish-network-segmentation-boundaries](https://docs.microsoft.com/en-us/security/benchmark/azure/security-controls-v3-network-security#ns-1-establish-network-segmentation-boundaries)

## 修复步骤


### Terraform

[https://docs.ST Cloud.com/checks/azure/azure-networking-policies/bc_azr_networking_3#terraform](https://docs.ST Cloud.com/checks/azure/azure-networking-policies/bc_azr_networking_3#terraform)

### Other

[https://www.trendmicro.com/cloudoneconformity-staging/knowledge-base/azure/Network/unrestricted-ssh-access.html](https://www.trendmicro.com/cloudoneconformity-staging/knowledge-base/azure/Network/unrestricted-ssh-access.html)

## 参考资料

- [https://docs.microsoft.com/en-us/azure/security/azure-security-network-security-best-practices#disable-rdpssh-access-to-azure-virtual-machines](https://docs.microsoft.com/en-us/azure/security/azure-security-network-security-best-practices#disable-rdpssh-access-to-azure-virtual-machines)
- [https://docs.microsoft.com/en-us/security/benchmark/azure/security-controls-v3-network-security#ns-1-establish-network-segmentation-boundaries](https://docs.microsoft.com/en-us/security/benchmark/azure/security-controls-v3-network-security#ns-1-establish-network-segmentation-boundaries)

## 技术信息

- Source Metadata：[sources/azure/network_ssh_internet_access_restricted/metadata.json](../../sources/azure/network_ssh_internet_access_restricted/metadata.json)
- Source Code：[sources/azure/network_ssh_internet_access_restricted/check.py](../../sources/azure/network_ssh_internet_access_restricted/check.py)
- Source Metadata Path：`sources/azure/network_ssh_internet_access_restricted/metadata.json`
- Source Code Path：`sources/azure/network_ssh_internet_access_restricted/check.py`
