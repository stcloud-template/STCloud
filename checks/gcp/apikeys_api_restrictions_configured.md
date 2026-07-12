# Ensure API Keys Are Restricted to Only APIs That Application Needs Access

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `apikeys_api_restrictions_configured` |
| クラウドプラットフォーム | GCP |
| サービス | apikeys |
| 重大度 | medium |
| カテゴリ | Uncategorized |
| リソースタイプ | API Key |
| リソースグループ | IAM |

## 説明

API Keys should only be used for services in cases where other authentication methods are unavailable. If they are in use it is recommended to rotate API keys every 90 days.

## リスク

Google Cloud Platform (GCP) API keys are simple encrypted strings that don't identify the user or the application that performs the API request. GCP API keys are typically accessible to clients, as they can be viewed publicly from within a browser, making it easy to discover and capture API keys.

## 推奨事項

Ensure that the usage of your Google Cloud API keys is restricted to specific APIs such as Cloud Key Management Service (KMS) API, Cloud Storage API, Cloud Monitoring API and/or Cloud Logging API. All Google Cloud API keys that are being used for production applications should use API restrictions. In order to follow cloud security best practices and reduce the attack surface, Google Cloud API keys should be restricted to call only those APIs required by your application.

- 推奨リンク：[https://cloud.google.com/docs/authentication/api-keys](https://cloud.google.com/docs/authentication/api-keys)

## 修正手順


### Other

[https://www.trendmicro.com/cloudoneconformity/knowledge-base/gcp/CloudAPI/check-for-api-key-api-restrictions.html](https://www.trendmicro.com/cloudoneconformity/knowledge-base/gcp/CloudAPI/check-for-api-key-api-restrictions.html)

## 参考資料

- [https://cloud.google.com/docs/authentication/api-keys](https://cloud.google.com/docs/authentication/api-keys)

## 技術情報

- Source Metadata：[sources/gcp/apikeys_api_restrictions_configured/metadata.json](../../sources/gcp/apikeys_api_restrictions_configured/metadata.json)
- Source Code：[sources/gcp/apikeys_api_restrictions_configured/check.py](../../sources/gcp/apikeys_api_restrictions_configured/check.py)
- Source Metadata Path：`sources/gcp/apikeys_api_restrictions_configured/metadata.json`
- Source Code Path：`sources/gcp/apikeys_api_restrictions_configured/check.py`
