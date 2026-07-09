# Ensure an Azure Bastion Host Exists

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `network_bastion_host_exists` |
| 云平台 | Azure |
| 服务 | network |
| 严重等级 | medium |
| 类别 | Uncategorized |
| 资源类型 | Network |
| 资源组 | network |

## 描述

The Azure Bastion service allows secure remote access to Azure Virtual Machines over the Internet without exposing remote access protocol ports and services directly to the Internet. The Azure Bastion service provides this access using TLS over 443/TCP, and subscribes to hardened configurations within an organization's Azure Active Directory service.

## 风险

The Azure Bastion service allows organizations a more secure means of accessing Azure Virtual Machines over the Internet without assigning public IP addresses to those Virtual Machines. The Azure Bastion service provides Remote Desktop Protocol (RDP) and Secure Shell (SSH) access to Virtual Machines using TLS within a web browser, thus preventing organizations from opening up 3389/TCP and 22/TCP to the Internet on Azure Virtual Machines. Additional benefits of the Bastion service includes Multi-Factor Authentication, Conditional Access Policies, and any other hardening measures configured within Azure Active Directory using a central point of access.

## 推荐措施

From Azure Portal* 1. Click on Bastions 2. Select the Subscription 3. Select the Resource group 4. Type a Name for the new Bastion host 5. Select a Region 6. Choose Standard next to Tier 7. Use the slider to set the Instance count 8. Select the Virtual network or Create new 9. Select the Subnet named AzureBastionSubnet. Create a Subnet named AzureBastionSubnet using a /26 CIDR range if it doesn't already exist. 10. Selct the appropriate Public IP address option. 11. If Create new is selected for the Public IP address option, provide a Public IP address name. 12. If Use existing is selected for Public IP address option, select an IP address from Choose public IP address 13. Click Next: Tags > 14. Configure the appropriate Tags 15. Click Next: Advanced > 16. Select the appropriate Advanced options 17. Click Next: Review + create > 18. Click Create From Azure CLI az network bastion create --location <location> --name <name of bastion host> --public-ip-address <public IP address name or ID> --resource-group <resource group name or ID> --vnet-name <virtual network containing subnet called 'AzureBastionSubnet'> --scale-units <integer> --sku Standard [--disable-copy- paste true|false] [--enable-ip-connect true|false] [--enable-tunneling true|false] From PowerShell Create the appropriate Virtual network settings and Public IP Address settings. $subnetName = 'AzureBastionSubnet' $subnet = New-AzVirtualNetworkSubnetConfig -Name $subnetName -AddressPrefix <IP address range in CIDR notation making sure to use a /26> $virtualNet = New-AzVirtualNetwork -Name <virtual network name> - ResourceGroupName <resource group name> -Location <location> -AddressPrefix <IP address range in CIDR notation> -Subnet $subnet $publicip = New-AzPublicIpAddress -ResourceGroupName <resource group name> - Name <public IP address name> -Location <location> -AllocationMethod Dynamic -Sku Standard

- 推荐链接：[https://learn.microsoft.com/en-us/powershell/module/az.network/get-azbastion?view=azps-9.2.0](https://learn.microsoft.com/en-us/powershell/module/az.network/get-azbastion?view=azps-9.2.0)

## 修复步骤


### CLI

```text
az network bastion create --location <location> --name <name of bastion host> --public-ip-address <public IP address name or ID> --resource-group <resource group name or ID> --vnet-name <virtual network containing subnet called 'AzureBastionSubnet'> --scale-units <integer> --sku Standard [--disable-copy- paste true|false] [--enable-ip-connect true|false] [--enable-tunneling true|false]
```

### Other

[https://www.trendmicro.com/cloudoneconformity-staging/knowledge-base/azure/Network/bastion-host-exists.html](https://www.trendmicro.com/cloudoneconformity-staging/knowledge-base/azure/Network/bastion-host-exists.html)

## 参考资料

- [https://learn.microsoft.com/en-us/azure/bastion/bastion-overview#sku](https://learn.microsoft.com/en-us/azure/bastion/bastion-overview#sku)
- [https://learn.microsoft.com/en-us/powershell/module/az.network/get-azbastion?view=azps-9.2.0](https://learn.microsoft.com/en-us/powershell/module/az.network/get-azbastion?view=azps-9.2.0)

## 技术信息

- Source Metadata：[sources/azure/network_bastion_host_exists/metadata.json](../../sources/azure/network_bastion_host_exists/metadata.json)
- Source Code：[sources/azure/network_bastion_host_exists/check.py](../../sources/azure/network_bastion_host_exists/check.py)
- Source Metadata Path：`sources/azure/network_bastion_host_exists/metadata.json`
- Source Code Path：`sources/azure/network_bastion_host_exists/check.py`
