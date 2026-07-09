# Ensure Web App Redirects All HTTP traffic to HTTPS in Azure App Service

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `app_ensure_http_is_redirected_to_https` |
| 云平台 | Azure |
| 服务 | app |
| 严重等级 | medium |
| 类别 | Uncategorized |
| 资源类型 | Microsoft.Web/sites/config |
| 资源组 | serverless |

## 描述

Azure Web Apps allows sites to run under both HTTP and HTTPS by default. Web apps can be accessed by anyone using non-secure HTTP links by default. Non-secure HTTP requests can be restricted and all HTTP requests redirected to the secure HTTPS port. It is recommended to enforce HTTPS-only traffic.

## 风险

Enabling HTTPS-only traffic will redirect all non-secure HTTP requests to HTTPS ports. HTTPS uses the TLS/SSL protocol to provide a secure connection which is both encrypted and authenticated. It is therefore important to support HTTPS for the security benefits.

## 推荐措施

1. Login to Azure Portal using https://portal.azure.com 2. Go to App Services 3. Click on each App 4. Under Setting section, Click on Configuration 5. In the General Settings section, set the HTTPS Only to On 6. Click Save

- 推荐链接：[https://learn.microsoft.com/en-us/security/benchmark/azure/security-controls-v3-data-protection#dp-3-encrypt-sensitive-data-in-transit](https://learn.microsoft.com/en-us/security/benchmark/azure/security-controls-v3-data-protection#dp-3-encrypt-sensitive-data-in-transit)

## 修复步骤


### CLI

```text
az webapp update --resource-group <RESOURCE_GROUP_NAME> --name <APP_NAME> --set httpsOnly=true
```

### Terraform

[https://docs.ST Cloud.com/checks/azure/azure-networking-policies/bc_azr_networking_5#terraform](https://docs.ST Cloud.com/checks/azure/azure-networking-policies/bc_azr_networking_5#terraform)

### Other

[https://www.trendmicro.com/cloudoneconformity/knowledge-base/azure/AppService/enable-https-only-traffic.html#](https://www.trendmicro.com/cloudoneconformity/knowledge-base/azure/AppService/enable-https-only-traffic.html#)

## 参考资料

- [https://learn.microsoft.com/en-us/azure/app-service/configure-ssl-bindings#enforce-https](https://learn.microsoft.com/en-us/azure/app-service/configure-ssl-bindings#enforce-https)
- [https://learn.microsoft.com/en-us/security/benchmark/azure/security-controls-v3-data-protection#dp-3-encrypt-sensitive-data-in-transit](https://learn.microsoft.com/en-us/security/benchmark/azure/security-controls-v3-data-protection#dp-3-encrypt-sensitive-data-in-transit)

## 技术信息

- Source Metadata：[sources/azure/app_ensure_http_is_redirected_to_https/metadata.json](../../sources/azure/app_ensure_http_is_redirected_to_https/metadata.json)
- Source Code：[sources/azure/app_ensure_http_is_redirected_to_https/check.py](../../sources/azure/app_ensure_http_is_redirected_to_https/check.py)
- Source Metadata Path：`sources/azure/app_ensure_http_is_redirected_to_https/metadata.json`
- Source Code Path：`sources/azure/app_ensure_http_is_redirected_to_https/check.py`
