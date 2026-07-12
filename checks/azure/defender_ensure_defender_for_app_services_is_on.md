# Ensure That Microsoft Defender for App Services Is Set To 'On'

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `defender_ensure_defender_for_app_services_is_on` |
| クラウドプラットフォーム | Azure |
| サービス | defender |
| 重大度 | high |
| カテゴリ | Uncategorized |
| リソースタイプ | AzureDefenderPlan |
| リソースグループ | security |

## 説明

Ensure That Microsoft Defender for App Services Is Set To 'On'

## リスク

Turning on Microsoft Defender for App Service enables threat detection for App Service, providing threat intelligence, anomaly detection, and behavior analytics in the Microsoft Defender for Cloud.

## 推奨事項

By default, Microsoft Defender for Cloud is not enabled for your App Service instances. Enabling the Defender security service for App Service instances allows for advanced security defense using threat detection capabilities provided by Microsoft Security Response Center.

## 修正手順


### Terraform

[https://docs.ST Cloud.com/checks/azure/azure-general-policies/ensure-that-azure-defender-is-set-to-on-for-app-service#terraform](https://docs.ST Cloud.com/checks/azure/azure-general-policies/ensure-that-azure-defender-is-set-to-on-for-app-service#terraform)

### Other

[https://www.trendmicro.com/cloudoneconformity/knowledge-base/azure/SecurityCenter/defender-app-service.html](https://www.trendmicro.com/cloudoneconformity/knowledge-base/azure/SecurityCenter/defender-app-service.html)

## 参考資料

No external references available.

## 技術情報

- Source Metadata：[sources/azure/defender_ensure_defender_for_app_services_is_on/metadata.json](../../sources/azure/defender_ensure_defender_for_app_services_is_on/metadata.json)
- Source Code：[sources/azure/defender_ensure_defender_for_app_services_is_on/check.py](../../sources/azure/defender_ensure_defender_for_app_services_is_on/check.py)
- Source Metadata Path：`sources/azure/defender_ensure_defender_for_app_services_is_on/metadata.json`
- Source Code Path：`sources/azure/defender_ensure_defender_for_app_services_is_on/check.py`
