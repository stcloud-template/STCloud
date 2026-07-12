# Ensure that Register with Azure Active Directory is enabled on App Service

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `app_register_with_identity` |
| クラウドプラットフォーム | Azure |
| サービス | app |
| 重大度 | medium |
| カテゴリ | Uncategorized |
| リソースタイプ | Microsoft.Web/sites |
| リソースグループ | serverless |

## 説明

Managed service identity in App Service provides more security by eliminating secrets from the app, such as credentials in the connection strings. When registering with Azure Active Directory in App Service, the app will connect to other Azure services securely without the need for usernames and passwords.

## リスク

App Service provides a highly scalable, self-patching web hosting service in Azure. It also provides a managed identity for apps, which is a turn-key solution for securing access to Azure SQL Database and other Azure services.

## 推奨事項

1. Login to Azure Portal using https://portal.azure.com 2. Go to App Services 3. Click on each App 4. Under Setting section, Click on Identity 5. Under the System assigned pane, set Status to On

- 推奨リンク：[https://learn.microsoft.com/en-us/azure/app-service/scenario-secure-app-authentication-app-service](https://learn.microsoft.com/en-us/azure/app-service/scenario-secure-app-authentication-app-service)

## 修正手順


### CLI

```text
az webapp identity assign --resource-group <RESOURCE_GROUP_NAME> --name <APP_NAME>
```

### Terraform

[https://docs.ST Cloud.com/checks/azure/azure-iam-policies/bc_azr_iam_1#terraform](https://docs.ST Cloud.com/checks/azure/azure-iam-policies/bc_azr_iam_1#terraform)

### Other

[https://www.trendmicro.com/cloudoneconformity/knowledge-base/azure/AppService/enable-registration-with-microsoft-entra-id.html](https://www.trendmicro.com/cloudoneconformity/knowledge-base/azure/AppService/enable-registration-with-microsoft-entra-id.html)

## 参考資料

- [https://learn.microsoft.com/en-us/azure/app-service/configure-authentication-provider-aad?tabs=workforce-tenant](https://learn.microsoft.com/en-us/azure/app-service/configure-authentication-provider-aad?tabs=workforce-tenant)
- [https://learn.microsoft.com/en-us/azure/app-service/scenario-secure-app-authentication-app-service](https://learn.microsoft.com/en-us/azure/app-service/scenario-secure-app-authentication-app-service)

## 技術情報

- Source Metadata：[sources/azure/app_register_with_identity/metadata.json](../../sources/azure/app_register_with_identity/metadata.json)
- Source Code：[sources/azure/app_register_with_identity/check.py](../../sources/azure/app_register_with_identity/check.py)
- Source Metadata Path：`sources/azure/app_register_with_identity/metadata.json`
- Source Code Path：`sources/azure/app_register_with_identity/check.py`
