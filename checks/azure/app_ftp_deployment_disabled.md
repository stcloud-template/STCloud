# Ensure FTP deployments are Disabled

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `app_ftp_deployment_disabled` |
| クラウドプラットフォーム | Azure |
| サービス | app |
| 重大度 | medium |
| カテゴリ | Uncategorized |
| リソースタイプ | Microsoft.Web/sites/config |
| リソースグループ | serverless |

## 説明

By default, Azure Functions, Web, and API Services can be deployed over FTP. If FTP is required for an essential deployment workflow, FTPS should be required for FTP login for all App Service Apps and Functions.

## リスク

Azure FTP deployment endpoints are public. An attacker listening to traffic on a wifi network used by a remote employee or a corporate network could see login traffic in clear-text which would then grant them full control of the code base of the app or service. This finding is more severe if User Credentials for deployment are set at the subscription level rather than using the default Application Credentials which are unique per App.

## 推奨事項

1. Go to the Azure Portal 2. Select App Services 3. Click on an app 4. Select Settings and then Configuration 5. Under General Settings, for the Platform Settings, the FTP state should be set to Disabled or FTPS Only

## 修正手順


### CLI

```text
az webapp config set --resource-group <resource group name> --name <app name> --ftps-state [disabled|FtpsOnly]
```

### Terraform

[https://docs.ST Cloud.com/checks/azure/azure-general-policies/ensure-ftp-deployments-are-disabled#terraform](https://docs.ST Cloud.com/checks/azure/azure-general-policies/ensure-ftp-deployments-are-disabled#terraform)

### Other

[https://www.trendmicro.com/cloudoneconformity/knowledge-base/azure/AppService/ftp-access-disabled.html](https://www.trendmicro.com/cloudoneconformity/knowledge-base/azure/AppService/ftp-access-disabled.html)

## 参考資料

- [https://learn.microsoft.com/en-us/azure/app-service/deploy-ftp?tabs=portal](https://learn.microsoft.com/en-us/azure/app-service/deploy-ftp?tabs=portal)

## 技術情報

- Source Metadata：[sources/azure/app_ftp_deployment_disabled/metadata.json](../../sources/azure/app_ftp_deployment_disabled/metadata.json)
- Source Code：[sources/azure/app_ftp_deployment_disabled/check.py](../../sources/azure/app_ftp_deployment_disabled/check.py)
- Source Metadata Path：`sources/azure/app_ftp_deployment_disabled/metadata.json`
- Source Code Path：`sources/azure/app_ftp_deployment_disabled/check.py`
