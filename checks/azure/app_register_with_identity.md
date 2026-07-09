# Ensure that Register with Azure Active Directory is enabled on App Service

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `app_register_with_identity` |
| 云平台 | Azure |
| 服务 | app |
| 严重等级 | medium |
| 类别 | Uncategorized |
| 资源类型 | Microsoft.Web/sites |
| 资源组 | serverless |

## 描述

Managed service identity in App Service provides more security by eliminating secrets from the app, such as credentials in the connection strings. When registering with Azure Active Directory in App Service, the app will connect to other Azure services securely without the need for usernames and passwords.

## 风险

App Service provides a highly scalable, self-patching web hosting service in Azure. It also provides a managed identity for apps, which is a turn-key solution for securing access to Azure SQL Database and other Azure services.

## 推荐措施

1. Login to Azure Portal using https://portal.azure.com 2. Go to App Services 3. Click on each App 4. Under Setting section, Click on Identity 5. Under the System assigned pane, set Status to On

- 推荐链接：[https://learn.microsoft.com/en-us/azure/app-service/scenario-secure-app-authentication-app-service](https://learn.microsoft.com/en-us/azure/app-service/scenario-secure-app-authentication-app-service)

## 修复步骤


### CLI

```text
az webapp identity assign --resource-group <RESOURCE_GROUP_NAME> --name <APP_NAME>
```

### Terraform

[https://docs.ST Cloud.com/checks/azure/azure-iam-policies/bc_azr_iam_1#terraform](https://docs.ST Cloud.com/checks/azure/azure-iam-policies/bc_azr_iam_1#terraform)

### Other

[https://www.trendmicro.com/cloudoneconformity/knowledge-base/azure/AppService/enable-registration-with-microsoft-entra-id.html](https://www.trendmicro.com/cloudoneconformity/knowledge-base/azure/AppService/enable-registration-with-microsoft-entra-id.html)

## 参考资料

- [https://learn.microsoft.com/en-us/azure/app-service/configure-authentication-provider-aad?tabs=workforce-tenant](https://learn.microsoft.com/en-us/azure/app-service/configure-authentication-provider-aad?tabs=workforce-tenant)
- [https://learn.microsoft.com/en-us/azure/app-service/scenario-secure-app-authentication-app-service](https://learn.microsoft.com/en-us/azure/app-service/scenario-secure-app-authentication-app-service)

## 技术信息

- Source Metadata：[sources/azure/app_register_with_identity/metadata.json](../../sources/azure/app_register_with_identity/metadata.json)
- Source Code：[sources/azure/app_register_with_identity/check.py](../../sources/azure/app_register_with_identity/check.py)
- Source Metadata Path：`sources/azure/app_register_with_identity/metadata.json`
- Source Code Path：`sources/azure/app_register_with_identity/check.py`
