# Ensure to use a private link for accessing the Azure Container Registry

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `containerregistry_uses_private_link` |
| 云平台 | Azure |
| 服务 | containerregistry |
| 严重等级 | medium |
| 类别 | Uncategorized |
| 资源类型 | ContainerRegistry |
| 资源组 | container |

## 描述

Ensure that a private link is used for accessing the Azure Container Registry to enhance security and restrict access to the registry over the public internet.

## 风险

Without using a private link, the Azure Container Registry may be exposed to the public internet, increasing the risk of unauthorized access and potential data breaches.

## 推荐措施

Create a private link for Azure Container Registry through the Azure Portal: 1. Navigate to your Container Registry. 2. In the settings, select 'Networking'. 3. Select 'Private access'. 4. Configure a private endpoint for the registry.

- 推荐链接：[https://learn.microsoft.com/en-us/azure/container-registry/container-registry-private-link](https://learn.microsoft.com/en-us/azure/container-registry/container-registry-private-link)

## 修复步骤


### CLI

```text
az network private-endpoint create  --connection-name <ConnectionName> --resource-group <ResourceGroupName> --name <Name> --private-connection-resource-id <RegistryId> --vnet-name <VnetName> --subnet <SubnetName> --group-ids registry
```

## 参考资料

- [https://learn.microsoft.com/en-us/azure/private-link/private-link-overview](https://learn.microsoft.com/en-us/azure/private-link/private-link-overview)
- [https://learn.microsoft.com/en-us/azure/container-registry/container-registry-private-link](https://learn.microsoft.com/en-us/azure/container-registry/container-registry-private-link)

## 技术信息

- Source Metadata：[sources/azure/containerregistry_uses_private_link/metadata.json](../../sources/azure/containerregistry_uses_private_link/metadata.json)
- Source Code：[sources/azure/containerregistry_uses_private_link/check.py](../../sources/azure/containerregistry_uses_private_link/check.py)
- Source Metadata Path：`sources/azure/containerregistry_uses_private_link/metadata.json`
- Source Code Path：`sources/azure/containerregistry_uses_private_link/check.py`
