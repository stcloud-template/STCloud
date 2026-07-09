# Ensure that public network access when using private endpoint is disabled.

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `keyvault_access_only_through_private_endpoints` |
| 云平台 | Azure |
| 服务 | keyvault |
| 严重等级 | high |
| 类别 | Uncategorized |
| 资源类型 | KeyVault |
| 资源组 | security |

## 描述

Checks if Key Vaults with private endpoints have public network access disabled.

## 风险

Allowing public network access to Key Vault when using private endpoint can expose sensitive data to unauthorized access.

## 推荐措施

Disable public network access for Key Vaults that use private endpoint to ensure network traffic only flows through the private endpoint.

- 推荐链接：[https://learn.microsoft.com/en-us/azure/private-link/private-endpoint-overview](https://learn.microsoft.com/en-us/azure/private-link/private-endpoint-overview)

## 修复步骤


### CLI

```text
az keyvault update --resource-group <resource_group> --name <vault_name> --public-network-access disabled
```

### Native IaC

```text
{
  "type": "Microsoft.KeyVault/vaults",
  "apiVersion": "2022-07-01",
  "properties": {
    "publicNetworkAccess": "disabled"
  }
}
```

### Terraform

```text
resource "azurerm_key_vault" "example" {
  # ... other configuration ...

  public_network_access_enabled = false
}
```

### Other

[https://www.trendmicro.com/cloudoneconformity/knowledge-base/azure/KeyVault/use-private-endpoints.html](https://www.trendmicro.com/cloudoneconformity/knowledge-base/azure/KeyVault/use-private-endpoints.html)

## 参考资料

- [https://learn.microsoft.com/en-us/azure/key-vault/general/network-security](https://learn.microsoft.com/en-us/azure/key-vault/general/network-security)
- [https://learn.microsoft.com/en-us/azure/private-link/private-endpoint-overview](https://learn.microsoft.com/en-us/azure/private-link/private-endpoint-overview)

## 技术信息

- Source Metadata：[sources/azure/keyvault_access_only_through_private_endpoints/metadata.json](../../sources/azure/keyvault_access_only_through_private_endpoints/metadata.json)
- Source Code：[sources/azure/keyvault_access_only_through_private_endpoints/check.py](../../sources/azure/keyvault_access_only_through_private_endpoints/check.py)
- Source Metadata Path：`sources/azure/keyvault_access_only_through_private_endpoints/metadata.json`
- Source Code Path：`sources/azure/keyvault_access_only_through_private_endpoints/check.py`
