# Ensure that RDP access from the Internet is evaluated and restricted

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `network_rdp_internet_access_restricted` |
| クラウドプラットフォーム | Azure |
| サービス | network |
| 重大度 | high |
| カテゴリ | Uncategorized |
| リソースタイプ | Network |
| リソースグループ | network |

## 説明

Network security groups should be periodically evaluated for port misconfigurations. Where certain ports and protocols may be exposed to the Internet, they should be evaluated for necessity and restricted wherever they are not explicitly required.

## リスク

The potential security problem with using RDP over the Internet is that attackers can use various brute force techniques to gain access to Azure Virtual Machines. Once the attackers gain access, they can use a virtual machine as a launch point for compromising other machines on an Azure Virtual Network or even attack networked devices outside of Azure.

## 推奨事項

Where RDP is not explicitly required and narrowly configured for resources attached to the Network Security Group, Internet-level access to your Azure resources should be restricted or eliminated. For internal access to relevant resources, configure an encrypted network tunnel such as: ExpressRoute Site-to-site VPN Point-to-site VPN

- 推奨リンク：[https://docs.microsoft.com/en-us/security/benchmark/azure/security-controls-v3-network-security#ns-1-establish-network-segmentation-boundaries](https://docs.microsoft.com/en-us/security/benchmark/azure/security-controls-v3-network-security#ns-1-establish-network-segmentation-boundaries)

## 修正手順


### Terraform

[https://docs.ST Cloud.com/checks/azure/azure-networking-policies/bc_azr_networking_2#terraform](https://docs.ST Cloud.com/checks/azure/azure-networking-policies/bc_azr_networking_2#terraform)

### Other

[https://www.trendmicro.com/cloudoneconformity-staging/knowledge-base/azure/Network/unrestricted-rdp-access.html#](https://www.trendmicro.com/cloudoneconformity-staging/knowledge-base/azure/Network/unrestricted-rdp-access.html#)

## 参考資料

- [https://docs.microsoft.com/en-us/azure/security/azure-security-network-security-best-practices#disable-rdpssh-access-to-azure-virtual-machines](https://docs.microsoft.com/en-us/azure/security/azure-security-network-security-best-practices#disable-rdpssh-access-to-azure-virtual-machines)
- [https://docs.microsoft.com/en-us/security/benchmark/azure/security-controls-v3-network-security#ns-1-establish-network-segmentation-boundaries](https://docs.microsoft.com/en-us/security/benchmark/azure/security-controls-v3-network-security#ns-1-establish-network-segmentation-boundaries)

## 技術情報

- Source Metadata：[sources/azure/network_rdp_internet_access_restricted/metadata.json](../../sources/azure/network_rdp_internet_access_restricted/metadata.json)
- Source Code：[sources/azure/network_rdp_internet_access_restricted/check.py](../../sources/azure/network_rdp_internet_access_restricted/check.py)
- Source Metadata Path：`sources/azure/network_rdp_internet_access_restricted/metadata.json`
- Source Code Path：`sources/azure/network_rdp_internet_access_restricted/check.py`
