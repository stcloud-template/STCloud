# Ensure API Keys Are Restricted to Only APIs That Application Needs Access

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `apikeys_api_restrictions_configured` |
| 云平台 | GCP |
| 服务 | apikeys |
| 严重等级 | medium |
| 类别 | Uncategorized |
| 资源类型 | API Key |
| 资源组 | IAM |

## 描述

API Keys should only be used for services in cases where other authentication methods are unavailable. If they are in use it is recommended to rotate API keys every 90 days.

## 风险

Google Cloud Platform (GCP) API keys are simple encrypted strings that don't identify the user or the application that performs the API request. GCP API keys are typically accessible to clients, as they can be viewed publicly from within a browser, making it easy to discover and capture API keys.

## 推荐措施

Ensure that the usage of your Google Cloud API keys is restricted to specific APIs such as Cloud Key Management Service (KMS) API, Cloud Storage API, Cloud Monitoring API and/or Cloud Logging API. All Google Cloud API keys that are being used for production applications should use API restrictions. In order to follow cloud security best practices and reduce the attack surface, Google Cloud API keys should be restricted to call only those APIs required by your application.

- 推荐链接：[https://cloud.google.com/docs/authentication/api-keys](https://cloud.google.com/docs/authentication/api-keys)

## 修复步骤


### Other

[https://www.trendmicro.com/cloudoneconformity/knowledge-base/gcp/CloudAPI/check-for-api-key-api-restrictions.html](https://www.trendmicro.com/cloudoneconformity/knowledge-base/gcp/CloudAPI/check-for-api-key-api-restrictions.html)

## 参考资料

- [https://cloud.google.com/docs/authentication/api-keys](https://cloud.google.com/docs/authentication/api-keys)

## 技术信息

- Source Metadata：[sources/gcp/apikeys_api_restrictions_configured/metadata.json](../../sources/gcp/apikeys_api_restrictions_configured/metadata.json)
- Source Code：[sources/gcp/apikeys_api_restrictions_configured/check.py](../../sources/gcp/apikeys_api_restrictions_configured/check.py)
- Source Metadata Path：`sources/gcp/apikeys_api_restrictions_configured/metadata.json`
- Source Code Path：`sources/gcp/apikeys_api_restrictions_configured/check.py`
