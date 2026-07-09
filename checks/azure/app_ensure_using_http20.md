# Ensure that 'HTTP Version' is the Latest, if Used to Run the Web App

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `app_ensure_using_http20` |
| 云平台 | Azure |
| 服务 | app |
| 严重等级 | low |
| 类别 | Uncategorized |
| 资源类型 | Microsoft.Web/sites |
| 资源组 | serverless |

## 描述

Periodically, newer versions are released for HTTP either due to security flaws or to include additional functionality. Using the latest HTTP version for web apps to take advantage of security fixes, if any, and/or new functionalities of the newer version.

## 风险

Newer versions may contain security enhancements and additional functionality. Using the latest version is recommended in order to take advantage of enhancements and new capabilities. With each software installation, organizations need to determine if a given update meets their requirements. They must also verify the compatibility and support provided for any additional software against the update revision that is selected. HTTP 2.0 has additional performance improvements on the head-of-line blocking problem of old HTTP version, header compression, and prioritization of requests. HTTP 2.0 no longer supports HTTP 1.1's chunked transfer encoding mechanism, as it provides its own, more efficient, mechanisms for data streaming.

## 推荐措施

1. Login to Azure Portal using https://portal.azure.com 2. Go to App Services 3. Click on each App 4. Under Setting section, Click on Configuration 5. Set HTTP version to 2.0 under General settings

- 推荐链接：[https://azure.microsoft.com/en-us/blog/announcing-http-2-support-in-azure-app-service/](https://azure.microsoft.com/en-us/blog/announcing-http-2-support-in-azure-app-service/)

## 修复步骤


### CLI

```text
az webapp config set --resource-group <RESOURCE_GROUP_NAME> --name <APP_NAME> --http20-enabled true
```

### Other

[https://www.trendmicro.com/cloudoneconformity/knowledge-base/azure/AppService/enable-http-2-for-app-service-web-applications.html](https://www.trendmicro.com/cloudoneconformity/knowledge-base/azure/AppService/enable-http-2-for-app-service-web-applications.html)

## 参考资料

- [https://learn.microsoft.com/en-us/azure/app-service/configure-common?tabs=portal#general-settings](https://learn.microsoft.com/en-us/azure/app-service/configure-common?tabs=portal#general-settings)
- [https://azure.microsoft.com/en-us/blog/announcing-http-2-support-in-azure-app-service/](https://azure.microsoft.com/en-us/blog/announcing-http-2-support-in-azure-app-service/)

## 技术信息

- Source Metadata：[sources/azure/app_ensure_using_http20/metadata.json](../../sources/azure/app_ensure_using_http20/metadata.json)
- Source Code：[sources/azure/app_ensure_using_http20/check.py](../../sources/azure/app_ensure_using_http20/check.py)
- Source Metadata Path：`sources/azure/app_ensure_using_http20/metadata.json`
- Source Code Path：`sources/azure/app_ensure_using_http20/check.py`
