# Restrict public network access to the AI Search Service

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `aisearch_service_not_publicly_accessible` |
| 云平台 | Azure |
| 服务 | aisearch |
| 严重等级 | high |
| 类别 | gen-ai |
| 资源类型 | AzureSearchService |
| 资源组 | database |

## 描述

Ensure that public network access to the Search Service is restricted.

## 风险

Public accessibility exposes the Search Service to potential attacks, unauthorized usage, and data breaches. Restricting access minimizes the surface area for attacks and ensures that only authorized networks can access the search service.

## 推荐措施

Ensure that the necessary virtual network configurations or IP rules are in place to allow access from required services once public access is restricted. Review the network access settings regularly to maintain a secure environment. To restrict public network access to your Search Service: 1. Navigate to your Search Service y in the Azure Portal. 2. Under 'Settings'->'Networking', configure the 'Public network access' settings to 'Disabled'. 3. Set up virtual network service endpoints or private endpoints as needed for secure access. 4. Review and adjust IP access rules as necessary.

- 推荐链接：[https://learn.microsoft.com/en-us/azure/search/service-configure-firewall#configure-network-access-in-azure-portal](https://learn.microsoft.com/en-us/azure/search/service-configure-firewall#configure-network-access-in-azure-portal)

## 修复步骤


### CLI

```text
az search service update --resource-group <resource_group_name> --name <service_name> --public-access disabled
```

## 参考资料

- [https://learn.microsoft.com/en-us/azure/search/service-configure-firewall#configure-network-access-in-azure-portal](https://learn.microsoft.com/en-us/azure/search/service-configure-firewall#configure-network-access-in-azure-portal)

## 技术信息

- Source Metadata：[sources/azure/aisearch_service_not_publicly_accessible/metadata.json](../../sources/azure/aisearch_service_not_publicly_accessible/metadata.json)
- Source Code：[sources/azure/aisearch_service_not_publicly_accessible/check.py](../../sources/azure/aisearch_service_not_publicly_accessible/check.py)
- Source Metadata Path：`sources/azure/aisearch_service_not_publicly_accessible/metadata.json`
- Source Code Path：`sources/azure/aisearch_service_not_publicly_accessible/check.py`
