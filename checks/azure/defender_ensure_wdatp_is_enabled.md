# Ensure that Microsoft Defender for Endpoint integration with Microsoft Defender for Cloud is selected

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `defender_ensure_wdatp_is_enabled` |
| クラウドプラットフォーム | Azure |
| サービス | defender |
| 重大度 | medium |
| カテゴリ | Uncategorized |
| リソースタイプ | DefenderSettings |
| リソースグループ | security |

## 説明

This integration setting enables Microsoft Defender for Endpoint (formerly 'Advanced Threat Protection' or 'ATP' or 'WDATP' - see additional info) to communicate with Microsoft Defender for Cloud.

## リスク

Microsoft Defender for Endpoint integration brings comprehensive Endpoint Detection and Response (EDR) capabilities within Microsoft Defender for Cloud. This integration helps to spot abnormalities, as well as detect and respond to advanced attacks on endpoints monitored by Microsoft Defender for Cloud. MDE works only with Standard Tier subscriptions.

## 推奨事項

No content available.

- 推奨リンク：[https://learn.microsoft.com/en-us/microsoft-365/security/defender-endpoint/azure-server-integration?view=o365-worldwide](https://learn.microsoft.com/en-us/microsoft-365/security/defender-endpoint/azure-server-integration?view=o365-worldwide)

## 修正手順


### Other

[https://www.trendmicro.com/cloudoneconformity/knowledge-base/azure/SecurityCenter/defender-endpoint-integration.html](https://www.trendmicro.com/cloudoneconformity/knowledge-base/azure/SecurityCenter/defender-endpoint-integration.html)

## 参考資料

- [https://learn.microsoft.com/en-in/azure/defender-for-cloud/integration-defender-for-endpoint?tabs=windows](https://learn.microsoft.com/en-in/azure/defender-for-cloud/integration-defender-for-endpoint?tabs=windows)
- [https://learn.microsoft.com/en-us/microsoft-365/security/defender-endpoint/azure-server-integration?view=o365-worldwide](https://learn.microsoft.com/en-us/microsoft-365/security/defender-endpoint/azure-server-integration?view=o365-worldwide)

## 技術情報

- Source Metadata：[sources/azure/defender_ensure_wdatp_is_enabled/metadata.json](../../sources/azure/defender_ensure_wdatp_is_enabled/metadata.json)
- Source Code：[sources/azure/defender_ensure_wdatp_is_enabled/check.py](../../sources/azure/defender_ensure_wdatp_is_enabled/check.py)
- Source Metadata Path：`sources/azure/defender_ensure_wdatp_is_enabled/metadata.json`
- Source Code Path：`sources/azure/defender_ensure_wdatp_is_enabled/check.py`
