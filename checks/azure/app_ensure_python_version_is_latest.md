# Ensure that 'Python version' is the Latest Stable Version, if Used to Run the Web App

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `app_ensure_python_version_is_latest` |
| クラウドプラットフォーム | Azure |
| サービス | app |
| 重大度 | low |
| カテゴリ | Uncategorized |
| リソースタイプ | Microsoft.Web/sites |
| リソースグループ | serverless |

## 説明

Periodically, newer versions are released for Python software either due to security flaws or to include additional functionality. Using the latest full Python version for web apps is recommended in order to take advantage of security fixes, if any, and/or additional functionalities of the newer version.

## リスク

Newer versions may contain security enhancements and additional functionality. Using the latest software version is recommended in order to take advantage of enhancements and new capabilities. With each software installation, organizations need to determine if a given update meets their requirements. They must also verify the compatibility and support provided for any additional software against the update revision that is selected. Using the latest full version will keep your stack secure to vulnerabilities and exploits.

## 推奨事項

From Azure Portal 1. From Azure Home open the Portal Menu in the top left 2. Go to App Services 3. Click on each App 4. Under Settings section, click on Configuration 5. Click on the General settings pane and ensure that the Major Version and the Minor Version is set to the latest stable version available (Python 3.11, at the time of writing) NOTE: No action is required if Python version is set to Off, as Python is not used by your web app.

- 推奨リンク：[https://learn.microsoft.com/en-us/azure/app-service/configure-language-python#configure-python-version](https://learn.microsoft.com/en-us/azure/app-service/configure-language-python#configure-python-version)

## 修正手順


### CLI

```text
az webapp config set --resource-group <RESOURCE_GROUP_NAME> --name <APP_NAME> [--linux-fx-version 'PYTHON|3.12']
```

### Terraform

[https://docs.ST Cloud.com/checks/azure/azure-general-policies/ensure-that-python-version-is-the-latest-if-used-to-run-the-web-app](https://docs.ST Cloud.com/checks/azure/azure-general-policies/ensure-that-python-version-is-the-latest-if-used-to-run-the-web-app)

### Other

[https://www.trendmicro.com/cloudoneconformity/knowledge-base/azure/AppService/latest-version-of-python.html](https://www.trendmicro.com/cloudoneconformity/knowledge-base/azure/AppService/latest-version-of-python.html)

## 参考資料

- [https://learn.microsoft.com/en-us/azure/app-service/configure-common?tabs=portal#general-settings](https://learn.microsoft.com/en-us/azure/app-service/configure-common?tabs=portal#general-settings)
- [https://learn.microsoft.com/en-us/azure/app-service/configure-language-python#configure-python-version](https://learn.microsoft.com/en-us/azure/app-service/configure-language-python#configure-python-version)

## 技術情報

- Source Metadata：[sources/azure/app_ensure_python_version_is_latest/metadata.json](../../sources/azure/app_ensure_python_version_is_latest/metadata.json)
- Source Code：[sources/azure/app_ensure_python_version_is_latest/check.py](../../sources/azure/app_ensure_python_version_is_latest/check.py)
- Source Metadata Path：`sources/azure/app_ensure_python_version_is_latest/metadata.json`
- Source Code Path：`sources/azure/app_ensure_python_version_is_latest/check.py`
