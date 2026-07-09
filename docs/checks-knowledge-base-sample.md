# Ensure that FTP and FTPS deployments are disabled for Azure Functions to prevent unauthorized access and data breaches.

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `app_function_ftps_deployment_disabled` |
| 云平台 | Azure |
| 服务 | app |
| 子服务 | function |
| 严重等级 | medium |
| 类别 | Uncategorized |
| 资源类型 | Microsoft.Web/sites |
| 资源组 | serverless |

## 描述

Azure FTP deployment endpoints are unencrypted and public, making them vulnerable to attacks. Disabling FTP and FTPS deployments enhances security by preventing unauthorized access to login credentials and sensitive codebases.

## 风险

If left enabled, attackers can intercept network traffic and gain full control of the app or service, leading to potential data breaches and unauthorized modifications.

## 推荐措施

It is recommended to disable FTP and FTPS deployments for Azure Functions to mitigate security risks. Instead, consider using more secure deployment methods such as Docker container or enabling continuous deployment with GitHub Actions.

- 推荐链接：[https://learn.microsoft.com/en-us/azure/azure-functions/functions-deployment-technologies?tabs=windows#trigger-syncing](https://learn.microsoft.com/en-us/azure/azure-functions/functions-deployment-technologies?tabs=windows#trigger-syncing)

## 修复步骤

### CLI

```text
az webapp config set --resource-group <resource-group> --name <app-name> --ftps-state Disabled
```

## 参考资料

- [https://docs.microsoft.com/en-us/azure/app-service/deploy-ftp](https://docs.microsoft.com/en-us/azure/app-service/deploy-ftp)
- [https://learn.microsoft.com/en-us/azure/azure-functions/functions-deployment-technologies?tabs=windows#trigger-syncing](https://learn.microsoft.com/en-us/azure/azure-functions/functions-deployment-technologies?tabs=windows#trigger-syncing)

## 技术信息

- Source Metadata：[`sources/azure/app_function_ftps_deployment_disabled/metadata.json`](../sources/azure/app_function_ftps_deployment_disabled/metadata.json)
- Source Code：[`sources/azure/app_function_ftps_deployment_disabled/check.py`](../sources/azure/app_function_ftps_deployment_disabled/check.py)
- Source Metadata Path：`sources/azure/app_function_ftps_deployment_disabled/metadata.json`
- Source Code Path：`sources/azure/app_function_ftps_deployment_disabled/check.py`
