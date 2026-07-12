# Ensure Web App is using the latest version of TLS encryption

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `app_minimum_tls_version_12` |
| クラウドプラットフォーム | Azure |
| サービス | app |
| 重大度 | high |
| カテゴリ | Uncategorized |
| リソースタイプ | Microsoft.Web/sites/config |
| リソースグループ | serverless |

## 説明

The TLS (Transport Layer Security) protocol secures transmission of data over the internet using standard encryption technology. Encryption should be set with the latest version of TLS. App service allows TLS 1.2 by default, which is the recommended TLS level by industry standards such as PCI DSS.

## リスク

App service currently allows the web app to set TLS versions 1.0, 1.1 and 1.2. It is highly recommended to use the latest TLS 1.2 version for web app secure connections.

## 推奨事項

1. Login to Azure Portal using https://portal.azure.com 2. Go to App Services 3. Click on each App 4. Under Setting section, Click on TLS/SSL settings 5. Under the Bindings pane, ensure that Minimum TLS Version set to 1.2 under Protocol Settings

- 推奨リンク：[https://docs.microsoft.com/en-us/security/benchmark/azure/security-controls-v3-data-protection#dp-3-encrypt-sensitive-data-in-transit](https://docs.microsoft.com/en-us/security/benchmark/azure/security-controls-v3-data-protection#dp-3-encrypt-sensitive-data-in-transit)

## 修正手順


### CLI

```text
az webapp config set --resource-group <RESOURCE_GROUP_NAME> --name <APP_NAME> --min-tls-version 1.2
```

### Terraform

[https://docs.ST Cloud.com/checks/azure/azure-networking-policies/bc_azr_networking_6#terraform](https://docs.ST Cloud.com/checks/azure/azure-networking-policies/bc_azr_networking_6#terraform)

### Other

[https://www.trendmicro.com/cloudoneconformity/knowledge-base/azure/AppService/latest-version-of-tls-encryption-in-use.html](https://www.trendmicro.com/cloudoneconformity/knowledge-base/azure/AppService/latest-version-of-tls-encryption-in-use.html)

## 参考資料

- [https://learn.microsoft.com/en-us/azure/app-service/configure-ssl-bindings#enforce-tls-versions](https://learn.microsoft.com/en-us/azure/app-service/configure-ssl-bindings#enforce-tls-versions)
- [https://docs.microsoft.com/en-us/security/benchmark/azure/security-controls-v3-data-protection#dp-3-encrypt-sensitive-data-in-transit](https://docs.microsoft.com/en-us/security/benchmark/azure/security-controls-v3-data-protection#dp-3-encrypt-sensitive-data-in-transit)

## 技術情報

- Source Metadata：[sources/azure/app_minimum_tls_version_12/metadata.json](../../sources/azure/app_minimum_tls_version_12/metadata.json)
- Source Code：[sources/azure/app_minimum_tls_version_12/check.py](../../sources/azure/app_minimum_tls_version_12/check.py)
- Source Metadata Path：`sources/azure/app_minimum_tls_version_12/metadata.json`
- Source Code Path：`sources/azure/app_minimum_tls_version_12/check.py`
