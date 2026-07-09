# Ensure App Service Authentication is set up for apps in Azure App Service

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `app_ensure_auth_is_set_up` |
| 云平台 | Azure |
| 服务 | app |
| 严重等级 | medium |
| 类别 | Uncategorized |
| 资源类型 | Microsoft.Web/sites |
| 资源组 | serverless |

## 描述

Azure App Service Authentication is a feature that can prevent anonymous HTTP requests from reaching a Web Application or authenticate those with tokens before they reach the app. If an anonymous request is received from a browser, App Service will redirect to a logon page. To handle the logon process, a choice from a set of identity providers can be made, or a custom authentication mechanism can be implemented.

## 风险

By Enabling App Service Authentication, every incoming HTTP request passes through it before being handled by the application code. It also handles authentication of users with the specified provider (Azure Active Directory, Facebook, Google, Microsoft Account, and Twitter), validation, storing and refreshing of tokens, managing the authenticated sessions and injecting identity information into request headers.

## 推荐措施

1. Login to Azure Portal using https://portal.azure.com 2. Go to App Services 3. Click on each App 4. Under Setting section, click on Authentication 5. If no identity providers are set up, then click Add identity provider 6. Choose other parameters as per your requirements and click on Add

- 推荐链接：[https://learn.microsoft.com/en-us/azure/role-based-access-control/built-in-roles#website-contributor](https://learn.microsoft.com/en-us/azure/role-based-access-control/built-in-roles#website-contributor)

## 修复步骤


### CLI

```text
az webapp auth update --resource-group <RESOURCE_GROUP_NAME> --name <APP_NAME> --enabled true
```

### Terraform

[https://docs.ST Cloud.com/checks/azure/azure-general-policies/bc_azr_general_2#terraform](https://docs.ST Cloud.com/checks/azure/azure-general-policies/bc_azr_general_2#terraform)

### Other

[https://www.trendmicro.com/cloudoneconformity/knowledge-base/azure/AppService/enable-app-service-authentication.html](https://www.trendmicro.com/cloudoneconformity/knowledge-base/azure/AppService/enable-app-service-authentication.html)

## 参考资料

- [https://learn.microsoft.com/en-us/azure/app-service/overview-authentication-authorization](https://learn.microsoft.com/en-us/azure/app-service/overview-authentication-authorization)
- [https://learn.microsoft.com/en-us/azure/role-based-access-control/built-in-roles#website-contributor](https://learn.microsoft.com/en-us/azure/role-based-access-control/built-in-roles#website-contributor)

## 技术信息

- Source Metadata：[sources/azure/app_ensure_auth_is_set_up/metadata.json](../../sources/azure/app_ensure_auth_is_set_up/metadata.json)
- Source Code：[sources/azure/app_ensure_auth_is_set_up/check.py](../../sources/azure/app_ensure_auth_is_set_up/check.py)
- Source Metadata Path：`sources/azure/app_ensure_auth_is_set_up/metadata.json`
- Source Code Path：`sources/azure/app_ensure_auth_is_set_up/check.py`
