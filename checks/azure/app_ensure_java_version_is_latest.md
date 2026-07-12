# Ensure that 'Java version' is the latest, if used to run the Web App

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `app_ensure_java_version_is_latest` |
| クラウドプラットフォーム | Azure |
| サービス | app |
| 重大度 | low |
| カテゴリ | Uncategorized |
| リソースタイプ | Microsoft.Web/sites |
| リソースグループ | serverless |

## 説明

Periodically, newer versions are released for Java software either due to security flaws or to include additional functionality. Using the latest Java version for web apps is recommended in order to take advantage of security fixes, if any, and/or new functionalities of the newer version.

## リスク

Newer versions may contain security enhancements and additional functionality. Using the latest software version is recommended in order to take advantage of enhancements and new capabilities. With each software installation, organizations need to determine if a given update meets their requirements. They must also verify the compatibility and support provided for any additional software against the update revision that is selected.

## 推奨事項

1. Login to Azure Portal using https://portal.azure.com 2. Go to App Services 3. Click on each App 4. Under Settings section, click on Configuration 5. Click on the General settings pane and ensure that for a Stack of Java the Major Version and Minor Version reflect the latest stable and supported release, and that the Java web server version is set to the auto-update option. NOTE: No action is required if Java version is set to Off, as Java is not used by your web app.

- 推奨リンク：[https://learn.microsoft.com/en-us/azure/app-service/configure-language-java?pivots=platform-linux#choosing-a-java-runtime-version](https://learn.microsoft.com/en-us/azure/app-service/configure-language-java?pivots=platform-linux#choosing-a-java-runtime-version)

## 修正手順


### Terraform

[https://docs.ST Cloud.com/checks/azure/azure-general-policies/ensure-that-java-version-is-the-latest-if-used-to-run-the-web-app#terraform](https://docs.ST Cloud.com/checks/azure/azure-general-policies/ensure-that-java-version-is-the-latest-if-used-to-run-the-web-app#terraform)

### Other

[https://www.trendmicro.com/cloudoneconformity/knowledge-base/azure/AppService/latest-version-of-java.html](https://www.trendmicro.com/cloudoneconformity/knowledge-base/azure/AppService/latest-version-of-java.html)

## 参考資料

- [https://learn.microsoft.com/en-us/azure/app-service/configure-common?tabs=portal#general-settings](https://learn.microsoft.com/en-us/azure/app-service/configure-common?tabs=portal#general-settings)
- [https://learn.microsoft.com/en-us/azure/app-service/configure-language-java?pivots=platform-linux#choosing-a-java-runtime-version](https://learn.microsoft.com/en-us/azure/app-service/configure-language-java?pivots=platform-linux#choosing-a-java-runtime-version)

## 技術情報

- Source Metadata：[sources/azure/app_ensure_java_version_is_latest/metadata.json](../../sources/azure/app_ensure_java_version_is_latest/metadata.json)
- Source Code：[sources/azure/app_ensure_java_version_is_latest/check.py](../../sources/azure/app_ensure_java_version_is_latest/check.py)
- Source Metadata Path：`sources/azure/app_ensure_java_version_is_latest/metadata.json`
- Source Code Path：`sources/azure/app_ensure_java_version_is_latest/check.py`
