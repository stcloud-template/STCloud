# Ensure that Azure Functions are using access keys for enhanced security

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `app_function_access_keys_configured` |
| クラウドプラットフォーム | Azure |
| サービス | app |
| サブサービス | function |
| 重大度 | high |
| カテゴリ | Uncategorized |
| リソースタイプ | Microsoft.Web/sites |
| リソースグループ | serverless |

## 説明

Azure Functions provide a way to secure HTTP function endpoints during development and production. Using access keys adds an extra layer of protection, ensuring that only authorized users or systems can access the functions. This is particularly important when dealing with public apps or sensitive data.

## リスク

Unprotected function endpoints may be vulnerable to unauthorized access, leading to potential data breaches or malicious activity.

## 推奨事項

Use access keys to secure Azure Functions. You can create and manage keys in the Azure portal or using the Azure CLI. For more information, see the official documentation.

- 推奨リンク：[https://learn.microsoft.com/en-us/azure/azure-functions/security-concepts?tabs=v4#function-access-keys](https://learn.microsoft.com/en-us/azure/azure-functions/security-concepts?tabs=v4#function-access-keys)

## 修正手順


### Other

[https://www.trendmicro.com/cloudoneconformity/knowledge-base/azure/Functions/azure-function-anonymous-access.html](https://www.trendmicro.com/cloudoneconformity/knowledge-base/azure/Functions/azure-function-anonymous-access.html)

## 参考資料

- [https://learn.microsoft.com/en-us/azure/azure-functions/functions-bindings-http-webhook-trigger?tabs=python-v2%2Cisolated-process%2Cnodejs-v4%2Cfunctionsv2&pivots=programming-language-csharp#authorization-keys](https://learn.microsoft.com/en-us/azure/azure-functions/functions-bindings-http-webhook-trigger?tabs=python-v2%2Cisolated-process%2Cnodejs-v4%2Cfunctionsv2&pivots=programming-language-csharp#authorization-keys)
- [https://learn.microsoft.com/en-us/azure/azure-functions/security-concepts?tabs=v4#function-access-keys](https://learn.microsoft.com/en-us/azure/azure-functions/security-concepts?tabs=v4#function-access-keys)

## 技術情報

- Source Metadata：[sources/azure/app_function_access_keys_configured/metadata.json](../../sources/azure/app_function_access_keys_configured/metadata.json)
- Source Code：[sources/azure/app_function_access_keys_configured/check.py](../../sources/azure/app_function_access_keys_configured/check.py)
- Source Metadata Path：`sources/azure/app_function_access_keys_configured/metadata.json`
- Source Code Path：`sources/azure/app_function_access_keys_configured/check.py`
