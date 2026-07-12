# Ensure Azure Functions are not publicly accessible

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `app_function_not_publicly_accessible` |
| クラウドプラットフォーム | Azure |
| サービス | app |
| サブサービス | function |
| 重大度 | high |
| カテゴリ | Uncategorized |
| リソースタイプ | Microsoft.Web/sites |
| リソースグループ | serverless |

## 説明

Azure Functions should not be exposed to the public internet. Restricting access helps protect applications from potential threats and reduces the attack surface.

## リスク

Exposing Azure Functions to the public internet increases the risk of unauthorized access, data breaches, and other security threats.

## 推奨事項

Review the Azure Functions security guidelines and ensure that access restrictions are in place. Use Azure Private Link and Key Vault for enhanced security.

- 推奨リンク：[https://learn.microsoft.com/en-us/azure/app-service/overview-access-restrictions](https://learn.microsoft.com/en-us/azure/app-service/overview-access-restrictions)

## 修正手順


### Other

[https://www.trendmicro.com/cloudoneconformity/knowledge-base/azure/Functions/azure-function-exposed.html](https://www.trendmicro.com/cloudoneconformity/knowledge-base/azure/Functions/azure-function-exposed.html)

## 参考資料

- [https://learn.microsoft.com/en-us/azure/azure-functions/functions-networking-options](https://learn.microsoft.com/en-us/azure/azure-functions/functions-networking-options)
- [https://learn.microsoft.com/en-us/azure/app-service/overview-access-restrictions](https://learn.microsoft.com/en-us/azure/app-service/overview-access-restrictions)

## 技術情報

- Source Metadata：[sources/azure/app_function_not_publicly_accessible/metadata.json](../../sources/azure/app_function_not_publicly_accessible/metadata.json)
- Source Code：[sources/azure/app_function_not_publicly_accessible/check.py](../../sources/azure/app_function_not_publicly_accessible/check.py)
- Source Metadata Path：`sources/azure/app_function_not_publicly_accessible/metadata.json`
- Source Code Path：`sources/azure/app_function_not_publicly_accessible/check.py`
