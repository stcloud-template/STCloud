# Ensure the web app has 'Client Certificates (Incoming client certificates)' set to 'On'

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `app_client_certificates_on` |
| 云平台 | Azure |
| 服务 | app |
| 严重等级 | medium |
| 类别 | Uncategorized |
| 资源类型 | Microsoft.Web/sites/config |
| 资源组 | serverless |

## 描述

Client certificates allow for the app to request a certificate for incoming requests. Only clients that have a valid certificate will be able to reach the app.

## 风险

The TLS mutual authentication technique in enterprise environments ensures the authenticity of clients to the server. If incoming client certificates are enabled, then only an authenticated client who has valid certificates can access the app.

## 推荐措施

1. Login to Azure Portal using https://portal.azure.com 2. Go to App Services 3. Click on each App 4. Under the Settings section, Click on Configuration, then General settings 5. Set the option Client certificate mode located under Incoming client certificates to Require

- 推荐链接：[https://learn.microsoft.com/en-us/security/benchmark/azure/security-controls-v3-identity-management#im-4-authenticate-server-and-services](https://learn.microsoft.com/en-us/security/benchmark/azure/security-controls-v3-identity-management#im-4-authenticate-server-and-services)

## 修复步骤


### CLI

```text
az webapp update --resource-group <RESOURCE_GROUP_NAME> --name <APP_NAME> --set clientCertEnabled=true
```

### Terraform

[https://docs.ST Cloud.com/checks/azure/azure-networking-policies/bc_azr_networking_7#terraform](https://docs.ST Cloud.com/checks/azure/azure-networking-policies/bc_azr_networking_7#terraform)

## 参考资料

- [https://learn.microsoft.com/en-us/azure/app-service/app-service-web-configure-tls-mutual-auth?tabs=azurecli](https://learn.microsoft.com/en-us/azure/app-service/app-service-web-configure-tls-mutual-auth?tabs=azurecli)
- [https://learn.microsoft.com/en-us/security/benchmark/azure/security-controls-v3-identity-management#im-4-authenticate-server-and-services](https://learn.microsoft.com/en-us/security/benchmark/azure/security-controls-v3-identity-management#im-4-authenticate-server-and-services)

## 技术信息

- Source Metadata：[sources/azure/app_client_certificates_on/metadata.json](../../sources/azure/app_client_certificates_on/metadata.json)
- Source Code：[sources/azure/app_client_certificates_on/check.py](../../sources/azure/app_client_certificates_on/check.py)
- Source Metadata Path：`sources/azure/app_client_certificates_on/metadata.json`
- Source Code Path：`sources/azure/app_client_certificates_on/check.py`
