# Ensure that Microsoft Defender for Cloud Apps integration with Microsoft Defender for Cloud is Selected

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `defender_ensure_mcas_is_enabled` |
| クラウドプラットフォーム | Azure |
| サービス | defender |
| 重大度 | medium |
| カテゴリ | Uncategorized |
| リソースタイプ | DefenderSettings |
| リソースグループ | security |

## 説明

This integration setting enables Microsoft Defender for Cloud Apps (formerly 'Microsoft Cloud App Security' or 'MCAS' - see additional info) to communicate with Microsoft Defender for Cloud.

## リスク

Microsoft Defender for Cloud offers an additional layer of protection by using Azure Resource Manager events, which is considered to be the control plane for Azure. By analyzing the Azure Resource Manager records, Microsoft Defender for Cloud detects unusual or potentially harmful operations in the Azure subscription environment. Several of the preceding analytics are powered by Microsoft Defender for Cloud Apps. To benefit from these analytics, subscription must have a Cloud App Security license. Microsoft Defender for Cloud Apps works only with Standard Tier subscriptions.

## 推奨事項

1. From Azure Home select the Portal Menu. 2. Select Microsoft Defender for Cloud. 3. Select Environment Settings blade. 4. Select the subscription. 5. Check App Service Defender Plan to On. 6. Select Save.

- 推奨リンク：[https://docs.microsoft.com/en-us/rest/api/securitycenter/settings/list](https://docs.microsoft.com/en-us/rest/api/securitycenter/settings/list)

## 修正手順


### Other

[https://www.trendmicro.com/cloudoneconformity/knowledge-base/azure/SecurityCenter/defender-cloud-apps-integration.html#](https://www.trendmicro.com/cloudoneconformity/knowledge-base/azure/SecurityCenter/defender-cloud-apps-integration.html#)

## 参考資料

- [https://learn.microsoft.com/en-in/azure/defender-for-cloud/defender-for-cloud-introduction#secure-cloud-applications](https://learn.microsoft.com/en-in/azure/defender-for-cloud/defender-for-cloud-introduction#secure-cloud-applications)
- [https://docs.microsoft.com/en-us/rest/api/securitycenter/settings/list](https://docs.microsoft.com/en-us/rest/api/securitycenter/settings/list)

## 技術情報

- Source Metadata：[sources/azure/defender_ensure_mcas_is_enabled/metadata.json](../../sources/azure/defender_ensure_mcas_is_enabled/metadata.json)
- Source Code：[sources/azure/defender_ensure_mcas_is_enabled/check.py](../../sources/azure/defender_ensure_mcas_is_enabled/check.py)
- Source Metadata Path：`sources/azure/defender_ensure_mcas_is_enabled/metadata.json`
- Source Code Path：`sources/azure/defender_ensure_mcas_is_enabled/check.py`
