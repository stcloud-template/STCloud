# Ensure that public network access when using private endpoint is disabled.

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `keyvault_access_only_through_private_endpoints` |
| クラウドプラットフォーム | Azure |
| サービス | keyvault |
| 重大度 | high |
| カテゴリ | Uncategorized |
| リソースタイプ | KeyVault |
| リソースグループ | security |

## 説明

Checks if Key Vaults with private endpoints have public network access disabled.

## リスク

Allowing public network access to Key Vault when using private endpoint can expose sensitive data to unauthorized access.

## 推奨事項

Disable public network access for Key Vaults that use private endpoint to ensure network traffic only flows through the private endpoint.

- 推奨リンク：[https://learn.microsoft.com/en-us/azure/private-link/private-endpoint-overview](https://learn.microsoft.com/en-us/azure/private-link/private-endpoint-overview)

## 修正手順


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

## 参考資料

- [https://learn.microsoft.com/en-us/azure/key-vault/general/network-security](https://learn.microsoft.com/en-us/azure/key-vault/general/network-security)
- [https://learn.microsoft.com/en-us/azure/private-link/private-endpoint-overview](https://learn.microsoft.com/en-us/azure/private-link/private-endpoint-overview)

## 技術情報

- Source Metadata：[sources/azure/keyvault_access_only_through_private_endpoints/metadata.json](../../sources/azure/keyvault_access_only_through_private_endpoints/metadata.json)
- Source Code：[sources/azure/keyvault_access_only_through_private_endpoints/check.py](../../sources/azure/keyvault_access_only_through_private_endpoints/check.py)
- Source Metadata Path：`sources/azure/keyvault_access_only_through_private_endpoints/metadata.json`
- Source Code Path：`sources/azure/keyvault_access_only_through_private_endpoints/check.py`
