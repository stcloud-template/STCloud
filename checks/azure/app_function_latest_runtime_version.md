# Ensure Azure Functions are using the latest supported runtime

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `app_function_latest_runtime_version` |
| 云平台 | Azure |
| 服务 | app |
| 子服务 | function |
| 严重等级 | high |
| 类别 | Uncategorized |
| 资源类型 | Microsoft.Web/sites |
| 资源组 | serverless |

## 描述

Keeping Azure Functions up to date with the latest supported runtime version is crucial for security and performance. Updates often include security patches and enhancements, helping to protect against known vulnerabilities and potential exploits. Additionally, newer runtime versions may offer improved functionality and optimized resource utilization.

## 风险

Using outdated runtime versions may introduce security risks and performance degradation. Outdated runtimes may have unpatched vulnerabilities, making them susceptible to attacks.

## 推荐措施

No content available.

- 推荐链接：[https://learn.microsoft.com/en-us/azure/azure-functions/migrate-version-3-version-4?tabs=net8%2Cazure-cli%2Cwindows&pivots=programming-language-python](https://learn.microsoft.com/en-us/azure/azure-functions/migrate-version-3-version-4?tabs=net8%2Cazure-cli%2Cwindows&pivots=programming-language-python)

## 修复步骤


### CLI

```text
az functionapp config appsettings set --name <function_app_name> --resource-group <resource_group_name> --settings FUNCTIONS_EXTENSION_VERSION=~4
```

### Other

[https://www.trendmicro.com/cloudoneconformity/knowledge-base/azure/Functions/azure-function-runtime-version.html](https://www.trendmicro.com/cloudoneconformity/knowledge-base/azure/Functions/azure-function-runtime-version.html)

## 参考资料

- [https://docs.microsoft.com/en-us/azure/azure-functions/functions-versions](https://docs.microsoft.com/en-us/azure/azure-functions/functions-versions)
- [https://learn.microsoft.com/en-us/azure/azure-functions/migrate-version-3-version-4?tabs=net8%2Cazure-cli%2Cwindows&pivots=programming-language-python](https://learn.microsoft.com/en-us/azure/azure-functions/migrate-version-3-version-4?tabs=net8%2Cazure-cli%2Cwindows&pivots=programming-language-python)

## 技术信息

- Source Metadata：[sources/azure/app_function_latest_runtime_version/metadata.json](../../sources/azure/app_function_latest_runtime_version/metadata.json)
- Source Code：[sources/azure/app_function_latest_runtime_version/check.py](../../sources/azure/app_function_latest_runtime_version/check.py)
- Source Metadata Path：`sources/azure/app_function_latest_runtime_version/metadata.json`
- Source Code Path：`sources/azure/app_function_latest_runtime_version/check.py`
