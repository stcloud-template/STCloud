# Ensure That 'PHP version' is the Latest, If Used to Run the Web App

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `app_ensure_php_version_is_latest` |
| 云平台 | Azure |
| 服务 | app |
| 严重等级 | low |
| 类别 | Uncategorized |
| 资源类型 | Microsoft.Web/sites |
| 资源组 | serverless |

## 描述

Periodically newer versions are released for PHP software either due to security flaws or to include additional functionality. Using the latest PHP version for web apps is recommended in order to take advantage of security fixes, if any, and/or additional functionalities of the newer version.

## 风险

Newer versions may contain security enhancements and additional functionality. Using the latest software version is recommended in order to take advantage of enhancements and new capabilities. With each software installation, organizations need to determine if a given update meets their requirements. They must also verify the compatibility and support provided for any additional software against the update revision that is selected.

## 推荐措施

1. From Azure Home open the Portal Menu in the top left 2. Go to App Services 3. Click on each App 4. Under Settings section, click on Configuration 5. Click on the General settings pane, ensure that for a Stack of PHP the Major Version and Minor Version reflect the latest stable and supported release. NOTE: No action is required If PHP version is set to Off or is set with an empty value as PHP is not used by your web app

- 推荐链接：[https://learn.microsoft.com/en-us/azure/app-service/configure-language-php?pivots=platform-linux#set-php-version](https://learn.microsoft.com/en-us/azure/app-service/configure-language-php?pivots=platform-linux#set-php-version)

## 修复步骤


### CLI

```text
az webapp config set --resource-group <resource group name> --name <app name> [--linux-fx-version <php runtime version>][--php-version <php version>]
```

### Terraform

[https://docs.ST Cloud.com/checks/azure/azure-general-policies/ensure-that-php-version-is-the-latest-if-used-to-run-the-web-app#terraform](https://docs.ST Cloud.com/checks/azure/azure-general-policies/ensure-that-php-version-is-the-latest-if-used-to-run-the-web-app#terraform)

### Other

[https://www.trendmicro.com/cloudoneconformity/knowledge-base/azure/AppService/latest-version-of-php.html](https://www.trendmicro.com/cloudoneconformity/knowledge-base/azure/AppService/latest-version-of-php.html)

## 参考资料

- [https://learn.microsoft.com/en-us/azure/app-service/configure-common?tabs=portal#general-settings](https://learn.microsoft.com/en-us/azure/app-service/configure-common?tabs=portal#general-settings)
- [https://learn.microsoft.com/en-us/azure/app-service/configure-language-php?pivots=platform-linux#set-php-version](https://learn.microsoft.com/en-us/azure/app-service/configure-language-php?pivots=platform-linux#set-php-version)

## 技术信息

- Source Metadata：[sources/azure/app_ensure_php_version_is_latest/metadata.json](../../sources/azure/app_ensure_php_version_is_latest/metadata.json)
- Source Code：[sources/azure/app_ensure_php_version_is_latest/check.py](../../sources/azure/app_ensure_php_version_is_latest/check.py)
- Source Metadata Path：`sources/azure/app_ensure_php_version_is_latest/metadata.json`
- Source Code Path：`sources/azure/app_ensure_php_version_is_latest/check.py`
