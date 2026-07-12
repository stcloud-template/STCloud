# Ensure that FTP and FTPS deployments are disabled for Azure Functions to prevent unauthorized access and data breaches.

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `app_function_ftps_deployment_disabled` |
| クラウドプラットフォーム | Azure |
| サービス | app |
| サブサービス | function |
| 重大度 | medium |
| カテゴリ | Uncategorized |
| リソースタイプ | Microsoft.Web/sites |
| リソースグループ | serverless |

## 説明

Azure FTP deployment endpoints are unencrypted and public, making them vulnerable to attacks. Disabling FTP and FTPS deployments enhances security by preventing unauthorized access to login credentials and sensitive codebases.

## リスク

If left enabled, attackers can intercept network traffic and gain full control of the app or service, leading to potential data breaches and unauthorized modifications.

## 推奨事項

It is recommended to disable FTP and FTPS deployments for Azure Functions to mitigate security risks. Instead, consider using more secure deployment methods such as Docker container or enabling continuous deployment with GitHub Actions.

- 推奨リンク：[https://learn.microsoft.com/en-us/azure/azure-functions/functions-deployment-technologies?tabs=windows#trigger-syncing](https://learn.microsoft.com/en-us/azure/azure-functions/functions-deployment-technologies?tabs=windows#trigger-syncing)

## 修正手順

### CLI

```text
az webapp config set --resource-group <resource-group> --name <app-name> --ftps-state Disabled
```

## 参考資料

- [https://docs.microsoft.com/en-us/azure/app-service/deploy-ftp](https://docs.microsoft.com/en-us/azure/app-service/deploy-ftp)
- [https://learn.microsoft.com/en-us/azure/azure-functions/functions-deployment-technologies?tabs=windows#trigger-syncing](https://learn.microsoft.com/en-us/azure/azure-functions/functions-deployment-technologies?tabs=windows#trigger-syncing)

## 技術情報

- Source Metadata：[`sources/azure/app_function_ftps_deployment_disabled/metadata.json`](../sources/azure/app_function_ftps_deployment_disabled/metadata.json)
- Source Code：[`sources/azure/app_function_ftps_deployment_disabled/check.py`](../sources/azure/app_function_ftps_deployment_disabled/check.py)
- Source Metadata Path：`sources/azure/app_function_ftps_deployment_disabled/metadata.json`
- Source Code Path：`sources/azure/app_function_ftps_deployment_disabled/check.py`
