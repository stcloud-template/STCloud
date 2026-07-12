# Ensure Azure function has system or user assigned managed identity configured

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `app_function_identity_is_configured` |
| クラウドプラットフォーム | Azure |
| サービス | app |
| サブサービス | function |
| 重大度 | medium |
| カテゴリ | Uncategorized |
| リソースタイプ | Microsoft.Web/sites |
| リソースグループ | serverless |

## 説明

Azure Functions should have managed identities configured for enhanced security and access control.

## リスク

Not using managed identities can lead to less secure authentication and authorization practices, potentially exposing sensitive data.

## 推奨事項

It is recommended to enable managed identities for Azure Functions to enhance security and access control. This allows the function app to easily access other Azure resources securely and with the appropriate permissions.

- 推奨リンク：[https://learn.microsoft.com/en-us/azure/app-service/overview-managed-identity](https://learn.microsoft.com/en-us/azure/app-service/overview-managed-identity)

## 修正手順


### CLI

```text
az functionapp identity assign --name <function_name> --resource-group <resource_group> --identities [system]
```

### Other

[https://www.trendmicro.com/cloudoneconformity/knowledge-base/azure/Functions/azure-function-system-assigned-identity.html](https://www.trendmicro.com/cloudoneconformity/knowledge-base/azure/Functions/azure-function-system-assigned-identity.html)

## 参考資料

- [https://learn.microsoft.com/en-us/entra/identity/managed-identities-azure-resources/overview](https://learn.microsoft.com/en-us/entra/identity/managed-identities-azure-resources/overview)
- [https://learn.microsoft.com/en-us/azure/app-service/overview-managed-identity](https://learn.microsoft.com/en-us/azure/app-service/overview-managed-identity)

## 技術情報

- Source Metadata：[sources/azure/app_function_identity_is_configured/metadata.json](../../sources/azure/app_function_identity_is_configured/metadata.json)
- Source Code：[sources/azure/app_function_identity_is_configured/check.py](../../sources/azure/app_function_identity_is_configured/check.py)
- Source Metadata Path：`sources/azure/app_function_identity_is_configured/metadata.json`
- Source Code Path：`sources/azure/app_function_identity_is_configured/check.py`
